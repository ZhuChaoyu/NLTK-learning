#!/usr/bin/env python
# coding=utf-8
from types import *
from copy_reg import dispatch_table
from copy_reg import _extension_registry, _inverted_registry, _extension_cache
import marshal
import sys
import struct
import re

def load(file):
    return Unpickler(file).load()

class _Stop(Exception):
    def __init__(self, value):
        self.value = value

class Unpickler:

    def __init__(self, file):
        """This takes a file-like object for reading a pickle data stream.

        The protocol version of the pickle is detected automatically, so no
        proto argument is needed.

        The file-like object must have two methods, a read() method that
        takes an integer argument, and a readline() method that requires no
        arguments.  Both methods should return a string.  Thus file-like
        object can be a file object opened for reading, a StringIO object,
        or any other custom object that meets this interface.
        """
        self.readline = file.readline
        self.read = file.read
        self.memo = {}

    def load(self):
        """Read a pickled object representation from the open file.
        Return the reconstituted object hierarchy specified in the file.
        """
        self.mark = object() # any new unique object
        self.stack = []
        self.append = self.stack.append
        read = self.read
        dispatch = self.dispatch
        try:
            while 1:
                key = read(1)
                print key
                dispatch[key](self)
        except _Stop, stopinst:
            return stopinst.value

    dispatch = {}
    def load_eof(self):
        raise EOFError
    dispatch[''] = load_eof

    def load_proto(self):
        proto = ord(self.read(1))
        if not 0 <= proto <= 2:
            raise ValueError, "unsupported pickle protocol: %d" % proto
    dispatch[PROTO] = load_proto

    def load_persid(self):
        pid = self.readline()[:-1]
        self.append(self.persistent_load(pid))
    dispatch[PERSID] = load_persid

    def load_binpersid(self):
        pid = self.stack.pop()
        self.append(self.persistent_load(pid))
    dispatch[BINPERSID] = load_binpersid

    def load_none(self):
        self.append(None)
    dispatch[NONE] = load_none

    def load_false(self):
        self.append(False)
    dispatch[NEWFALSE] = load_false

    def load_true(self):
        self.append(True)
    dispatch[NEWTRUE] = load_true

    def load_int(self):
        data = self.readline()
        if data == FALSE[1:]:
            val = False
        elif data == TRUE[1:]:
            val = True
        else:
            try:
                val = int(data)
            except ValueError:
                val = long(data)
        self.append(val)
    dispatch[INT] = load_int

    def load_binint(self):
        self.append(mloads('i' + self.read(4)))
    dispatch[BININT] = load_binint

    def load_binint1(self):
        self.append(ord(self.read(1)))
    dispatch[BININT1] = load_binint1

    def load_binint2(self):
        self.append(mloads('i' + self.read(2) + '\000\000'))
    dispatch[BININT2] = load_binint2

    def load_long(self):
        self.append(long(self.readline()[:-1], 0))
    dispatch[LONG] = load_long

    def load_long1(self):
        n = ord(self.read(1))
        bytes = self.read(n)
        self.append(decode_long(bytes))
    dispatch[LONG1] = load_long1

    def load_long4(self):
        n = mloads('i' + self.read(4))
        bytes = self.read(n)
        self.append(decode_long(bytes))
    dispatch[LONG4] = load_long4

    def load_float(self):
        self.append(float(self.readline()[:-1]))
    dispatch[FLOAT] = load_float

    def load_binfloat(self, unpack=struct.unpack):
        self.append(unpack('>d', self.read(8))[0])
    dispatch[BINFLOAT] = load_binfloat

    def load_string(self):
        rep = self.readline()[:-1]
        for q in "\"'": # double or single quote
            if rep.startswith(q):
                if len(rep) < 2 or not rep.endswith(q):
                    raise ValueError, "insecure string pickle"
                rep = rep[len(q):-len(q)]
                break
        else:
            raise ValueError, "insecure string pickle"
        self.append(rep.decode("string-escape"))
    dispatch[STRING] = load_string

    def load_binstring(self):
        len = mloads('i' + self.read(4))
        self.append(self.read(len))
    dispatch[BINSTRING] = load_binstring

    def load_unicode(self):
        self.append(unicode(self.readline()[:-1],'raw-unicode-escape'))
    dispatch[UNICODE] = load_unicode

    def load_binunicode(self):
        len = mloads('i' + self.read(4))
        self.append(unicode(self.read(len),'utf-8'))
    dispatch[BINUNICODE] = load_binunicode

    def load_short_binstring(self):
        len = ord(self.read(1))
        self.append(self.read(len))
    dispatch[SHORT_BINSTRING] = load_short_binstring

    def load_tuple(self):
        k = self.marker()
        self.stack[k:] = [tuple(self.stack[k+1:])]
    dispatch[TUPLE] = load_tuple

    def load_empty_tuple(self):
        self.stack.append(())
    dispatch[EMPTY_TUPLE] = load_empty_tuple


    def load_tuple1(self):
        self.stack[-1] = (self.stack[-1],)
    dispatch[TUPLE1] = load_tuple1

    def load_tuple2(self):
        self.stack[-2:] = [(self.stack[-2], self.stack[-1])]
    dispatch[TUPLE2] = load_tuple2

    def load_tuple3(self):
        self.stack[-3:] = [(self.stack[-3], self.stack[-2], self.stack[-1])]
    dispatch[TUPLE3] = load_tuple3

    def load_empty_list(self):
        self.stack.append([])
    dispatch[EMPTY_LIST] = load_empty_list

    def load_empty_dictionary(self):
        self.stack.append({})
    dispatch[EMPTY_DICT] = load_empty_dictionary

    def load_dict(self):
        k = self.marker()
        d = {}
        items = self.stack[k+1:]
        for i in range(0, len(items), 2):
            key = items[i]
            value = items[i+1]
            d[key] = value
        self.stack[k:] = [d]
    dispatch[DICT] = load_dict



   



