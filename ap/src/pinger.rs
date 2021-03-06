extern crate get_if_addrs;
extern crate ring;

use std::{thread, time};
use std::net::UdpSocket;
use std::mem::transmute;

use self::ring::rand;
use self::ring::rand::SecureRandom;

use util::p2p_iface_braddr;
use error::Error;

static mut SEQID: i64 = 0;

pub struct Pinger;

impl Pinger {
  pub fn new(port: i64) -> Result<Pinger, Error> {
    let sock = UdpSocket::bind(format!("0.0.0.0:{}", port))?;
    sock.set_broadcast(true)?;
    thread::spawn(move || {
      let rand = rand::SystemRandom::new();
      loop {
        thread::sleep(time::Duration::from_millis(300));
        match p2p_iface_braddr() {
          Ok(braddr) =>
            match braddr {
              Some(brip) => {
                unsafe { rand.fill(transmute::<&mut i64, &mut [u8;8]>(&mut SEQID)).unwrap(); };
                Pinger::ping(&sock, format!("{}:{}", brip, port));
              },
              _ => unsafe { SEQID = 0; }
            },
          Err(err) => {
            println!("Error getting interfaces: {}", err);
            unsafe { SEQID = 0; }
          }
        }
      }
    });
    Ok(Pinger{})
  }

  pub fn get_seqid(&self) -> i64 {
    unsafe { SEQID }
  }

  fn ping(sock: &UdpSocket, addr: String) {
    // convert SEQID to a byte array
    let data : [u8; 8] = unsafe { transmute(SEQID.to_be()) };
    match sock.send_to(&data, &addr) {
      Ok(n) => if n == 8 {
        println!("pinged {} with seqid {}", addr,
                 unsafe { transmute::<[u8; 8], i64>(data) }); },
      Err(err) => println!("failed to send ping: {}", err)
    }
  }
}
