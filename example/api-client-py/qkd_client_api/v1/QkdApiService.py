# -*- coding: utf8 -*-
#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,slots,no_utf8strings,coding=utf8
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(object):
  def get_by_length(self, key_length):
    """
    Получить новый ключ указанной длины и его идентификатор

    Parameters:
     - key_length: длина запрашиваемого ключа в байтах
    """
    pass

  def get_by_id(self, key_id):
    """
    Получить существующий ключ по его идентификатору

    Parameters:
     - key_id: идентификатор ключа (квид), указанный в структуре KeyInfo при получении
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def get_by_length(self, key_length):
    """
    Получить новый ключ указанной длины и его идентификатор

    Parameters:
     - key_length: длина запрашиваемого ключа в байтах
    """
    self.send_get_by_length(key_length)
    return self.recv_get_by_length()

  def send_get_by_length(self, key_length):
    self._oprot.writeMessageBegin('get_by_length', TMessageType.CALL, self._seqid)
    args = get_by_length_args()
    args.key_length = key_length
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_by_length(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = get_by_length_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.qse is not None:
      raise result.qse
    if result.qce is not None:
      raise result.qce
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_by_length failed: unknown result")

  def get_by_id(self, key_id):
    """
    Получить существующий ключ по его идентификатору

    Parameters:
     - key_id: идентификатор ключа (квид), указанный в структуре KeyInfo при получении
    """
    self.send_get_by_id(key_id)
    return self.recv_get_by_id()

  def send_get_by_id(self, key_id):
    self._oprot.writeMessageBegin('get_by_id', TMessageType.CALL, self._seqid)
    args = get_by_id_args()
    args.key_id = key_id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get_by_id(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = get_by_id_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.qse is not None:
      raise result.qse
    if result.qce is not None:
      raise result.qce
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get_by_id failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["get_by_length"] = Processor.process_get_by_length
    self._processMap["get_by_id"] = Processor.process_get_by_id

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_get_by_length(self, seqid, iprot, oprot):
    args = get_by_length_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_by_length_result()
    try:
      result.success = self._handler.get_by_length(args.key_length)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except QkdServerError as qse:
      msg_type = TMessageType.REPLY
      result.qse = qse
    except QkdClientError as qce:
      msg_type = TMessageType.REPLY
      result.qce = qce
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("get_by_length", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_get_by_id(self, seqid, iprot, oprot):
    args = get_by_id_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_by_id_result()
    try:
      result.success = self._handler.get_by_id(args.key_id)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except QkdServerError as qse:
      msg_type = TMessageType.REPLY
      result.qse = qse
    except QkdClientError as qce:
      msg_type = TMessageType.REPLY
      result.qce = qce
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("get_by_id", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class get_by_length_args(object):
  """
  Attributes:
   - key_length: длина запрашиваемого ключа в байтах
  """

  __slots__ = [ 
    'key_length',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'key_length', None, None, ), # 1
  )

  def __init__(self, key_length=None,):
    self.key_length = key_length

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.key_length = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_by_length_args')
    if self.key_length is not None:
      oprot.writeFieldBegin('key_length', TType.I32, 1)
      oprot.writeI32(self.key_length)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.key_length)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class get_by_length_result(object):
  """
  Attributes:
   - success
   - qse
   - qce
  """

  __slots__ = [ 
    'success',
    'qse',
    'qce',
   ]

  thrift_spec = (
    (0, TType.STRUCT, 'success', (KeyInfo, KeyInfo.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'qse', (QkdServerError, QkdServerError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'qce', (QkdClientError, QkdClientError.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, qse=None, qce=None,):
    self.success = success
    self.qse = qse
    self.qce = qce

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = KeyInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.qse = QkdServerError()
          self.qse.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.qce = QkdClientError()
          self.qce.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_by_length_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.qse is not None:
      oprot.writeFieldBegin('qse', TType.STRUCT, 1)
      self.qse.write(oprot)
      oprot.writeFieldEnd()
    if self.qce is not None:
      oprot.writeFieldBegin('qce', TType.STRUCT, 2)
      self.qce.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.qse)
    value = (value * 31) ^ hash(self.qce)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class get_by_id_args(object):
  """
  Attributes:
   - key_id: идентификатор ключа (квид), указанный в структуре KeyInfo при получении
  """

  __slots__ = [ 
    'key_id',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'key_id', None, None, ), # 1
  )

  def __init__(self, key_id=None,):
    self.key_id = key_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.key_id = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_by_id_args')
    if self.key_id is not None:
      oprot.writeFieldBegin('key_id', TType.STRING, 1)
      oprot.writeString(self.key_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.key_id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class get_by_id_result(object):
  """
  Attributes:
   - success
   - qse
   - qce
  """

  __slots__ = [ 
    'success',
    'qse',
    'qce',
   ]

  thrift_spec = (
    (0, TType.STRUCT, 'success', (KeyInfo, KeyInfo.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'qse', (QkdServerError, QkdServerError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'qce', (QkdClientError, QkdClientError.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, qse=None, qce=None,):
    self.success = success
    self.qse = qse
    self.qce = qce

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = KeyInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.qse = QkdServerError()
          self.qse.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.qce = QkdClientError()
          self.qce.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_by_id_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.qse is not None:
      oprot.writeFieldBegin('qse', TType.STRUCT, 1)
      self.qse.write(oprot)
      oprot.writeFieldEnd()
    if self.qce is not None:
      oprot.writeFieldBegin('qce', TType.STRUCT, 2)
      self.qce.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.qse)
    value = (value * 31) ^ hash(self.qce)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

