# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modelRunner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modelRunner.proto',
  package='pbModelRunner',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11modelRunner.proto\x12\rpbModelRunner\"%\n\x10LoadModelMessage\x12\x11\n\tModelName\x18\x01 \x01(\t\":\n\x0fRunModelMessage\x12\x11\n\tModelName\x18\x01 \x01(\t\x12\x14\n\x0cObservations\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2Q\n\x0bModelRunner\x12\x42\n\x08RunModel\x12\x1e.pbModelRunner.RunModelMessage\x1a\x14.pbModelRunner.Empty\"\x00\x62\x06proto3')
)




_LOADMODELMESSAGE = _descriptor.Descriptor(
  name='LoadModelMessage',
  full_name='pbModelRunner.LoadModelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ModelName', full_name='pbModelRunner.LoadModelMessage.ModelName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=73,
)


_RUNMODELMESSAGE = _descriptor.Descriptor(
  name='RunModelMessage',
  full_name='pbModelRunner.RunModelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ModelName', full_name='pbModelRunner.RunModelMessage.ModelName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Observations', full_name='pbModelRunner.RunModelMessage.Observations', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=133,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='pbModelRunner.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['LoadModelMessage'] = _LOADMODELMESSAGE
DESCRIPTOR.message_types_by_name['RunModelMessage'] = _RUNMODELMESSAGE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoadModelMessage = _reflection.GeneratedProtocolMessageType('LoadModelMessage', (_message.Message,), dict(
  DESCRIPTOR = _LOADMODELMESSAGE,
  __module__ = 'modelRunner_pb2'
  # @@protoc_insertion_point(class_scope:pbModelRunner.LoadModelMessage)
  ))
_sym_db.RegisterMessage(LoadModelMessage)

RunModelMessage = _reflection.GeneratedProtocolMessageType('RunModelMessage', (_message.Message,), dict(
  DESCRIPTOR = _RUNMODELMESSAGE,
  __module__ = 'modelRunner_pb2'
  # @@protoc_insertion_point(class_scope:pbModelRunner.RunModelMessage)
  ))
_sym_db.RegisterMessage(RunModelMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'modelRunner_pb2'
  # @@protoc_insertion_point(class_scope:pbModelRunner.Empty)
  ))
_sym_db.RegisterMessage(Empty)



_MODELRUNNER = _descriptor.ServiceDescriptor(
  name='ModelRunner',
  full_name='pbModelRunner.ModelRunner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=144,
  serialized_end=225,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunModel',
    full_name='pbModelRunner.ModelRunner.RunModel',
    index=0,
    containing_service=None,
    input_type=_RUNMODELMESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELRUNNER)

DESCRIPTOR.services_by_name['ModelRunner'] = _MODELRUNNER

# @@protoc_insertion_point(module_scope)
