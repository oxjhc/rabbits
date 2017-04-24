# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  serialized_pb=_b('\n\x0emessages.proto\"P\n\x08ProofReq\x12\x0b\n\x03uid\x18\x01 \x02(\x0c\x12\x0e\n\x06unonce\x18\x02 \x02(\x0c\x12\r\n\x05seqid\x18\x03 \x02(\x03\x12\x0b\n\x03vid\x18\x04 \x02(\x0c\x12\x0b\n\x03sig\x18\x05 \x02(\x0c\"5\n\tProofResp\x12\x0b\n\x03uid\x18\x01 \x02(\x0c\x12\x0e\n\x06unonce\x18\x02 \x02(\x0c\x12\x0b\n\x03sig\x18\x03 \x02(\x0c\"\xd0\x01\n\x08VaultMsg\x12\x1e\n\x05vault\x18\x01 \x02(\x0b\x32\x0f.VaultMsg.Vault\x12\x0b\n\x03uid\x18\x02 \x02(\x0c\x12\x0e\n\x06unonce\x18\x03 \x02(\x0c\x12\x0c\n\x04\x61pid\x18\x04 \x02(\x0c\x12\x0f\n\x07\x61pnonce\x18\x05 \x02(\x0c\x12\x0c\n\x04time\x18\x06 \x02(\x06\x12\x0b\n\x03sig\x18\x07 \x02(\x0c\x1aM\n\x05Vault\x12%\n\x06points\x18\x01 \x03(\x0b\x32\x15.VaultMsg.Vault.Point\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\r\x12\t\n\x01y\x18\x02 \x02(\r\"u\n\tLocnProof\x12\x11\n\tvault_key\x18\x01 \x02(\x0c\x12\x0b\n\x03uid\x18\x02 \x02(\x0c\x12\x0e\n\x06unonce\x18\x03 \x02(\x0c\x12\x0c\n\x04\x61pid\x18\x04 \x02(\x0c\x12\x0f\n\x07\x61pnonce\x18\x05 \x02(\x0c\x12\x0c\n\x04time\x18\x06 \x02(\x06\x12\x0b\n\x03sig\x18\x07 \x02(\x0c\")\n\x05Token\x12\x0e\n\x06vnonce\x18\x01 \x02(\x0c\x12\x10\n\x08locn_tag\x18\x02 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROOFREQ = _descriptor.Descriptor(
  name='ProofReq',
  full_name='ProofReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ProofReq.uid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unonce', full_name='ProofReq.unonce', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqid', full_name='ProofReq.seqid', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vid', full_name='ProofReq.vid', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='ProofReq.sig', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=98,
)


_PROOFRESP = _descriptor.Descriptor(
  name='ProofResp',
  full_name='ProofResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ProofResp.uid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unonce', full_name='ProofResp.unonce', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='ProofResp.sig', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=153,
)


_VAULTMSG_VAULT_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='VaultMsg.Vault.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='VaultMsg.Vault.Point.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='VaultMsg.Vault.Point.y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=364,
)

_VAULTMSG_VAULT = _descriptor.Descriptor(
  name='Vault',
  full_name='VaultMsg.Vault',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='VaultMsg.Vault.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VAULTMSG_VAULT_POINT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=364,
)

_VAULTMSG = _descriptor.Descriptor(
  name='VaultMsg',
  full_name='VaultMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vault', full_name='VaultMsg.vault', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='VaultMsg.uid', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unonce', full_name='VaultMsg.unonce', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apid', full_name='VaultMsg.apid', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apnonce', full_name='VaultMsg.apnonce', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='VaultMsg.time', index=5,
      number=6, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='VaultMsg.sig', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VAULTMSG_VAULT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=364,
)


_LOCNPROOF = _descriptor.Descriptor(
  name='LocnProof',
  full_name='LocnProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vault_key', full_name='LocnProof.vault_key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='LocnProof.uid', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unonce', full_name='LocnProof.unonce', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apid', full_name='LocnProof.apid', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apnonce', full_name='LocnProof.apnonce', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='LocnProof.time', index=5,
      number=6, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='LocnProof.sig', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=483,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vnonce', full_name='Token.vnonce', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locn_tag', full_name='Token.locn_tag', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=526,
)

_VAULTMSG_VAULT_POINT.containing_type = _VAULTMSG_VAULT
_VAULTMSG_VAULT.fields_by_name['points'].message_type = _VAULTMSG_VAULT_POINT
_VAULTMSG_VAULT.containing_type = _VAULTMSG
_VAULTMSG.fields_by_name['vault'].message_type = _VAULTMSG_VAULT
DESCRIPTOR.message_types_by_name['ProofReq'] = _PROOFREQ
DESCRIPTOR.message_types_by_name['ProofResp'] = _PROOFRESP
DESCRIPTOR.message_types_by_name['VaultMsg'] = _VAULTMSG
DESCRIPTOR.message_types_by_name['LocnProof'] = _LOCNPROOF
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN

ProofReq = _reflection.GeneratedProtocolMessageType('ProofReq', (_message.Message,), dict(
  DESCRIPTOR = _PROOFREQ,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ProofReq)
  ))
_sym_db.RegisterMessage(ProofReq)

ProofResp = _reflection.GeneratedProtocolMessageType('ProofResp', (_message.Message,), dict(
  DESCRIPTOR = _PROOFRESP,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ProofResp)
  ))
_sym_db.RegisterMessage(ProofResp)

VaultMsg = _reflection.GeneratedProtocolMessageType('VaultMsg', (_message.Message,), dict(

  Vault = _reflection.GeneratedProtocolMessageType('Vault', (_message.Message,), dict(

    Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
      DESCRIPTOR = _VAULTMSG_VAULT_POINT,
      __module__ = 'messages_pb2'
      # @@protoc_insertion_point(class_scope:VaultMsg.Vault.Point)
      ))
    ,
    DESCRIPTOR = _VAULTMSG_VAULT,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:VaultMsg.Vault)
    ))
  ,
  DESCRIPTOR = _VAULTMSG,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:VaultMsg)
  ))
_sym_db.RegisterMessage(VaultMsg)
_sym_db.RegisterMessage(VaultMsg.Vault)
_sym_db.RegisterMessage(VaultMsg.Vault.Point)

LocnProof = _reflection.GeneratedProtocolMessageType('LocnProof', (_message.Message,), dict(
  DESCRIPTOR = _LOCNPROOF,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:LocnProof)
  ))
_sym_db.RegisterMessage(LocnProof)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
  DESCRIPTOR = _TOKEN,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Token)
  ))
_sym_db.RegisterMessage(Token)


# @@protoc_insertion_point(module_scope)
