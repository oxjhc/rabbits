extern crate toml;

use std::collections::BTreeMap as Map;
use std::fs::File;
use std::io::Read;

use self::toml::Value;

use galois_field::GF;
use crypto::PrivKey;
use error::Error;

pub struct Config {
  pub name: String,
  pub key: PrivKey,
  pub server_url: String,
  pub ping_port: i64,
  pub http_port: i64,
  pub locn_tag: Vec<GF>,
  pub wpa_ctrl_path: String,
  pub _t_vid_file: String
}

impl Config {
  pub fn new() -> Result<Config, Error> {
    let cfgv = match Config::read_cfg() {
      Ok(res) => res,
      Err(err) => panic!("Error reading config: {:?}", err)
    };

    match cfgv.get("config") {
      Some(v) => match v.as_table() {
        Some(keys) =>
          Ok(Config{
            name: match keys.get("name") {
              Some(v) => match v.as_str() {
                Some(v) => Ok(v),
                None => Err(Error::cfg_err("Error reading config: name isn't a string"))
              },
              None => Ok("Dormouse")
            }?.to_string(),

            key: match keys.get("privkey") {
              Some(v) => match v.as_str() {
                Some(key_fname) => PrivKey::from_file(key_fname),
                None =>
                  Err(Error::cfg_err("Error reading config: privkey isn't a string!"))
              },
              None => Err(Error::cfg_err("Error reading config: no privkey provided"))
            }?,

            server_url: match keys.get("server_url") {
              Some(v) => match v.as_str() {
                Some(v) => Ok(v),
                None =>
                  Err(Error::cfg_err("Error reading config: server_url isn't a string!"))
              },
              None => Ok("http://oxjhc.club")
            }?.to_string(),

            ping_port: match keys.get("ping_port") {
              Some(v) => match v.as_integer() {
                Some(v) => Ok(v),
                None =>
                  Err(Error::cfg_err("Error reading config: ping_port isn't an integer!"))
              },
              None => Ok(1832)
            }?,

            http_port: match keys.get("http_port") {
              Some(v) => match v.as_integer() {
                Some(v) => Ok(v),
                None =>
                  Err(Error::cfg_err("Error reading config: http_port isn't an integer!"))
              },
              None => Ok(80)
            }?,

            locn_tag: match keys.get("locn_tag") {
              Some(v) => match v.as_array() {
                Some(arr) => {
                  let mut tag = Vec::with_capacity(10);
                  for v in arr {
                    match v.as_integer() {
                      Some(i) => tag.push(From::from(i)),
                      None =>
                        return Err(Error::cfg_err("Error reading config: locn_tag contains a non-integer"))
                    }
                  }
                  Ok(tag)
                },
                None =>
                  Err(Error::cfg_err("Error reading config: locn_tag isn't an array!"))
              },
              None => Err(Error::cfg_err("Error reading config: no locn_tag!"))
            }?,

            wpa_ctrl_path: match keys.get("wpa_ctrl_path") {
              Some(v) => match v.as_str() {
                Some(v) => Ok(v),
                None => Err(Error::cfg_err("Error reading config: wpa_ctrl_path isn't a string"))
              },
              None => Ok("/var/run/wpa_supplicant")
            }?.to_string(),

            _t_vid_file: match keys.get("_t_verif_pubkey") {
              Some(v) => match v.as_str() {
                Some(v) => Ok(v),
                None => Err(Error::cfg_err("Error reading config: _t_verif_pubkey isn't a string"))
              },
              None => Ok("")
            }?.to_string()
          }),
        None => Err(Error::cfg_err("'key' should be a table"))
      },
      None => Err(Error::cfg_err("Error reading config: section 'config' does not exist"))
    }
  }

  fn read_cfg() -> Result<Map<String, Value>, Error> {
    let mut cfg_file = File::open("/etc/dormouse/config.toml")?;
    let mut contents = String::new();
    cfg_file.read_to_string(&mut contents)?;
    match contents.parse::<Value>() {
      Ok(res) => match res.as_table() {
        Some(table) => Ok(table.clone()),
        None => Err(Error::cfg_err("not a table"))
      },
      Err(err) => Err(Error::TomlDeErr(err))
    }
  }
}
