# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='GBHandle.proto',
  package='D3.GameBalance',
  serialized_pb='\n\x0eGBHandle.proto\x12\x0e\x44\x33.GameBalance\"1\n\x06Handle\x12\x19\n\x11game_balance_type\x18\x01 \x02(\x11\x12\x0c\n\x04gbid\x18\x02 \x02(\x0f')




_HANDLE = descriptor.Descriptor(
  name='Handle',
  full_name='D3.GameBalance.Handle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='game_balance_type', full_name='D3.GameBalance.Handle.game_balance_type', index=0,
      number=1, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gbid', full_name='D3.GameBalance.Handle.gbid', index=1,
      number=2, type=15, cpp_type=1, label=2,
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
  serialized_start=34,
  serialized_end=83,
)



class Handle(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANDLE
  
  # @@protoc_insertion_point(class_scope:D3.GameBalance.Handle)

# @@protoc_insertion_point(module_scope)
