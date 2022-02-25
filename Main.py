import sys

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
import sys as python_lib_Sys
import re as python_lib_Re
import builtins as python_lib_Builtins
import functools as python_lib_Functools
try:
    import msvcrt as python_lib_Msvcrt
except:
    pass
import os as python_lib_Os
import random as python_lib_Random
import shutil as python_lib_Shutil
import subprocess as python_lib_Subprocess
try:
    import termios as python_lib_Termios
except:
    pass
import time as python_lib_Time
import timeit as python_lib_Timeit
import traceback as python_lib_Traceback
try:
    import tty as python_lib_Tty
except:
    pass
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timedelta as python_lib_datetime_Timedelta
from datetime import tzinfo as python_lib_datetime_Tzinfo
from datetime import timezone as python_lib_datetime_Timezone
from io import IOBase as python_lib_io_IOBase
from io import BufferedIOBase as python_lib_io_BufferedIOBase
from io import RawIOBase as python_lib_io_RawIOBase
from io import FileIO as python_lib_io_FileIO
from io import TextIOBase as python_lib_io_TextIOBase
from io import StringIO as python_lib_io_StringIO
from time import struct_time as python_lib_time_StructTime
import urllib.parse as python_lib_urllib_Parse


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tag = None
        _hx_o.index = None
        _hx_o.params = None
Enum._hx_class = Enum


class Class: pass


class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "getUTCHours", "getUTCMinutes", "getUTCSeconds", "getUTCFullYear", "getUTCMonth", "getUTCDate", "getUTCDay", "getTimezoneOffset", "toString"]
    _hx_statics = ["now", "fromTime", "makeLocal", "UTC", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def getTime(self):
        return (self.date.timestamp() * 1000)

    def getHours(self):
        return self.date.hour

    def getMinutes(self):
        return self.date.minute

    def getSeconds(self):
        return self.date.second

    def getFullYear(self):
        return self.date.year

    def getMonth(self):
        return (self.date.month - 1)

    def getDate(self):
        return self.date.day

    def getDay(self):
        return HxOverrides.mod(self.date.isoweekday(), 7)

    def getUTCHours(self):
        return self.dateUTC.hour

    def getUTCMinutes(self):
        return self.dateUTC.minute

    def getUTCSeconds(self):
        return self.dateUTC.second

    def getUTCFullYear(self):
        return self.dateUTC.year

    def getUTCMonth(self):
        return (self.dateUTC.month - 1)

    def getUTCDate(self):
        return self.dateUTC.day

    def getUTCDay(self):
        return HxOverrides.mod(self.dateUTC.isoweekday(), 7)

    def getTimezoneOffset(self):
        x = (self.date.utcoffset() / python_lib_datetime_Timedelta(0,60))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        return -tmp

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def fromTime(t):
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def makeLocal(date):
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

    @staticmethod
    def UTC(year,month,day,hour,_hx_min,sec):
        return (python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0,python_lib_datetime_Timezone.utc).timestamp() * 1000)

    @staticmethod
    def fromString(s):
        _g = len(s)
        if (_g == 8):
            k = s.split(":")
            return Date.fromTime((((Std.parseInt((k[0] if 0 < len(k) else None)) * 3600000.) + ((Std.parseInt((k[1] if 1 < len(k) else None)) * 60000.))) + ((Std.parseInt((k[2] if 2 < len(k) else None)) * 1000.))))
        elif (_g == 10):
            k = s.split("-")
            return Date(Std.parseInt((k[0] if 0 < len(k) else None)),(Std.parseInt((k[1] if 1 < len(k) else None)) - 1),Std.parseInt((k[2] if 2 < len(k) else None)),0,0,0)
        elif (_g == 19):
            k = s.split(" ")
            _this = (k[0] if 0 < len(k) else None)
            y = _this.split("-")
            _this = (k[1] if 1 < len(k) else None)
            t = _this.split(":")
            return Date(Std.parseInt((y[0] if 0 < len(y) else None)),(Std.parseInt((y[1] if 1 < len(y) else None)) - 1),Std.parseInt((y[2] if 2 < len(y) else None)),Std.parseInt((t[0] if 0 < len(t) else None)),Std.parseInt((t[1] if 1 < len(t) else None)),Std.parseInt((t[2] if 2 < len(t) else None)))
        else:
            raise haxe_Exception.thrown(("Invalid date format : " + ("null" if s is None else s)))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.date = None
        _hx_o.dateUTC = None
Date._hx_class = Date


class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]
    _hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]
    _hx_statics = ["escape"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)

    def match(self,s):
        self.matchObj = python_lib_Re.search(self.pattern,s)
        return (self.matchObj is not None)

    def matched(self,n):
        return self.matchObj.group(n)

    def matchedLeft(self):
        return HxString.substr(self.matchObj.string,0,self.matchObj.start())

    def matchedRight(self):
        return HxString.substr(self.matchObj.string,self.matchObj.end(),None)

    def matchedPos(self):
        return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

    def matchSub(self,s,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        if (_hx_len != -1):
            self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
        else:
            self.matchObj = self.pattern.search(s,pos)
        return (self.matchObj is not None)

    def split(self,s):
        if self._hx_global:
            ret = []
            lastEnd = 0
            x = python_HaxeIterator(python_lib_Re.finditer(self.pattern,s))
            while x.hasNext():
                x1 = x.next()
                x2 = HxString.substring(s,lastEnd,x1.start())
                ret.append(x2)
                lastEnd = x1.end()
            x = HxString.substr(s,lastEnd,None)
            ret.append(x)
            return ret
        else:
            self.matchObj = python_lib_Re.search(self.pattern,s)
            if (self.matchObj is None):
                return [s]
            else:
                return [HxString.substring(s,0,self.matchObj.start()), HxString.substr(s,self.matchObj.end(),None)]

    def replace(self,s,by):
        _this = by.split("$$")
        by = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_0(x):
            res = by
            g = x.groups()
            _g = 0
            _g1 = len(g)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                gs = g[i]
                if (gs is None):
                    continue
                delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
                _this = (list(res) if ((delimiter == "")) else res.split(delimiter))
                res = gs.join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = res.split("_hx_#repl#__")
            res = "$".join([python_Boot.toString1(x1,'') for x1 in _this])
            return res
        replace = _hx_local_0
        return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

    def map(self,s,f):
        buf_b = python_lib_io_StringIO()
        pos = 0
        right = s
        cur = self
        while (pos < len(s)):
            if (self.matchObj is None):
                self.matchObj = python_lib_Re.search(self.pattern,s)
            else:
                self.matchObj = self.matchObj.re.search(s,pos)
            if (self.matchObj is None):
                break
            pos1 = self.matchObj.end()
            curPos_pos = cur.matchObj.start()
            curPos_len = (cur.matchObj.end() - cur.matchObj.start())
            buf_b.write(Std.string(HxString.substr(HxString.substr(cur.matchObj.string,0,cur.matchObj.start()),pos,None)))
            buf_b.write(Std.string(f(cur)))
            right = HxString.substr(cur.matchObj.string,cur.matchObj.end(),None)
            if (not self._hx_global):
                buf_b.write(Std.string(right))
                return buf_b.getvalue()
            if (curPos_len == 0):
                buf_b.write(Std.string(("" if (((pos1 < 0) or ((pos1 >= len(s))))) else s[pos1])))
                right = HxString.substr(right,1,None)
                pos = (pos1 + 1)
            else:
                pos = pos1
        buf_b.write(Std.string(right))
        return buf_b.getvalue()

    @staticmethod
    def escape(s):
        return python_lib_Re.escape(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.matchObj = None
        _hx_o._hx_global = None
EReg._hx_class = EReg


class _EnumValue_EnumValue_Impl_:
    _hx_class_name = "_EnumValue.EnumValue_Impl_"
    __slots__ = ()
    _hx_statics = ["match"]

    @staticmethod
    def match(this1,pattern):
        return False
_EnumValue_EnumValue_Impl_._hx_class = _EnumValue_EnumValue_Impl_


class IntIterator:
    _hx_class_name = "IntIterator"
    __slots__ = ("min", "max")
    _hx_fields = ["min", "max"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_min,_hx_max):
        self.min = _hx_min
        self.max = _hx_max

    def hasNext(self):
        return (self.min < self.max)

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.min
                _hx_local_0.min = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_local_2()
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.min = None
        _hx_o.max = None
IntIterator._hx_class = IntIterator


class MainCLI:
    _hx_class_name = "MainCLI"
    __slots__ = ()
    _hx_statics = ["main"]

    @staticmethod
    def main():
        args = Sys.args()
        if (len(args) != 2):
            _hx_str = "usage: <PlantUML> foo.puml foo.svg"
            python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
            return
        content = sys_io_File.getContent((args[0] if 0 < len(args) else None))
        plantu = com_plantuml_api_v1_Plantuml()
        plantu.addLines(content)
        sys_io_File.saveContent((args[1] if 1 < len(args) else None),plantu.getSvg())
MainCLI._hx_class = MainCLI


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "isClosure", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

    @staticmethod
    def hasField(o,field):
        return python_Boot.hasField(o,field)

    @staticmethod
    def field(o,field):
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def getProperty(o,field):
        if (o is None):
            return None
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if isinstance(o,_hx_AnonObject):
            return Reflect.field(o,field)
        tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
        if ((tmp is not None) and callable(tmp)):
            return tmp()
        else:
            return Reflect.field(o,field)

    @staticmethod
    def setProperty(o,field,value):
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if isinstance(o,_hx_AnonObject):
            setattr(o,field1,value)
        elif hasattr(o,("set_" + ("null" if field1 is None else field1))):
            getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
        else:
            setattr(o,field1,value)

    @staticmethod
    def callMethod(o,func,args):
        if callable(func):
            return func(*args)
        else:
            return None

    @staticmethod
    def fields(o):
        return python_Boot.fields(o)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1

    @staticmethod
    def isClosure(v):
        return isinstance(v,python_internal_MethodClosure)

    @staticmethod
    def compareMethods(f1,f2):
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False

    @staticmethod
    def isObject(v):
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 4):
            return True
        elif (tmp == 6):
            _g1 = _g.params[0]
            return True
        else:
            return False

    @staticmethod
    def isEnumValue(v):
        if not HxOverrides.eq(v,Enum):
            return isinstance(v,Enum)
        else:
            return False

    @staticmethod
    def deleteField(o,field):
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if (not python_Boot.hasField(o,field)):
            return False
        o.__delattr__(field)
        return True

    @staticmethod
    def copy(o):
        if (o is None):
            return None
        o2 = _hx_AnonObject({})
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        return o2

    @staticmethod
    def makeVarArgs(f):
        def _hx_local_0(*v):
            this1 = v
            return f((list(this1) if ((not Std.isOfType(this1,list))) else this1))
        return _hx_local_0
Reflect._hx_class = Reflect


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["downcast", "instance", "isMetaType", "is", "isOfType", "string", "int", "parseInt", "shortenPossibleNumber", "parseFloat", "random"]

    @staticmethod
    def downcast(value,c):
        try:
            tmp = None
            if (not isinstance(value,c)):
                if c._hx_is_interface:
                    cls = c
                    loop = None
                    def _hx_local_1(intf):
                        f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                        if (f is not None):
                            _g = 0
                            while (_g < len(f)):
                                i = (f[_g] if _g >= 0 and _g < len(f) else None)
                                _g = (_g + 1)
                                if (i == cls):
                                    return True
                                else:
                                    l = loop(i)
                                    if l:
                                        return True
                            return False
                        else:
                            return False
                    loop = _hx_local_1
                    currentClass = value.__class__
                    result = False
                    while (currentClass is not None):
                        if loop(currentClass):
                            result = True
                            break
                        currentClass = python_Boot.getSuperClass(currentClass)
                    tmp = result
                else:
                    tmp = False
            else:
                tmp = True
            if tmp:
                return value
            else:
                return None
        except BaseException as _g:
            None
            return None

    @staticmethod
    def instance(value,c):
        return Std.downcast(value,c)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def _hx_is(v,t):
        return Std.isOfType(v,t)

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        isBool = isinstance(v,bool)
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        isEnumType = ((type(t) == type) and (t == Enum))
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = ((type(t) == type) and (t == Class))
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def int(x):
        try:
            return int(x)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None

    @staticmethod
    def shortenPossibleNumber(x):
        r = ""
        _g = 0
        _g1 = len(x)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(x))))) else x[i])
            _g2 = HxString.charCodeAt(c,0)
            if (_g2 is None):
                break
            else:
                _g3 = _g2
                if (((((((((((_g3 == 57) or ((_g3 == 56))) or ((_g3 == 55))) or ((_g3 == 54))) or ((_g3 == 53))) or ((_g3 == 52))) or ((_g3 == 51))) or ((_g3 == 50))) or ((_g3 == 49))) or ((_g3 == 48))) or ((_g3 == 46))):
                    r = (("null" if r is None else r) + ("null" if c is None else c))
                else:
                    break
        return r

    @staticmethod
    def parseFloat(x):
        try:
            return float(x)
        except BaseException as _g:
            None
            if (x is not None):
                r1 = Std.shortenPossibleNumber(x)
                if (r1 != x):
                    return Std.parseFloat(r1)
            return Math.NaN

    @staticmethod
    def random(x):
        if (x <= 0):
            return 0
        else:
            return int((python_lib_Random.random() * x))
Std._hx_class = Std


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

    def add(self,x):
        s = Std.string(x)
        self.b.write(s)

    def add1(self,s):
        self.b.write(s)

    def addChar(self,c):
        s = "".join(map(chr,[c]))
        self.b.write(s)

    def addSub(self,s,pos,_hx_len = None):
        s1 = (HxString.substr(s,pos,None) if ((_hx_len is None)) else HxString.substr(s,pos,_hx_len))
        self.b.write(s1)

    def toString(self):
        return self.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
StringBuf._hx_class = StringBuf


class haxe_SysTools:
    _hx_class_name = "haxe.SysTools"
    __slots__ = ()
    _hx_statics = ["winMetaCharacters", "quoteUnixArg", "quoteWinArg"]

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            return argument
        return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument
haxe_SysTools._hx_class = haxe_SysTools


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "contains", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "unsafeCodeAt", "iterator", "keyValueIterator", "isEof", "quoteUnixArg", "winMetaCharacters", "quoteWinArg"]

    @staticmethod
    def urlEncode(s):
        return python_lib_urllib_Parse.quote(s,"")

    @staticmethod
    def urlDecode(s):
        return python_lib_urllib_Parse.unquote(s)

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def htmlUnescape(s):
        _this = s.split("&gt;")
        _this1 = ">".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&lt;")
        _this1 = "<".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&quot;")
        _this1 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&#039;")
        _this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&amp;")
        return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def contains(s,value):
        startIndex = None
        return (((s.find(value) if ((startIndex is None)) else HxString.indexOfImpl(s,value,startIndex))) != -1)

    @staticmethod
    def startsWith(s,start):
        return s.startswith(start)

    @staticmethod
    def endsWith(s,end):
        return s.endswith(end)

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        s1 = Std.string(s)
        buf.b.write(s1)
        while (buf.get_length() < l):
            s = Std.string(c)
            buf.b.write(s)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def hex(n,digits = None):
        s = ""
        hexChars = "0123456789ABCDEF"
        while True:
            index = (n & 15)
            s = (HxOverrides.stringOrNull((("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index]))) + ("null" if s is None else s))
            n = HxOverrides.rshift(n, 4)
            if (not ((n > 0))):
                break
        if ((digits is not None) and ((len(s) < digits))):
            diff = (digits - len(s))
            _g = 0
            _g1 = diff
            while (_g < _g1):
                _ = _g
                _g = (_g + 1)
                s = ("0" + ("null" if s is None else s))
        return s

    @staticmethod
    def fastCodeAt(s,index):
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    @staticmethod
    def unsafeCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def iterator(s):
        return haxe_iterators_StringIterator(s)

    @staticmethod
    def keyValueIterator(s):
        return haxe_iterators_StringKeyValueIterator(s)

    @staticmethod
    def isEof(c):
        return (c == -1)

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        else:
            _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
            _this.matchObj = python_lib_Re.search(_this.pattern,argument)
            if (_this.matchObj is None):
                return argument
            else:
                return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        argument1 = argument
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument1)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument1.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument1," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument1.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument1,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument1 == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument1,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument1 = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument1,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument1
StringTools._hx_class = StringTools


class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    __slots__ = ()
    _hx_statics = ["exists", "stat", "rename", "fullPath", "absolutePath", "isDirectory", "createDirectory", "deleteFile", "deleteDirectory", "readDirectory"]

    @staticmethod
    def exists(path):
        return python_lib_os_Path.exists(path)

    @staticmethod
    def stat(path):
        s = python_lib_Os.stat(path)
        return _hx_AnonObject({'gid': s.st_gid, 'uid': s.st_uid, 'atime': Date.fromTime((1000 * s.st_atime)), 'mtime': Date.fromTime((1000 * s.st_mtime)), 'ctime': Date.fromTime((1000 * s.st_ctime)), 'size': s.st_size, 'dev': s.st_dev, 'ino': s.st_ino, 'nlink': s.st_nlink, 'rdev': getattr(s,"st_rdev",0), 'mode': s.st_mode})

    @staticmethod
    def rename(path,newPath):
        python_lib_Os.rename(path,newPath)

    @staticmethod
    def fullPath(relPath):
        return python_lib_os_Path.realpath(relPath)

    @staticmethod
    def absolutePath(relPath):
        if haxe_io_Path.isAbsolute(relPath):
            return relPath
        return haxe_io_Path.join([Sys.getCwd(), relPath])

    @staticmethod
    def isDirectory(path):
        return python_lib_os_Path.isdir(path)

    @staticmethod
    def createDirectory(path):
        python_lib_Os.makedirs(path,511,True)

    @staticmethod
    def deleteFile(path):
        python_lib_Os.remove(path)

    @staticmethod
    def deleteDirectory(path):
        python_lib_Os.rmdir(path)

    @staticmethod
    def readDirectory(path):
        return python_lib_Os.listdir(path)
sys_FileSystem._hx_class = sys_FileSystem


class Sys:
    _hx_class_name = "Sys"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "time", "exit", "print", "println", "args", "getEnv", "putEnv", "environment", "sleep", "setTimeLocale", "getCwd", "setCwd", "systemName", "command", "cpuTime", "executablePath", "_programPath", "programPath", "getChar", "stdin", "stdout", "stderr"]
    environ = None

    @staticmethod
    def get_environ():
        _g = Sys.environ
        if (_g is None):
            environ = haxe_ds_StringMap()
            env = python_lib_Os.environ
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                value = env.get(key1,None)
                environ.h[key1] = value
            def _hx_local_1():
                def _hx_local_0():
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            env = _g
            return env

    @staticmethod
    def time():
        return python_lib_Time.time()

    @staticmethod
    def exit(code):
        python_lib_Sys.exit(code)

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def args():
        argv = python_lib_Sys.argv
        return argv[1:None]

    @staticmethod
    def getEnv(s):
        return Sys.get_environ().h.get(s,None)

    @staticmethod
    def putEnv(s,v):
        python_lib_Os.putenv(s,v)
        Sys.get_environ().h[s] = v

    @staticmethod
    def environment():
        return Sys.get_environ()

    @staticmethod
    def sleep(seconds):
        python_lib_Time.sleep(seconds)

    @staticmethod
    def setTimeLocale(loc):
        return False

    @staticmethod
    def getCwd():
        return python_lib_Os.getcwd()

    @staticmethod
    def setCwd(s):
        python_lib_Os.chdir(s)

    @staticmethod
    def systemName():
        _g = python_lib_Sys.platform
        x = _g
        if x.startswith("linux"):
            return "Linux"
        else:
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 5):
                if (_g1 == "win32"):
                    return "Windows"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            elif (_hx_local_0 == 6):
                if (_g1 == "cygwin"):
                    return "Windows"
                elif (_g1 == "darwin"):
                    return "Mac"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            else:
                raise haxe_Exception.thrown("not supported platform")

    @staticmethod
    def command(cmd,args = None):
        if (args is None):
            return python_lib_Subprocess.call(cmd,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'shell': True})))
        else:
            return python_lib_Subprocess.call(([cmd] + args))

    @staticmethod
    def cpuTime():
        return python_lib_Timeit.default_timer()

    @staticmethod
    def executablePath():
        return python_internal_ArrayImpl._get(python_lib_Sys.argv, 0)

    @staticmethod
    def programPath():
        return Sys._programPath

    @staticmethod
    def getChar(echo):
        ch = None
        _g = Sys.systemName()
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "Linux"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_1():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_1
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 3):
            if (_g1 == "Mac"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_2():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_2
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 7):
            if (_g1 == "Windows"):
                ch = HxString.charCodeAt(python_lib_Msvcrt.getwch(),0)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        else:
            x = _g
            raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        if echo:
            python_Lib.printString(Std.string("".join(map(chr,[ch]))))
        return ch

    @staticmethod
    def stdin():
        return python_io_IoTools.createFileInputFromText(python_lib_Sys.stdin)

    @staticmethod
    def stdout():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

    @staticmethod
    def stderr():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys

class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType


class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def getEnum(o):
        if (o is None):
            return None
        return o.__class__

    @staticmethod
    def getSuperClass(c):
        return python_Boot.getSuperClass(c)

    @staticmethod
    def getClassName(c):
        if hasattr(c,"_hx_class_name"):
            return c._hx_class_name
        else:
            if (c == list):
                return "Array"
            if (c == Math):
                return "Math"
            if (c == str):
                return "String"
            try:
                return c.__name__
            except BaseException as _g:
                None
                return None

    @staticmethod
    def getEnumName(e):
        return e._hx_class_name

    @staticmethod
    def resolveClass(name):
        if (name == "Array"):
            return list
        if (name == "Math"):
            return Math
        if (name == "String"):
            return str
        cl = _hx_classes.get(name,None)
        tmp = None
        if (cl is not None):
            o = cl
            tmp = (not (((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))))
        else:
            tmp = True
        if tmp:
            return None
        return cl

    @staticmethod
    def resolveEnum(name):
        if (name == "Bool"):
            return Bool
        o = Type.resolveClass(name)
        if hasattr(o,"_hx_constructs"):
            return o
        else:
            return None

    @staticmethod
    def createInstance(cl,args):
        return cl(*args)

    @staticmethod
    def createEmptyInstance(cl):
        i = cl.__new__(cl)
        callInit = None
        def _hx_local_0(cl):
            sc = Type.getSuperClass(cl)
            if (sc is not None):
                callInit(sc)
            if hasattr(cl,"_hx_empty_init"):
                cl._hx_empty_init(i)
        callInit = _hx_local_0
        callInit(cl)
        return i

    @staticmethod
    def createEnum(e,constr,params = None):
        f = Reflect.field(e,constr)
        if (f is None):
            raise haxe_Exception.thrown(("No such constructor " + ("null" if constr is None else constr)))
        if Reflect.isFunction(f):
            if (params is None):
                raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
            return Reflect.callMethod(e,f,params)
        if ((params is not None) and ((len(params) != 0))):
            raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
        return f

    @staticmethod
    def createEnumIndex(e,index,params = None):
        c = python_internal_ArrayImpl._get(e._hx_constructs, index)
        if (c is None):
            raise haxe_Exception.thrown((Std.string(index) + " is not a valid enum constructor index"))
        return Type.createEnum(e,c,params)

    @staticmethod
    def getInstanceFields(c):
        return python_Boot.getInstanceFields(c)

    @staticmethod
    def getClassFields(c):
        return python_Boot.getClassFields(c)

    @staticmethod
    def getEnumConstructs(e):
        if hasattr(e,"_hx_constructs"):
            x = e._hx_constructs
            return list(x)
        else:
            return []

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown

    @staticmethod
    def asEnumImpl(x):
        return x

    @staticmethod
    def enumEq(a,b):
        if HxOverrides.eq(a,b):
            return True
        try:
            if ((b is None) and (not HxOverrides.eq(a,b))):
                return False
            if (a.tag != b.tag):
                return False
            p1 = a.params
            p2 = b.params
            if (len(p1) != len(p2)):
                return False
            _g = 0
            _g1 = len(p1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not Type.enumEq(p1[i],p2[i])):
                    return False
            if (a._hx_class != b._hx_class):
                return False
        except BaseException as _g:
            None
            return False
        return True

    @staticmethod
    def enumConstructor(e):
        return e.tag

    @staticmethod
    def enumParameters(e):
        return list(e.params)

    @staticmethod
    def enumIndex(e):
        return e.index

    @staticmethod
    def allEnums(e):
        ctors = Type.getEnumConstructs(e)
        ret = []
        _g = 0
        while (_g < len(ctors)):
            ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
            _g = (_g + 1)
            v = Reflect.field(e,ctor)
            if Std.isOfType(v,e):
                ret.append(v)
        return ret
Type._hx_class = Type


class _Xml_XmlType_Impl_:
    _hx_class_name = "_Xml.XmlType_Impl_"
    __slots__ = ()
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "toString"]

    @staticmethod
    def toString(this1):
        _g = this1
        if (_g == 0):
            return "Element"
        elif (_g == 1):
            return "PCData"
        elif (_g == 2):
            return "CData"
        elif (_g == 3):
            return "Comment"
        elif (_g == 4):
            return "DocType"
        elif (_g == 5):
            return "ProcessingInstruction"
        elif (_g == 6):
            return "Document"
        else:
            pass
_Xml_XmlType_Impl_._hx_class = _Xml_XmlType_Impl_


class Xml:
    _hx_class_name = "Xml"
    __slots__ = ("nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap")
    _hx_fields = ["nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap"]
    _hx_methods = ["get_nodeName", "set_nodeName", "get_nodeValue", "set_nodeValue", "get", "set", "remove", "exists", "attributes", "iterator", "elements", "elementsNamed", "firstChild", "firstElement", "addChild", "removeChild", "insertChild", "toString", "ensureElementType"]
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "parse", "createElement", "createPCData", "createCData", "createComment", "createDocType", "createProcessingInstruction", "createDocument"]

    def __init__(self,nodeType):
        self.parent = None
        self.nodeValue = None
        self.nodeName = None
        self.nodeType = nodeType
        self.children = []
        self.attributeMap = haxe_ds_StringMap()

    def get_nodeName(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeName

    def set_nodeName(self,v):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeName = v
                return self.nodeName
            return _hx_local_0()
        return _hx_local_1()

    def get_nodeValue(self):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeValue

    def set_nodeValue(self,v):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeValue = v
                return self.nodeValue
            return _hx_local_0()
        return _hx_local_1()

    def get(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.h.get(att,None)

    def set(self,att,value):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.h[att] = value

    def remove(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.remove(att)

    def exists(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (att in self.attributeMap.h)

    def attributes(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.keys()

    def iterator(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return haxe_iterators_ArrayIterator(self.children)

    def elements(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            if (child.nodeType == Xml.Element):
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def elementsNamed(self,name):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            tmp = None
            if (child.nodeType == Xml.Element):
                if (child.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((child.nodeType is None)) else _Xml_XmlType_Impl_.toString(child.nodeType))))))
                tmp = (child.nodeName == name)
            else:
                tmp = False
            if tmp:
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def firstChild(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (self.children[0] if 0 < len(self.children) else None)

    def firstElement(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = 0
        _g1 = self.children
        while (_g < len(_g1)):
            child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (child.nodeType == Xml.Element):
                return child
        return None

    def addChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            x.parent.removeChild(x)
        _this = self.children
        _this.append(x)
        x.parent = self

    def removeChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if python_internal_ArrayImpl.remove(self.children,x):
            x.parent = None
            return True
        return False

    def insertChild(self,x,pos):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            python_internal_ArrayImpl.remove(x.parent.children,x)
        self.children.insert(pos, x)
        x.parent = self

    def toString(self):
        return haxe_xml_Printer.print(self)

    def ensureElementType(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))

    @staticmethod
    def parse(_hx_str):
        return haxe_xml_Parser.parse(_hx_str)

    @staticmethod
    def createElement(name):
        xml = Xml(Xml.Element)
        if (xml.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeName = name
        return xml

    @staticmethod
    def createPCData(data):
        xml = Xml(Xml.PCData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createCData(data):
        xml = Xml(Xml.CData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createComment(data):
        xml = Xml(Xml.Comment)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocType(data):
        xml = Xml(Xml.DocType)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createProcessingInstruction(data):
        xml = Xml(Xml.ProcessingInstruction)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocument():
        return Xml(Xml.Document)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.nodeType = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.attributeMap = None
Xml._hx_class = Xml

class com_plantuml_Direction(Enum):
    __slots__ = ()
    _hx_class_name = "com.plantuml.Direction"
    _hx_constructs = ["RIGHT", "LEFT", "DOWN", "UP"]
com_plantuml_Direction.RIGHT = com_plantuml_Direction("RIGHT", 0, ())
com_plantuml_Direction.LEFT = com_plantuml_Direction("LEFT", 1, ())
com_plantuml_Direction.DOWN = com_plantuml_Direction("DOWN", 2, ())
com_plantuml_Direction.UP = com_plantuml_Direction("UP", 3, ())
com_plantuml_Direction._hx_class = com_plantuml_Direction


class com_plantuml_ISkinParam:
    _hx_class_name = "com.plantuml.ISkinParam"
    __slots__ = ()
    _hx_methods = ["getCurrentStyleBuilder"]
com_plantuml_ISkinParam._hx_class = com_plantuml_ISkinParam


class com_plantuml_SkinParam:
    _hx_class_name = "com.plantuml.SkinParam"
    __slots__ = ()
    _hx_methods = ["getCurrentStyleBuilder"]
    _hx_interfaces = [com_plantuml_ISkinParam]

    def __init__(self):
        pass

    def getCurrentStyleBuilder(self):
        return com_plantuml_style_StyleBuilder()

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_SkinParam._hx_class = com_plantuml_SkinParam


class com_plantuml_api_v1_Plantuml:
    _hx_class_name = "com.plantuml.api.v1.Plantuml"
    __slots__ = ("format", "data")
    _hx_fields = ["format", "data"]
    _hx_methods = ["addLineSingle", "addLines", "addLinesArray", "toString", "setFormat", "setSvgLinkTarget", "setWatermark", "setScale", "setStyle", "compile", "getSvg"]

    def __init__(self):
        self.data = []
        self.format = "svg"

    def addLineSingle(self,line):
        if (line != ""):
            python_internal_ArrayImpl._set(self.data, len(self.data), line)

    def addLines(self,lines):
        _g = 0
        _g1 = lines.split("\n")
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            self.addLineSingle(s)

    def addLinesArray(self,lines):
        _g = 0
        while (_g < len(lines)):
            s = (lines[_g] if _g >= 0 and _g < len(lines) else None)
            _g = (_g + 1)
            self.addLineSingle(s)

    def toString(self):
        _this = self.data
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "]")

    def setFormat(self,arg0):
        pass

    def setSvgLinkTarget(self,arg0):
        pass

    def setWatermark(self,arg0):
        pass

    def setScale(self,arg0):
        pass

    def setStyle(self,arg0):
        pass

    def compile(self):
        _g = 0
        _g1 = self.data
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            haxe_Log.trace(s,_hx_AnonObject({'fileName': "src/com/plantuml/api/v1/Plantuml.hx", 'lineNumber': 46, 'className': "com.plantuml.api.v1.Plantuml", 'methodName': "compile"}))

    def getSvg(self):
        factory = com_plantuml_mindmap_MindMapDiagramFactory()
        lines = com_plantuml_command_BlocLines(self.data)
        diagram = factory.createSystem(lines)
        svg = com_plantuml_ugraphic_UGraphicSvg.create()
        diagram.exportDiagramNow(svg)
        s = svg.getSvg()
        return s

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.format = None
        _hx_o.data = None
com_plantuml_api_v1_Plantuml._hx_class = com_plantuml_api_v1_Plantuml


class com_plantuml_awt_geom_Dimension2D:
    _hx_class_name = "com.plantuml.awt.geom.Dimension2D"
    __slots__ = ("width", "height")
    _hx_fields = ["width", "height"]
    _hx_methods = ["getHeight", "getWidth", "toString", "delta"]

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def toString(self):
        return ((("" + Std.string(self.width)) + " x ") + Std.string(self.height))

    def delta(self,deltaWidth,deltaHeight):
        return com_plantuml_awt_geom_Dimension2D((self.width + deltaWidth),(self.height + deltaHeight))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.width = None
        _hx_o.height = None
com_plantuml_awt_geom_Dimension2D._hx_class = com_plantuml_awt_geom_Dimension2D


class com_plantuml_awt_geom_Line2D:
    _hx_class_name = "com.plantuml.awt.geom.Line2D"
    __slots__ = ("x1", "y1", "x2", "y2")
    _hx_fields = ["x1", "y1", "x2", "y2"]
    _hx_methods = ["getX1", "getY1", "getX2", "getY2"]

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getX1(self):
        return self.x1

    def getY1(self):
        return self.y1

    def getX2(self):
        return self.x2

    def getY2(self):
        return self.y2

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x1 = None
        _hx_o.y1 = None
        _hx_o.x2 = None
        _hx_o.y2 = None
com_plantuml_awt_geom_Line2D._hx_class = com_plantuml_awt_geom_Line2D


class com_plantuml_awt_geom_Point2D:
    _hx_class_name = "com.plantuml.awt.geom.Point2D"
    __slots__ = ("x", "y")
    _hx_fields = ["x", "y"]
    _hx_methods = ["getX", "getY", "asTranslate"]

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def asTranslate(self):
        return com_plantuml_ugraphic_UTranslate(self.x,self.y)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
        _hx_o.y = None
com_plantuml_awt_geom_Point2D._hx_class = com_plantuml_awt_geom_Point2D


class com_plantuml_command_BlocLines:
    _hx_class_name = "com.plantuml.command.BlocLines"
    __slots__ = ("lines",)
    _hx_fields = ["lines"]
    _hx_methods = ["getLines", "toString", "size"]
    _hx_statics = ["single"]

    def __init__(self,lines):
        self.lines = list(lines)

    def getLines(self):
        return self.lines

    def toString(self):
        _this = self.lines
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "]")

    def size(self):
        return len(self.lines)

    @staticmethod
    def single(s):
        return com_plantuml_command_BlocLines([s])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.lines = None
com_plantuml_command_BlocLines._hx_class = com_plantuml_command_BlocLines


class com_plantuml_command_Command:
    _hx_class_name = "com.plantuml.command.Command"
    __slots__ = ()
    _hx_methods = ["isValid", "execute"]
com_plantuml_command_Command._hx_class = com_plantuml_command_Command

class com_plantuml_command_CommandControl(Enum):
    __slots__ = ()
    _hx_class_name = "com.plantuml.command.CommandControl"
    _hx_constructs = ["OK", "NOT_OK", "OK_PARTIAL"]
com_plantuml_command_CommandControl.OK = com_plantuml_command_CommandControl("OK", 0, ())
com_plantuml_command_CommandControl.NOT_OK = com_plantuml_command_CommandControl("NOT_OK", 1, ())
com_plantuml_command_CommandControl.OK_PARTIAL = com_plantuml_command_CommandControl("OK_PARTIAL", 2, ())
com_plantuml_command_CommandControl._hx_class = com_plantuml_command_CommandControl

class com_plantuml_command_CommandExecutionResult(Enum):
    __slots__ = ()
    _hx_class_name = "com.plantuml.command.CommandExecutionResult"
    _hx_constructs = ["OK", "ERROR"]

    @staticmethod
    def ERROR(msg):
        return com_plantuml_command_CommandExecutionResult("ERROR", 1, (msg,))
com_plantuml_command_CommandExecutionResult.OK = com_plantuml_command_CommandExecutionResult("OK", 0, ())
com_plantuml_command_CommandExecutionResult._hx_class = com_plantuml_command_CommandExecutionResult


class com_plantuml_command_SingleLineCommand:
    _hx_class_name = "com.plantuml.command.SingleLineCommand"
    __slots__ = ("regex",)
    _hx_fields = ["regex"]
    _hx_methods = ["_init", "getPattern", "isValid", "execute", "executeArg"]
    _hx_interfaces = [com_plantuml_command_Command]

    def _init(self,array):
        self.regex = com_plantuml_command_regex_RegexConcat(array)

    def getPattern(self):
        return self.regex.getPattern()

    def isValid(self,lines):
        if (lines.size() != 1):
            return com_plantuml_command_CommandControl.NOT_OK
        s = python_internal_ArrayImpl._get(lines.getLines(), 0)
        if self.regex.match(s):
            return com_plantuml_command_CommandControl.OK
        return com_plantuml_command_CommandControl.NOT_OK

    def execute(self,diagram,lines):
        _hx_map = self.regex.matcher(python_internal_ArrayImpl._get(lines.getLines(), 0))
        return self.executeArg(diagram,lines,_hx_map)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.regex = None
com_plantuml_command_SingleLineCommand._hx_class = com_plantuml_command_SingleLineCommand


class com_plantuml_command_regex_IRegex:
    _hx_class_name = "com.plantuml.command.regex.IRegex"
    __slots__ = ()
    _hx_methods = ["getSize", "getPattern", "match", "eat"]
com_plantuml_command_regex_IRegex._hx_class = com_plantuml_command_regex_IRegex


class com_plantuml_command_regex_AbstractRegex:
    _hx_class_name = "com.plantuml.command.regex.AbstractRegex"
    __slots__ = ("pattern",)
    _hx_fields = ["pattern"]
    _hx_methods = ["getSize", "eat", "getPattern", "match", "matchArray"]
    _hx_interfaces = [com_plantuml_command_regex_IRegex]

    def getPattern(self):
        return self.pattern

    def match(self,full):
        r = EReg(self.pattern,"i")
        r.matchObj = python_lib_Re.search(r.pattern,full)
        return (r.matchObj is not None)

    def matchArray(self,full):
        r = EReg(self.pattern,"i")
        r.matchObj = python_lib_Re.search(r.pattern,full)
        if ((r.matchObj is not None) == False):
            return None
        result = []
        i = 1
        try:
            while True:
                x = r.matchObj.group(i)
                result.append(x)
                i = (i + 1)
        except BaseException as _g:
            return result

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
com_plantuml_command_regex_AbstractRegex._hx_class = com_plantuml_command_regex_AbstractRegex


class com_plantuml_command_regex_MyPattern:
    _hx_class_name = "com.plantuml.command.regex.MyPattern"
    __slots__ = ()
    _hx_statics = ["transform"]

    @staticmethod
    def transform(p):
        p = StringTools.replace(p,"%s","\\s ")
        return p
com_plantuml_command_regex_MyPattern._hx_class = com_plantuml_command_regex_MyPattern


class com_plantuml_command_regex_RegexConcat(com_plantuml_command_regex_AbstractRegex):
    _hx_class_name = "com.plantuml.command.regex.RegexConcat"
    __slots__ = ("all",)
    _hx_fields = ["all"]
    _hx_methods = ["getSize", "matcher", "eat"]
    _hx_statics = []
    _hx_interfaces = [com_plantuml_command_regex_IRegex]
    _hx_super = com_plantuml_command_regex_AbstractRegex


    def __init__(self,all):
        self.all = all
        tmp = ""
        _g = 0
        while (_g < len(all)):
            r = (all[_g] if _g >= 0 and _g < len(all) else None)
            _g = (_g + 1)
            tmp = (("null" if tmp is None else tmp) + HxOverrides.stringOrNull(r.getPattern()))
        self.pattern = tmp

    def getSize(self):
        size = 0
        _g = 0
        _g1 = self.all
        while (_g < len(_g1)):
            r = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            size = (size + r.getSize())
        return size

    def matcher(self,full):
        array = self.matchArray(full)
        array.reverse()
        _hx_map = haxe_ds_StringMap()
        self.eat(array,_hx_map)
        return _hx_map

    def eat(self,array,_hx_map):
        _g = 0
        _g1 = self.all
        while (_g < len(_g1)):
            r = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            r.eat(array,_hx_map)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.all = None
com_plantuml_command_regex_RegexConcat._hx_class = com_plantuml_command_regex_RegexConcat


class com_plantuml_command_regex_RegexLeaf(com_plantuml_command_regex_AbstractRegex):
    _hx_class_name = "com.plantuml.command.regex.RegexLeaf"
    __slots__ = ("name", "size")
    _hx_fields = ["name", "size"]
    _hx_methods = ["getSize", "toString", "eat"]
    _hx_statics = ["start", "end", "spaceZeroOrMore", "spaceOneOrMore"]
    _hx_interfaces = [com_plantuml_command_regex_IRegex]
    _hx_super = com_plantuml_command_regex_AbstractRegex


    def __init__(self,size,pattern,name = None):
        self.name = name
        self.pattern = com_plantuml_command_regex_MyPattern.transform(pattern)
        self.size = size

    def getSize(self):
        return self.size

    def toString(self):
        return ((HxOverrides.stringOrNull(self.name) + "=") + HxOverrides.stringOrNull(self.pattern))

    def eat(self,array,_hx_map):
        if (self.size == 1):
            s = (None if ((len(array) == 0)) else array.pop())
            _hx_map.h[self.name] = s
        else:
            _g = 0
            _g1 = self.size
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                s = (None if ((len(array) == 0)) else array.pop())
                _hx_map.h[(HxOverrides.stringOrNull(self.name) + Std.string(i))] = s

    @staticmethod
    def start():
        return com_plantuml_command_regex_RegexLeaf(0,"^")

    @staticmethod
    def end():
        return com_plantuml_command_regex_RegexLeaf(0,"$")

    @staticmethod
    def spaceZeroOrMore():
        return com_plantuml_command_regex_RegexLeaf(0,"[%s]*")

    @staticmethod
    def spaceOneOrMore():
        return com_plantuml_command_regex_RegexLeaf(0,"[%s]+")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.size = None
com_plantuml_command_regex_RegexLeaf._hx_class = com_plantuml_command_regex_RegexLeaf


class com_plantuml_command_regex_RegexOptional(com_plantuml_command_regex_AbstractRegex):
    _hx_class_name = "com.plantuml.command.regex.RegexOptional"
    __slots__ = ("orig",)
    _hx_fields = ["orig"]
    _hx_methods = ["getSize", "eat"]
    _hx_statics = []
    _hx_interfaces = [com_plantuml_command_regex_IRegex]
    _hx_super = com_plantuml_command_regex_AbstractRegex


    def __init__(self,orig):
        self.orig = orig
        self.pattern = (("(?:" + HxOverrides.stringOrNull(orig.getPattern())) + ")?")

    def getSize(self):
        return self.orig.getSize()

    def eat(self,array,_hx_map):
        s = (array[0] if 0 < len(array) else None)
        if (s is None):
            if (len(array) != 0):
                array.pop()
        self.orig.eat(array,_hx_map)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.orig = None
com_plantuml_command_regex_RegexOptional._hx_class = com_plantuml_command_regex_RegexOptional


class com_plantuml_core_Diagram:
    _hx_class_name = "com.plantuml.core.Diagram"
    __slots__ = ()
    _hx_methods = ["exportDiagramNow"]

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_core_Diagram._hx_class = com_plantuml_core_Diagram


class com_plantuml_cucadiagram_Display:
    _hx_class_name = "com.plantuml.cucadiagram.Display"
    __slots__ = ("label",)
    _hx_fields = ["label"]
    _hx_methods = ["getEndingStereotype", "removeEndingStereotype", "get", "toString"]
    _hx_statics = ["getWithNewlines"]

    def __init__(self,label):
        self.label = label

    def getEndingStereotype(self):
        return None

    def removeEndingStereotype(self):
        return self

    def get(self,i):
        return self.label

    def toString(self):
        return self.label

    @staticmethod
    def getWithNewlines(label):
        return com_plantuml_cucadiagram_Display(label)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.label = None
com_plantuml_cucadiagram_Display._hx_class = com_plantuml_cucadiagram_Display


class com_plantuml_graphic_StringBounder:
    _hx_class_name = "com.plantuml.graphic.StringBounder"
    __slots__ = ()
    _hx_methods = ["calculateDimension"]
com_plantuml_graphic_StringBounder._hx_class = com_plantuml_graphic_StringBounder


class com_plantuml_ugraphic_UShape:
    _hx_class_name = "com.plantuml.ugraphic.UShape"
    __slots__ = ()
com_plantuml_ugraphic_UShape._hx_class = com_plantuml_ugraphic_UShape


class com_plantuml_graphic_UDrawable:
    _hx_class_name = "com.plantuml.graphic.UDrawable"
    __slots__ = ()
    _hx_methods = ["drawU"]
com_plantuml_graphic_UDrawable._hx_class = com_plantuml_graphic_UDrawable


class com_plantuml_graphic_TextBlock:
    _hx_class_name = "com.plantuml.graphic.TextBlock"
    __slots__ = ()
    _hx_methods = ["calculateDimension"]
    _hx_interfaces = [com_plantuml_ugraphic_UShape, com_plantuml_graphic_UDrawable]
com_plantuml_graphic_TextBlock._hx_class = com_plantuml_graphic_TextBlock


class com_plantuml_graphic_TextBlockMarged:
    _hx_class_name = "com.plantuml.graphic.TextBlockMarged"
    __slots__ = ("textBlock", "top", "right", "bottom", "left")
    _hx_fields = ["textBlock", "top", "right", "bottom", "left"]
    _hx_methods = ["drawU", "calculateDimension"]
    _hx_interfaces = [com_plantuml_graphic_TextBlock]

    def __init__(self,textBlock,top,right,bottom,left):
        self.textBlock = textBlock
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def drawU(self,ug):
        translate = com_plantuml_ugraphic_UTranslate(self.left,self.top)
        self.textBlock.drawU(ug.apply(translate))

    def calculateDimension(self,stringBounder):
        dim = self.textBlock.calculateDimension(stringBounder)
        return dim.delta((self.left + self.right),(self.top + self.bottom))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.textBlock = None
        _hx_o.top = None
        _hx_o.right = None
        _hx_o.bottom = None
        _hx_o.left = None
com_plantuml_graphic_TextBlockMarged._hx_class = com_plantuml_graphic_TextBlockMarged


class com_plantuml_mindmap_Branch:
    _hx_class_name = "com.plantuml.mindmap.Branch"
    __slots__ = ("root", "last", "finger")
    _hx_fields = ["root", "last", "finger"]
    _hx_methods = ["hasRoot", "initRoot", "add", "getParentOfLast", "hasFinger", "hasChildren", "initFinger", "doNotDrawFirstPhalanx", "drawU", "getHalfThickness", "getFullElongation", "getX12"]
    _hx_interfaces = [com_plantuml_graphic_UDrawable]

    def __init__(self):
        self.finger = None
        self.last = None
        self.root = None

    def hasRoot(self):
        return (self.root is not None)

    def initRoot(self,styleBuilder,backColor,label,shape,stereotype):
        self.root = com_plantuml_mindmap_Idea.createIdeaSimple(styleBuilder,backColor,label,shape,stereotype)
        self.last = self.root

    def add(self,styleBuilder,backColor,level,label,shape,stereotype):
        if (self.last is None):
            return com_plantuml_command_CommandExecutionResult.ERROR("Check your indentation ?")
        if (level == ((self.last.getLevel() + 1))):
            newIdea = self.last.createIdea(styleBuilder,backColor,level,label,shape,stereotype)
            self.last = newIdea
            return com_plantuml_command_CommandExecutionResult.OK
        if (level <= self.last.getLevel()):
            diff = ((self.last.getLevel() - level) + 1)
            newIdea = self.getParentOfLast(diff).createIdea(styleBuilder,backColor,level,label,shape,stereotype)
            self.last = newIdea
            return com_plantuml_command_CommandExecutionResult.OK
        return com_plantuml_command_CommandExecutionResult.ERROR("error42L")

    def getParentOfLast(self,nb):
        result = self.last
        _g = 0
        _g1 = nb
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            result = result.getParent()
        return result

    def hasFinger(self):
        return (self.finger is not None)

    def hasChildren(self):
        return self.root.hasChildren()

    def initFinger(self,skinParam,direction):
        self.finger = com_plantuml_mindmap_FingerImpl.build(self.root,skinParam,direction)

    def doNotDrawFirstPhalanx(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/Branch.hx", 'lineNumber': 66, 'className': "com.plantuml.mindmap.Branch", 'methodName': "doNotDrawFirstPhalanx"}))

    def drawU(self,ug):
        if (self.finger is not None):
            self.finger.drawU(ug)

    def getHalfThickness(self,stringBounder):
        if (self.finger is None):
            return 0
        return (self.finger.getFullThickness(stringBounder) / 2)

    def getFullElongation(self,stringBounder):
        if (self.finger is None):
            return 0
        return self.finger.getFullElongation(stringBounder)

    def getX12(self,stringBounder):
        if (self.finger is None):
            return 0
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = self.finger
                if (Std.isOfType(_hx_local_0,com_plantuml_mindmap_FingerImpl) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return (self.finger.getFullElongation(stringBounder) + (_hx_local_1()).getX12())
        return _hx_local_2()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
        _hx_o.last = None
        _hx_o.finger = None
com_plantuml_mindmap_Branch._hx_class = com_plantuml_mindmap_Branch


class com_plantuml_mindmap_CommandMindMapDirection(com_plantuml_command_SingleLineCommand):
    _hx_class_name = "com.plantuml.mindmap.CommandMindMapDirection"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["executeArg"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = com_plantuml_command_SingleLineCommand


    def __init__(self):
        self._init([com_plantuml_command_regex_RegexLeaf.start(), com_plantuml_command_regex_RegexLeaf(0,"[^*]*"), com_plantuml_command_regex_RegexLeaf(0,"\\b"), com_plantuml_command_regex_RegexLeaf(1,"(left|right)","DIRECTION"), com_plantuml_command_regex_RegexLeaf(0,"\\b"), com_plantuml_command_regex_RegexLeaf(0,"[^*]*"), com_plantuml_command_regex_RegexLeaf.end()])

    def executeArg(self,diagram,lines,_hx_map):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/CommandMindMapDirection.hx", 'lineNumber': 21, 'className': "com.plantuml.mindmap.CommandMindMapDirection", 'methodName': "executeArg"}))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_mindmap_CommandMindMapDirection._hx_class = com_plantuml_mindmap_CommandMindMapDirection


class com_plantuml_mindmap_CommandMindMapOrgmode(com_plantuml_command_SingleLineCommand):
    _hx_class_name = "com.plantuml.mindmap.CommandMindMapOrgmode"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["executeArg"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = com_plantuml_command_SingleLineCommand


    def __init__(self):
        self._init([com_plantuml_command_regex_RegexLeaf.start(), com_plantuml_command_regex_RegexLeaf(1,"([ \t]*[*]+)","TYPE"), com_plantuml_command_regex_RegexOptional(com_plantuml_command_regex_RegexLeaf(1,"\\[(#\\w+)\\]","BACKCOLOR")), com_plantuml_command_regex_RegexLeaf(1,"(_)?","SHAPE"), com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(), com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"), com_plantuml_command_regex_RegexLeaf.end()])

    def executeArg(self,diagram_,lines,arg):
        def _hx_local_1():
            _hx_local_0 = diagram_
            if (Std.isOfType(_hx_local_0,com_plantuml_mindmap_MindMapDiagram) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        diagram = _hx_local_1()
        _hx_type = arg.h.get("TYPE",None)
        label = arg.h.get("LABEL",None)
        stringColor = arg.h.get("BACKCOLOR",None)
        backColor = None
        shape = com_plantuml_mindmap_IdeaShapeUtils.fromDesc(arg.h.get("SHAPE",None))
        return diagram.addIdea(backColor,diagram.getSmartLevel(_hx_type),com_plantuml_cucadiagram_Display.getWithNewlines(label),shape)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_mindmap_CommandMindMapOrgmode._hx_class = com_plantuml_mindmap_CommandMindMapOrgmode


class com_plantuml_mindmap_CommandMindMapPlus(com_plantuml_command_SingleLineCommand):
    _hx_class_name = "com.plantuml.mindmap.CommandMindMapPlus"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["executeArg"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = com_plantuml_command_SingleLineCommand


    def __init__(self):
        self._init([com_plantuml_command_regex_RegexLeaf.start(), com_plantuml_command_regex_RegexLeaf(1,"([+-]+)","TYPE"), com_plantuml_command_regex_RegexOptional(com_plantuml_command_regex_RegexLeaf(1,"\\[(#\\w+)\\]","BACKCOLOR")), com_plantuml_command_regex_RegexLeaf(1,"(_)?","SHAPE"), com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(), com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"), com_plantuml_command_regex_RegexLeaf.end()])

    def executeArg(self,diagram,lines,_hx_map):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/CommandMindMapPlus.hx", 'lineNumber': 21, 'className': "com.plantuml.mindmap.CommandMindMapPlus", 'methodName': "executeArg"}))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_mindmap_CommandMindMapPlus._hx_class = com_plantuml_mindmap_CommandMindMapPlus


class com_plantuml_mindmap_CommandMindMapRoot(com_plantuml_command_SingleLineCommand):
    _hx_class_name = "com.plantuml.mindmap.CommandMindMapRoot"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["executeArg"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = com_plantuml_command_SingleLineCommand


    def __init__(self):
        self._init([com_plantuml_command_regex_RegexLeaf.start(), com_plantuml_command_regex_RegexLeaf(1,"(0)","TYPE"), com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(), com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"), com_plantuml_command_regex_RegexLeaf.end()])

    def executeArg(self,diagram,lines,_hx_map):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/CommandMindMapRoot.hx", 'lineNumber': 19, 'className': "com.plantuml.mindmap.CommandMindMapRoot", 'methodName': "executeArg"}))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_mindmap_CommandMindMapRoot._hx_class = com_plantuml_mindmap_CommandMindMapRoot


class com_plantuml_mindmap_Finger:
    _hx_class_name = "com.plantuml.mindmap.Finger"
    __slots__ = ()
    _hx_methods = ["getPhalanxThickness", "getNailThickness", "getFullThickness", "getPhalanxElongation", "getNailElongation", "getFullElongation", "doNotDrawFirstPhalanx"]
    _hx_interfaces = [com_plantuml_graphic_UDrawable]
com_plantuml_mindmap_Finger._hx_class = com_plantuml_mindmap_Finger


class com_plantuml_mindmap_FingerImpl:
    _hx_class_name = "com.plantuml.mindmap.FingerImpl"
    __slots__ = ("label", "backColor", "stereotype", "skinParam", "styleBuilder", "shape", "direction", "level", "drawPhalanx", "marginLeft", "marginRight", "marginTop", "marginBottom", "nail", "tetris")
    _hx_fields = ["label", "backColor", "stereotype", "skinParam", "styleBuilder", "shape", "direction", "level", "drawPhalanx", "marginLeft", "marginRight", "marginTop", "marginBottom", "nail", "tetris"]
    _hx_methods = ["drawU", "getPhalanxThickness", "getNailThickness", "getFullThickness", "getPhalanxElongation", "getNailElongation", "getFullElongation", "doNotDrawFirstPhalanx", "getX12", "addInNail", "getPhalanx", "getTetris", "asSymetricalTee", "getX1", "getX2", "drawLine"]
    _hx_statics = ["build"]
    _hx_interfaces = [com_plantuml_graphic_UDrawable, com_plantuml_mindmap_Finger]

    def __init__(self,styleBuilder,backColor,label,skinParam,shape,direction,level,stereotype):
        self.tetris = None
        self.nail = []
        self.marginBottom = 10.0
        self.marginTop = 10.0
        self.marginRight = 10.0
        self.marginLeft = 10.0
        self.drawPhalanx = True
        self.backColor = backColor
        self.stereotype = stereotype
        self.level = level
        self.label = label
        self.skinParam = skinParam
        self.styleBuilder = styleBuilder
        self.shape = shape
        self.direction = direction

    def drawU(self,ug):
        stringBounder = ug.getStringBounder()
        phalanx = self.getPhalanx()
        dimPhalanx = phalanx.calculateDimension(stringBounder)
        if self.drawPhalanx:
            posY = (-self.getPhalanxThickness(stringBounder) / 2)
            posX = (0 if ((self.direction == com_plantuml_Direction.RIGHT)) else -dimPhalanx.getWidth())
            phalanx.drawU(ug.apply(com_plantuml_ugraphic_UTranslate(posX,posY)))
        p1 = com_plantuml_awt_geom_Point2D((dimPhalanx.getWidth() if ((self.direction == com_plantuml_Direction.RIGHT)) else -dimPhalanx.getWidth()),0)
        _g = 0
        _g1 = len(self.nail)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            child = (self.nail[i] if i >= 0 and i < len(self.nail) else None)
            stp = python_internal_ArrayImpl._get(self.getTetris(stringBounder).getElements(), i)
            x = ((dimPhalanx.getWidth() + self.getX12()) if ((self.direction == com_plantuml_Direction.RIGHT)) else (-dimPhalanx.getWidth() - self.getX12()))
            p2 = com_plantuml_awt_geom_Point2D(x,stp.getY())
            child.drawU(ug.apply(p2.asTranslate()))
            self.drawLine(ug,p1,p2)

    def getPhalanxThickness(self,stringBounder):
        return self.getPhalanx().calculateDimension(stringBounder).getHeight()

    def getNailThickness(self,stringBounder):
        return self.getTetris(stringBounder).getHeight()

    def getFullThickness(self,stringBounder):
        thickness1 = self.getPhalanxThickness(stringBounder)
        thickness2 = self.getNailThickness(stringBounder)
        if python_lib_Math.isnan(thickness1):
            return thickness1
        elif python_lib_Math.isnan(thickness2):
            return thickness2
        else:
            return max(thickness1,thickness2)

    def getPhalanxElongation(self,stringBounder):
        return self.getPhalanx().calculateDimension(stringBounder).getWidth()

    def getNailElongation(self,stringBounder):
        return self.getTetris(stringBounder).getWidth()

    def getFullElongation(self,stringBounder):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/FingerImpl.hx", 'lineNumber': 80, 'className': "com.plantuml.mindmap.FingerImpl", 'methodName': "getFullElongation"}))

    def doNotDrawFirstPhalanx(self):
        pass

    def getX12(self):
        return (self.getX1() + self.getX2())

    def addInNail(self,child):
        _this = self.nail
        _this.append(child)

    def getPhalanx(self):
        if (self.drawPhalanx == False):
            return com_plantuml_ugraphic_TextBlockUtils.empty(0,0)
        if (self.shape == com_plantuml_mindmap_IdeaShape.BOX):
            box = com_plantuml_mindmap_FtileBoxOld.createMindMap(self.styleBuilder,self.label)
            return com_plantuml_ugraphic_TextBlockUtils.withMargin(box,0,0,self.marginTop,self.marginBottom)
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/FingerImpl.hx", 'lineNumber': 121, 'className': "com.plantuml.mindmap.FingerImpl", 'methodName': "getPhalanx"}))

    def getTetris(self,stringBounder):
        if (self.tetris is None):
            self.tetris = com_plantuml_mindmap_Tetris(self.label.get(0))
            _g = 0
            _g1 = self.nail
            while (_g < len(_g1)):
                child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                self.tetris.add(child.asSymetricalTee(stringBounder))
            self.tetris.balance()
        return self.tetris

    def asSymetricalTee(self,stringBounder):
        thickness1 = self.getPhalanxThickness(stringBounder)
        elongation1 = self.getPhalanxElongation(stringBounder)
        if (len(self.nail) == 0):
            return com_plantuml_mindmap_SymetricalTee(thickness1,elongation1,0,0)
        thickness2 = self.getNailThickness(stringBounder)
        elongation2 = self.getNailElongation(stringBounder)
        return com_plantuml_mindmap_SymetricalTee(thickness1,(elongation1 + self.getX1()),thickness2,(self.getX2() + elongation2))

    def getX1(self):
        return self.marginLeft

    def getX2(self):
        return (self.marginRight + 30)

    def drawLine(self,ug,p1,p2):
        path = com_plantuml_ugraphic_UPath()
        delta1 = (10 if ((self.direction == com_plantuml_Direction.RIGHT)) else -10)
        delta2 = (25 if ((self.direction == com_plantuml_Direction.RIGHT)) else -25)
        path.moveToPoint(p1)
        path.lineTo((p1.getX() + delta1),p1.getY())
        path.cubicTo((p1.getX() + delta2),p1.getY(),(p2.getX() - delta2),p2.getY(),(p2.getX() - delta1),p2.getY())
        path.lineToPoint(p2)
        ug.draw(path)

    @staticmethod
    def build(idea,skinParam,direction):
        result = com_plantuml_mindmap_FingerImpl(idea.getStyleBuilder(),idea.getBackColor(),idea.getLabel(),skinParam,idea.getShape(),direction,idea.getLevel(),idea.getStereotype())
        _g = 0
        _g1 = idea.getChildren()
        while (_g < len(_g1)):
            child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            result.addInNail(com_plantuml_mindmap_FingerImpl.build(child,skinParam,direction))
        return result

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.label = None
        _hx_o.backColor = None
        _hx_o.stereotype = None
        _hx_o.skinParam = None
        _hx_o.styleBuilder = None
        _hx_o.shape = None
        _hx_o.direction = None
        _hx_o.level = None
        _hx_o.drawPhalanx = None
        _hx_o.marginLeft = None
        _hx_o.marginRight = None
        _hx_o.marginTop = None
        _hx_o.marginBottom = None
        _hx_o.nail = None
        _hx_o.tetris = None
com_plantuml_mindmap_FingerImpl._hx_class = com_plantuml_mindmap_FingerImpl


class com_plantuml_mindmap_FtileBoxOld:
    _hx_class_name = "com.plantuml.mindmap.FtileBoxOld"
    __slots__ = ("padding", "label")
    _hx_fields = ["padding", "label"]
    _hx_methods = ["drawU", "getDimRaw", "calculateDimension"]
    _hx_statics = ["createMindMap"]
    _hx_interfaces = [com_plantuml_graphic_TextBlock]

    def __init__(self,label):
        self.label = label
        self.padding = com_plantuml_style_ClockwiseTopRightBottomLeft.same(10)

    def drawU(self,ug):
        dim2 = self.calculateDimension(ug.getStringBounder())
        ug.draw(com_plantuml_ugraphic_URectangle(dim2.getWidth(),dim2.getHeight()))
        ug = ug.apply(com_plantuml_ugraphic_UTranslate(self.padding.getLeft(),self.padding.getTop()))
        dim = self.getDimRaw(ug.getStringBounder())
        ug.draw(com_plantuml_ugraphic_UText(self.label.get(0)))

    def getDimRaw(self,stringBounder):
        return stringBounder.calculateDimension(com_plantuml_ugraphic_UFont(),self.label.get(0))

    def calculateDimension(self,stringBounder):
        dimRaw = self.getDimRaw(stringBounder)
        dimRaw = dimRaw.delta((self.padding.getLeft() + self.padding.getRight()),(self.padding.getBottom() + self.padding.getTop()))
        return dimRaw

    @staticmethod
    def createMindMap(styleBuilder,label):
        return com_plantuml_mindmap_FtileBoxOld(label)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.padding = None
        _hx_o.label = None
com_plantuml_mindmap_FtileBoxOld._hx_class = com_plantuml_mindmap_FtileBoxOld


class com_plantuml_mindmap_Idea:
    _hx_class_name = "com.plantuml.mindmap.Idea"
    __slots__ = ("label", "level", "parent", "children", "shape", "backColor", "styleBuilder", "stereotype")
    _hx_fields = ["label", "level", "parent", "children", "shape", "backColor", "styleBuilder", "stereotype"]
    _hx_methods = ["getLevel", "createIdea", "getParent", "hasChildren", "getStyleBuilder", "getBackColor", "getLabel", "getShape", "getStereotype", "getChildren"]
    _hx_statics = ["createIdeaSimple"]

    def __init__(self,styleBuilder,backColor,level,parent,label,shape,stereotype):
        self.children = []
        self.backColor = backColor
        self.styleBuilder = styleBuilder
        self.label = label
        self.level = level
        self.parent = parent
        self.shape = shape
        self.stereotype = stereotype

    def getLevel(self):
        return self.level

    def createIdea(self,styleBuilder,backColor,newLevel,newDisplay,newShape,stereotype):
        result = com_plantuml_mindmap_Idea(styleBuilder,backColor,newLevel,self,newDisplay,newShape,stereotype)
        _this = self.children
        _this.append(result)
        return result

    def getParent(self):
        return self.parent

    def hasChildren(self):
        return (len(self.children) > 0)

    def getStyleBuilder(self):
        return self.styleBuilder

    def getBackColor(self):
        return self.backColor

    def getLabel(self):
        return self.label

    def getShape(self):
        return self.shape

    def getStereotype(self):
        return self.stereotype

    def getChildren(self):
        return self.children

    @staticmethod
    def createIdeaSimple(styleBuilder,backColor,label,shape,stereotype):
        return com_plantuml_mindmap_Idea(styleBuilder,backColor,0,None,label,shape,stereotype)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.label = None
        _hx_o.level = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.shape = None
        _hx_o.backColor = None
        _hx_o.styleBuilder = None
        _hx_o.stereotype = None
com_plantuml_mindmap_Idea._hx_class = com_plantuml_mindmap_Idea

class com_plantuml_mindmap_IdeaShape(Enum):
    __slots__ = ()
    _hx_class_name = "com.plantuml.mindmap.IdeaShape"
    _hx_constructs = ["BOX", "NONE"]
com_plantuml_mindmap_IdeaShape.BOX = com_plantuml_mindmap_IdeaShape("BOX", 0, ())
com_plantuml_mindmap_IdeaShape.NONE = com_plantuml_mindmap_IdeaShape("NONE", 1, ())
com_plantuml_mindmap_IdeaShape._hx_class = com_plantuml_mindmap_IdeaShape


class com_plantuml_mindmap_IdeaShapeUtils:
    _hx_class_name = "com.plantuml.mindmap.IdeaShapeUtils"
    __slots__ = ()
    _hx_statics = ["fromDesc"]

    @staticmethod
    def fromDesc(s):
        if ("_" == s):
            return com_plantuml_mindmap_IdeaShape.NONE
        return com_plantuml_mindmap_IdeaShape.BOX
com_plantuml_mindmap_IdeaShapeUtils._hx_class = com_plantuml_mindmap_IdeaShapeUtils


class com_plantuml_mindmap_MindMap:
    _hx_class_name = "com.plantuml.mindmap.MindMap"
    __slots__ = ("left", "right", "skinParam")
    _hx_fields = ["left", "right", "skinParam"]
    _hx_methods = ["isFull", "addIdeaInternal", "drawU", "computeFinger"]

    def __init__(self,skinParam):
        self.right = com_plantuml_mindmap_Branch()
        self.left = com_plantuml_mindmap_Branch()
        self.skinParam = skinParam

    def isFull(self,level):
        if (level == 0):
            return self.right.hasRoot()
        else:
            return False

    def addIdeaInternal(self,stereotype,backColor,level,label,shape,direction):
        if ((self.left.hasRoot() == False) and ((self.right.hasRoot() == False))):
            level = 0
        if (level == 0):
            self.right.initRoot(self.skinParam.getCurrentStyleBuilder(),backColor,label,shape,stereotype)
            self.left.initRoot(self.skinParam.getCurrentStyleBuilder(),backColor,label,shape,stereotype)
            return com_plantuml_command_CommandExecutionResult.OK
        if (direction == com_plantuml_Direction.LEFT):
            return self.left.add(self.skinParam.getCurrentStyleBuilder(),backColor,level,label,shape,stereotype)
        return self.right.add(self.skinParam.getCurrentStyleBuilder(),backColor,level,label,shape,stereotype)

    def drawU(self,ug):
        if ((self.left.hasRoot() == False) and ((self.right.hasRoot() == False))):
            return
        self.computeFinger()
        stringBounder = ug.getStringBounder()
        y1 = self.right.getHalfThickness(stringBounder)
        y2 = self.left.getHalfThickness(stringBounder)
        y = (y1 if (python_lib_Math.isnan(y1)) else (y2 if (python_lib_Math.isnan(y2)) else max(y1,y2)))
        x = self.left.getX12(stringBounder)
        self.right.drawU(ug.apply(com_plantuml_ugraphic_UTranslate(x,y)))
        self.left.drawU(ug.apply(com_plantuml_ugraphic_UTranslate(x,y)))

    def computeFinger(self):
        if ((self.left.hasFinger() == False) and ((self.right.hasFinger() == False))):
            if self.left.hasChildren():
                self.left.initFinger(self.skinParam,com_plantuml_Direction.LEFT)
            if ((self.left.hasFinger() == False) or self.right.hasChildren()):
                self.right.initFinger(self.skinParam,com_plantuml_Direction.RIGHT)
            if (self.left.hasFinger() and self.right.hasFinger()):
                self.left.doNotDrawFirstPhalanx()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.left = None
        _hx_o.right = None
        _hx_o.skinParam = None
com_plantuml_mindmap_MindMap._hx_class = com_plantuml_mindmap_MindMap


class com_plantuml_mindmap_MindMapDiagram(com_plantuml_core_Diagram):
    _hx_class_name = "com.plantuml.mindmap.MindMapDiagram"
    __slots__ = ("first", "mindmaps", "defaultDirection")
    _hx_fields = ["first", "mindmaps", "defaultDirection"]
    _hx_methods = ["getSmartLevel", "last", "getSkinParam", "addIdea", "exportDiagramNow"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = com_plantuml_core_Diagram


    def __init__(self):
        self.mindmaps = None
        self.first = None
        self.defaultDirection = com_plantuml_Direction.RIGHT
        self.mindmaps = [com_plantuml_mindmap_MindMap(self.getSkinParam())]

    def getSmartLevel(self,_hx_type):
        if (self.first is None):
            self.first = _hx_type
        if hx_strings_Strings.endsWith(_hx_type,"**"):
            _hx_type = hx_strings_Strings.trim(hx_strings_Strings.replaceAll(_hx_type,"\t"," "))
        _hx_type = hx_strings_Strings.replaceAll(_hx_type,"\t"," ")
        tmp = None
        if (_hx_type is None):
            tmp = False
        else:
            startIndex = None
            tmp = (((_hx_type.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(_hx_type," ",startIndex))) > -1)
        if (tmp == False):
            return (len(_hx_type) - 1)
        if hx_strings_Strings.endsWith(_hx_type,self.first):
            return (len(_hx_type) - len(self.first))
        if (len(hx_strings_Strings.trim(_hx_type)) == 1):
            return (len(_hx_type) - 1)
        if hx_strings_Strings.startsWith(_hx_type,self.first):
            return (len(_hx_type) - len(self.first))
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/MindMapDiagram.hx", 'lineNumber': 41, 'className': "com.plantuml.mindmap.MindMapDiagram", 'methodName': "getSmartLevel"}))

    def last(self):
        return python_internal_ArrayImpl._get(self.mindmaps, (len(self.mindmaps) - 1))

    def getSkinParam(self):
        return com_plantuml_SkinParam()

    def addIdea(self,backColor,level,label,shape,direction = None):
        stereotype = label.getEndingStereotype()
        if (stereotype is not None):
            label = label.removeEndingStereotype()
        if self.last().isFull(level):
            _this = self.mindmaps
            x = com_plantuml_mindmap_MindMap(self.getSkinParam())
            _this.append(x)
        if (direction is None):
            direction = self.defaultDirection
        return self.last().addIdeaInternal(stereotype,backColor,level,label,shape,direction)

    def exportDiagramNow(self,ug):
        _g = 0
        _g1 = self.mindmaps
        while (_g < len(_g1)):
            mindmap = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            mindmap.drawU(ug)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.first = None
        _hx_o.mindmaps = None
        _hx_o.defaultDirection = None
com_plantuml_mindmap_MindMapDiagram._hx_class = com_plantuml_mindmap_MindMapDiagram


class com_plantuml_mindmap_MindMapDiagramFactory:
    _hx_class_name = "com.plantuml.mindmap.MindMapDiagramFactory"
    __slots__ = ("cmds",)
    _hx_fields = ["cmds"]
    _hx_methods = ["createCommands", "getCandidate", "createSystem"]

    def __init__(self):
        self.cmds = None
        self.cmds = self.createCommands()

    def createCommands(self):
        cmds = []
        x = com_plantuml_mindmap_CommandMindMapOrgmode()
        cmds.append(x)
        x = com_plantuml_mindmap_CommandMindMapRoot()
        cmds.append(x)
        x = com_plantuml_mindmap_CommandMindMapPlus()
        cmds.append(x)
        x = com_plantuml_mindmap_CommandMindMapDirection()
        cmds.append(x)
        return cmds

    def getCandidate(self,s):
        _g = 0
        _g1 = self.cmds
        while (_g < len(_g1)):
            cmd = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (cmd.isValid(com_plantuml_command_BlocLines.single(s)) == com_plantuml_command_CommandControl.OK):
                return cmd
        return None

    def createSystem(self,lines):
        diagram = com_plantuml_mindmap_MindMapDiagram()
        _g = 0
        _g1 = lines.getLines()
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((s == "") or hx_strings_Strings.startsWith(s,"@start")) or hx_strings_Strings.startsWith(s,"@end")):
                continue
            cmd = self.getCandidate(s)
            if (cmd is None):
                raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/MindMapDiagramFactory.hx", 'lineNumber': 44, 'className': "com.plantuml.mindmap.MindMapDiagramFactory", 'methodName': "createSystem"}))
            _hx_exec = cmd.execute(diagram,com_plantuml_command_BlocLines.single(s))
        return diagram

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.cmds = None
com_plantuml_mindmap_MindMapDiagramFactory._hx_class = com_plantuml_mindmap_MindMapDiagramFactory


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()
    _hx_methods = ["get", "set", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
haxe_IMap._hx_class = haxe_IMap


class haxe_ds_BalancedTree:
    _hx_class_name = "haxe.ds.BalancedTree"
    __slots__ = ("root",)
    _hx_fields = ["root"]
    _hx_methods = ["set", "get", "remove", "exists", "iterator", "keyValueIterator", "keys", "copy", "setLoop", "removeLoop", "keysLoop", "merge", "minBinding", "removeMinBinding", "balance", "compare", "toString", "clear"]
    _hx_statics = ["iteratorLoop"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.root = None

    def set(self,key,value):
        self.root = self.setLoop(key,value,self.root)

    def get(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return node.value
            if (c < 0):
                node = node.left
            else:
                node = node.right
        return None

    def remove(self,key):
        try:
            self.root = self.removeLoop(key,self.root)
            return True
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),str):
                return False
            else:
                raise _g

    def exists(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return True
            elif (c < 0):
                node = node.left
            else:
                node = node.right
        return False

    def iterator(self):
        ret = []
        haxe_ds_BalancedTree.iteratorLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def keys(self):
        ret = []
        self.keysLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def copy(self):
        copied = haxe_ds_BalancedTree()
        copied.root = self.root
        return copied

    def setLoop(self,k,v,node):
        if (node is None):
            return haxe_ds_TreeNode(None,k,v,None)
        c = self.compare(k,node.key)
        if (c == 0):
            return haxe_ds_TreeNode(node.left,k,v,node.right,(0 if ((node is None)) else node._height))
        elif (c < 0):
            nl = self.setLoop(k,v,node.left)
            return self.balance(nl,node.key,node.value,node.right)
        else:
            nr = self.setLoop(k,v,node.right)
            return self.balance(node.left,node.key,node.value,nr)

    def removeLoop(self,k,node):
        if (node is None):
            raise haxe_Exception.thrown("Not_found")
        c = self.compare(k,node.key)
        if (c == 0):
            return self.merge(node.left,node.right)
        elif (c < 0):
            return self.balance(self.removeLoop(k,node.left),node.key,node.value,node.right)
        else:
            return self.balance(node.left,node.key,node.value,self.removeLoop(k,node.right))

    def keysLoop(self,node,acc):
        if (node is not None):
            self.keysLoop(node.left,acc)
            x = node.key
            acc.append(x)
            self.keysLoop(node.right,acc)

    def merge(self,t1,t2):
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1
        t = self.minBinding(t2)
        return self.balance(t1,t.key,t.value,self.removeMinBinding(t2))

    def minBinding(self,t):
        if (t is None):
            raise haxe_Exception.thrown("Not_found")
        elif (t.left is None):
            return t
        else:
            return self.minBinding(t.left)

    def removeMinBinding(self,t):
        if (t.left is None):
            return t.right
        else:
            return self.balance(self.removeMinBinding(t.left),t.key,t.value,t.right)

    def balance(self,l,k,v,r):
        hl = (0 if ((l is None)) else l._height)
        hr = (0 if ((r is None)) else r._height)
        if (hl > ((hr + 2))):
            _this = l.left
            _this1 = l.right
            if (((0 if ((_this is None)) else _this._height)) >= ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(l.left,l.key,l.value,haxe_ds_TreeNode(l.right,k,v,r))
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left,l.key,l.value,l.right.left),l.right.key,l.right.value,haxe_ds_TreeNode(l.right.right,k,v,r))
        elif (hr > ((hl + 2))):
            _this = r.right
            _this1 = r.left
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left),r.key,r.value,r.right)
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left.left),r.left.key,r.left.value,haxe_ds_TreeNode(r.left.right,r.key,r.value,r.right))
        else:
            return haxe_ds_TreeNode(l,k,v,r,(((hl if ((hl > hr)) else hr)) + 1))

    def compare(self,k1,k2):
        return Reflect.compare(k1,k2)

    def toString(self):
        if (self.root is None):
            return "{}"
        else:
            return (("{" + HxOverrides.stringOrNull(self.root.toString())) + "}")

    def clear(self):
        self.root = None

    @staticmethod
    def iteratorLoop(node,acc):
        if (node is not None):
            haxe_ds_BalancedTree.iteratorLoop(node.left,acc)
            x = node.value
            acc.append(x)
            haxe_ds_BalancedTree.iteratorLoop(node.right,acc)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree


class com_plantuml_mindmap_BalancedTreeStripe(haxe_ds_BalancedTree):
    _hx_class_name = "com.plantuml.mindmap.BalancedTreeStripe"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["compare", "size", "add"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_ds_BalancedTree


    def __init__(self):
        super().__init__()

    def compare(self,k1,k2):
        return Reflect.compare(k1.getStart(),k2.getStart())

    def size(self):
        cpt = 0
        k = self.keys()
        while k.hasNext():
            k1 = k.next()
            cpt = (cpt + 1)
        return cpt

    def add(self,key):
        self.set(key,True)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_mindmap_BalancedTreeStripe._hx_class = com_plantuml_mindmap_BalancedTreeStripe


class com_plantuml_mindmap_Stripe:
    _hx_class_name = "com.plantuml.mindmap.Stripe"
    __slots__ = ("x1", "x2", "value")
    _hx_fields = ["x1", "x2", "value"]
    _hx_methods = ["contains", "toString", "getValue", "getStart", "getEnd"]

    def __init__(self,x1,x2,value):
        if (x2 <= x1):
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/Stripe.hx", 'lineNumber': 29, 'className': "com.plantuml.mindmap.Stripe", 'methodName': "new"}))
        self.x1 = x1
        self.x2 = x2
        self.value = value

    def contains(self,x):
        if (x >= self.x1):
            return (x <= self.x2)
        else:
            return False

    def toString(self):
        return (((((("" + Std.string(self.x1)) + "->") + Std.string(self.x2)) + " (") + Std.string(self.value)) + ")")

    def getValue(self):
        return self.value

    def getStart(self):
        return self.x1

    def getEnd(self):
        return self.x2

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x1 = None
        _hx_o.x2 = None
        _hx_o.value = None
com_plantuml_mindmap_Stripe._hx_class = com_plantuml_mindmap_Stripe


class com_plantuml_mindmap_StripeFrontier:
    _hx_class_name = "com.plantuml.mindmap.StripeFrontier"
    __slots__ = ("stripes",)
    _hx_fields = ["stripes"]
    _hx_methods = ["isEmpty", "addSegment", "collisionning", "addSingleInternal", "getContact"]

    def __init__(self):
        self.stripes = com_plantuml_mindmap_BalancedTreeStripe()
        self.stripes.set(com_plantuml_mindmap_Stripe(-com_plantuml_mindmap_Tetris.MAX_VALUE,com_plantuml_mindmap_Tetris.MAX_VALUE,-com_plantuml_mindmap_Tetris.MAX_VALUE),True)

    def isEmpty(self):
        return (self.stripes.size() == 1)

    def addSegment(self,x1,x2,value):
        if (x2 <= x1):
            haxe_Log.trace(("x1=" + Std.string(x1)),_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/StripeFrontier.hx", 'lineNumber': 19, 'className': "com.plantuml.mindmap.StripeFrontier", 'methodName': "addSegment"}))
            haxe_Log.trace(("x2=" + Std.string(x2)),_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/StripeFrontier.hx", 'lineNumber': 20, 'className': "com.plantuml.mindmap.StripeFrontier", 'methodName': "addSegment"}))
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/StripeFrontier.hx", 'lineNumber': 21, 'className': "com.plantuml.mindmap.StripeFrontier", 'methodName': "addSegment"}))
        collisions = self.collisionning(x1,x2)
        if (collisions.size() > 1):
            it = collisions.keys()
            it.next()
            x = x1
            while it.hasNext():
                tmp = it.next()
                self.addSegment(x,tmp.getStart(),value)
                x = tmp.getStart()
            self.addSegment(x,x2,value)
        else:
            touch = collisions.keys().next()
            self.addSingleInternal(x1,x2,value,touch)

    def collisionning(self,x1,x2):
        result = com_plantuml_mindmap_BalancedTreeStripe()
        stripe = self.stripes.keys()
        while stripe.hasNext():
            stripe1 = stripe.next()
            if (x1 >= stripe1.getEnd()):
                continue
            result.add(stripe1)
            if (x2 <= stripe1.getEnd()):
                return result
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/StripeFrontier.hx", 'lineNumber': 49, 'className': "com.plantuml.mindmap.StripeFrontier", 'methodName': "collisionning"}))

    def addSingleInternal(self,x1,x2,value,touch):
        if (value <= touch.getValue()):
            return
        ok = self.stripes.remove(touch)
        if (not ok):
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/StripeFrontier.hx", 'lineNumber': 58, 'className': "com.plantuml.mindmap.StripeFrontier", 'methodName': "addSingleInternal"}))
        if (touch.getStart() != x1):
            self.stripes.add(com_plantuml_mindmap_Stripe(touch.getStart(),x1,touch.getValue()))
        self.stripes.add(com_plantuml_mindmap_Stripe(x1,x2,value))
        if (x2 != touch.getEnd()):
            self.stripes.add(com_plantuml_mindmap_Stripe(x2,touch.getEnd(),touch.getValue()))

    def getContact(self,x1,x2):
        collisions = self.collisionning(x1,x2)
        result = -com_plantuml_mindmap_Tetris.MAX_VALUE
        strip = collisions.keys()
        while strip.hasNext():
            strip1 = strip.next()
            b = strip1.getValue()
            if (not python_lib_Math.isnan(result)):
                result = (b if (python_lib_Math.isnan(b)) else max(result,b))
        return result

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stripes = None
com_plantuml_mindmap_StripeFrontier._hx_class = com_plantuml_mindmap_StripeFrontier


class com_plantuml_mindmap_SymetricalTee:
    _hx_class_name = "com.plantuml.mindmap.SymetricalTee"
    __slots__ = ("thickness1", "elongation1", "thickness2", "elongation2")
    _hx_fields = ["thickness1", "elongation1", "thickness2", "elongation2"]
    _hx_methods = ["getThickness1", "getElongation1", "getThickness2", "getElongation2", "getFullElongation", "getFullThickness"]

    def __init__(self,thickness1,elongation1,thickness2,elongation2):
        self.thickness1 = thickness1
        self.elongation1 = elongation1
        self.thickness2 = thickness2
        self.elongation2 = elongation2

    def getThickness1(self):
        return self.thickness1

    def getElongation1(self):
        return self.elongation1

    def getThickness2(self):
        return self.thickness2

    def getElongation2(self):
        return self.elongation2

    def getFullElongation(self):
        return (self.elongation1 + self.elongation2)

    def getFullThickness(self):
        a = self.thickness1
        b = self.thickness2
        if python_lib_Math.isnan(a):
            return a
        elif python_lib_Math.isnan(b):
            return b
        else:
            return max(a,b)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.thickness1 = None
        _hx_o.elongation1 = None
        _hx_o.thickness2 = None
        _hx_o.elongation2 = None
com_plantuml_mindmap_SymetricalTee._hx_class = com_plantuml_mindmap_SymetricalTee


class com_plantuml_mindmap_SymetricalTeePositioned:
    _hx_class_name = "com.plantuml.mindmap.SymetricalTeePositioned"
    __slots__ = ("tee", "y")
    _hx_fields = ["tee", "y"]
    _hx_methods = ["getSegmentA1", "getSegmentB1", "getSegmentA2", "getSegmentB2", "moveSoThatSegmentA1isOn", "moveSoThatSegmentA2isOn", "getMax", "getMaxY", "getMinY", "getY", "move", "getMaxX"]
    _hx_statics = ["create"]

    def __init__(self,tee,y):
        self.tee = tee
        self.y = y

    def getSegmentA1(self):
        return com_plantuml_awt_geom_Line2D(0,(self.y - ((self.tee.getThickness1() / 2))),self.tee.getElongation1(),(self.y - ((self.tee.getThickness1() / 2))))

    def getSegmentB1(self):
        return com_plantuml_awt_geom_Line2D(0,(self.y + ((self.tee.getThickness1() / 2))),self.tee.getElongation1(),(self.y + ((self.tee.getThickness1() / 2))))

    def getSegmentA2(self):
        return com_plantuml_awt_geom_Line2D(self.tee.getElongation1(),(self.y - ((self.tee.getThickness2() / 2))),(self.tee.getElongation1() + self.tee.getElongation2()),(self.y - ((self.tee.getThickness2() / 2))))

    def getSegmentB2(self):
        return com_plantuml_awt_geom_Line2D(self.tee.getElongation1(),(self.y + ((self.tee.getThickness2() / 2))),(self.tee.getElongation1() + self.tee.getElongation2()),(self.y + ((self.tee.getThickness2() / 2))))

    def moveSoThatSegmentA1isOn(self,newY):
        current = self.getSegmentA1().getY1()
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.y
        _hx_local_0.y = (_hx_local_1 + ((newY - current)))
        _hx_local_0.y

    def moveSoThatSegmentA2isOn(self,newY):
        current = self.getSegmentA2().getY1()
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.y
        _hx_local_0.y = (_hx_local_1 + ((newY - current)))
        _hx_local_0.y

    def getMax(self,other):
        if (self.tee != other.tee):
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/SymetricalTeePositioned.hx", 'lineNumber': 52, 'className': "com.plantuml.mindmap.SymetricalTeePositioned", 'methodName': "getMax"}))
        if (other.y > self.y):
            return other
        return self

    def getMaxY(self):
        tmp = self.y
        a = (self.tee.getThickness1() / 2)
        b = (self.tee.getThickness2() / 2)
        return (tmp + ((a if (python_lib_Math.isnan(a)) else (b if (python_lib_Math.isnan(b)) else max(a,b)))))

    def getMinY(self):
        tmp = self.y
        a = (self.tee.getThickness1() / 2)
        b = (self.tee.getThickness2() / 2)
        return (tmp - ((a if (python_lib_Math.isnan(a)) else (b if (python_lib_Math.isnan(b)) else max(a,b)))))

    def getY(self):
        return self.y

    def move(self,delta):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.y
        _hx_local_0.y = (_hx_local_1 + delta)
        _hx_local_0.y

    def getMaxX(self):
        return (self.tee.getElongation1() + self.tee.getElongation2())

    @staticmethod
    def create(tee):
        return com_plantuml_mindmap_SymetricalTeePositioned(tee,0)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tee = None
        _hx_o.y = None
com_plantuml_mindmap_SymetricalTeePositioned._hx_class = com_plantuml_mindmap_SymetricalTeePositioned


class com_plantuml_mindmap_Tetris:
    _hx_class_name = "com.plantuml.mindmap.Tetris"
    __slots__ = ("frontier", "elements", "minY", "maxY", "name")
    _hx_fields = ["frontier", "elements", "minY", "maxY", "name"]
    _hx_methods = ["add", "getHeight", "balance", "addInternal", "getElements", "getWidth"]
    _hx_statics = ["MAX_VALUE"]

    def __init__(self,name):
        self.maxY = -com_plantuml_mindmap_Tetris.MAX_VALUE
        self.minY = com_plantuml_mindmap_Tetris.MAX_VALUE
        self.elements = []
        self.frontier = com_plantuml_mindmap_StripeFrontier()
        self.name = name

    def add(self,tee):
        if self.frontier.isEmpty():
            p1 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee)
            self.addInternal(p1)
            return
        c1 = self.frontier.getContact(0,tee.getElongation1())
        c2 = self.frontier.getContact(tee.getElongation1(),(tee.getElongation1() + tee.getElongation2()))
        p1 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee)
        p1.moveSoThatSegmentA1isOn(c1)
        p2 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee)
        p2.moveSoThatSegmentA2isOn(c2)
        result = p1.getMax(p2)
        self.addInternal(result)

    def getHeight(self):
        if (len(self.elements) == 0):
            return 0
        return (self.maxY - self.minY)

    def balance(self):
        if (len(self.elements) == 0):
            return
        if (self.minY != com_plantuml_mindmap_Tetris.MAX_VALUE):
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/mindmap/Tetris.hx", 'lineNumber': 55, 'className': "com.plantuml.mindmap.Tetris", 'methodName': "balance"}))
        _g = 0
        _g1 = self.elements
        while (_g < len(_g1)):
            element = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            a = self.minY
            b = element.getMinY()
            self.minY = (a if (python_lib_Math.isnan(a)) else (b if (python_lib_Math.isnan(b)) else min(a,b)))
            a1 = self.maxY
            b1 = element.getMaxY()
            self.maxY = (a1 if (python_lib_Math.isnan(a1)) else (b1 if (python_lib_Math.isnan(b1)) else max(a1,b1)))
        mean = (((self.minY + self.maxY)) / 2)
        _g = 0
        _g1 = self.elements
        while (_g < len(_g1)):
            stp = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            stp.move(-mean)

    def addInternal(self,result):
        _this = self.elements
        _this.append(result)
        b1 = result.getSegmentB1()
        self.frontier.addSegment(b1.getX1(),b1.getX2(),b1.getY1())
        b2 = result.getSegmentB2()
        if (b2.getX1() != b2.getX2()):
            self.frontier.addSegment(b2.getX1(),b2.getX2(),b2.getY1())

    def getElements(self):
        return self.elements

    def getWidth(self):
        result = 0
        _g = 0
        _g1 = self.elements
        while (_g < len(_g1)):
            tee = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b = tee.getMaxX()
            if (not python_lib_Math.isnan(result)):
                result = (b if (python_lib_Math.isnan(b)) else max(result,b))
        return result

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.frontier = None
        _hx_o.elements = None
        _hx_o.minY = None
        _hx_o.maxY = None
        _hx_o.name = None
com_plantuml_mindmap_Tetris._hx_class = com_plantuml_mindmap_Tetris


class com_plantuml_style_ClockwiseTopRightBottomLeft:
    _hx_class_name = "com.plantuml.style.ClockwiseTopRightBottomLeft"
    __slots__ = ("top", "right", "bottom", "left")
    _hx_fields = ["top", "right", "bottom", "left"]
    _hx_methods = ["getTop", "getRight", "getBottom", "getLeft"]
    _hx_statics = ["same", "none"]

    def __init__(self,top,right,bottom,left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def getTop(self):
        return self.top

    def getRight(self):
        return self.right

    def getBottom(self):
        return self.bottom

    def getLeft(self):
        return self.left

    @staticmethod
    def same(value):
        return com_plantuml_style_ClockwiseTopRightBottomLeft(value,value,value,value)

    @staticmethod
    def none():
        return com_plantuml_style_ClockwiseTopRightBottomLeft(0,0,0,0)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.top = None
        _hx_o.right = None
        _hx_o.bottom = None
        _hx_o.left = None
com_plantuml_style_ClockwiseTopRightBottomLeft._hx_class = com_plantuml_style_ClockwiseTopRightBottomLeft


class com_plantuml_style_StyleBuilder:
    _hx_class_name = "com.plantuml.style.StyleBuilder"
    __slots__ = ()

    def __init__(self):
        pass
com_plantuml_style_StyleBuilder._hx_class = com_plantuml_style_StyleBuilder


class com_plantuml_ugraphic_UDriver:
    _hx_class_name = "com.plantuml.ugraphic.UDriver"
    __slots__ = ()
    _hx_methods = ["draw"]
com_plantuml_ugraphic_UDriver._hx_class = com_plantuml_ugraphic_UDriver


class com_plantuml_svg_DriverPathSvg:
    _hx_class_name = "com.plantuml.svg.DriverPathSvg"
    __slots__ = ()
    _hx_methods = ["draw"]
    _hx_interfaces = [com_plantuml_ugraphic_UDriver]

    def __init__(self):
        pass

    def draw(self,shape2,x,y,mapper,param,object):
        def _hx_local_1():
            _hx_local_0 = shape2
            if (Std.isOfType(_hx_local_0,com_plantuml_ugraphic_UPath) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        shape = _hx_local_1()
        object.svgPath(x,y,shape,shape.getDeltaShadow())

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_svg_DriverPathSvg._hx_class = com_plantuml_svg_DriverPathSvg


class com_plantuml_svg_DriverRectangleSvg:
    _hx_class_name = "com.plantuml.svg.DriverRectangleSvg"
    __slots__ = ()
    _hx_methods = ["draw"]
    _hx_interfaces = [com_plantuml_ugraphic_UDriver]

    def __init__(self):
        pass

    def draw(self,shape,x,y,mapper,param,object):
        def _hx_local_1():
            _hx_local_0 = shape
            if (Std.isOfType(_hx_local_0,com_plantuml_ugraphic_URectangle) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        rect = _hx_local_1()
        width = rect.getWidth()
        height = rect.getHeight()
        rx = 0
        ry = 0
        object.svgRectangle(x,y,width,height,(rx / 2),(ry / 2),rect.getDeltaShadow(),rect.getComment(),rect.getCodeLine())

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_svg_DriverRectangleSvg._hx_class = com_plantuml_svg_DriverRectangleSvg


class com_plantuml_svg_DriverTextSvg:
    _hx_class_name = "com.plantuml.svg.DriverTextSvg"
    __slots__ = ()
    _hx_methods = ["draw"]
    _hx_interfaces = [com_plantuml_ugraphic_UDriver]

    def __init__(self):
        pass

    def draw(self,shape,x,y,mapper,param,object):
        def _hx_local_1():
            _hx_local_0 = shape
            if (Std.isOfType(_hx_local_0,com_plantuml_ugraphic_UText) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        text = _hx_local_1()
        object.text(text.getText(),x,(y + 12),"",16,"","plain","",100,haxe_ds_StringMap(),"")

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_svg_DriverTextSvg._hx_class = com_plantuml_svg_DriverTextSvg


class com_plantuml_svg_SvgGraphics:
    _hx_class_name = "com.plantuml.svg.SvgGraphics"
    __slots__ = ("root", "defs", "gRoot")
    _hx_fields = ["root", "defs", "gRoot"]
    _hx_methods = ["text", "svgRectangle", "createRectangleInternal", "getG", "format", "toSvg", "fillMe", "getStyleSpecial", "getStyle", "svgPath"]

    def __init__(self):
        self.gRoot = Xml.createElement("g")
        self.defs = Xml.createElement("defs")
        self.root = Xml.createElement("svg")
        self.root.set("xmlns","http://www.w3.org/2000/svg")
        self.root.set("xmlns:xlink","http://www.w3.org/1999/xlink")
        self.root.set("version","1.1")
        maxXscaled = 800
        maxYscaled = 800
        style = (((("width:" + Std.string(maxXscaled)) + " px;height: ") + Std.string(maxYscaled)) + " + px;")
        self.root.set("style",style)
        self.root.set("width",(("" + Std.string(maxXscaled)) + "px"))
        self.root.set("height",(("" + Std.string(maxYscaled)) + "px"))
        self.root.addChild(self.defs)
        self.root.addChild(self.gRoot)

    def text(self,text,x,y,fontFamily,fontSize,fontWeight,fontStyle,textDecoration,textLength,attributes,textBackColor):
        elt = Xml.createElement("text")
        elt.set("x",self.format(x))
        elt.set("y",self.format(y))
        elt.set("font-size",self.format(fontSize))
        elt.addChild(Xml.createCData(text))
        self.getG().addChild(elt)

    def svgRectangle(self,x,y,width,height,rx,ry,deltaShadow,id,codeLine):
        elt = self.createRectangleInternal(x,y,width,height)
        self.getG().addChild(elt)

    def createRectangleInternal(self,x,y,width,height):
        elt = Xml.createElement("rect")
        elt.set("x",self.format(x))
        elt.set("y",self.format(y))
        elt.set("width",self.format(width))
        elt.set("height",self.format(height))
        self.fillMe(elt)
        elt.set("style",self.getStyleSpecial())
        return elt

    def getG(self):
        return self.gRoot

    def format(self,x):
        return Std.string(x)

    def toSvg(self):
        return haxe_xml_Printer.print(self.root)

    def fillMe(self,elt):
        elt.set("fill","white")

    def getStyleSpecial(self):
        style = hx_strings_StringBuilder()
        style.add("stroke:black;")
        return style.toString()

    def getStyle(self):
        style = hx_strings_StringBuilder()
        style.add("stroke:black;")
        style.add("fill:none;")
        return style.toString()

    def svgPath(self,x,y,path,deltaShadow):
        sb = hx_strings_StringBuilder()
        _g = 0
        _g1 = path.getSegments()
        while (_g < len(_g1)):
            seg = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            _hx_type = seg.getSegmentType()
            coord = seg.getCoord()
            if (_hx_type == com_plantuml_ugraphic_USegmentType.SEG_MOVETO):
                sb.add((((("M" + HxOverrides.stringOrNull(self.format(((coord[0] if 0 < len(coord) else None) + x)))) + ",") + HxOverrides.stringOrNull(self.format(((coord[1] if 1 < len(coord) else None) + y)))) + " "))
            elif (_hx_type == com_plantuml_ugraphic_USegmentType.SEG_LINETO):
                sb.add((((("L" + HxOverrides.stringOrNull(self.format(((coord[0] if 0 < len(coord) else None) + x)))) + ",") + HxOverrides.stringOrNull(self.format(((coord[1] if 1 < len(coord) else None) + y)))) + " "))
            elif (_hx_type == com_plantuml_ugraphic_USegmentType.SEG_CUBICTO):
                sb.add((((((((((((("C" + HxOverrides.stringOrNull(self.format(((coord[0] if 0 < len(coord) else None) + x)))) + ",") + HxOverrides.stringOrNull(self.format(((coord[1] if 1 < len(coord) else None) + y)))) + " ") + HxOverrides.stringOrNull(self.format(((coord[2] if 2 < len(coord) else None) + x)))) + ",") + HxOverrides.stringOrNull(self.format(((coord[3] if 3 < len(coord) else None) + y)))) + " ") + HxOverrides.stringOrNull(self.format(((coord[4] if 4 < len(coord) else None) + x)))) + ",") + HxOverrides.stringOrNull(self.format(((coord[5] if 5 < len(coord) else None) + y)))) + " "))
            else:
                haxe_Log.trace(_hx_type,_hx_AnonObject({'fileName': "src/com/plantuml/svg/SvgGraphics.hx", 'lineNumber': 109, 'className': "com.plantuml.svg.SvgGraphics", 'methodName': "svgPath"}))
                raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/svg/SvgGraphics.hx", 'lineNumber': 110, 'className': "com.plantuml.svg.SvgGraphics", 'methodName': "svgPath"}))
        elt = Xml.createElement("path")
        elt.set("d",sb.toString())
        elt.set("style",self.getStyle())
        self.getG().addChild(elt)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
        _hx_o.defs = None
        _hx_o.gRoot = None
com_plantuml_svg_SvgGraphics._hx_class = com_plantuml_svg_SvgGraphics


class com_plantuml_ugraphic_UGraphic:
    _hx_class_name = "com.plantuml.ugraphic.UGraphic"
    __slots__ = ()
    _hx_methods = ["getStringBounder", "apply", "draw"]
com_plantuml_ugraphic_UGraphic._hx_class = com_plantuml_ugraphic_UGraphic


class com_plantuml_ugraphic_AbstractCommonUGraphic:
    _hx_class_name = "com.plantuml.ugraphic.AbstractCommonUGraphic"
    __slots__ = ("translate", "drivers")
    _hx_fields = ["translate", "drivers"]
    _hx_methods = ["getStringBounder", "draw", "getTranslateX", "getTranslateY", "apply", "copyUGraphic"]
    _hx_interfaces = [com_plantuml_ugraphic_UGraphic]

    def __init__(self):
        self.drivers = haxe_ds_StringMap()
        self.translate = com_plantuml_ugraphic_UTranslate(0,0)

    def getTranslateX(self):
        return self.translate.getDx()

    def getTranslateY(self):
        return self.translate.getDy()

    def apply(self,change):
        result = self.copyUGraphic()
        if Std.isOfType(change,com_plantuml_ugraphic_UTranslate):
            def _hx_local_1():
                _hx_local_0 = change
                if (Std.isOfType(_hx_local_0,com_plantuml_ugraphic_UTranslate) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            translate = _hx_local_1()
            result.translate = result.translate.compose(translate)
            return result
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/ugraphic/AbstractCommonUGraphic.hx", 'lineNumber': 23, 'className': "com.plantuml.ugraphic.AbstractCommonUGraphic", 'methodName': "apply"}))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.translate = None
        _hx_o.drivers = None
com_plantuml_ugraphic_AbstractCommonUGraphic._hx_class = com_plantuml_ugraphic_AbstractCommonUGraphic


class com_plantuml_ugraphic_Empty:
    _hx_class_name = "com.plantuml.ugraphic.Empty"
    __slots__ = ("width", "height")
    _hx_fields = ["width", "height"]
    _hx_methods = ["drawU", "calculateDimension"]
    _hx_interfaces = [com_plantuml_graphic_TextBlock]

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def drawU(self,ug):
        pass

    def calculateDimension(self,stringBounder):
        return com_plantuml_awt_geom_Dimension2D(self.width,self.height)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.width = None
        _hx_o.height = None
com_plantuml_ugraphic_Empty._hx_class = com_plantuml_ugraphic_Empty


class com_plantuml_ugraphic_TextBlockUtils:
    _hx_class_name = "com.plantuml.ugraphic.TextBlockUtils"
    __slots__ = ()
    _hx_statics = ["empty", "withMargin"]

    @staticmethod
    def empty(width,height):
        return com_plantuml_ugraphic_Empty(width,height)

    @staticmethod
    def withMargin(textBlock,marginX1,marginX2,marginY1,marginY2):
        return com_plantuml_graphic_TextBlockMarged(textBlock,marginY1,marginX2,marginY2,marginX1)
com_plantuml_ugraphic_TextBlockUtils._hx_class = com_plantuml_ugraphic_TextBlockUtils


class com_plantuml_ugraphic_UChange:
    _hx_class_name = "com.plantuml.ugraphic.UChange"
    __slots__ = ()
com_plantuml_ugraphic_UChange._hx_class = com_plantuml_ugraphic_UChange


class com_plantuml_ugraphic_UFont:
    _hx_class_name = "com.plantuml.ugraphic.UFont"
    __slots__ = ()

    def __init__(self):
        pass
com_plantuml_ugraphic_UFont._hx_class = com_plantuml_ugraphic_UFont


class com_plantuml_ugraphic_StringBounderSvg:
    _hx_class_name = "com.plantuml.ugraphic.StringBounderSvg"
    __slots__ = ()
    _hx_methods = ["calculateDimension"]
    _hx_interfaces = [com_plantuml_graphic_StringBounder]

    def __init__(self):
        pass

    def calculateDimension(self,font,text):
        width = len(text)
        height = 16
        return com_plantuml_awt_geom_Dimension2D((width * 12),height)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
com_plantuml_ugraphic_StringBounderSvg._hx_class = com_plantuml_ugraphic_StringBounderSvg


class com_plantuml_ugraphic_UGraphicSvg(com_plantuml_ugraphic_AbstractCommonUGraphic):
    _hx_class_name = "com.plantuml.ugraphic.UGraphicSvg"
    __slots__ = ("core",)
    _hx_fields = ["core"]
    _hx_methods = ["getStringBounder", "draw", "getSvg", "copyUGraphic"]
    _hx_statics = ["create"]
    _hx_interfaces = [com_plantuml_ugraphic_UGraphic]
    _hx_super = com_plantuml_ugraphic_AbstractCommonUGraphic


    def __init__(self,core):
        self.core = None
        super().__init__()
        self.core = core
        this1 = self.drivers
        key = Type.getClassName(com_plantuml_ugraphic_UText)
        value = com_plantuml_svg_DriverTextSvg()
        this1.h[key] = value
        this1 = self.drivers
        key = Type.getClassName(com_plantuml_ugraphic_URectangle)
        value = com_plantuml_svg_DriverRectangleSvg()
        this1.h[key] = value
        this1 = self.drivers
        key = Type.getClassName(com_plantuml_ugraphic_UPath)
        value = com_plantuml_svg_DriverPathSvg()
        this1.h[key] = value

    def getStringBounder(self):
        return com_plantuml_ugraphic_StringBounderSvg()

    def draw(self,shape):
        cl = Type.getClass(shape)
        this1 = self.drivers
        key = Type.getClassName(cl)
        driver = this1.h.get(key,None)
        if (driver is None):
            haxe_Log.trace(shape,_hx_AnonObject({'fileName': "src/com/plantuml/ugraphic/UGraphicSvg.hx", 'lineNumber': 45, 'className': "com.plantuml.ugraphic.UGraphicSvg", 'methodName': "draw"}))
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/ugraphic/UGraphicSvg.hx", 'lineNumber': 46, 'className': "com.plantuml.ugraphic.UGraphicSvg", 'methodName': "draw"}))
        else:
            driver.draw(shape,self.getTranslateX(),self.getTranslateY(),None,None,self.core)

    def getSvg(self):
        return self.core.toSvg()

    def copyUGraphic(self):
        result = com_plantuml_ugraphic_UGraphicSvg(self.core)
        result.translate = self.translate.copy()
        return result

    @staticmethod
    def create():
        return com_plantuml_ugraphic_UGraphicSvg(com_plantuml_svg_SvgGraphics())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.core = None
com_plantuml_ugraphic_UGraphicSvg._hx_class = com_plantuml_ugraphic_UGraphicSvg


class com_plantuml_ugraphic_UParam:
    _hx_class_name = "com.plantuml.ugraphic.UParam"
    __slots__ = ()
com_plantuml_ugraphic_UParam._hx_class = com_plantuml_ugraphic_UParam


class com_plantuml_ugraphic_UPath:
    _hx_class_name = "com.plantuml.ugraphic.UPath"
    __slots__ = ("segments",)
    _hx_fields = ["segments"]
    _hx_methods = ["getSegments", "moveToPoint", "lineToPoint", "lineTo", "cubicTo", "addInternal", "add", "getDeltaShadow"]
    _hx_interfaces = [com_plantuml_ugraphic_UShape]

    def __init__(self):
        self.segments = []

    def getSegments(self):
        return self.segments

    def moveToPoint(self,p1):
        x = p1.getX()
        y = p1.getY()
        self.add([x, y],com_plantuml_ugraphic_USegmentType.SEG_MOVETO)

    def lineToPoint(self,p1):
        x = p1.getX()
        y = p1.getY()
        self.lineTo(x,y)

    def lineTo(self,x,y):
        self.add([x, y],com_plantuml_ugraphic_USegmentType.SEG_LINETO)

    def cubicTo(self,ctrlx1,ctrly1,ctrlx2,ctrly2,x2,y2):
        self.add([ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2],com_plantuml_ugraphic_USegmentType.SEG_CUBICTO)

    def addInternal(self,segment):
        _this = self.segments
        _this.append(segment)

    def add(self,coord,pathType):
        self.addInternal(com_plantuml_ugraphic_USegment(coord,pathType))

    def getDeltaShadow(self):
        return 0

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.segments = None
com_plantuml_ugraphic_UPath._hx_class = com_plantuml_ugraphic_UPath


class com_plantuml_ugraphic_URectangle:
    _hx_class_name = "com.plantuml.ugraphic.URectangle"
    __slots__ = ("width", "height")
    _hx_fields = ["width", "height"]
    _hx_methods = ["getWidth", "getHeight", "getDeltaShadow", "getComment", "getCodeLine"]
    _hx_interfaces = [com_plantuml_ugraphic_UShape]

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDeltaShadow(self):
        return 0

    def getComment(self):
        return ""

    def getCodeLine(self):
        return ""

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.width = None
        _hx_o.height = None
com_plantuml_ugraphic_URectangle._hx_class = com_plantuml_ugraphic_URectangle


class com_plantuml_ugraphic_USegment:
    _hx_class_name = "com.plantuml.ugraphic.USegment"
    __slots__ = ("coord", "pathType")
    _hx_fields = ["coord", "pathType"]
    _hx_methods = ["getSegmentType", "getCoord"]

    def __init__(self,coord,pathType):
        self.coord = coord
        self.pathType = pathType

    def getSegmentType(self):
        return self.pathType

    def getCoord(self):
        return self.coord

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.coord = None
        _hx_o.pathType = None
com_plantuml_ugraphic_USegment._hx_class = com_plantuml_ugraphic_USegment

class com_plantuml_ugraphic_USegmentType(Enum):
    __slots__ = ()
    _hx_class_name = "com.plantuml.ugraphic.USegmentType"
    _hx_constructs = ["SEG_MOVETO", "SEG_LINETO", "SEG_QUADTO", "SEG_CUBICTO", "SEG_CLOSE", "SEG_ARCTO"]
com_plantuml_ugraphic_USegmentType.SEG_MOVETO = com_plantuml_ugraphic_USegmentType("SEG_MOVETO", 0, ())
com_plantuml_ugraphic_USegmentType.SEG_LINETO = com_plantuml_ugraphic_USegmentType("SEG_LINETO", 1, ())
com_plantuml_ugraphic_USegmentType.SEG_QUADTO = com_plantuml_ugraphic_USegmentType("SEG_QUADTO", 2, ())
com_plantuml_ugraphic_USegmentType.SEG_CUBICTO = com_plantuml_ugraphic_USegmentType("SEG_CUBICTO", 3, ())
com_plantuml_ugraphic_USegmentType.SEG_CLOSE = com_plantuml_ugraphic_USegmentType("SEG_CLOSE", 4, ())
com_plantuml_ugraphic_USegmentType.SEG_ARCTO = com_plantuml_ugraphic_USegmentType("SEG_ARCTO", 5, ())
com_plantuml_ugraphic_USegmentType._hx_class = com_plantuml_ugraphic_USegmentType


class com_plantuml_ugraphic_USegmentType_:
    _hx_class_name = "com.plantuml.ugraphic.USegmentType_"
    __slots__ = ()
    _hx_statics = ["getNbPoints"]

    @staticmethod
    def getNbPoints(me):
        tmp = me.index
        if (tmp == 0):
            return 1
        elif (tmp == 1):
            return 1
        elif (tmp == 3):
            return 3
        elif (tmp == 4):
            return 0
        else:
            raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "src/com/plantuml/ugraphic/USegmentType.hx", 'lineNumber': 24, 'className': "com.plantuml.ugraphic.USegmentType_", 'methodName': "getNbPoints"}))
com_plantuml_ugraphic_USegmentType_._hx_class = com_plantuml_ugraphic_USegmentType_


class com_plantuml_ugraphic_UText:
    _hx_class_name = "com.plantuml.ugraphic.UText"
    __slots__ = ("text",)
    _hx_fields = ["text"]
    _hx_methods = ["getText"]
    _hx_interfaces = [com_plantuml_ugraphic_UShape]

    def __init__(self,text):
        self.text = text

    def getText(self):
        return self.text

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.text = None
com_plantuml_ugraphic_UText._hx_class = com_plantuml_ugraphic_UText


class com_plantuml_ugraphic_UTranslate:
    _hx_class_name = "com.plantuml.ugraphic.UTranslate"
    __slots__ = ("dx", "dy")
    _hx_fields = ["dx", "dy"]
    _hx_methods = ["getDx", "getDy", "copy", "compose"]
    _hx_interfaces = [com_plantuml_ugraphic_UChange]

    def __init__(self,dx,dy):
        self.dx = dx
        self.dy = dy

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def copy(self):
        return com_plantuml_ugraphic_UTranslate(self.dx,self.dy)

    def compose(self,other):
        return com_plantuml_ugraphic_UTranslate((self.dx + other.dx),(self.dy + other.dy))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.dx = None
        _hx_o.dy = None
com_plantuml_ugraphic_UTranslate._hx_class = com_plantuml_ugraphic_UTranslate


class com_plantuml_ugraphic_color_ColorMapper:
    _hx_class_name = "com.plantuml.ugraphic.color.ColorMapper"
    __slots__ = ()
com_plantuml_ugraphic_color_ColorMapper._hx_class = com_plantuml_ugraphic_color_ColorMapper


class com_plantuml_ugraphic_color_HColor:
    _hx_class_name = "com.plantuml.ugraphic.color.HColor"
    __slots__ = ()
    _hx_interfaces = [com_plantuml_ugraphic_UChange]
com_plantuml_ugraphic_color_HColor._hx_class = com_plantuml_ugraphic_color_HColor

class haxe_StackItem(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.StackItem"
    _hx_constructs = ["CFunction", "Module", "FilePos", "Method", "LocalFunction"]

    @staticmethod
    def Module(m):
        return haxe_StackItem("Module", 1, (m,))

    @staticmethod
    def FilePos(s,file,line,column = None):
        return haxe_StackItem("FilePos", 2, (s,file,line,column))

    @staticmethod
    def Method(classname,method):
        return haxe_StackItem("Method", 3, (classname,method))

    @staticmethod
    def LocalFunction(v = None):
        return haxe_StackItem("LocalFunction", 4, (v,))
haxe_StackItem.CFunction = haxe_StackItem("CFunction", 0, ())
haxe_StackItem._hx_class = haxe_StackItem


class haxe__CallStack_CallStack_Impl_:
    _hx_class_name = "haxe._CallStack.CallStack_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "callStack", "exceptionStack", "toString", "subtract", "copy", "get", "asArray", "equalItems", "exceptionToString", "itemToString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return haxe_NativeStackTrace.toHaxe(infos)

    @staticmethod
    def exceptionStack(fullStack = None):
        if (fullStack is None):
            fullStack = False
        eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack())
        return (eStack if fullStack else haxe__CallStack_CallStack_Impl_.subtract(eStack,haxe__CallStack_CallStack_Impl_.callStack()))

    @staticmethod
    def toString(stack):
        b = StringBuf()
        _g = 0
        _g1 = stack
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b.b.write("\nCalled from ")
            haxe__CallStack_CallStack_Impl_.itemToString(b,s)
        return b.b.getvalue()

    @staticmethod
    def subtract(this1,stack):
        startIndex = -1
        i = -1
        while True:
            i = (i + 1)
            tmp = i
            if (not ((tmp < len(this1)))):
                break
            _g = 0
            _g1 = len(stack)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                if haxe__CallStack_CallStack_Impl_.equalItems((this1[i] if i >= 0 and i < len(this1) else None),python_internal_ArrayImpl._get(stack, j)):
                    if (startIndex < 0):
                        startIndex = i
                    i = (i + 1)
                    if (i >= len(this1)):
                        break
                else:
                    startIndex = -1
            if (startIndex >= 0):
                break
        if (startIndex >= 0):
            return this1[0:startIndex]
        else:
            return this1

    @staticmethod
    def copy(this1):
        return list(this1)

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def asArray(this1):
        return this1

    @staticmethod
    def equalItems(item1,item2):
        if (item1 is None):
            if (item2 is None):
                return True
            else:
                return False
        else:
            tmp = item1.index
            if (tmp == 0):
                if (item2 is None):
                    return False
                elif (item2.index == 0):
                    return True
                else:
                    return False
            elif (tmp == 1):
                if (item2 is None):
                    return False
                elif (item2.index == 1):
                    m2 = item2.params[0]
                    m1 = item1.params[0]
                    return (m1 == m2)
                else:
                    return False
            elif (tmp == 2):
                if (item2 is None):
                    return False
                elif (item2.index == 2):
                    item21 = item2.params[0]
                    file2 = item2.params[1]
                    line2 = item2.params[2]
                    col2 = item2.params[3]
                    col1 = item1.params[3]
                    line1 = item1.params[2]
                    file1 = item1.params[1]
                    item11 = item1.params[0]
                    if (((file1 == file2) and ((line1 == line2))) and ((col1 == col2))):
                        return haxe__CallStack_CallStack_Impl_.equalItems(item11,item21)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 3):
                if (item2 is None):
                    return False
                elif (item2.index == 3):
                    class2 = item2.params[0]
                    method2 = item2.params[1]
                    method1 = item1.params[1]
                    class1 = item1.params[0]
                    if (class1 == class2):
                        return (method1 == method2)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 4):
                if (item2 is None):
                    return False
                elif (item2.index == 4):
                    v2 = item2.params[0]
                    v1 = item1.params[0]
                    return (v1 == v2)
                else:
                    return False
            else:
                pass

    @staticmethod
    def exceptionToString(e):
        if (e.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(e.toString()))
            tmp1 = e.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        result = ""
        e1 = e
        prev = None
        while (e1 is not None):
            if (prev is None):
                result1 = ("Exception: " + HxOverrides.stringOrNull(e1.get_message()))
                tmp = e1.get_stack()
                result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
            else:
                prevStack = haxe__CallStack_CallStack_Impl_.subtract(e1.get_stack(),prev.get_stack())
                result = (((("Exception: " + HxOverrides.stringOrNull(e1.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
            prev = e1
            e1 = e1.get_previous()
        return result

    @staticmethod
    def itemToString(b,s):
        tmp = s.index
        if (tmp == 0):
            b.b.write("a C function")
        elif (tmp == 1):
            m = s.params[0]
            b.b.write("module ")
            s1 = Std.string(m)
            b.b.write(s1)
        elif (tmp == 2):
            s1 = s.params[0]
            file = s.params[1]
            line = s.params[2]
            col = s.params[3]
            if (s1 is not None):
                haxe__CallStack_CallStack_Impl_.itemToString(b,s1)
                b.b.write(" (")
            s2 = Std.string(file)
            b.b.write(s2)
            b.b.write(" line ")
            s2 = Std.string(line)
            b.b.write(s2)
            if (col is not None):
                b.b.write(" column ")
                s2 = Std.string(col)
                b.b.write(s2)
            if (s1 is not None):
                b.b.write(")")
        elif (tmp == 3):
            cname = s.params[0]
            meth = s.params[1]
            s1 = Std.string(("<unknown>" if ((cname is None)) else cname))
            b.b.write(s1)
            b.b.write(".")
            s1 = Std.string(meth)
            b.b.write(s1)
        elif (tmp == 4):
            n = s.params[0]
            b.b.write("local function #")
            s = Std.string(n)
            b.b.write(s)
        else:
            pass
haxe__CallStack_CallStack_Impl_._hx_class = haxe__CallStack_CallStack_Impl_


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___exceptionStack", "_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__exceptionStack", "__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "details", "__shiftStack", "get_message", "get_previous", "get_native", "get_stack"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___exceptionStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def details(self):
        if (self.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(self.toString()))
            tmp1 = self.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        else:
            result = ""
            e = self
            prev = None
            while (e is not None):
                if (prev is None):
                    result1 = ("Exception: " + HxOverrides.stringOrNull(e.get_message()))
                    tmp = e.get_stack()
                    result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
                else:
                    prevStack = haxe__CallStack_CallStack_Impl_.subtract(e.get_stack(),prev.get_stack())
                    result = (((("Exception: " + HxOverrides.stringOrNull(e.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
                prev = e
                e = e.get_previous()
            return result

    def _hx___shiftStack(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def get_message(self):
        return str(self)

    def get_previous(self):
        return self._hx___previousException

    def get_native(self):
        return self._hx___nativeException

    def get_stack(self):
        _g = self._hx___exceptionStack
        if (_g is None):
            def _hx_local_1():
                def _hx_local_0():
                    self._hx___exceptionStack = haxe_NativeStackTrace.toHaxe(self._hx___nativeStack,self._hx___skipStack)
                    return self._hx___exceptionStack
                return _hx_local_0()
            return _hx_local_1()
        else:
            s = _g
            return s

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___exceptionStack = None
        _hx_o._hx___nativeStack = None
        _hx_o._hx___skipStack = None
        _hx_o._hx___nativeException = None
        _hx_o._hx___previousException = None
haxe_Exception._hx_class = haxe_Exception


class haxe__Int32_Int32_Impl_:
    _hx_class_name = "haxe._Int32.Int32_Impl_"
    __slots__ = ()
    _hx_statics = ["negate", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "complement", "or", "orInt", "xor", "xorInt", "shr", "shrInt", "intShr", "shl", "shlInt", "intShl", "toFloat", "ucompare", "clamp"]

    @staticmethod
    def negate(this1):
        return (((~this1 + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def preIncrement(this1):
        this1 = (this1 + 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this1 = (this1 + 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this1 = (this1 - 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this1 = (this1 - 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def addInt(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def sub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def subInt(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intSub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mul(a,b):
        return ((((a * ((b & 65535))) + ((((((a * (HxOverrides.rshift(b, 16))) << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mulInt(a,b):
        return haxe__Int32_Int32_Impl_.mul(a,b)

    @staticmethod
    def complement(a):
        return ((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def _hx_or(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def orInt(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xor(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xorInt(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shrInt(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shlInt(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def toFloat(this1):
        return this1

    @staticmethod
    def ucompare(a,b):
        if (a < 0):
            if (b < 0):
                return (((((~b + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - (((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            else:
                return 1
        if (b < 0):
            return -1
        else:
            return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def clamp(x):
        return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
haxe__Int32_Int32_Impl_._hx_class = haxe__Int32_Int32_Impl_


class haxe__Int64_Int64_Impl_:
    _hx_class_name = "haxe._Int64.Int64_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "copy", "make", "ofInt", "toInt", "is", "isInt64", "getHigh", "getLow", "isNeg", "isZero", "compare", "ucompare", "toStr", "toString", "parseString", "fromFloat", "divMod", "neg", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "div", "divInt", "intDiv", "mod", "modInt", "intMod", "eq", "eqInt", "neq", "neqInt", "lt", "ltInt", "intLt", "lte", "lteInt", "intLte", "gt", "gtInt", "intGt", "gte", "gteInt", "intGte", "complement", "and", "or", "xor", "shl", "shr", "ushr", "get_high", "set_high", "get_low", "set_low"]
    high = None
    low = None

    @staticmethod
    def _new(x):
        this1 = x
        return this1

    @staticmethod
    def copy(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        return this2

    @staticmethod
    def make(high,low):
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def ofInt(x):
        this1 = haxe__Int64____Int64((x >> 31),x)
        return this1

    @staticmethod
    def toInt(x):
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        return x.low

    @staticmethod
    def _hx_is(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def isInt64(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def getHigh(x):
        return x.high

    @staticmethod
    def getLow(x):
        return x.low

    @staticmethod
    def isNeg(x):
        return (x.high < 0)

    @staticmethod
    def isZero(x):
        b_high = 0
        b_low = 0
        if (x.high == b_high):
            return (x.low == b_low)
        else:
            return False

    @staticmethod
    def compare(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        if (a.high < 0):
            if (b.high < 0):
                return v
            else:
                return -1
        elif (b.high >= 0):
            return v
        else:
            return 1

    @staticmethod
    def ucompare(a,b):
        v = haxe__Int32_Int32_Impl_.ucompare(a.high,b.high)
        if (v != 0):
            return v
        else:
            return haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)

    @staticmethod
    def toStr(x):
        return haxe__Int64_Int64_Impl_.toString(x)

    @staticmethod
    def toString(this1):
        i = this1
        b_high = 0
        b_low = 0
        if ((i.high == b_high) and ((i.low == b_low))):
            return "0"
        _hx_str = ""
        neg = False
        if (i.high < 0):
            neg = True
        this1 = haxe__Int64____Int64(0,10)
        ten = this1
        while True:
            b_high = 0
            b_low = 0
            if (not (((i.high != b_high) or ((i.low != b_low))))):
                break
            r = haxe__Int64_Int64_Impl_.divMod(i,ten)
            if (r.modulus.high < 0):
                x = r.modulus
                high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low == 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this_high = high
                this_low = low
                _hx_str = (Std.string(this_low) + ("null" if _hx_str is None else _hx_str))
                x1 = r.quotient
                high1 = ((~x1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low1 = (((~x1.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low1 == 0):
                    ret1 = high1
                    high1 = (high1 + 1)
                    high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this1 = haxe__Int64____Int64(high1,low1)
                i = this1
            else:
                _hx_str = (Std.string(r.modulus.low) + ("null" if _hx_str is None else _hx_str))
                i = r.quotient
        if neg:
            _hx_str = ("-" + ("null" if _hx_str is None else _hx_str))
        return _hx_str

    @staticmethod
    def parseString(sParam):
        return haxe_Int64Helper.parseString(sParam)

    @staticmethod
    def fromFloat(f):
        return haxe_Int64Helper.fromFloat(f)

    @staticmethod
    def divMod(dividend,divisor):
        if (divisor.high == 0):
            _g = divisor.low
            if (_g == 0):
                raise haxe_Exception.thrown("divide by zero")
            elif (_g == 1):
                this1 = haxe__Int64____Int64(dividend.high,dividend.low)
                this2 = haxe__Int64____Int64(0,0)
                return _hx_AnonObject({'quotient': this1, 'modulus': this2})
            else:
                pass
        divSign = ((dividend.high < 0) != ((divisor.high < 0)))
        modulus = None
        if (dividend.high < 0):
            high = ((~dividend.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~dividend.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        else:
            this1 = haxe__Int64____Int64(dividend.high,dividend.low)
            modulus = this1
        if (divisor.high < 0):
            high = ((~divisor.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~divisor.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            divisor = this1
        this1 = haxe__Int64____Int64(0,0)
        quotient = this1
        this1 = haxe__Int64____Int64(0,1)
        mask = this1
        while (not ((divisor.high < 0))):
            v = haxe__Int32_Int32_Impl_.ucompare(divisor.high,modulus.high)
            cmp = (v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(divisor.low,modulus.low))
            b = 1
            b = (b & 63)
            if (b == 0):
                this1 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this1
            elif (b < 32):
                this2 = haxe__Int64____Int64(((((((((divisor.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((divisor.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this2
            else:
                this3 = haxe__Int64____Int64(((((divisor.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                divisor = this3
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this4 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this4
            elif (b1 < 32):
                this5 = haxe__Int64____Int64(((((((((mask.high << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, ((32 - b1))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((mask.low << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this5
            else:
                this6 = haxe__Int64____Int64(((((mask.low << ((b1 - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                mask = this6
            if (cmp >= 0):
                break
        while True:
            b_high = 0
            b_low = 0
            if (not (((mask.high != b_high) or ((mask.low != b_low))))):
                break
            v = haxe__Int32_Int32_Impl_.ucompare(modulus.high,divisor.high)
            if (((v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low))) >= 0):
                this1 = haxe__Int64____Int64(((((quotient.high | mask.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((quotient.low | mask.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                quotient = this1
                high = (((modulus.high - divisor.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((modulus.low - divisor.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low) < 0):
                    ret = high
                    high = (high - 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this2 = haxe__Int64____Int64(high,low)
                modulus = this2
            b = 1
            b = (b & 63)
            if (b == 0):
                this3 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this3
            elif (b < 32):
                this4 = haxe__Int64____Int64(HxOverrides.rshift(mask.high, b),((((((((mask.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this4
            else:
                this5 = haxe__Int64____Int64(0,HxOverrides.rshift(mask.high, ((b - 32))))
                mask = this5
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this6 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this6
            elif (b1 < 32):
                this7 = haxe__Int64____Int64(HxOverrides.rshift(divisor.high, b1),((((((((divisor.high << ((32 - b1)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, b1))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this7
            else:
                this8 = haxe__Int64____Int64(0,HxOverrides.rshift(divisor.high, ((b1 - 32))))
                divisor = this8
        if divSign:
            high = ((~quotient.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~quotient.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            quotient = this1
        if (dividend.high < 0):
            high = ((~modulus.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~modulus.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        return _hx_AnonObject({'quotient': quotient, 'modulus': modulus})

    @staticmethod
    def neg(x):
        high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (low == 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def preIncrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_1():
            _hx_local_0 = this1.low
            this1.low = (this1.low + 1)
            return _hx_local_0
        ret = _hx_local_1()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_3():
                _hx_local_2 = this1.high
                this1.high = (this1.high + 1)
                return _hx_local_2
            ret = _hx_local_3()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_2():
            _hx_local_0 = this1
            _hx_local_1 = _hx_local_0.low
            _hx_local_0.low = (_hx_local_1 + 1)
            return _hx_local_1
        ret1 = _hx_local_2()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_5():
                _hx_local_3 = this1
                _hx_local_4 = _hx_local_3.high
                _hx_local_3.high = (_hx_local_4 + 1)
                return _hx_local_4
            ret1 = _hx_local_5()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_1():
                _hx_local_0 = this1.high
                this1.high = (this1.high - 1)
                return _hx_local_0
            ret = _hx_local_1()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_3():
            _hx_local_2 = this1.low
            this1.low = (this1.low - 1)
            return _hx_local_2
        ret = _hx_local_3()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_2():
                _hx_local_0 = this1
                _hx_local_1 = _hx_local_0.high
                _hx_local_0.high = (_hx_local_1 - 1)
                return _hx_local_1
            ret1 = _hx_local_2()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_5():
            _hx_local_3 = this1
            _hx_local_4 = _hx_local_3.low
            _hx_local_3.low = (_hx_local_4 - 1)
            return _hx_local_4
        ret1 = _hx_local_5()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        high = (((a.high + b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def addInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high + b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def sub(a,b):
        high = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def subInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b_low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def intSub(a,b):
        a_high = (a >> 31)
        a_low = a
        high = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a_low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a_low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mul(a,b):
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b.low & mask)
        bh = HxOverrides.rshift(b.low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b.high) + haxe__Int32_Int32_Impl_.mul(a.high,b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mulInt(a,b):
        b_high = (b >> 31)
        b_low = b
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b_low & mask)
        bh = HxOverrides.rshift(b_low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b_high) + haxe__Int32_Int32_Impl_.mul(a.high,b_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def div(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).quotient

    @staticmethod
    def divInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        return haxe__Int64_Int64_Impl_.divMod(a,this1).quotient

    @staticmethod
    def intDiv(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).quotient
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def mod(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).modulus

    @staticmethod
    def modInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        x = haxe__Int64_Int64_Impl_.divMod(a,this1).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def intMod(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def eq(a,b):
        if (a.high == b.high):
            return (a.low == b.low)
        else:
            return False

    @staticmethod
    def eqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low == b_low)
        else:
            return False

    @staticmethod
    def neq(a,b):
        if (a.high == b.high):
            return (a.low != b.low)
        else:
            return True

    @staticmethod
    def neqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low != b_low)
        else:
            return True

    @staticmethod
    def lt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def ltInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) < 0)

    @staticmethod
    def intLt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def lte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def lteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) <= 0)

    @staticmethod
    def intLte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def gt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gtInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) > 0)

    @staticmethod
    def intGt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def gteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) >= 0)

    @staticmethod
    def intGte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def complement(a):
        this1 = haxe__Int64____Int64(((~a.high + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((~a.low + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def _hx_and(a,b):
        this1 = haxe__Int64____Int64((a.high & b.high),(a.low & b.low))
        return this1

    @staticmethod
    def _hx_or(a,b):
        this1 = haxe__Int64____Int64(((((a.high | b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low | b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def xor(a,b):
        this1 = haxe__Int64____Int64(((((a.high ^ b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low ^ b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def shl(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((((((a.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
            return this1

    @staticmethod
    def shr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((a.high >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.high >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.high >> ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1

    @staticmethod
    def ushr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(HxOverrides.rshift(a.high, b),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(0,HxOverrides.rshift(a.high, ((b - 32))))
            return this1

    @staticmethod
    def get_high(this1):
        return this1.high

    @staticmethod
    def set_high(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.high = x
                return this1.high
            return _hx_local_0()
        return _hx_local_1()

    @staticmethod
    def get_low(this1):
        return this1.low

    @staticmethod
    def set_low(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.low = x
                return this1.low
            return _hx_local_0()
        return _hx_local_1()
haxe__Int64_Int64_Impl_._hx_class = haxe__Int64_Int64_Impl_


class haxe__Int64____Int64:
    _hx_class_name = "haxe._Int64.___Int64"
    __slots__ = ("high", "low")
    _hx_fields = ["high", "low"]
    _hx_methods = ["toString"]

    def __init__(self,high,low):
        self.high = high
        self.low = low

    def toString(self):
        return haxe__Int64_Int64_Impl_.toString(self)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.high = None
        _hx_o.low = None
haxe__Int64____Int64._hx_class = haxe__Int64____Int64


class haxe_Int64Helper:
    _hx_class_name = "haxe.Int64Helper"
    __slots__ = ()
    _hx_statics = ["parseString", "fromFloat"]

    @staticmethod
    def parseString(sParam):
        base_high = 0
        base_low = 10
        this1 = haxe__Int64____Int64(0,0)
        current = this1
        this1 = haxe__Int64____Int64(0,1)
        multiplier = this1
        sIsNegative = False
        s = StringTools.trim(sParam)
        if ((("" if ((0 >= len(s))) else s[0])) == "-"):
            sIsNegative = True
            s = HxString.substring(s,1,len(s))
        _hx_len = len(s)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            digitInt = (HxString.charCodeAt(s,((_hx_len - 1) - i)) - 48)
            if ((digitInt < 0) or ((digitInt > 9))):
                raise haxe_Exception.thrown("NumberFormatError")
            if (digitInt != 0):
                digit_high = (digitInt >> 31)
                digit_low = digitInt
                if sIsNegative:
                    mask = 65535
                    al = (multiplier.low & mask)
                    ah = HxOverrides.rshift(multiplier.low, 16)
                    bl = (digit_low & mask)
                    bh = HxOverrides.rshift(digit_low, 16)
                    p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
                    p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
                    p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
                    p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
                    low = p00
                    high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
                        ret = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
                        ret1 = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high = (((high + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high = high
                    b_low = low
                    high1 = (((current.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low1 = (((current.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(current.low,b_low) < 0):
                        ret2 = high1
                        high1 = (high1 - 1)
                        high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this1 = haxe__Int64____Int64(high1,low1)
                    current = this1
                    if (not ((current.high < 0))):
                        raise haxe_Exception.thrown("NumberFormatError: Underflow")
                else:
                    mask1 = 65535
                    al1 = (multiplier.low & mask1)
                    ah1 = HxOverrides.rshift(multiplier.low, 16)
                    bl1 = (digit_low & mask1)
                    bh1 = HxOverrides.rshift(digit_low, 16)
                    p001 = haxe__Int32_Int32_Impl_.mul(al1,bl1)
                    p101 = haxe__Int32_Int32_Impl_.mul(ah1,bl1)
                    p011 = haxe__Int32_Int32_Impl_.mul(al1,bh1)
                    p111 = haxe__Int32_Int32_Impl_.mul(ah1,bh1)
                    low2 = p001
                    high2 = ((((((p111 + (HxOverrides.rshift(p011, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p101, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p011 = ((((p011 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p011) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p011) < 0):
                        ret3 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p101 = ((((p101 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p101) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p101) < 0):
                        ret4 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high2 = (((high2 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high1 = high2
                    b_low1 = low2
                    high3 = (((current.high + b_high1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low3 = (((current.low + b_low1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low3,current.low) < 0):
                        ret5 = high3
                        high3 = (high3 + 1)
                        high3 = ((high3 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this2 = haxe__Int64____Int64(high3,low3)
                    current = this2
                    if (current.high < 0):
                        raise haxe_Exception.thrown("NumberFormatError: Overflow")
            mask2 = 65535
            al2 = (multiplier.low & mask2)
            ah2 = HxOverrides.rshift(multiplier.low, 16)
            bl2 = (base_low & mask2)
            bh2 = HxOverrides.rshift(base_low, 16)
            p002 = haxe__Int32_Int32_Impl_.mul(al2,bl2)
            p102 = haxe__Int32_Int32_Impl_.mul(ah2,bl2)
            p012 = haxe__Int32_Int32_Impl_.mul(al2,bh2)
            p112 = haxe__Int32_Int32_Impl_.mul(ah2,bh2)
            low4 = p002
            high4 = ((((((p112 + (HxOverrides.rshift(p012, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p102, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p012 = ((((p012 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p012) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p012) < 0):
                ret6 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p102 = ((((p102 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p102) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p102) < 0):
                ret7 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            high4 = (((high4 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,base_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,base_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this3 = haxe__Int64____Int64(high4,low4)
            multiplier = this3
        return current

    @staticmethod
    def fromFloat(f):
        if (python_lib_Math.isnan(f) or (not ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))))):
            raise haxe_Exception.thrown("Number is NaN or Infinite")
        noFractions = (f - (HxOverrides.modf(f, 1)))
        if (noFractions > 9007199254740991):
            raise haxe_Exception.thrown("Conversion overflow")
        if (noFractions < -9007199254740991):
            raise haxe_Exception.thrown("Conversion underflow")
        this1 = haxe__Int64____Int64(0,0)
        result = this1
        neg = (noFractions < 0)
        rest = (-noFractions if neg else noFractions)
        i = 0
        while (rest >= 1):
            curr = HxOverrides.modf(rest, 2)
            rest = (rest / 2)
            if (curr >= 1):
                a_high = 0
                a_low = 1
                b = i
                b = (b & 63)
                b1 = None
                if (b == 0):
                    this1 = haxe__Int64____Int64(a_high,a_low)
                    b1 = this1
                elif (b < 32):
                    this2 = haxe__Int64____Int64(((((((((a_high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a_low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a_low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                    b1 = this2
                else:
                    this3 = haxe__Int64____Int64(((((a_low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                    b1 = this3
                high = (((result.high + b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((result.low + b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(low,result.low) < 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this4 = haxe__Int64____Int64(high,low)
                result = this4
            i = (i + 1)
        if neg:
            high = ((~result.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~result.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            result = this1
        return result
haxe_Int64Helper._hx_class = haxe_Int64Helper


class haxe_Log:
    _hx_class_name = "haxe.Log"
    __slots__ = ()
    _hx_statics = ["formatOutput", "trace"]

    @staticmethod
    def formatOutput(v,infos):
        _hx_str = Std.string(v)
        if (infos is None):
            return _hx_str
        pstr = ((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber))
        if (Reflect.field(infos,"customParams") is not None):
            _g = 0
            _g1 = Reflect.field(infos,"customParams")
            while (_g < len(_g1)):
                v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _hx_str = (("null" if _hx_str is None else _hx_str) + ((", " + Std.string(v))))
        return ((("null" if pstr is None else pstr) + ": ") + ("null" if _hx_str is None else _hx_str))

    @staticmethod
    def trace(v,infos = None):
        _hx_str = haxe_Log.formatOutput(v,infos)
        str1 = Std.string(_hx_str)
        python_Lib.printString((("" + ("null" if str1 is None else str1)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
haxe_Log._hx_class = haxe_Log


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "callStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return infos

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        if (skip is None):
            skip = 0
        stack = []
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (skip > i):
                continue
            elem = (native[i] if i >= 0 and i < len(native) else None)
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace


class haxe__Rest_Rest_Impl_:
    _hx_class_name = "haxe._Rest.Rest_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "of", "_new", "get", "toArray", "iterator", "keyValueIterator", "append", "prepend", "toString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def of(array):
        this1 = array
        return this1

    @staticmethod
    def _new(array):
        this1 = array
        return this1

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def iterator(this1):
        return haxe_iterators_RestIterator(this1)

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_RestKeyValueIterator(this1)

    @staticmethod
    def append(this1,item):
        result = list(this1)
        result.append(item)
        this1 = result
        return this1

    @staticmethod
    def prepend(this1,item):
        result = list(this1)
        result.insert(0, item)
        this1 = result
        return this1

    @staticmethod
    def toString(this1):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in this1]))) + "]")
haxe__Rest_Rest_Impl_._hx_class = haxe__Rest_Rest_Impl_


class haxe_Utf8:
    _hx_class_name = "haxe.Utf8"
    __slots__ = ("_hx___b",)
    _hx_fields = ["__b"]
    _hx_methods = ["addChar", "toString"]
    _hx_statics = ["iter", "encode", "decode", "charCodeAt", "validate", "length", "compare", "sub"]

    def __init__(self,size = None):
        self._hx___b = ""

    def addChar(self,c):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___b
        _hx_local_0._hx___b = (("null" if _hx_local_1 is None else _hx_local_1) + HxOverrides.stringOrNull("".join(map(chr,[c]))))
        _hx_local_0._hx___b

    def toString(self):
        return self._hx___b

    @staticmethod
    def iter(s,chars):
        _g = 0
        _g1 = len(s)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            chars(HxString.charCodeAt(s,i))

    @staticmethod
    def encode(s):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/Utf8.hx", 'lineNumber': 66, 'className': "haxe.Utf8", 'methodName': "encode"}))

    @staticmethod
    def decode(s):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/Utf8.hx", 'lineNumber': 74, 'className': "haxe.Utf8", 'methodName': "decode"}))

    @staticmethod
    def charCodeAt(s,index):
        return HxString.charCodeAt(s,index)

    @staticmethod
    def validate(s):
        return True

    @staticmethod
    def length(s):
        return len(s)

    @staticmethod
    def compare(a,b):
        if (a > b):
            return 1
        elif (a == b):
            return 0
        else:
            return -1

    @staticmethod
    def sub(s,pos,_hx_len):
        return HxString.substr(s,pos,_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___b = None
haxe_Utf8._hx_class = haxe_Utf8


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def unwrap(self):
        return self.value

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
haxe_ValueException._hx_class = haxe_ValueException


class haxe_crypto_Adler32:
    _hx_class_name = "haxe.crypto.Adler32"
    __slots__ = ("a1", "a2")
    _hx_fields = ["a1", "a2"]
    _hx_methods = ["get", "update", "equals", "toString"]
    _hx_statics = ["read", "make"]

    def __init__(self):
        self.a1 = 1
        self.a2 = 0

    def get(self):
        return ((self.a2 << 16) | self.a1)

    def update(self,b,pos,_hx_len):
        a1 = self.a1
        a2 = self.a2
        _g = pos
        _g1 = (pos + _hx_len)
        while (_g < _g1):
            p = _g
            _g = (_g + 1)
            c = b.b[p]
            a1 = HxOverrides.mod(((a1 + c)), 65521)
            a2 = HxOverrides.mod(((a2 + a1)), 65521)
        self.a1 = a1
        self.a2 = a2

    def equals(self,a):
        if (a.a1 == self.a1):
            return (a.a2 == self.a2)
        else:
            return False

    def toString(self):
        return (HxOverrides.stringOrNull(StringTools.hex(self.a2,8)) + HxOverrides.stringOrNull(StringTools.hex(self.a1,8)))

    @staticmethod
    def read(i):
        a = haxe_crypto_Adler32()
        a2a = i.readByte()
        a2b = i.readByte()
        a1a = i.readByte()
        a1b = i.readByte()
        a.a1 = ((a1a << 8) | a1b)
        a.a2 = ((a2a << 8) | a2b)
        return a

    @staticmethod
    def make(b):
        a = haxe_crypto_Adler32()
        a.update(b,0,b.length)
        return a.get()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.a1 = None
        _hx_o.a2 = None
haxe_crypto_Adler32._hx_class = haxe_crypto_Adler32


class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
    _hx_statics = ["alloc", "ofString", "ofData", "ofHex", "fastGet"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def get(self,pos):
        return self.b[pos]

    def set(self,pos,v):
        self.b[pos] = (v & 255)

    def blit(self,pos,src,srcpos,_hx_len):
        if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

    def fill(self,pos,_hx_len,value):
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            pos1 = pos
            pos = (pos + 1)
            self.b[pos1] = (value & 255)

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def compare(self,other):
        b1 = self.b
        b2 = other.b
        _hx_len = (self.length if ((self.length < other.length)) else other.length)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (b1[i] != b2[i]):
                return (b1[i] - b2[i])
        return (self.length - other.length)

    def getDouble(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        pos1 = (pos + 4)
        v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        return haxe_io_FPHelper.i64ToDouble(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))

    def getFloat(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        return haxe_io_FPHelper.i32ToFloat(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v))

    def setDouble(self,pos,v):
        i = haxe_io_FPHelper.doubleToI64(v)
        v = i.low
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)
        pos1 = (pos + 4)
        v = i.high
        self.b[pos1] = (v & 255)
        self.b[(pos1 + 1)] = ((v >> 8) & 255)
        self.b[(pos1 + 2)] = ((v >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setFloat(self,pos,v):
        v1 = haxe_io_FPHelper.floatToI32(v)
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getUInt16(self,pos):
        return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

    def setUInt16(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)

    def getInt32(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        if (((v & -2147483648)) != 0):
            return (v | -2147483648)
        else:
            return v

    def getInt64(self,pos):
        pos1 = (pos + 4)
        v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        this1 = haxe__Int64____Int64(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))
        return this1

    def setInt32(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setInt64(self,pos,v):
        v1 = v.low
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
        pos1 = (pos + 4)
        v1 = v.high
        self.b[pos1] = (v1 & 255)
        self.b[(pos1 + 1)] = ((v1 >> 8) & 255)
        self.b[(pos1 + 2)] = ((v1 >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def readString(self,pos,_hx_len):
        return self.getString(pos,_hx_len)

    def toString(self):
        return self.getString(0,self.length)

    def toHex(self):
        s_b = python_lib_io_StringIO()
        chars = []
        _hx_str = "0123456789abcdef"
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            x = HxString.charCodeAt(_hx_str,i)
            chars.append(x)
        _g = 0
        _g1 = self.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = self.b[i]
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))])))
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))])))
        return s_b.getvalue()

    def getData(self):
        return self.b

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofHex(s):
        _hx_len = len(s)
        if (((_hx_len & 1)) != 0):
            raise haxe_Exception.thrown("Not a hex string (odd number of digits)")
        ret = haxe_io_Bytes.alloc((_hx_len >> 1))
        _g = 0
        _g1 = ret.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            index = (i * 2)
            high = (-1 if ((index >= len(s))) else ord(s[index]))
            index1 = ((i * 2) + 1)
            low = (-1 if ((index1 >= len(s))) else ord(s[index1]))
            high = (((high & 15)) + ((((((high & 64)) >> 6)) * 9)))
            low = (((low & 15)) + ((((((low & 64)) >> 6)) * 9)))
            ret.b[i] = (((((high << 4) | low)) & 255) & 255)
        return ret

    @staticmethod
    def fastGet(b,pos):
        return b[pos]

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.length = None
        _hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes


class haxe_crypto_Base64:
    _hx_class_name = "haxe.crypto.Base64"
    __slots__ = ()
    _hx_statics = ["CHARS", "BYTES", "URL_CHARS", "URL_BYTES", "encode", "decode", "urlEncode", "urlDecode"]

    @staticmethod
    def encode(_hx_bytes,complement = None):
        if (complement is None):
            complement = True
        _hx_str = haxe_crypto_BaseCode(haxe_crypto_Base64.BYTES).encodeBytes(_hx_bytes).toString()
        if complement:
            _g = HxOverrides.mod(_hx_bytes.length, 3)
            if (_g == 1):
                _hx_str = (("null" if _hx_str is None else _hx_str) + "==")
            elif (_g == 2):
                _hx_str = (("null" if _hx_str is None else _hx_str) + "=")
            else:
                pass
        return _hx_str

    @staticmethod
    def decode(_hx_str,complement = None):
        if (complement is None):
            complement = True
        if complement:
            while (HxString.charCodeAt(_hx_str,(len(_hx_str) - 1)) == 61):
                _hx_str = HxString.substr(_hx_str,0,-1)
        return haxe_crypto_BaseCode(haxe_crypto_Base64.BYTES).decodeBytes(haxe_io_Bytes.ofString(_hx_str))

    @staticmethod
    def urlEncode(_hx_bytes,complement = None):
        if (complement is None):
            complement = False
        _hx_str = haxe_crypto_BaseCode(haxe_crypto_Base64.URL_BYTES).encodeBytes(_hx_bytes).toString()
        if complement:
            _g = HxOverrides.mod(_hx_bytes.length, 3)
            if (_g == 1):
                _hx_str = (("null" if _hx_str is None else _hx_str) + "==")
            elif (_g == 2):
                _hx_str = (("null" if _hx_str is None else _hx_str) + "=")
            else:
                pass
        return _hx_str

    @staticmethod
    def urlDecode(_hx_str,complement = None):
        if (complement is None):
            complement = False
        if complement:
            while (HxString.charCodeAt(_hx_str,(len(_hx_str) - 1)) == 61):
                _hx_str = HxString.substr(_hx_str,0,-1)
        return haxe_crypto_BaseCode(haxe_crypto_Base64.URL_BYTES).decodeBytes(haxe_io_Bytes.ofString(_hx_str))
haxe_crypto_Base64._hx_class = haxe_crypto_Base64


class haxe_crypto_BaseCode:
    _hx_class_name = "haxe.crypto.BaseCode"
    __slots__ = ("base", "nbits", "tbl")
    _hx_fields = ["base", "nbits", "tbl"]
    _hx_methods = ["encodeBytes", "initTable", "decodeBytes", "encodeString", "decodeString"]
    _hx_statics = ["encode", "decode"]

    def __init__(self,base):
        self.tbl = None
        _hx_len = base.length
        nbits = 1
        while (_hx_len > ((1 << nbits))):
            nbits = (nbits + 1)
        if ((nbits > 8) or ((_hx_len != ((1 << nbits))))):
            raise haxe_Exception.thrown("BaseCode : base length must be a power of two.")
        self.base = base
        self.nbits = nbits

    def encodeBytes(self,b):
        nbits = self.nbits
        base = self.base
        x = ((b.length * 8) / nbits)
        size = None
        try:
            size = int(x)
        except BaseException as _g:
            None
            size = None
        out = haxe_io_Bytes.alloc((size + ((0 if ((HxOverrides.mod((b.length * 8), nbits) == 0)) else 1))))
        buf = 0
        curbits = 0
        mask = (((1 << nbits)) - 1)
        pin = 0
        pout = 0
        while (pout < size):
            while (curbits < nbits):
                curbits = (curbits + 8)
                buf = (buf << 8)
                pos = pin
                pin = (pin + 1)
                buf = (buf | b.b[pos])
            curbits = (curbits - nbits)
            pos1 = pout
            pout = (pout + 1)
            v = base.b[((buf >> curbits) & mask)]
            out.b[pos1] = (v & 255)
        if (curbits > 0):
            pos = pout
            pout = (pout + 1)
            v = base.b[((buf << ((nbits - curbits))) & mask)]
            out.b[pos] = (v & 255)
        return out

    def initTable(self):
        tbl = list()
        _g = 0
        while (_g < 256):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(tbl, i, -1)
        _g = 0
        _g1 = self.base.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(tbl, self.base.b[i], i)
        self.tbl = tbl

    def decodeBytes(self,b):
        nbits = self.nbits
        base = self.base
        if (self.tbl is None):
            self.initTable()
        tbl = self.tbl
        size = ((b.length * nbits) >> 3)
        out = haxe_io_Bytes.alloc(size)
        buf = 0
        curbits = 0
        pin = 0
        pout = 0
        while (pout < size):
            while (curbits < 8):
                curbits = (curbits + nbits)
                buf = (buf << nbits)
                pos = pin
                pin = (pin + 1)
                i = python_internal_ArrayImpl._get(tbl, b.b[pos])
                if (i == -1):
                    raise haxe_Exception.thrown("BaseCode : invalid encoded char")
                buf = (buf | i)
            curbits = (curbits - 8)
            pos1 = pout
            pout = (pout + 1)
            out.b[pos1] = (((buf >> curbits) & 255) & 255)
        return out

    def encodeString(self,s):
        return self.encodeBytes(haxe_io_Bytes.ofString(s)).toString()

    def decodeString(self,s):
        return self.decodeBytes(haxe_io_Bytes.ofString(s)).toString()

    @staticmethod
    def encode(s,base):
        b = haxe_crypto_BaseCode(haxe_io_Bytes.ofString(base))
        return b.encodeString(s)

    @staticmethod
    def decode(s,base):
        b = haxe_crypto_BaseCode(haxe_io_Bytes.ofString(base))
        return b.decodeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.base = None
        _hx_o.nbits = None
        _hx_o.tbl = None
haxe_crypto_BaseCode._hx_class = haxe_crypto_BaseCode


class haxe_crypto_Crc32:
    _hx_class_name = "haxe.crypto.Crc32"
    __slots__ = ("crc",)
    _hx_fields = ["crc"]
    _hx_methods = ["byte", "update", "get"]
    _hx_statics = ["make"]

    def __init__(self):
        self.crc = -1

    def byte(self,b):
        tmp = (((self.crc ^ b)) & 255)
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        self.crc = (HxOverrides.rshift(self.crc, 8) ^ tmp)

    def update(self,b,pos,_hx_len):
        b1 = b.b
        _g = pos
        _g1 = (pos + _hx_len)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            tmp = (((self.crc ^ b1[i])) & 255)
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            self.crc = (HxOverrides.rshift(self.crc, 8) ^ tmp)

    def get(self):
        return (self.crc ^ -1)

    @staticmethod
    def make(data):
        c_crc = -1
        b = data.b
        _g = 0
        _g1 = data.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            tmp = (((c_crc ^ b[i])) & 255)
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            c_crc = (HxOverrides.rshift(c_crc, 8) ^ tmp)
        return (c_crc ^ -1)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.crc = None
haxe_crypto_Crc32._hx_class = haxe_crypto_Crc32


class haxe_ds_TreeNode:
    _hx_class_name = "haxe.ds.TreeNode"
    __slots__ = ("left", "right", "key", "value", "_height")
    _hx_fields = ["left", "right", "key", "value", "_height"]
    _hx_methods = ["toString"]

    def __init__(self,l,k,v,r,h = None):
        if (h is None):
            h = -1
        self._height = None
        self.left = l
        self.key = k
        self.value = v
        self.right = r
        if (h == -1):
            tmp = None
            _this = self.left
            _this1 = self.right
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                _this = self.left
                tmp = (0 if ((_this is None)) else _this._height)
            else:
                _this = self.right
                tmp = (0 if ((_this is None)) else _this._height)
            self._height = (tmp + 1)
        else:
            self._height = h

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.left is None)) else (HxOverrides.stringOrNull(self.left.toString()) + ", ")))) + (((("" + Std.string(self.key)) + "=") + Std.string(self.value)))) + HxOverrides.stringOrNull((("" if ((self.right is None)) else (", " + HxOverrides.stringOrNull(self.right.toString()))))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.left = None
        _hx_o.right = None
        _hx_o.key = None
        _hx_o.value = None
        _hx_o._height = None
haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode


class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):
    _hx_class_name = "haxe.ds.EnumValueMap"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["compare", "compareArgs", "compareArg", "copy"]
    _hx_statics = []
    _hx_interfaces = [haxe_IMap]
    _hx_super = haxe_ds_BalancedTree


    def __init__(self):
        super().__init__()

    def compare(self,k1,k2):
        d = (k1.index - k2.index)
        if (d != 0):
            return d
        p1 = list(k1.params)
        p2 = list(k2.params)
        if ((len(p1) == 0) and ((len(p2) == 0))):
            return 0
        return self.compareArgs(p1,p2)

    def compareArgs(self,a1,a2):
        ld = (len(a1) - len(a2))
        if (ld != 0):
            return ld
        _g = 0
        _g1 = len(a1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            d = self.compareArg((a1[i] if i >= 0 and i < len(a1) else None),(a2[i] if i >= 0 and i < len(a2) else None))
            if (d != 0):
                return d
        return 0

    def compareArg(self,v1,v2):
        if (Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2)):
            return self.compare(v1,v2)
        elif (Std.isOfType(v1,list) and Std.isOfType(v2,list)):
            return self.compareArgs(v1,v2)
        else:
            return Reflect.compare(v1,v2)

    def copy(self):
        copied = haxe_ds_EnumValueMap()
        copied.root = self.root
        return copied

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap


class haxe_ds__HashMap_HashMap_Impl_:
    _hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "copy", "iterator", "keyValueIterator", "clear"]

    @staticmethod
    def _new():
        this1 = haxe_ds__HashMap_HashMapData()
        return this1

    @staticmethod
    def set(this1,k,v):
        this1.keys.set(k.hashCode(),k)
        this1.values.set(k.hashCode(),v)

    @staticmethod
    def get(this1,k):
        _this = this1.values
        key = k.hashCode()
        return _this.h.get(key,None)

    @staticmethod
    def exists(this1,k):
        _this = this1.values
        return (k.hashCode() in _this.h)

    @staticmethod
    def remove(this1,k):
        this1.values.remove(k.hashCode())
        return this1.keys.remove(k.hashCode())

    @staticmethod
    def keys(this1):
        return this1.keys.iterator()

    @staticmethod
    def copy(this1):
        copied = haxe_ds__HashMap_HashMapData()
        copied.keys = this1.keys.copy()
        copied.values = this1.values.copy()
        return copied

    @staticmethod
    def iterator(this1):
        return this1.values.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_HashMapKeyValueIterator(this1)

    @staticmethod
    def clear(this1):
        this1.keys.h.clear()
        this1.values.h.clear()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_


class haxe_ds__HashMap_HashMapData:
    _hx_class_name = "haxe.ds._HashMap.HashMapData"
    __slots__ = ("keys", "values")
    _hx_fields = ["keys", "values"]

    def __init__(self):
        self.keys = haxe_ds_IntMap()
        self.values = haxe_ds_IntMap()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.keys = None
        _hx_o.values = None
haxe_ds__HashMap_HashMapData._hx_class = haxe_ds__HashMap_HashMapData


class haxe_ds_IntMap:
    _hx_class_name = "haxe.ds.IntMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        if (not (key in self.h)):
            return False
        del self.h[key]
        return True

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_IntMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_IntMap._hx_class = haxe_ds_IntMap


class haxe_ds__Map_Map_Impl_:
    _hx_class_name = "haxe.ds._Map.Map_Impl_"
    __slots__ = ()
    _hx_statics = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear", "arrayWrite", "toStringMap", "toIntMap", "toEnumValueMapMap", "toObjectMap", "fromStringMap", "fromIntMap", "fromObjectMap"]

    @staticmethod
    def set(this1,key,value):
        this1.set(key,value)

    @staticmethod
    def get(this1,key):
        return this1.get(key)

    @staticmethod
    def exists(this1,key):
        return this1.exists(key)

    @staticmethod
    def remove(this1,key):
        return this1.remove(key)

    @staticmethod
    def keys(this1):
        return this1.keys()

    @staticmethod
    def iterator(this1):
        return this1.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return this1.keyValueIterator()

    @staticmethod
    def copy(this1):
        return this1.copy()

    @staticmethod
    def toString(this1):
        return this1.toString()

    @staticmethod
    def clear(this1):
        this1.clear()

    @staticmethod
    def arrayWrite(this1,k,v):
        this1.set(k,v)
        return v

    @staticmethod
    def toStringMap(t):
        return haxe_ds_StringMap()

    @staticmethod
    def toIntMap(t):
        return haxe_ds_IntMap()

    @staticmethod
    def toEnumValueMapMap(t):
        return haxe_ds_EnumValueMap()

    @staticmethod
    def toObjectMap(t):
        return haxe_ds_ObjectMap()

    @staticmethod
    def fromStringMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromIntMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromObjectMap(_hx_map):
        return _hx_map
haxe_ds__Map_Map_Impl_._hx_class = haxe_ds__Map_Map_Impl_


class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        r = (key in self.h)
        if r:
            del self.h[key]
        return r

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_ObjectMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(Std.string(i1)))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap


class haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_:
    _hx_class_name = "haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "get", "concat"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def get(this1,i):
        return (this1[i] if i >= 0 and i < len(this1) else None)

    @staticmethod
    def concat(this1,a):
        return (this1 + a)
haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_._hx_class = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        has = (key in self.h)
        if has:
            del self.h[key]
        return has

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_StringMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            value = self.h.get(key1,None)
            copied.h[key1] = value
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap


class haxe_ds__Vector_Vector_Impl_:
    _hx_class_name = "haxe.ds._Vector.Vector_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "get", "set", "get_length", "blit", "toArray", "toData", "fromData", "fromArrayCopy", "copy", "join", "map", "sort"]
    length = None

    @staticmethod
    def _new(length):
        this1 = [None]*length
        return this1

    @staticmethod
    def get(this1,index):
        return this1[index]

    @staticmethod
    def set(this1,index,val):
        this1[index] = val
        return val

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def blit(src,srcPos,dest,destPos,_hx_len):
        if (src is dest):
            if (srcPos < destPos):
                i = (srcPos + _hx_len)
                j = (destPos + _hx_len)
                _g = 0
                _g1 = _hx_len
                while (_g < _g1):
                    k = _g
                    _g = (_g + 1)
                    i = (i - 1)
                    j = (j - 1)
                    val = src[i]
                    src[j] = val
            elif (srcPos > destPos):
                i = srcPos
                j = destPos
                _g = 0
                _g1 = _hx_len
                while (_g < _g1):
                    k = _g
                    _g = (_g + 1)
                    val = src[i]
                    src[j] = val
                    i = (i + 1)
                    j = (j + 1)
        else:
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                val = src[(srcPos + i)]
                dest[(destPos + i)] = val

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def toData(this1):
        return this1

    @staticmethod
    def fromData(data):
        return data

    @staticmethod
    def fromArrayCopy(array):
        return list(array)

    @staticmethod
    def copy(this1):
        this2 = [None]*len(this1)
        r = this2
        haxe_ds__Vector_Vector_Impl_.blit(this1,0,r,0,len(this1))
        return r

    @staticmethod
    def join(this1,sep):
        b_b = python_lib_io_StringIO()
        _hx_len = len(this1)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            b_b.write(Std.string(Std.string(this1[i])))
            if (i < ((_hx_len - 1))):
                b_b.write(Std.string(sep))
        return b_b.getvalue()

    @staticmethod
    def map(this1,f):
        length = len(this1)
        this2 = [None]*length
        r = this2
        _hx_len = length
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            v = f(this1[i])
            r[i] = v
        return r

    @staticmethod
    def sort(this1,f):
        this1.sort(key= python_lib_Functools.cmp_to_key(f))
haxe_ds__Vector_Vector_Impl_._hx_class = haxe_ds__Vector_Vector_Impl_


class haxe_ds_WeakMap:
    _hx_class_name = "haxe.ds.WeakMap"
    __slots__ = ()
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        raise haxe_exceptions_NotImplementedException("Not implemented for this platform",None,_hx_AnonObject({'fileName': "haxe/ds/WeakMap.hx", 'lineNumber': 39, 'className': "haxe.ds.WeakMap", 'methodName': "new"}))

    def set(self,key,value):
        pass

    def get(self,key):
        return None

    def exists(self,key):
        return False

    def remove(self,key):
        return False

    def keys(self):
        return None

    def iterator(self):
        return None

    def keyValueIterator(self):
        return None

    def copy(self):
        return None

    def toString(self):
        return None

    def clear(self):
        pass

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap


class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.posInfos = None
haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException


class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException


class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

    def __init__(self):
        self.b = bytearray()

    def get_length(self):
        return len(self.b)

    def addByte(self,byte):
        self.b.append(byte)

    def add(self,src):
        self.b.extend(src.b)

    def addString(self,v,encoding = None):
        self.b.extend(bytearray(v,"UTF-8"))

    def addInt32(self,v):
        self.b.append((v & 255))
        self.b.append(((v >> 8) & 255))
        self.b.append(((v >> 16) & 255))
        self.b.append(HxOverrides.rshift(v, 24))

    def addInt64(self,v):
        self.addInt32(v.low)
        self.addInt32(v.high)

    def addFloat(self,v):
        self.addInt32(haxe_io_FPHelper.floatToI32(v))

    def addDouble(self,v):
        self.addInt64(haxe_io_FPHelper.doubleToI64(v))

    def addBytes(self,src,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b.extend(src.b[pos:(pos + _hx_len)])

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def write(self,s):
        l = s.length
        p = 0
        while (l > 0):
            k = self.writeBytes(s,p,l)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            l = (l - k)

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeFloat(self,x):
        self.writeInt32(haxe_io_FPHelper.floatToI32(x))

    def writeDouble(self,x):
        i64 = haxe_io_FPHelper.doubleToI64(x)
        if self.bigEndian:
            self.writeInt32(i64.high)
            self.writeInt32(i64.low)
        else:
            self.writeInt32(i64.low)
            self.writeInt32(i64.high)

    def writeInt8(self,x):
        if ((x < -128) or ((x >= 128))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeByte((x & 255))

    def writeInt16(self,x):
        if ((x < -32768) or ((x >= 32768))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt16((x & 65535))

    def writeUInt16(self,x):
        if ((x < 0) or ((x >= 65536))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 8))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte((x >> 8))

    def writeInt24(self,x):
        if ((x < -8388608) or ((x >= 8388608))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt24((x & 16777215))

    def writeUInt24(self,x):
        if ((x < 0) or ((x >= 16777216))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 16))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x >> 16))

    def writeInt32(self,x):
        if self.bigEndian:
            self.writeByte(HxOverrides.rshift(x, 24))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(HxOverrides.rshift(x, 24))

    def prepare(self,nbytes):
        pass

    def writeInput(self,i,bufsize = None):
        if (bufsize is None):
            bufsize = 4096
        buf = haxe_io_Bytes.alloc(bufsize)
        try:
            while True:
                _hx_len = i.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                p = 0
                while (_hx_len > 0):
                    k = self.writeBytes(buf,p,_hx_len)
                    if (k == 0):
                        raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                    p = (p + k)
                    _hx_len = (_hx_len - k)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output


class haxe_io_BytesOutput(haxe_io_Output):
    _hx_class_name = "haxe.io.BytesOutput"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "writeByte", "writeBytes", "getBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self):
        self.b = haxe_io_BytesBuffer()
        self.set_bigEndian(False)

    def get_length(self):
        return len(self.b.b)

    def writeByte(self,c):
        self.b.b.append(c)

    def writeBytes(self,buf,pos,_hx_len):
        _this = self.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        _this.b.extend(buf.b[pos:(pos + _hx_len)])
        return _hx_len

    def getBytes(self):
        return self.b.getBytes()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesOutput._hx_class = haxe_io_BytesOutput

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        return "Eof"

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_io_Eof._hx_class = haxe_io_Eof

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error


class haxe_io_FPHelper:
    _hx_class_name = "haxe.io.FPHelper"
    __slots__ = ()
    _hx_statics = ["i64tmp", "LN2", "_i32ToFloat", "_i64ToDouble", "_floatToI32", "_doubleToI64", "i32ToFloat", "floatToI32", "i64ToDouble", "doubleToI64"]

    @staticmethod
    def _i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
        return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def _i64ToDouble(lo,hi):
        sign = (1 - ((HxOverrides.rshift(hi, 31) << 1)))
        e = ((hi >> 20) & 2047)
        if (e == 2047):
            if ((lo == 0) and ((((hi & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = (2.220446049250313e-16 * ((((((hi & 1048575)) * 4294967296.) + (((HxOverrides.rshift(lo, 31)) * 2147483648.))) + ((lo & 2147483647)))))
        if (e == 0):
            m = (m * 2.0)
        else:
            m = (m + 1.0)
        return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def _floatToI32(f):
        if (f == 0):
            return 0
        af = (-f if ((f < 0)) else f)
        exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
        if (exp > 127):
            return 2139095040
        else:
            if (exp <= -127):
                exp = -127
                af = (af * 7.1362384635298e+44)
            else:
                af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
            return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def _doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64

    @staticmethod
    def i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
            return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def floatToI32(f):
        if (f == 0):
            return 0
        else:
            af = (-f if ((f < 0)) else f)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
            if (exp > 127):
                return 2139095040
            else:
                if (exp <= -127):
                    exp = -127
                    af = (af * 7.1362384635298e+44)
                else:
                    af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
                return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def i64ToDouble(low,high):
        sign = (1 - ((HxOverrides.rshift(high, 31) << 1)))
        e = ((high >> 20) & 2047)
        if (e == 2047):
            if ((low == 0) and ((((high & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = (2.220446049250313e-16 * ((((((high & 1048575)) * 4294967296.) + (((HxOverrides.rshift(low, 31)) * 2147483648.))) + ((low & 2147483647)))))
            if (e == 0):
                m = (m * 2.0)
            else:
                m = (m + 1.0)
            return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64
haxe_io_FPHelper._hx_class = haxe_io_FPHelper


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def readAll(self,bufsize = None):
        if (bufsize is None):
            bufsize = 16384
        buf = haxe_io_Bytes.alloc(bufsize)
        total = haxe_io_BytesBuffer()
        try:
            while True:
                _hx_len = self.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                total.b.extend(buf.b[0:_hx_len])
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return total.getBytes()

    def readFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.readBytes(s,pos,_hx_len)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def read(self,nbytes):
        s = haxe_io_Bytes.alloc(nbytes)
        p = 0
        while (nbytes > 0):
            k = self.readBytes(s,p,nbytes)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            nbytes = (nbytes - k)
        return s

    def readUntil(self,end):
        buf = haxe_io_BytesBuffer()
        last = None
        while True:
            last = self.readByte()
            if (not ((last != end))):
                break
            buf.b.append(last)
        return buf.getBytes().toString()

    def readLine(self):
        buf = haxe_io_BytesBuffer()
        last = None
        s = None
        try:
            while True:
                last = self.readByte()
                if (not ((last != 10))):
                    break
                buf.b.append(last)
            s = buf.getBytes().toString()
            if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
                s = HxString.substr(s,0,-1)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,haxe_io_Eof):
                e = _g1
                s = buf.getBytes().toString()
                if (len(s) == 0):
                    raise haxe_Exception.thrown(e)
            else:
                raise _g
        return s

    def readFloat(self):
        return haxe_io_FPHelper.i32ToFloat(self.readInt32())

    def readDouble(self):
        i1 = self.readInt32()
        i2 = self.readInt32()
        if self.bigEndian:
            return haxe_io_FPHelper.i64ToDouble(i2,i1)
        else:
            return haxe_io_FPHelper.i64ToDouble(i1,i2)

    def readInt8(self):
        n = self.readByte()
        if (n >= 128):
            return (n - 256)
        return n

    def readInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        n = ((ch2 | ((ch1 << 8))) if (self.bigEndian) else (ch1 | ((ch2 << 8))))
        if (((n & 32768)) != 0):
            return (n - 65536)
        return n

    def readUInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        if self.bigEndian:
            return (ch2 | ((ch1 << 8)))
        else:
            return (ch1 | ((ch2 << 8)))

    def readInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        n = (((ch3 | ((ch2 << 8))) | ((ch1 << 16))) if (self.bigEndian) else ((ch1 | ((ch2 << 8))) | ((ch3 << 16))))
        if (((n & 8388608)) != 0):
            return (n - 16777216)
        return n

    def readUInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        if self.bigEndian:
            return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
        else:
            return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

    def readInt32(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        ch4 = self.readByte()
        n = ((((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24))) if (self.bigEndian) else (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24))))
        if (((n & -2147483648)) != 0):
            return (n | -2147483648)
        else:
            return n

    def readString(self,_hx_len,encoding = None):
        b = haxe_io_Bytes.alloc(_hx_len)
        self.readFullBytes(b,0,_hx_len)
        return b.getString(0,_hx_len,encoding)

    def getDoubleSig(self,_hx_bytes):
        return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input


class haxe_io_Path:
    _hx_class_name = "haxe.io.Path"
    __slots__ = ("dir", "file", "ext", "backslash")
    _hx_fields = ["dir", "file", "ext", "backslash"]
    _hx_methods = ["toString"]
    _hx_statics = ["withoutExtension", "withoutDirectory", "directory", "extension", "withExtension", "join", "normalize", "addTrailingSlash", "removeTrailingSlashes", "isAbsolute", "unescape", "escape"]

    def __init__(self,path):
        self.backslash = None
        self.ext = None
        self.file = None
        self.dir = None
        path1 = path
        _hx_local_0 = len(path1)
        if (_hx_local_0 == 1):
            if (path1 == "."):
                self.dir = path
                self.file = ""
                return
        elif (_hx_local_0 == 2):
            if (path1 == ".."):
                self.dir = path
                self.file = ""
                return
        else:
            pass
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            self.dir = HxString.substr(path,0,c2)
            path = HxString.substr(path,(c2 + 1),None)
            self.backslash = True
        elif (c2 < c1):
            self.dir = HxString.substr(path,0,c1)
            path = HxString.substr(path,(c1 + 1),None)
        else:
            self.dir = None
        startIndex = None
        cp = None
        if (startIndex is None):
            cp = path.rfind(".", 0, len(path))
        else:
            i = path.rfind(".", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
            check = path.find(".", startLeft, len(path))
            cp = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (cp != -1):
            self.ext = HxString.substr(path,(cp + 1),None)
            self.file = HxString.substr(path,0,cp)
        else:
            self.ext = None
            self.file = path

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.dir is None)) else (HxOverrides.stringOrNull(self.dir) + HxOverrides.stringOrNull((("\\" if (self.backslash) else "/"))))))) + HxOverrides.stringOrNull(self.file)) + HxOverrides.stringOrNull((("" if ((self.ext is None)) else ("." + HxOverrides.stringOrNull(self.ext))))))

    @staticmethod
    def withoutExtension(path):
        s = haxe_io_Path(path)
        s.ext = None
        return s.toString()

    @staticmethod
    def withoutDirectory(path):
        s = haxe_io_Path(path)
        s.dir = None
        return s.toString()

    @staticmethod
    def directory(path):
        s = haxe_io_Path(path)
        if (s.dir is None):
            return ""
        return s.dir

    @staticmethod
    def extension(path):
        s = haxe_io_Path(path)
        if (s.ext is None):
            return ""
        return s.ext

    @staticmethod
    def withExtension(path,ext):
        s = haxe_io_Path(path)
        s.ext = ext
        return s.toString()

    @staticmethod
    def join(paths):
        def _hx_local_0(s):
            if (s is not None):
                return (s != "")
            else:
                return False
        paths1 = list(filter(_hx_local_0,paths))
        if (len(paths1) == 0):
            return ""
        path = (paths1[0] if 0 < len(paths1) else None)
        _g = 1
        _g1 = len(paths1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            path = haxe_io_Path.addTrailingSlash(path)
            path = (("null" if path is None else path) + HxOverrides.stringOrNull((paths1[i] if i >= 0 and i < len(paths1) else None)))
        return haxe_io_Path.normalize(path)

    @staticmethod
    def normalize(path):
        slash = "/"
        _this = path.split("\\")
        path = slash.join([python_Boot.toString1(x1,'') for x1 in _this])
        if (path == slash):
            return slash
        target = []
        _g = 0
        _g1 = (list(path) if ((slash == "")) else path.split(slash))
        while (_g < len(_g1)):
            token = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((token == "..") and ((len(target) > 0))) and ((python_internal_ArrayImpl._get(target, (len(target) - 1)) != ".."))):
                if (len(target) != 0):
                    target.pop()
            elif (token == ""):
                if ((len(target) > 0) or ((HxString.charCodeAt(path,0) == 47))):
                    target.append(token)
            elif (token != "."):
                target.append(token)
        tmp = slash.join([python_Boot.toString1(x1,'') for x1 in target])
        acc_b = python_lib_io_StringIO()
        colon = False
        slashes = False
        _g = 0
        _g1 = len(tmp)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = (-1 if ((i >= len(tmp))) else ord(tmp[i]))
            _g3 = _g2
            if (_g3 == 47):
                if (not colon):
                    slashes = True
                else:
                    i1 = _g2
                    colon = False
                    if slashes:
                        acc_b.write("/")
                        slashes = False
                    acc_b.write("".join(map(chr,[i1])))
            elif (_g3 == 58):
                acc_b.write(":")
                colon = True
            else:
                i2 = _g2
                colon = False
                if slashes:
                    acc_b.write("/")
                    slashes = False
                acc_b.write("".join(map(chr,[i2])))
        return acc_b.getvalue()

    @staticmethod
    def addTrailingSlash(path):
        if (len(path) == 0):
            return "/"
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            if (c2 != ((len(path) - 1))):
                return (("null" if path is None else path) + "\\")
            else:
                return path
        elif (c1 != ((len(path) - 1))):
            return (("null" if path is None else path) + "/")
        else:
            return path

    @staticmethod
    def removeTrailingSlashes(path):
        while True:
            _g = HxString.charCodeAt(path,(len(path) - 1))
            if (_g is None):
                break
            else:
                _g1 = _g
                if ((_g1 == 92) or ((_g1 == 47))):
                    path = HxString.substr(path,0,-1)
                else:
                    break
        return path

    @staticmethod
    def isAbsolute(path):
        if path.startswith("/"):
            return True
        if ((("" if ((1 >= len(path))) else path[1])) == ":"):
            return True
        if path.startswith("\\\\"):
            return True
        return False

    @staticmethod
    def unescape(path):
        regex = EReg("-x([0-9][0-9])","g")
        def _hx_local_1():
            def _hx_local_0(regex):
                code = Std.parseInt(regex.matchObj.group(1))
                return "".join(map(chr,[code]))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def escape(path,allowSlashes = None):
        if (allowSlashes is None):
            allowSlashes = False
        regex = (EReg("[^A-Za-z0-9_/\\\\\\.]","g") if allowSlashes else EReg("[^A-Za-z0-9_\\.]","g"))
        def _hx_local_1():
            def _hx_local_0(v):
                return ("-x" + Std.string(HxString.charCodeAt(v.matchObj.group(0),0)))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.dir = None
        _hx_o.file = None
        _hx_o.ext = None
        _hx_o.backslash = None
haxe_io_Path._hx_class = haxe_io_Path


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.array = None
        _hx_o.current = None
haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.current = None
        _hx_o.array = None
haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator


class haxe_iterators_HashMapKeyValueIterator:
    _hx_class_name = "haxe.iterators.HashMapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys.iterator()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        _this = self.map.values
        key1 = key.hashCode()
        return _hx_AnonObject({'value': _this.h.get(key1,None), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_HashMapKeyValueIterator._hx_class = haxe_iterators_HashMapKeyValueIterator


class haxe_iterators_MapKeyValueIterator:
    _hx_class_name = "haxe.iterators.MapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        return _hx_AnonObject({'value': self.map.get(key), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_MapKeyValueIterator._hx_class = haxe_iterators_MapKeyValueIterator


class haxe_iterators_RestIterator:
    _hx_class_name = "haxe.iterators.RestIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        index = self.current
        self.current = (self.current + 1)
        return python_internal_ArrayImpl._get(self.args, index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestIterator._hx_class = haxe_iterators_RestIterator


class haxe_iterators_RestKeyValueIterator:
    _hx_class_name = "haxe.iterators.RestKeyValueIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        tmp = self.current
        index = self.current
        self.current = (self.current + 1)
        return _hx_AnonObject({'key': tmp, 'value': python_internal_ArrayImpl._get(self.args, index)})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestKeyValueIterator._hx_class = haxe_iterators_RestKeyValueIterator


class haxe_iterators_StringIterator:
    _hx_class_name = "haxe.iterators.StringIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIterator._hx_class = haxe_iterators_StringIterator


class haxe_iterators_StringIteratorUnicode:
    _hx_class_name = "haxe.iterators.StringIteratorUnicode"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]
    _hx_statics = ["unicodeIterator"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def unicodeIterator(s):
        return haxe_iterators_StringIteratorUnicode(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIteratorUnicode._hx_class = haxe_iterators_StringIteratorUnicode


class haxe_iterators_StringKeyValueIterator:
    _hx_class_name = "haxe.iterators.StringKeyValueIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        tmp = self.offset
        s = self.s
        index = self.offset
        self.offset = (self.offset + 1)
        return _hx_AnonObject({'key': tmp, 'value': (-1 if ((index >= len(s))) else ord(s[index]))})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringKeyValueIterator._hx_class = haxe_iterators_StringKeyValueIterator


class haxe_xml_XmlParserException:
    _hx_class_name = "haxe.xml.XmlParserException"
    __slots__ = ("message", "lineNumber", "positionAtLine", "position", "xml")
    _hx_fields = ["message", "lineNumber", "positionAtLine", "position", "xml"]
    _hx_methods = ["toString"]

    def __init__(self,message,xml,position):
        self.xml = xml
        self.message = message
        self.position = position
        self.lineNumber = 1
        self.positionAtLine = 0
        _g = 0
        _g1 = position
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(xml))) else ord(xml[i]))
            if (c == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.lineNumber
                _hx_local_0.lineNumber = (_hx_local_1 + 1)
                _hx_local_1
                self.positionAtLine = 0
            elif (c != 13):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.positionAtLine
                _hx_local_2.positionAtLine = (_hx_local_3 + 1)
                _hx_local_3

    def toString(self):
        return ((((((HxOverrides.stringOrNull(Type.getClassName(Type.getClass(self))) + ": ") + HxOverrides.stringOrNull(self.message)) + " at line ") + Std.string(self.lineNumber)) + " char ") + Std.string(self.positionAtLine))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.message = None
        _hx_o.lineNumber = None
        _hx_o.positionAtLine = None
        _hx_o.position = None
        _hx_o.xml = None
haxe_xml_XmlParserException._hx_class = haxe_xml_XmlParserException


class haxe_xml_Parser:
    _hx_class_name = "haxe.xml.Parser"
    __slots__ = ()
    _hx_statics = ["escapes", "parse", "doParse", "isValidChar"]

    @staticmethod
    def parse(_hx_str,strict = None):
        if (strict is None):
            strict = False
        doc = Xml.createDocument()
        haxe_xml_Parser.doParse(_hx_str,strict,0,doc)
        return doc

    @staticmethod
    def doParse(_hx_str,strict,p = None,parent = None):
        if (p is None):
            p = 0
        xml = None
        state = 1
        next = 1
        aname = None
        start = 0
        nsubs = 0
        nbrackets = 0
        buf = StringBuf()
        escapeNext = 1
        attrValQuote = -1
        while (p < len(_hx_str)):
            c = ord(_hx_str[p])
            state1 = state
            if (state1 == 0):
                c1 = c
                if ((((c1 == 32) or ((c1 == 13))) or ((c1 == 10))) or ((c1 == 9))):
                    pass
                else:
                    state = next
                    continue
            elif (state1 == 1):
                if (c == 60):
                    state = 0
                    next = 2
                else:
                    start = p
                    state = 13
                    continue
            elif (state1 == 2):
                c2 = c
                if (c2 == 33):
                    index = (p + 1)
                    if (((-1 if ((index >= len(_hx_str))) else ord(_hx_str[index]))) == 91):
                        p = (p + 2)
                        if (HxString.substr(_hx_str,p,6).upper() != "CDATA["):
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <![CDATA[",_hx_str,p))
                        p = (p + 5)
                        state = 17
                        start = (p + 1)
                    else:
                        tmp = None
                        index1 = (p + 1)
                        if (((-1 if ((index1 >= len(_hx_str))) else ord(_hx_str[index1]))) != 68):
                            index2 = (p + 1)
                            tmp = (((-1 if ((index2 >= len(_hx_str))) else ord(_hx_str[index2]))) == 100)
                        else:
                            tmp = True
                        if tmp:
                            if (HxString.substr(_hx_str,(p + 2),6).upper() != "OCTYPE"):
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!DOCTYPE",_hx_str,p))
                            p = (p + 8)
                            state = 16
                            start = (p + 1)
                        else:
                            tmp1 = None
                            index3 = (p + 1)
                            if (((-1 if ((index3 >= len(_hx_str))) else ord(_hx_str[index3]))) == 45):
                                index4 = (p + 2)
                                tmp1 = (((-1 if ((index4 >= len(_hx_str))) else ord(_hx_str[index4]))) != 45)
                            else:
                                tmp1 = True
                            if tmp1:
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!--",_hx_str,p))
                            else:
                                p = (p + 2)
                                state = 15
                                start = (p + 1)
                elif (c2 == 47):
                    if (parent is None):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    start = (p + 1)
                    state = 0
                    next = 10
                elif (c2 == 63):
                    state = 14
                    start = p
                else:
                    state = 3
                    start = p
                    continue
            elif (state1 == 3):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (p == start):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    xml = Xml.createElement(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(xml)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 4
                    continue
            elif (state1 == 4):
                c3 = c
                if (c3 == 47):
                    state = 11
                elif (c3 == 62):
                    state = 9
                else:
                    state = 5
                    start = p
                    continue
            elif (state1 == 5):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected attribute name",_hx_str,p))
                    tmp2 = HxString.substr(_hx_str,start,(p - start))
                    aname = tmp2
                    if xml.exists(aname):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Duplicate attribute [" + ("null" if aname is None else aname)) + "]"),_hx_str,p))
                    state = 0
                    next = 6
                    continue
            elif (state1 == 6):
                if (c == 61):
                    state = 0
                    next = 7
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected =",_hx_str,p))
            elif (state1 == 7):
                c4 = c
                if ((c4 == 39) or ((c4 == 34))):
                    buf = StringBuf()
                    state = 8
                    start = (p + 1)
                    attrValQuote = c
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected \"",_hx_str,p))
            elif (state1 == 8):
                c5 = c
                if (c5 == 38):
                    _hx_len = (p - start)
                    s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                    buf.b.write(s)
                    state = 18
                    escapeNext = 8
                    start = (p + 1)
                elif ((c5 == 62) or ((c5 == 60))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Invalid unescaped " + HxOverrides.stringOrNull("".join(map(chr,[c])))) + " in attribute value"),_hx_str,p))
                    elif (c == attrValQuote):
                        len1 = (p - start)
                        s1 = (HxString.substr(_hx_str,start,None) if ((len1 is None)) else HxString.substr(_hx_str,start,len1))
                        buf.b.write(s1)
                        val = buf.b.getvalue()
                        buf = StringBuf()
                        xml.set(aname,val)
                        state = 0
                        next = 4
                elif (c == attrValQuote):
                    len2 = (p - start)
                    s2 = (HxString.substr(_hx_str,start,None) if ((len2 is None)) else HxString.substr(_hx_str,start,len2))
                    buf.b.write(s2)
                    val1 = buf.b.getvalue()
                    buf = StringBuf()
                    xml.set(aname,val1)
                    state = 0
                    next = 4
            elif (state1 == 9):
                p = haxe_xml_Parser.doParse(_hx_str,strict,p,xml)
                start = p
                state = 1
            elif (state1 == 10):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    v = HxString.substr(_hx_str,start,(p - start))
                    if ((parent is None) or ((parent.nodeType != 0))):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unexpected </" + ("null" if v is None else v)) + ">, tag is not open"),_hx_str,p))
                    if (parent.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                    if (v != parent.nodeName):
                        if (parent.nodeType != Xml.Element):
                            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Expected </" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
                    state = 0
                    next = 12
                    continue
            elif (state1 == 11):
                if (c == 62):
                    state = 1
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 12):
                if (c == 62):
                    if (nsubs == 0):
                        parent.addChild(Xml.createPCData(""))
                    return p
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 13):
                if (c == 60):
                    len3 = (p - start)
                    s3 = (HxString.substr(_hx_str,start,None) if ((len3 is None)) else HxString.substr(_hx_str,start,len3))
                    buf.b.write(s3)
                    child = Xml.createPCData(buf.b.getvalue())
                    buf = StringBuf()
                    parent.addChild(child)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 2
                elif (c == 38):
                    len4 = (p - start)
                    s4 = (HxString.substr(_hx_str,start,None) if ((len4 is None)) else HxString.substr(_hx_str,start,len4))
                    buf.b.write(s4)
                    state = 18
                    escapeNext = 13
                    start = (p + 1)
            elif (state1 == 14):
                tmp3 = None
                if (c == 63):
                    index5 = (p + 1)
                    tmp3 = (((-1 if ((index5 >= len(_hx_str))) else ord(_hx_str[index5]))) == 62)
                else:
                    tmp3 = False
                if tmp3:
                    p = (p + 1)
                    str1 = HxString.substr(_hx_str,(start + 1),((p - start) - 2))
                    parent.addChild(Xml.createProcessingInstruction(str1))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 15):
                tmp4 = None
                tmp5 = None
                if (c == 45):
                    index6 = (p + 1)
                    tmp5 = (((-1 if ((index6 >= len(_hx_str))) else ord(_hx_str[index6]))) == 45)
                else:
                    tmp5 = False
                if tmp5:
                    index7 = (p + 2)
                    tmp4 = (((-1 if ((index7 >= len(_hx_str))) else ord(_hx_str[index7]))) == 62)
                else:
                    tmp4 = False
                if tmp4:
                    parent.addChild(Xml.createComment(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 16):
                if (c == 91):
                    nbrackets = (nbrackets + 1)
                elif (c == 93):
                    nbrackets = (nbrackets - 1)
                elif ((c == 62) and ((nbrackets == 0))):
                    parent.addChild(Xml.createDocType(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 17):
                tmp6 = None
                tmp7 = None
                if (c == 93):
                    index8 = (p + 1)
                    tmp7 = (((-1 if ((index8 >= len(_hx_str))) else ord(_hx_str[index8]))) == 93)
                else:
                    tmp7 = False
                if tmp7:
                    index9 = (p + 2)
                    tmp6 = (((-1 if ((index9 >= len(_hx_str))) else ord(_hx_str[index9]))) == 62)
                else:
                    tmp6 = False
                if tmp6:
                    child1 = Xml.createCData(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(child1)
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 18):
                if (c == 59):
                    s5 = HxString.substr(_hx_str,start,(p - start))
                    if (((-1 if ((0 >= len(s5))) else ord(s5[0]))) == 35):
                        c6 = (Std.parseInt(("0" + HxOverrides.stringOrNull(HxString.substr(s5,1,(len(s5) - 1))))) if ((((-1 if ((1 >= len(s5))) else ord(s5[1]))) == 120)) else Std.parseInt(HxString.substr(s5,1,(len(s5) - 1))))
                        s6 = "".join(map(chr,[c6]))
                        buf.b.write(s6)
                    elif (not (s5 in haxe_xml_Parser.escapes.h)):
                        if strict:
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Undefined entity: " + ("null" if s5 is None else s5)),_hx_str,p))
                        s7 = Std.string((("&" + ("null" if s5 is None else s5)) + ";"))
                        buf.b.write(s7)
                    else:
                        s8 = Std.string(haxe_xml_Parser.escapes.h.get(s5,None))
                        buf.b.write(s8)
                    start = (p + 1)
                    state = escapeNext
                elif ((not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))) and ((c != 35))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Invalid character in entity: " + HxOverrides.stringOrNull("".join(map(chr,[c])))),_hx_str,p))
                    s9 = "".join(map(chr,[38]))
                    buf.b.write(s9)
                    len5 = (p - start)
                    s10 = (HxString.substr(_hx_str,start,None) if ((len5 is None)) else HxString.substr(_hx_str,start,len5))
                    buf.b.write(s10)
                    p = (p - 1)
                    start = (p + 1)
                    state = escapeNext
            else:
                pass
            p = (p + 1)
        if (state == 1):
            start = p
            state = 13
        if (state == 13):
            if (parent.nodeType == 0):
                if (parent.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unclosed node <" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
            if ((p != start) or ((nsubs == 0))):
                _hx_len = (p - start)
                s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                buf.b.write(s)
                parent.addChild(Xml.createPCData(buf.b.getvalue()))
                nsubs = (nsubs + 1)
            return p
        if (((not strict) and ((state == 18))) and ((escapeNext == 13))):
            s = "".join(map(chr,[38]))
            buf.b.write(s)
            _hx_len = (p - start)
            s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
            buf.b.write(s)
            parent.addChild(Xml.createPCData(buf.b.getvalue()))
            nsubs = (nsubs + 1)
            return p
        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Unexpected end",_hx_str,p))

    @staticmethod
    def isValidChar(c):
        if (not ((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))))):
            return (c == 45)
        else:
            return True
haxe_xml_Parser._hx_class = haxe_xml_Parser


class haxe_xml_Printer:
    _hx_class_name = "haxe.xml.Printer"
    __slots__ = ("output", "pretty")
    _hx_fields = ["output", "pretty"]
    _hx_methods = ["writeNode", "write", "newline", "hasChildren"]
    _hx_statics = ["print"]

    def __init__(self,pretty):
        self.output = StringBuf()
        self.pretty = pretty

    def writeNode(self,value,tabs):
        _g = value.nodeType
        if (_g == 0):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<"))
            _this.b.write(s)
            if (value.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeName)
            _this.b.write(s)
            attribute = value.attributes()
            while attribute.hasNext():
                attribute1 = attribute.next()
                _this = self.output
                s = Std.string(((" " + ("null" if attribute1 is None else attribute1)) + "=\""))
                _this.b.write(s)
                input = StringTools.htmlEscape(value.get(attribute1),True)
                _this1 = self.output
                s1 = Std.string(input)
                _this1.b.write(s1)
                self.output.b.write("\"")
            if self.hasChildren(value):
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
                if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _g_current = 0
                _g_array = value.children
                while (_g_current < len(_g_array)):
                    child = _g_current
                    _g_current = (_g_current + 1)
                    child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                    self.writeNode(child1,((("null" if tabs is None else tabs) + "\t") if (self.pretty) else tabs))
                _this = self.output
                s = Std.string((("null" if tabs is None else tabs) + "</"))
                _this.b.write(s)
                if (value.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _this = self.output
                s = Std.string(value.nodeName)
                _this.b.write(s)
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
            else:
                self.output.b.write("/>")
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 1):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            nodeValue = value.nodeValue
            if (len(nodeValue) != 0):
                input = (("null" if tabs is None else tabs) + HxOverrides.stringOrNull(StringTools.htmlEscape(nodeValue)))
                _this = self.output
                s = Std.string(input)
                _this.b.write(s)
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 2):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<![CDATA["))
            _this.b.write(s)
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeValue)
            _this.b.write(s)
            self.output.b.write("]]>")
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 3):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            commentContent = value.nodeValue
            commentContent = EReg("[\n\r\t]+","g").replace(commentContent,"")
            commentContent = (("<!--" + ("null" if commentContent is None else commentContent)) + "-->")
            _this = self.output
            s = Std.string(tabs)
            _this.b.write(s)
            input = StringTools.trim(commentContent)
            _this = self.output
            s = Std.string(input)
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 4):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<!DOCTYPE " + HxOverrides.stringOrNull(value.nodeValue)) + ">"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 5):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<?" + HxOverrides.stringOrNull(value.nodeValue)) + "?>"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 6):
            if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _g_current = 0
            _g_array = value.children
            while (_g_current < len(_g_array)):
                child = _g_current
                _g_current = (_g_current + 1)
                child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                self.writeNode(child1,tabs)
        else:
            pass

    def write(self,input):
        _this = self.output
        s = Std.string(input)
        _this.b.write(s)

    def newline(self):
        if self.pretty:
            self.output.b.write("\n")

    def hasChildren(self,value):
        if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
        _g_current = 0
        _g_array = value.children
        while (_g_current < len(_g_array)):
            child = _g_current
            _g_current = (_g_current + 1)
            child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
            _g = child1.nodeType
            if ((_g == 1) or ((_g == 0))):
                return True
            elif ((_g == 3) or ((_g == 2))):
                if ((child1.nodeType == Xml.Document) or ((child1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((child1.nodeType is None)) else _Xml_XmlType_Impl_.toString(child1.nodeType))))))
                if (len(StringTools.ltrim(child1.nodeValue)) != 0):
                    return True
            else:
                pass
        return False

    @staticmethod
    def print(xml,pretty = None):
        if (pretty is None):
            pretty = False
        printer = haxe_xml_Printer(pretty)
        printer.writeNode(xml,"")
        return printer.output.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.output = None
        _hx_o.pretty = None
haxe_xml_Printer._hx_class = haxe_xml_Printer


class hx_strings__AnyAsString_AnyAsString_Impl_:
    _hx_class_name = "hx.strings._AnyAsString.AnyAsString_Impl_"
    __slots__ = ()
    _hx_statics = ["fromBool", "fromAny"]

    @staticmethod
    def fromBool(value):
        if value:
            return "true"
        else:
            return "false"

    @staticmethod
    def fromAny(value):
        return Std.string(value)
hx_strings__AnyAsString_AnyAsString_Impl_._hx_class = hx_strings__AnyAsString_AnyAsString_Impl_


class hx_strings__Char_CharCaseMapper:
    _hx_class_name = "hx.strings._Char.CharCaseMapper"
    __slots__ = ("mapU2L", "mapL2U")
    _hx_fields = ["mapU2L", "mapL2U"]
    _hx_methods = ["_addCaseMapping", "isLowerCase", "isUpperCase", "toLowerCase", "toUpperCase"]

    def __init__(self):
        self.mapL2U = haxe_ds_IntMap()
        self.mapU2L = haxe_ds_IntMap()
        self._addCaseMapping(97,65)
        self._addCaseMapping(98,66)
        self._addCaseMapping(99,67)
        self._addCaseMapping(100,68)
        self._addCaseMapping(101,69)
        self._addCaseMapping(102,70)
        self._addCaseMapping(103,71)
        self._addCaseMapping(104,72)
        self._addCaseMapping(105,73)
        self._addCaseMapping(106,74)
        self._addCaseMapping(107,75)
        self._addCaseMapping(108,76)
        self._addCaseMapping(109,77)
        self._addCaseMapping(110,78)
        self._addCaseMapping(111,79)
        self._addCaseMapping(112,80)
        self._addCaseMapping(113,81)
        self._addCaseMapping(114,82)
        self._addCaseMapping(115,83)
        self._addCaseMapping(116,84)
        self._addCaseMapping(117,85)
        self._addCaseMapping(118,86)
        self._addCaseMapping(119,87)
        self._addCaseMapping(120,88)
        self._addCaseMapping(121,89)
        self._addCaseMapping(122,90)
        self._addCaseMapping(224,192)
        self._addCaseMapping(225,193)
        self._addCaseMapping(226,194)
        self._addCaseMapping(227,195)
        self._addCaseMapping(228,196)
        self._addCaseMapping(229,197)
        self._addCaseMapping(230,198)
        self._addCaseMapping(231,199)
        self._addCaseMapping(232,200)
        self._addCaseMapping(233,201)
        self._addCaseMapping(234,202)
        self._addCaseMapping(235,203)
        self._addCaseMapping(236,204)
        self._addCaseMapping(237,205)
        self._addCaseMapping(238,206)
        self._addCaseMapping(239,207)
        self._addCaseMapping(240,208)
        self._addCaseMapping(241,209)
        self._addCaseMapping(242,210)
        self._addCaseMapping(243,211)
        self._addCaseMapping(244,212)
        self._addCaseMapping(245,213)
        self._addCaseMapping(246,214)
        self._addCaseMapping(248,216)
        self._addCaseMapping(249,217)
        self._addCaseMapping(250,218)
        self._addCaseMapping(251,219)
        self._addCaseMapping(252,220)
        self._addCaseMapping(253,221)
        self._addCaseMapping(254,222)
        self._addCaseMapping(255,376)
        self._addCaseMapping(257,256)
        self._addCaseMapping(259,258)
        self._addCaseMapping(261,260)
        self._addCaseMapping(263,262)
        self._addCaseMapping(265,264)
        self._addCaseMapping(267,266)
        self._addCaseMapping(269,268)
        self._addCaseMapping(271,270)
        self._addCaseMapping(273,272)
        self._addCaseMapping(275,274)
        self._addCaseMapping(277,276)
        self._addCaseMapping(279,278)
        self._addCaseMapping(281,280)
        self._addCaseMapping(283,282)
        self._addCaseMapping(285,284)
        self._addCaseMapping(287,286)
        self._addCaseMapping(289,288)
        self._addCaseMapping(291,290)
        self._addCaseMapping(293,292)
        self._addCaseMapping(295,294)
        self._addCaseMapping(297,296)
        self._addCaseMapping(299,298)
        self._addCaseMapping(301,300)
        self._addCaseMapping(303,302)
        self._addCaseMapping(305,73)
        self._addCaseMapping(307,306)
        self._addCaseMapping(309,308)
        self._addCaseMapping(311,310)
        self._addCaseMapping(314,313)
        self._addCaseMapping(316,315)
        self._addCaseMapping(318,317)
        self._addCaseMapping(320,319)
        self._addCaseMapping(322,321)
        self._addCaseMapping(324,323)
        self._addCaseMapping(326,325)
        self._addCaseMapping(328,327)
        self._addCaseMapping(331,330)
        self._addCaseMapping(333,332)
        self._addCaseMapping(335,334)
        self._addCaseMapping(337,336)
        self._addCaseMapping(339,338)
        self._addCaseMapping(341,340)
        self._addCaseMapping(343,342)
        self._addCaseMapping(345,344)
        self._addCaseMapping(347,346)
        self._addCaseMapping(349,348)
        self._addCaseMapping(351,350)
        self._addCaseMapping(353,352)
        self._addCaseMapping(355,354)
        self._addCaseMapping(357,356)
        self._addCaseMapping(359,358)
        self._addCaseMapping(361,360)
        self._addCaseMapping(363,362)
        self._addCaseMapping(365,364)
        self._addCaseMapping(367,366)
        self._addCaseMapping(369,368)
        self._addCaseMapping(371,370)
        self._addCaseMapping(373,372)
        self._addCaseMapping(375,374)
        self._addCaseMapping(378,377)
        self._addCaseMapping(380,379)
        self._addCaseMapping(382,381)
        self._addCaseMapping(387,386)
        self._addCaseMapping(389,388)
        self._addCaseMapping(392,391)
        self._addCaseMapping(396,395)
        self._addCaseMapping(402,401)
        self._addCaseMapping(409,408)
        self._addCaseMapping(417,416)
        self._addCaseMapping(419,418)
        self._addCaseMapping(421,420)
        self._addCaseMapping(424,423)
        self._addCaseMapping(429,428)
        self._addCaseMapping(432,431)
        self._addCaseMapping(436,435)
        self._addCaseMapping(438,437)
        self._addCaseMapping(441,440)
        self._addCaseMapping(445,444)
        self._addCaseMapping(454,452)
        self._addCaseMapping(457,455)
        self._addCaseMapping(460,458)
        self._addCaseMapping(462,461)
        self._addCaseMapping(464,463)
        self._addCaseMapping(466,465)
        self._addCaseMapping(468,467)
        self._addCaseMapping(470,469)
        self._addCaseMapping(472,471)
        self._addCaseMapping(474,473)
        self._addCaseMapping(476,475)
        self._addCaseMapping(479,478)
        self._addCaseMapping(481,480)
        self._addCaseMapping(483,482)
        self._addCaseMapping(485,484)
        self._addCaseMapping(487,486)
        self._addCaseMapping(489,488)
        self._addCaseMapping(491,490)
        self._addCaseMapping(493,492)
        self._addCaseMapping(495,494)
        self._addCaseMapping(499,497)
        self._addCaseMapping(501,500)
        self._addCaseMapping(507,506)
        self._addCaseMapping(509,508)
        self._addCaseMapping(511,510)
        self._addCaseMapping(513,512)
        self._addCaseMapping(515,514)
        self._addCaseMapping(517,516)
        self._addCaseMapping(519,518)
        self._addCaseMapping(521,520)
        self._addCaseMapping(523,522)
        self._addCaseMapping(525,524)
        self._addCaseMapping(527,526)
        self._addCaseMapping(529,528)
        self._addCaseMapping(531,530)
        self._addCaseMapping(533,532)
        self._addCaseMapping(535,534)
        self._addCaseMapping(595,385)
        self._addCaseMapping(596,390)
        self._addCaseMapping(599,394)
        self._addCaseMapping(600,398)
        self._addCaseMapping(601,399)
        self._addCaseMapping(603,400)
        self._addCaseMapping(608,403)
        self._addCaseMapping(611,404)
        self._addCaseMapping(616,407)
        self._addCaseMapping(617,406)
        self._addCaseMapping(623,412)
        self._addCaseMapping(626,413)
        self._addCaseMapping(629,415)
        self._addCaseMapping(643,425)
        self._addCaseMapping(648,430)
        self._addCaseMapping(650,433)
        self._addCaseMapping(651,434)
        self._addCaseMapping(658,439)
        self._addCaseMapping(924,181)
        self._addCaseMapping(940,902)
        self._addCaseMapping(941,904)
        self._addCaseMapping(942,905)
        self._addCaseMapping(943,906)
        self._addCaseMapping(945,913)
        self._addCaseMapping(946,914)
        self._addCaseMapping(947,915)
        self._addCaseMapping(948,916)
        self._addCaseMapping(949,917)
        self._addCaseMapping(950,918)
        self._addCaseMapping(951,919)
        self._addCaseMapping(952,920)
        self._addCaseMapping(953,921)
        self._addCaseMapping(954,922)
        self._addCaseMapping(955,923)
        self._addCaseMapping(956,924)
        self._addCaseMapping(957,925)
        self._addCaseMapping(958,926)
        self._addCaseMapping(959,927)
        self._addCaseMapping(960,928)
        self._addCaseMapping(961,929)
        self._addCaseMapping(963,931)
        self._addCaseMapping(964,932)
        self._addCaseMapping(965,933)
        self._addCaseMapping(966,934)
        self._addCaseMapping(967,935)
        self._addCaseMapping(968,936)
        self._addCaseMapping(969,937)
        self._addCaseMapping(970,938)
        self._addCaseMapping(971,939)
        self._addCaseMapping(972,908)
        self._addCaseMapping(973,910)
        self._addCaseMapping(974,911)
        self._addCaseMapping(995,994)
        self._addCaseMapping(997,996)
        self._addCaseMapping(999,998)
        self._addCaseMapping(1001,1000)
        self._addCaseMapping(1003,1002)
        self._addCaseMapping(1005,1004)
        self._addCaseMapping(1007,1006)
        self._addCaseMapping(1072,1040)
        self._addCaseMapping(1073,1041)
        self._addCaseMapping(1074,1042)
        self._addCaseMapping(1075,1043)
        self._addCaseMapping(1076,1044)
        self._addCaseMapping(1077,1045)
        self._addCaseMapping(1078,1046)
        self._addCaseMapping(1079,1047)
        self._addCaseMapping(1080,1048)
        self._addCaseMapping(1081,1049)
        self._addCaseMapping(1082,1050)
        self._addCaseMapping(1083,1051)
        self._addCaseMapping(1084,1052)
        self._addCaseMapping(1085,1053)
        self._addCaseMapping(1086,1054)
        self._addCaseMapping(1087,1055)
        self._addCaseMapping(1088,1056)
        self._addCaseMapping(1089,1057)
        self._addCaseMapping(1090,1058)
        self._addCaseMapping(1091,1059)
        self._addCaseMapping(1092,1060)
        self._addCaseMapping(1093,1061)
        self._addCaseMapping(1094,1062)
        self._addCaseMapping(1095,1063)
        self._addCaseMapping(1096,1064)
        self._addCaseMapping(1097,1065)
        self._addCaseMapping(1098,1066)
        self._addCaseMapping(1099,1067)
        self._addCaseMapping(1100,1068)
        self._addCaseMapping(1101,1069)
        self._addCaseMapping(1102,1070)
        self._addCaseMapping(1103,1071)
        self._addCaseMapping(1105,1025)
        self._addCaseMapping(1106,1026)
        self._addCaseMapping(1107,1027)
        self._addCaseMapping(1108,1028)
        self._addCaseMapping(1109,1029)
        self._addCaseMapping(1110,1030)
        self._addCaseMapping(1111,1031)
        self._addCaseMapping(1112,1032)
        self._addCaseMapping(1113,1033)
        self._addCaseMapping(1114,1034)
        self._addCaseMapping(1115,1035)
        self._addCaseMapping(1116,1036)
        self._addCaseMapping(1118,1038)
        self._addCaseMapping(1119,1039)
        self._addCaseMapping(1121,1120)
        self._addCaseMapping(1123,1122)
        self._addCaseMapping(1125,1124)
        self._addCaseMapping(1127,1126)
        self._addCaseMapping(1129,1128)
        self._addCaseMapping(1131,1130)
        self._addCaseMapping(1133,1132)
        self._addCaseMapping(1135,1134)
        self._addCaseMapping(1137,1136)
        self._addCaseMapping(1139,1138)
        self._addCaseMapping(1141,1140)
        self._addCaseMapping(1143,1142)
        self._addCaseMapping(1145,1144)
        self._addCaseMapping(1147,1146)
        self._addCaseMapping(1149,1148)
        self._addCaseMapping(1151,1150)
        self._addCaseMapping(1153,1152)
        self._addCaseMapping(1169,1168)
        self._addCaseMapping(1171,1170)
        self._addCaseMapping(1173,1172)
        self._addCaseMapping(1175,1174)
        self._addCaseMapping(1177,1176)
        self._addCaseMapping(1179,1178)
        self._addCaseMapping(1181,1180)
        self._addCaseMapping(1183,1182)
        self._addCaseMapping(1185,1184)
        self._addCaseMapping(1187,1186)
        self._addCaseMapping(1189,1188)
        self._addCaseMapping(1191,1190)
        self._addCaseMapping(1193,1192)
        self._addCaseMapping(1195,1194)
        self._addCaseMapping(1197,1196)
        self._addCaseMapping(1199,1198)
        self._addCaseMapping(1201,1200)
        self._addCaseMapping(1203,1202)
        self._addCaseMapping(1205,1204)
        self._addCaseMapping(1207,1206)
        self._addCaseMapping(1209,1208)
        self._addCaseMapping(1211,1210)
        self._addCaseMapping(1213,1212)
        self._addCaseMapping(1215,1214)
        self._addCaseMapping(1218,1217)
        self._addCaseMapping(1220,1219)
        self._addCaseMapping(1224,1223)
        self._addCaseMapping(1228,1227)
        self._addCaseMapping(1233,1232)
        self._addCaseMapping(1235,1234)
        self._addCaseMapping(1237,1236)
        self._addCaseMapping(1239,1238)
        self._addCaseMapping(1241,1240)
        self._addCaseMapping(1243,1242)
        self._addCaseMapping(1245,1244)
        self._addCaseMapping(1247,1246)
        self._addCaseMapping(1249,1248)
        self._addCaseMapping(1251,1250)
        self._addCaseMapping(1253,1252)
        self._addCaseMapping(1255,1254)
        self._addCaseMapping(1257,1256)
        self._addCaseMapping(1259,1258)
        self._addCaseMapping(1263,1262)
        self._addCaseMapping(1265,1264)
        self._addCaseMapping(1267,1266)
        self._addCaseMapping(1269,1268)
        self._addCaseMapping(1273,1272)
        self._addCaseMapping(1377,1329)
        self._addCaseMapping(1378,1330)
        self._addCaseMapping(1379,1331)
        self._addCaseMapping(1380,1332)
        self._addCaseMapping(1381,1333)
        self._addCaseMapping(1382,1334)
        self._addCaseMapping(1383,1335)
        self._addCaseMapping(1384,1336)
        self._addCaseMapping(1385,1337)
        self._addCaseMapping(1386,1338)
        self._addCaseMapping(1387,1339)
        self._addCaseMapping(1388,1340)
        self._addCaseMapping(1389,1341)
        self._addCaseMapping(1390,1342)
        self._addCaseMapping(1391,1343)
        self._addCaseMapping(1392,1344)
        self._addCaseMapping(1393,1345)
        self._addCaseMapping(1394,1346)
        self._addCaseMapping(1395,1347)
        self._addCaseMapping(1396,1348)
        self._addCaseMapping(1397,1349)
        self._addCaseMapping(1398,1350)
        self._addCaseMapping(1399,1351)
        self._addCaseMapping(1400,1352)
        self._addCaseMapping(1401,1353)
        self._addCaseMapping(1402,1354)
        self._addCaseMapping(1403,1355)
        self._addCaseMapping(1404,1356)
        self._addCaseMapping(1405,1357)
        self._addCaseMapping(1406,1358)
        self._addCaseMapping(1407,1359)
        self._addCaseMapping(1408,1360)
        self._addCaseMapping(1409,1361)
        self._addCaseMapping(1410,1362)
        self._addCaseMapping(1411,1363)
        self._addCaseMapping(1412,1364)
        self._addCaseMapping(1413,1365)
        self._addCaseMapping(1414,1366)
        self._addCaseMapping(4304,4256)
        self._addCaseMapping(4305,4257)
        self._addCaseMapping(4306,4258)
        self._addCaseMapping(4307,4259)
        self._addCaseMapping(4308,4260)
        self._addCaseMapping(4309,4261)
        self._addCaseMapping(4310,4262)
        self._addCaseMapping(4311,4263)
        self._addCaseMapping(4312,4264)
        self._addCaseMapping(4313,4265)
        self._addCaseMapping(4314,4266)
        self._addCaseMapping(4315,4267)
        self._addCaseMapping(4316,4268)
        self._addCaseMapping(4317,4269)
        self._addCaseMapping(4318,4270)
        self._addCaseMapping(4319,4271)
        self._addCaseMapping(4320,4272)
        self._addCaseMapping(4321,4273)
        self._addCaseMapping(4322,4274)
        self._addCaseMapping(4323,4275)
        self._addCaseMapping(4324,4276)
        self._addCaseMapping(4325,4277)
        self._addCaseMapping(4326,4278)
        self._addCaseMapping(4327,4279)
        self._addCaseMapping(4328,4280)
        self._addCaseMapping(4329,4281)
        self._addCaseMapping(4330,4282)
        self._addCaseMapping(4331,4283)
        self._addCaseMapping(4332,4284)
        self._addCaseMapping(4333,4285)
        self._addCaseMapping(4334,4286)
        self._addCaseMapping(4335,4287)
        self._addCaseMapping(4336,4288)
        self._addCaseMapping(4337,4289)
        self._addCaseMapping(4338,4290)
        self._addCaseMapping(4339,4291)
        self._addCaseMapping(4340,4292)
        self._addCaseMapping(4341,4293)
        self._addCaseMapping(7681,7680)
        self._addCaseMapping(7683,7682)
        self._addCaseMapping(7685,7684)
        self._addCaseMapping(7687,7686)
        self._addCaseMapping(7689,7688)
        self._addCaseMapping(7691,7690)
        self._addCaseMapping(7693,7692)
        self._addCaseMapping(7695,7694)
        self._addCaseMapping(7697,7696)
        self._addCaseMapping(7699,7698)
        self._addCaseMapping(7701,7700)
        self._addCaseMapping(7703,7702)
        self._addCaseMapping(7705,7704)
        self._addCaseMapping(7707,7706)
        self._addCaseMapping(7709,7708)
        self._addCaseMapping(7711,7710)
        self._addCaseMapping(7713,7712)
        self._addCaseMapping(7715,7714)
        self._addCaseMapping(7717,7716)
        self._addCaseMapping(7719,7718)
        self._addCaseMapping(7721,7720)
        self._addCaseMapping(7723,7722)
        self._addCaseMapping(7725,7724)
        self._addCaseMapping(7727,7726)
        self._addCaseMapping(7729,7728)
        self._addCaseMapping(7731,7730)
        self._addCaseMapping(7733,7732)
        self._addCaseMapping(7735,7734)
        self._addCaseMapping(7737,7736)
        self._addCaseMapping(7739,7738)
        self._addCaseMapping(7741,7740)
        self._addCaseMapping(7743,7742)
        self._addCaseMapping(7745,7744)
        self._addCaseMapping(7747,7746)
        self._addCaseMapping(7749,7748)
        self._addCaseMapping(7751,7750)
        self._addCaseMapping(7753,7752)
        self._addCaseMapping(7755,7754)
        self._addCaseMapping(7757,7756)
        self._addCaseMapping(7759,7758)
        self._addCaseMapping(7761,7760)
        self._addCaseMapping(7763,7762)
        self._addCaseMapping(7765,7764)
        self._addCaseMapping(7767,7766)
        self._addCaseMapping(7769,7768)
        self._addCaseMapping(7771,7770)
        self._addCaseMapping(7773,7772)
        self._addCaseMapping(7775,7774)
        self._addCaseMapping(7777,7776)
        self._addCaseMapping(7779,7778)
        self._addCaseMapping(7781,7780)
        self._addCaseMapping(7783,7782)
        self._addCaseMapping(7785,7784)
        self._addCaseMapping(7787,7786)
        self._addCaseMapping(7789,7788)
        self._addCaseMapping(7791,7790)
        self._addCaseMapping(7793,7792)
        self._addCaseMapping(7795,7794)
        self._addCaseMapping(7797,7796)
        self._addCaseMapping(7799,7798)
        self._addCaseMapping(7801,7800)
        self._addCaseMapping(7803,7802)
        self._addCaseMapping(7805,7804)
        self._addCaseMapping(7807,7806)
        self._addCaseMapping(7809,7808)
        self._addCaseMapping(7811,7810)
        self._addCaseMapping(7813,7812)
        self._addCaseMapping(7815,7814)
        self._addCaseMapping(7817,7816)
        self._addCaseMapping(7819,7818)
        self._addCaseMapping(7821,7820)
        self._addCaseMapping(7823,7822)
        self._addCaseMapping(7825,7824)
        self._addCaseMapping(7827,7826)
        self._addCaseMapping(7829,7828)
        self._addCaseMapping(7841,7840)
        self._addCaseMapping(7843,7842)
        self._addCaseMapping(7845,7844)
        self._addCaseMapping(7847,7846)
        self._addCaseMapping(7849,7848)
        self._addCaseMapping(7851,7850)
        self._addCaseMapping(7853,7852)
        self._addCaseMapping(7855,7854)
        self._addCaseMapping(7857,7856)
        self._addCaseMapping(7859,7858)
        self._addCaseMapping(7861,7860)
        self._addCaseMapping(7863,7862)
        self._addCaseMapping(7865,7864)
        self._addCaseMapping(7867,7866)
        self._addCaseMapping(7869,7868)
        self._addCaseMapping(7871,7870)
        self._addCaseMapping(7873,7872)
        self._addCaseMapping(7875,7874)
        self._addCaseMapping(7877,7876)
        self._addCaseMapping(7879,7878)
        self._addCaseMapping(7881,7880)
        self._addCaseMapping(7883,7882)
        self._addCaseMapping(7885,7884)
        self._addCaseMapping(7887,7886)
        self._addCaseMapping(7889,7888)
        self._addCaseMapping(7891,7890)
        self._addCaseMapping(7893,7892)
        self._addCaseMapping(7895,7894)
        self._addCaseMapping(7897,7896)
        self._addCaseMapping(7899,7898)
        self._addCaseMapping(7901,7900)
        self._addCaseMapping(7903,7902)
        self._addCaseMapping(7905,7904)
        self._addCaseMapping(7907,7906)
        self._addCaseMapping(7909,7908)
        self._addCaseMapping(7911,7910)
        self._addCaseMapping(7913,7912)
        self._addCaseMapping(7915,7914)
        self._addCaseMapping(7917,7916)
        self._addCaseMapping(7919,7918)
        self._addCaseMapping(7921,7920)
        self._addCaseMapping(7923,7922)
        self._addCaseMapping(7925,7924)
        self._addCaseMapping(7927,7926)
        self._addCaseMapping(7929,7928)
        self._addCaseMapping(7936,7944)
        self._addCaseMapping(7937,7945)
        self._addCaseMapping(7938,7946)
        self._addCaseMapping(7939,7947)
        self._addCaseMapping(7940,7948)
        self._addCaseMapping(7941,7949)
        self._addCaseMapping(7942,7950)
        self._addCaseMapping(7943,7951)
        self._addCaseMapping(7952,7960)
        self._addCaseMapping(7953,7961)
        self._addCaseMapping(7954,7962)
        self._addCaseMapping(7955,7963)
        self._addCaseMapping(7956,7964)
        self._addCaseMapping(7957,7965)
        self._addCaseMapping(7968,7976)
        self._addCaseMapping(7969,7977)
        self._addCaseMapping(7970,7978)
        self._addCaseMapping(7971,7979)
        self._addCaseMapping(7972,7980)
        self._addCaseMapping(7973,7981)
        self._addCaseMapping(7974,7982)
        self._addCaseMapping(7975,7983)
        self._addCaseMapping(7984,7992)
        self._addCaseMapping(7985,7993)
        self._addCaseMapping(7986,7994)
        self._addCaseMapping(7987,7995)
        self._addCaseMapping(7988,7996)
        self._addCaseMapping(7989,7997)
        self._addCaseMapping(7990,7998)
        self._addCaseMapping(7991,7999)
        self._addCaseMapping(8000,8008)
        self._addCaseMapping(8001,8009)
        self._addCaseMapping(8002,8010)
        self._addCaseMapping(8003,8011)
        self._addCaseMapping(8004,8012)
        self._addCaseMapping(8005,8013)
        self._addCaseMapping(8017,8025)
        self._addCaseMapping(8019,8027)
        self._addCaseMapping(8021,8029)
        self._addCaseMapping(8023,8031)
        self._addCaseMapping(8032,8040)
        self._addCaseMapping(8033,8041)
        self._addCaseMapping(8034,8042)
        self._addCaseMapping(8035,8043)
        self._addCaseMapping(8036,8044)
        self._addCaseMapping(8037,8045)
        self._addCaseMapping(8038,8046)
        self._addCaseMapping(8039,8047)
        self._addCaseMapping(8064,8072)
        self._addCaseMapping(8065,8073)
        self._addCaseMapping(8066,8074)
        self._addCaseMapping(8067,8075)
        self._addCaseMapping(8068,8076)
        self._addCaseMapping(8069,8077)
        self._addCaseMapping(8070,8078)
        self._addCaseMapping(8071,8079)
        self._addCaseMapping(8080,8088)
        self._addCaseMapping(8081,8089)
        self._addCaseMapping(8082,8090)
        self._addCaseMapping(8083,8091)
        self._addCaseMapping(8084,8092)
        self._addCaseMapping(8085,8093)
        self._addCaseMapping(8086,8094)
        self._addCaseMapping(8087,8095)
        self._addCaseMapping(8096,8104)
        self._addCaseMapping(8097,8105)
        self._addCaseMapping(8098,8106)
        self._addCaseMapping(8099,8107)
        self._addCaseMapping(8100,8108)
        self._addCaseMapping(8101,8109)
        self._addCaseMapping(8102,8110)
        self._addCaseMapping(8103,8111)
        self._addCaseMapping(8112,8120)
        self._addCaseMapping(8113,8121)
        self._addCaseMapping(8144,8152)
        self._addCaseMapping(8145,8153)
        self._addCaseMapping(8160,8168)
        self._addCaseMapping(8161,8169)
        self._addCaseMapping(9424,9398)
        self._addCaseMapping(9425,9399)
        self._addCaseMapping(9426,9400)
        self._addCaseMapping(9427,9401)
        self._addCaseMapping(9428,9402)
        self._addCaseMapping(9429,9403)
        self._addCaseMapping(9430,9404)
        self._addCaseMapping(9431,9405)
        self._addCaseMapping(9432,9406)
        self._addCaseMapping(9433,9407)
        self._addCaseMapping(9434,9408)
        self._addCaseMapping(9435,9409)
        self._addCaseMapping(9436,9410)
        self._addCaseMapping(9437,9411)
        self._addCaseMapping(9438,9412)
        self._addCaseMapping(9439,9413)
        self._addCaseMapping(9440,9414)
        self._addCaseMapping(9441,9415)
        self._addCaseMapping(9442,9416)
        self._addCaseMapping(9443,9417)
        self._addCaseMapping(9444,9418)
        self._addCaseMapping(9445,9419)
        self._addCaseMapping(9446,9420)
        self._addCaseMapping(9447,9421)
        self._addCaseMapping(9448,9422)
        self._addCaseMapping(9449,9423)
        self._addCaseMapping(65345,65313)
        self._addCaseMapping(65346,65314)
        self._addCaseMapping(65347,65315)
        self._addCaseMapping(65348,65316)
        self._addCaseMapping(65349,65317)
        self._addCaseMapping(65350,65318)
        self._addCaseMapping(65351,65319)
        self._addCaseMapping(65352,65320)
        self._addCaseMapping(65353,65321)
        self._addCaseMapping(65354,65322)
        self._addCaseMapping(65355,65323)
        self._addCaseMapping(65356,65324)
        self._addCaseMapping(65357,65325)
        self._addCaseMapping(65358,65326)
        self._addCaseMapping(65359,65327)
        self._addCaseMapping(65360,65328)
        self._addCaseMapping(65361,65329)
        self._addCaseMapping(65362,65330)
        self._addCaseMapping(65363,65331)
        self._addCaseMapping(65364,65332)
        self._addCaseMapping(65365,65333)
        self._addCaseMapping(65366,65334)
        self._addCaseMapping(65367,65335)
        self._addCaseMapping(65368,65336)
        self._addCaseMapping(65369,65337)
        self._addCaseMapping(65370,65338)

    def _addCaseMapping(self,lowerChar,upperChar):
        if (not (upperChar in self.mapU2L.h)):
            self.mapU2L.set(upperChar,lowerChar)
        if (not (lowerChar in self.mapL2U.h)):
            self.mapL2U.set(lowerChar,upperChar)

    def isLowerCase(self,ch):
        return (ch in self.mapL2U.h)

    def isUpperCase(self,ch):
        return (ch in self.mapU2L.h)

    def toLowerCase(self,ch):
        lowerChar = self.mapU2L.h.get(ch,None)
        if (lowerChar is None):
            return ch
        else:
            return lowerChar

    def toUpperCase(self,ch):
        upperChar = self.mapL2U.h.get(ch,None)
        if (upperChar is None):
            return ch
        else:
            return upperChar

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.mapU2L = None
        _hx_o.mapL2U = None
hx_strings__Char_CharCaseMapper._hx_class = hx_strings__Char_CharCaseMapper


class hx_strings__Char_Char_Impl_:
    _hx_class_name = "hx.strings._Char.Char_Impl_"
    __slots__ = ()
    _hx_statics = ["CHAR_CASE_MAPPER", "BACKSPACE", "TAB", "LF", "CR", "ESC", "SPACE", "EXCLAMATION_MARK", "DOUBLE_QUOTE", "HASH", "DOLLAR", "AMPERSAND", "SINGLE_QUOTE", "BRACKET_ROUND_LEFT", "BRACKET_ROUND_RIGHT", "ASTERISK", "PLUS", "COMMA", "MINUS", "DOT", "SLASH", "ZERO", "ONE", "TWO", "TRHEE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "COLON", "SEMICOLON", "LOWER_THAN", "EQUALS", "GREATER_THAN", "QUESTION_MARK", "BRACKET_SQUARE_LEFT", "BACKSLASH", "BRACKET_SQUARE_RIGHT", "CARET", "UNDERSCORE", "BRACKET_CURLY_LEFT", "PIPE", "BRACKET_CURLY_RIGHT", "fromString", "of", "op_plus_string", "op_plus_string2", "op_plus", "isAscii", "isAsciiAlpha", "isAsciiAlphanumeric", "isAsciiControl", "isAsciiPrintable", "isDigit", "isEOF", "isSpace", "isUTF8", "isWhitespace", "isLowerCase", "isUpperCase", "toLowerCase", "toUpperCase", "toInt", "toString"]

    @staticmethod
    def fromString(_hx_str):
        return hx_strings_Strings.charCodeAt8(_hx_str,0)

    @staticmethod
    def of(ch):
        return ch

    @staticmethod
    def op_plus_string(ch,other):
        return (HxOverrides.stringOrNull("".join(map(chr,[ch]))) + ("null" if other is None else other))

    @staticmethod
    def op_plus_string2(_hx_str,ch):
        return (("null" if _hx_str is None else _hx_str) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))

    @staticmethod
    def op_plus(ch,other):
        return (ch + other)

    @staticmethod
    def isAscii(this1):
        if (this1 > -1):
            return (this1 < 128)
        else:
            return False

    @staticmethod
    def isAsciiAlpha(this1):
        if (not (((this1 > 64) and ((this1 < 91))))):
            if (this1 > 96):
                return (this1 < 123)
            else:
                return False
        else:
            return True

    @staticmethod
    def isAsciiAlphanumeric(this1):
        if (not ((((this1 > 64) and ((this1 < 91))) or (((this1 > 96) and ((this1 < 123))))))):
            if (this1 > 47):
                return (this1 < 58)
            else:
                return False
        else:
            return True

    @staticmethod
    def isAsciiControl(this1):
        if (not (((this1 > -1) and ((this1 < 32))))):
            return (this1 == 127)
        else:
            return True

    @staticmethod
    def isAsciiPrintable(this1):
        if (this1 > 31):
            return (this1 < 127)
        else:
            return False

    @staticmethod
    def isDigit(this1):
        if (this1 > 47):
            return (this1 < 58)
        else:
            return False

    @staticmethod
    def isEOF(this1):
        return (this1 == -1)

    @staticmethod
    def isSpace(this1):
        return (this1 == 32)

    @staticmethod
    def isUTF8(this1):
        if (this1 > -1):
            return (this1 < 1114112)
        else:
            return False

    @staticmethod
    def isWhitespace(this1):
        if (not (((this1 > 8) and ((this1 < 14))))):
            return (this1 == 32)
        else:
            return True

    @staticmethod
    def isLowerCase(this1):
        return (this1 in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapL2U.h)

    @staticmethod
    def isUpperCase(this1):
        return (this1 in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h)

    @staticmethod
    def toLowerCase(this1):
        lowerChar = hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h.get(this1,None)
        if (lowerChar is None):
            return this1
        else:
            return lowerChar

    @staticmethod
    def toUpperCase(this1):
        upperChar = hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapL2U.h.get(this1,None)
        if (upperChar is None):
            return this1
        else:
            return upperChar

    @staticmethod
    def toInt(this1):
        return this1

    @staticmethod
    def toString(this1):
        return "".join(map(chr,[this1]))
hx_strings__Char_Char_Impl_._hx_class = hx_strings__Char_Char_Impl_


class hx_strings_CharIterator:
    _hx_class_name = "hx.strings.CharIterator"
    __slots__ = ("index", "line", "col", "currChar", "prevBuffer", "prevBufferPrevIdx", "prevBufferNextIdx")
    _hx_fields = ["index", "line", "col", "currChar", "prevBuffer", "prevBufferPrevIdx", "prevBufferNextIdx"]
    _hx_methods = ["get_current", "get_pos", "hasPrev", "prev", "hasNext", "next", "getChar", "isEOF"]
    _hx_statics = ["fromString", "fromArray", "fromInput", "fromIterator"]

    def __init__(self,prevBufferSize):
        self.prevBufferNextIdx = -1
        self.prevBufferPrevIdx = -1
        self.currChar = -1
        self.col = 0
        self.line = 0
        self.index = -1
        tmp = None
        if (prevBufferSize > 0):
            this1 = hx_strings_internal__RingBuffer_RingBufferImpl((prevBufferSize + 1))
            tmp = this1
        else:
            tmp = None
        self.prevBuffer = tmp

    def get_current(self):
        if (self.index > -1):
            return self.currChar
        else:
            return None

    def get_pos(self):
        return hx_strings_CharPos(self.index,self.line,self.col)

    def hasPrev(self):
        return (self.prevBufferPrevIdx > -1)

    def prev(self):
        if (self.prevBufferPrevIdx <= -1):
            raise haxe_Exception.thrown(haxe_io_Eof())
        prevChar = self.prevBuffer.get(self.prevBufferPrevIdx)
        self.currChar = prevChar.char
        self.index = prevChar.index
        self.line = prevChar.line
        self.col = prevChar.col
        self.prevBufferNextIdx = ((self.prevBufferPrevIdx + 1) if (((self.prevBufferPrevIdx + 1) < self.prevBuffer.length)) else -1)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.prevBufferPrevIdx
        _hx_local_0.prevBufferPrevIdx = (_hx_local_1 - 1)
        _hx_local_1
        return self.currChar

    def hasNext(self):
        if (self.prevBufferNextIdx > -1):
            return True
        else:
            return (not self.isEOF())

    def next(self):
        if (self.prevBufferNextIdx > -1):
            prevChar = self.prevBuffer.get(self.prevBufferNextIdx)
            self.currChar = prevChar.char
            self.index = prevChar.index
            self.line = prevChar.line
            self.col = prevChar.col
            self.prevBufferPrevIdx = (self.prevBufferNextIdx - 1)
            self.prevBufferNextIdx = ((self.prevBufferNextIdx + 1) if (((self.prevBufferNextIdx + 1) < self.prevBuffer.length)) else -1)
            return self.currChar
        if self.isEOF():
            raise haxe_Exception.thrown(haxe_io_Eof())
        if ((self.currChar == 10) or ((self.currChar < 0))):
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.line
            _hx_local_0.line = (_hx_local_1 + 1)
            _hx_local_1
            self.col = 0
        _hx_local_2 = self
        _hx_local_3 = _hx_local_2.index
        _hx_local_2.index = (_hx_local_3 + 1)
        _hx_local_3
        _hx_local_4 = self
        _hx_local_5 = _hx_local_4.col
        _hx_local_4.col = (_hx_local_5 + 1)
        _hx_local_5
        self.currChar = self.getChar()
        if (self.prevBuffer is not None):
            self.prevBuffer.add(hx_strings__CharIterator_CharWithPos(self.currChar,self.index,self.col,self.line))
            self.prevBufferPrevIdx = (self.prevBuffer.length - 2)
            self.prevBufferNextIdx = -1
        return self.currChar

    def getChar(self):
        raise haxe_Exception.thrown("Not implemented")

    def isEOF(self):
        raise haxe_Exception.thrown("Not implemented")

    @staticmethod
    def fromString(chars,prevBufferSize = None):
        if (prevBufferSize is None):
            prevBufferSize = 0
        if (chars is None):
            return hx_strings__CharIterator_NullCharIterator.INSTANCE
        return hx_strings__CharIterator_StringCharIterator(chars,prevBufferSize)

    @staticmethod
    def fromArray(chars,prevBufferSize = None):
        if (prevBufferSize is None):
            prevBufferSize = 0
        if (chars is None):
            return hx_strings__CharIterator_NullCharIterator.INSTANCE
        return hx_strings__CharIterator_ArrayCharIterator(chars,prevBufferSize)

    @staticmethod
    def fromInput(chars,prevBufferSize = None):
        if (prevBufferSize is None):
            prevBufferSize = 0
        if (chars is None):
            return hx_strings__CharIterator_NullCharIterator.INSTANCE
        return hx_strings__CharIterator_InputCharIterator(chars,prevBufferSize)

    @staticmethod
    def fromIterator(chars,prevBufferSize = None):
        if (prevBufferSize is None):
            prevBufferSize = 0
        if (chars is None):
            return hx_strings__CharIterator_NullCharIterator.INSTANCE
        return hx_strings__CharIterator_IteratorCharIterator(chars,prevBufferSize)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.index = None
        _hx_o.line = None
        _hx_o.col = None
        _hx_o.currChar = None
        _hx_o.prevBuffer = None
        _hx_o.prevBufferPrevIdx = None
        _hx_o.prevBufferNextIdx = None
hx_strings_CharIterator._hx_class = hx_strings_CharIterator


class hx_strings_CharPos:
    _hx_class_name = "hx.strings.CharPos"
    __slots__ = ("index", "line", "col")
    _hx_fields = ["index", "line", "col"]
    _hx_methods = ["toString"]

    def __init__(self,index,line,col):
        self.index = index
        self.line = line
        self.col = col

    def toString(self):
        return (((((("CharPos[index=" + Std.string(self.index)) + ", line=") + Std.string(self.line)) + ", col=") + Std.string(self.col)) + "]")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.index = None
        _hx_o.line = None
        _hx_o.col = None
hx_strings_CharPos._hx_class = hx_strings_CharPos


class hx_strings__CharIterator_CharWithPos(hx_strings_CharPos):
    _hx_class_name = "hx.strings._CharIterator.CharWithPos"
    __slots__ = ("char",)
    _hx_fields = ["char"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hx_strings_CharPos


    def __init__(self,char,index,line,col):
        self.char = None
        super().__init__(index,line,col)
        self.char = char

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.char = None
hx_strings__CharIterator_CharWithPos._hx_class = hx_strings__CharIterator_CharWithPos


class hx_strings_internal__RingBuffer_RingBufferImpl:
    _hx_class_name = "hx.strings.internal._RingBuffer.RingBufferImpl"
    __slots__ = ("buffer", "bufferStartIdx", "bufferEndIdx", "bufferMaxIdx", "length", "size")
    _hx_fields = ["buffer", "bufferStartIdx", "bufferEndIdx", "bufferMaxIdx", "length", "size"]
    _hx_methods = ["add", "get", "iterator", "toArray"]

    def __init__(self,size):
        self.length = 0
        self.bufferEndIdx = -1
        self.bufferStartIdx = 0
        if (size < 1):
            raise haxe_Exception.thrown("[size] must be > 0")
        this1 = [None]*size
        self.buffer = this1
        self.size = size
        self.bufferMaxIdx = (size - 1)

    def add(self,item):
        if (self.length == self.size):
            self.bufferEndIdx = self.bufferStartIdx
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.bufferStartIdx
            _hx_local_0.bufferStartIdx = (_hx_local_1 + 1)
            _hx_local_1
            if (self.bufferStartIdx > self.bufferMaxIdx):
                self.bufferStartIdx = 0
        else:
            _hx_local_2 = self
            _hx_local_3 = _hx_local_2.bufferEndIdx
            _hx_local_2.bufferEndIdx = (_hx_local_3 + 1)
            _hx_local_3
            _hx_local_4 = self
            _hx_local_5 = _hx_local_4.length
            _hx_local_4.length = (_hx_local_5 + 1)
            _hx_local_5
        self.buffer[self.bufferEndIdx] = item

    def get(self,index):
        if ((index < 0) or ((index > self.bufferMaxIdx))):
            raise haxe_Exception.thrown((("[index] " + Std.string(index)) + " is out of bound"))
        realIdx = (self.bufferStartIdx + index)
        if (realIdx > self.bufferMaxIdx):
            realIdx = (realIdx - self.length)
        return self.buffer[realIdx]

    def iterator(self):
        return hx_strings_internal__RingBuffer_RingBufferIterator(self)

    def toArray(self):
        arr = list()
        i = self.iterator()
        while i.hasNext():
            i1 = i.next()
            arr.append(i1)
        return arr

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buffer = None
        _hx_o.bufferStartIdx = None
        _hx_o.bufferEndIdx = None
        _hx_o.bufferMaxIdx = None
        _hx_o.length = None
        _hx_o.size = None
hx_strings_internal__RingBuffer_RingBufferImpl._hx_class = hx_strings_internal__RingBuffer_RingBufferImpl


class hx_strings__CharIterator_NullCharIterator(hx_strings_CharIterator):
    _hx_class_name = "hx.strings._CharIterator.NullCharIterator"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["isEOF"]
    _hx_statics = ["INSTANCE"]
    _hx_interfaces = []
    _hx_super = hx_strings_CharIterator


    def __init__(self):
        super().__init__(0)

    def isEOF(self):
        return True

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
hx_strings__CharIterator_NullCharIterator._hx_class = hx_strings__CharIterator_NullCharIterator


class hx_strings__CharIterator_ArrayCharIterator(hx_strings_CharIterator):
    _hx_class_name = "hx.strings._CharIterator.ArrayCharIterator"
    __slots__ = ("chars", "charsMaxIndex")
    _hx_fields = ["chars", "charsMaxIndex"]
    _hx_methods = ["isEOF", "getChar"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hx_strings_CharIterator


    def __init__(self,chars,prevBufferSize):
        self.charsMaxIndex = None
        self.chars = None
        super().__init__(prevBufferSize)
        self.chars = chars
        self.charsMaxIndex = (len(chars) - 1)

    def isEOF(self):
        return (self.index >= self.charsMaxIndex)

    def getChar(self):
        return python_internal_ArrayImpl._get(self.chars, self.index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.chars = None
        _hx_o.charsMaxIndex = None
hx_strings__CharIterator_ArrayCharIterator._hx_class = hx_strings__CharIterator_ArrayCharIterator


class hx_strings__CharIterator_IteratorCharIterator(hx_strings_CharIterator):
    _hx_class_name = "hx.strings._CharIterator.IteratorCharIterator"
    __slots__ = ("chars",)
    _hx_fields = ["chars"]
    _hx_methods = ["isEOF", "getChar"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hx_strings_CharIterator


    def __init__(self,chars,prevBufferSize):
        self.chars = None
        super().__init__(prevBufferSize)
        self.chars = chars

    def isEOF(self):
        return (not self.chars.hasNext())

    def getChar(self):
        return self.chars.next()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.chars = None
hx_strings__CharIterator_IteratorCharIterator._hx_class = hx_strings__CharIterator_IteratorCharIterator


class hx_strings__CharIterator_InputCharIterator(hx_strings_CharIterator):
    _hx_class_name = "hx.strings._CharIterator.InputCharIterator"
    __slots__ = ("byteIndex", "input", "currCharIndex", "nextChar", "nextCharAvailable")
    _hx_fields = ["byteIndex", "input", "currCharIndex", "nextChar", "nextCharAvailable"]
    _hx_methods = ["isEOF", "getChar", "readUtf8Char", "readUtf8MultiSequenceByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hx_strings_CharIterator


    def __init__(self,chars,prevBufferSize):
        self.input = None
        self.nextCharAvailable = None
        self.nextChar = -1
        self.currCharIndex = -1
        self.byteIndex = 0
        super().__init__(prevBufferSize)
        self.input = chars

    def isEOF(self):
        if (self.nextCharAvailable == None):
            try:
                byte1 = self.input.readByte()
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.byteIndex
                _hx_local_0.byteIndex = (_hx_local_1 + 1)
                _hx_local_1
                tmp = None
                if (byte1 <= 127):
                    tmp = byte1
                else:
                    byte1 = (byte1 & -129)
                    byte1 = (byte1 & -65)
                    totalBytes = 2
                    isBit6Set = (1 == (((byte1 >> 5) & 1)))
                    isBit5Set = False
                    if isBit6Set:
                        byte1 = (byte1 & -33)
                        totalBytes = (totalBytes + 1)
                        isBit5Set = (1 == (((byte1 >> 4) & 1)))
                        if isBit5Set:
                            byte1 = (byte1 & -17)
                            totalBytes = (totalBytes + 1)
                            if (1 == (((byte1 >> 3) & 1))):
                                raise haxe_Exception.thrown((((("Valid UTF-8 byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte1)) + "]!"))
                    result = (byte1 << ((6 * ((totalBytes - 1)))))
                    byte = self.input.readByte()
                    _hx_local_8 = self
                    _hx_local_9 = _hx_local_8.byteIndex
                    _hx_local_8.byteIndex = (_hx_local_9 + 1)
                    _hx_local_9
                    if (1 != (((byte >> 7) & 1))):
                        raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                    if (1 == (((byte >> 6) & 1))):
                        raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                    byte2 = (byte & -129)
                    result = (result + ((byte2 << ((6 * ((totalBytes - 2)))))))
                    if isBit6Set:
                        byte = self.input.readByte()
                        _hx_local_11 = self
                        _hx_local_12 = _hx_local_11.byteIndex
                        _hx_local_11.byteIndex = (_hx_local_12 + 1)
                        _hx_local_12
                        if (1 != (((byte >> 7) & 1))):
                            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                        if (1 == (((byte >> 6) & 1))):
                            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                        byte3 = (byte & -129)
                        result = (result + ((byte3 << ((6 * ((totalBytes - 3)))))))
                        if isBit5Set:
                            byte = self.input.readByte()
                            _hx_local_14 = self
                            _hx_local_15 = _hx_local_14.byteIndex
                            _hx_local_14.byteIndex = (_hx_local_15 + 1)
                            _hx_local_15
                            if (1 != (((byte >> 7) & 1))):
                                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                            if (1 == (((byte >> 6) & 1))):
                                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                            byte4 = (byte & -129)
                            result = (result + ((byte4 << ((6 * ((totalBytes - 4)))))))
                    if ((self.index == 0) and ((result == 65279))):
                        byte1 = self.input.readByte()
                        _hx_local_17 = self
                        _hx_local_18 = _hx_local_17.byteIndex
                        _hx_local_17.byteIndex = (_hx_local_18 + 1)
                        _hx_local_18
                        if (byte1 <= 127):
                            tmp = byte1
                        else:
                            byte1 = (byte1 & -129)
                            byte1 = (byte1 & -65)
                            totalBytes = 2
                            isBit6Set = (1 == (((byte1 >> 5) & 1)))
                            isBit5Set = False
                            if isBit6Set:
                                byte1 = (byte1 & -33)
                                totalBytes = (totalBytes + 1)
                                isBit5Set = (1 == (((byte1 >> 4) & 1)))
                                if isBit5Set:
                                    byte1 = (byte1 & -17)
                                    totalBytes = (totalBytes + 1)
                                    if (1 == (((byte1 >> 3) & 1))):
                                        raise haxe_Exception.thrown((((("Valid UTF-8 byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte1)) + "]!"))
                            result1 = (byte1 << ((6 * ((totalBytes - 1)))))
                            byte = self.input.readByte()
                            _hx_local_25 = self
                            _hx_local_26 = _hx_local_25.byteIndex
                            _hx_local_25.byteIndex = (_hx_local_26 + 1)
                            _hx_local_26
                            if (1 != (((byte >> 7) & 1))):
                                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                            if (1 == (((byte >> 6) & 1))):
                                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                            byte2 = (byte & -129)
                            result1 = (result1 + ((byte2 << ((6 * ((totalBytes - 2)))))))
                            if isBit6Set:
                                byte = self.input.readByte()
                                _hx_local_28 = self
                                _hx_local_29 = _hx_local_28.byteIndex
                                _hx_local_28.byteIndex = (_hx_local_29 + 1)
                                _hx_local_29
                                if (1 != (((byte >> 7) & 1))):
                                    raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                                if (1 == (((byte >> 6) & 1))):
                                    raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                                byte3 = (byte & -129)
                                result1 = (result1 + ((byte3 << ((6 * ((totalBytes - 3)))))))
                                if isBit5Set:
                                    byte = self.input.readByte()
                                    _hx_local_31 = self
                                    _hx_local_32 = _hx_local_31.byteIndex
                                    _hx_local_31.byteIndex = (_hx_local_32 + 1)
                                    _hx_local_32
                                    if (1 != (((byte >> 7) & 1))):
                                        raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                                    if (1 == (((byte >> 6) & 1))):
                                        raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                                    byte4 = (byte & -129)
                                    result1 = (result1 + ((byte4 << ((6 * ((totalBytes - 4)))))))
                            tmp = (self.readUtf8Char() if (((self.index == 0) and ((result1 == 65279)))) else result1)
                    else:
                        tmp = result
                self.nextChar = tmp
                self.nextCharAvailable = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                    self.nextCharAvailable = False
                else:
                    raise _g
        return (self.nextCharAvailable != True)

    def getChar(self):
        if (self.index != self.currCharIndex):
            self.currCharIndex = self.index
            self.nextCharAvailable = None
            return self.nextChar
        return self.currChar

    def readUtf8Char(self):
        byte1 = self.input.readByte()
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.byteIndex
        _hx_local_0.byteIndex = (_hx_local_1 + 1)
        _hx_local_1
        if (byte1 <= 127):
            return byte1
        byte1 = (byte1 & -129)
        byte1 = (byte1 & -65)
        totalBytes = 2
        isBit6Set = (1 == (((byte1 >> 5) & 1)))
        isBit5Set = False
        if isBit6Set:
            byte1 = (byte1 & -33)
            totalBytes = (totalBytes + 1)
            isBit5Set = (1 == (((byte1 >> 4) & 1)))
            if isBit5Set:
                byte1 = (byte1 & -17)
                totalBytes = (totalBytes + 1)
                if (1 == (((byte1 >> 3) & 1))):
                    raise haxe_Exception.thrown((((("Valid UTF-8 byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte1)) + "]!"))
        result = (byte1 << ((6 * ((totalBytes - 1)))))
        byte = self.input.readByte()
        _hx_local_8 = self
        _hx_local_9 = _hx_local_8.byteIndex
        _hx_local_8.byteIndex = (_hx_local_9 + 1)
        _hx_local_9
        if (1 != (((byte >> 7) & 1))):
            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
        if (1 == (((byte >> 6) & 1))):
            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
        byte2 = (byte & -129)
        result = (result + ((byte2 << ((6 * ((totalBytes - 2)))))))
        if isBit6Set:
            byte = self.input.readByte()
            _hx_local_11 = self
            _hx_local_12 = _hx_local_11.byteIndex
            _hx_local_11.byteIndex = (_hx_local_12 + 1)
            _hx_local_12
            if (1 != (((byte >> 7) & 1))):
                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
            if (1 == (((byte >> 6) & 1))):
                raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
            byte3 = (byte & -129)
            result = (result + ((byte3 << ((6 * ((totalBytes - 3)))))))
            if isBit5Set:
                byte = self.input.readByte()
                _hx_local_14 = self
                _hx_local_15 = _hx_local_14.byteIndex
                _hx_local_14.byteIndex = (_hx_local_15 + 1)
                _hx_local_15
                if (1 != (((byte >> 7) & 1))):
                    raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                if (1 == (((byte >> 6) & 1))):
                    raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
                byte4 = (byte & -129)
                result = (result + ((byte4 << ((6 * ((totalBytes - 4)))))))
        if ((self.index == 0) and ((result == 65279))):
            return self.readUtf8Char()
        return result

    def readUtf8MultiSequenceByte(self):
        byte = self.input.readByte()
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.byteIndex
        _hx_local_0.byteIndex = (_hx_local_1 + 1)
        _hx_local_1
        if (1 != (((byte >> 7) & 1))):
            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
        if (1 == (((byte >> 6) & 1))):
            raise haxe_Exception.thrown((((("Valid UTF-8 multi-sequence byte expected at position [" + Std.string(self.byteIndex)) + "] but found byte with value [") + Std.string(byte)) + "]!"))
        return (byte & -129)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.byteIndex = None
        _hx_o.input = None
        _hx_o.currCharIndex = None
        _hx_o.nextChar = None
        _hx_o.nextCharAvailable = None
hx_strings__CharIterator_InputCharIterator._hx_class = hx_strings__CharIterator_InputCharIterator


class hx_strings__CharIterator_StringCharIterator(hx_strings_CharIterator):
    _hx_class_name = "hx.strings._CharIterator.StringCharIterator"
    __slots__ = ("chars", "charsMaxIndex")
    _hx_fields = ["chars", "charsMaxIndex"]
    _hx_methods = ["isEOF", "getChar"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = hx_strings_CharIterator


    def __init__(self,chars,prevBufferSize):
        self.charsMaxIndex = None
        self.chars = None
        super().__init__(prevBufferSize)
        self.chars = chars
        self.charsMaxIndex = (((0 if ((chars is None)) else len(chars))) - 1)

    def isEOF(self):
        return (self.index >= self.charsMaxIndex)

    def getChar(self):
        return HxString.charCodeAt(self.chars,self.index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.chars = None
        _hx_o.charsMaxIndex = None
hx_strings__CharIterator_StringCharIterator._hx_class = hx_strings__CharIterator_StringCharIterator


class hx_strings_Pattern:
    _hx_class_name = "hx.strings.Pattern"
    __slots__ = ("pattern", "options", "ereg")
    _hx_fields = ["pattern", "options", "ereg"]
    _hx_methods = ["matcher", "replace", "remove", "split"]
    _hx_statics = ["__meta__", "compile"]

    def __init__(self,pattern,options):
        self.pattern = pattern
        self.options = options
        self.ereg = EReg(pattern,options)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.options
        _hx_local_0.options = (("null" if _hx_local_1 is None else _hx_local_1) + "u")
        _hx_local_0.options

    def matcher(self,_hx_str):
        return hx_strings__Pattern_MatcherImpl(self.ereg,self.pattern,self.options,_hx_str)

    def replace(self,_hx_str,replaceWith):
        return self.ereg.replace(_hx_str,replaceWith)

    def remove(self,_hx_str):
        return self.ereg.replace(_hx_str,"")

    def split(self,_hx_str):
        return self.ereg.split(_hx_str)

    @staticmethod
    def compile(pattern,options = None):
        if (options is None):
            return hx_strings_Pattern(pattern,"")
        _g = options
        tmp = None
        tmp1 = _g.index
        if (tmp1 == 0):
            _hx_str = _g.params[0]
            str1 = hx_strings_Strings.toLowerCase8(_hx_str)
            if ((str1 is None) or ((len(str1) == 0))):
                tmp = str1
            else:
                def _hx_local_0(ch):
                    return "".join(map(chr,[ch]))
                def _hx_local_1(ch):
                    if (not (((ch == hx_strings_Strings.charCodeAt8("i",0)) or ((ch == hx_strings_Strings.charCodeAt8("m",0)))))):
                        return (ch == hx_strings_Strings.charCodeAt8("g",0))
                    else:
                        return True
                _this = list(map(_hx_local_0,list(filter(_hx_local_1,hx_strings_Strings.toChars(str1)))))
                tmp = "".join([python_Boot.toString1(x1,'') for x1 in _this])
        elif (tmp1 == 1):
            opt = _g.params[0]
            tmp = Std.string(opt)
        elif (tmp1 == 2):
            arr = _g.params[0]
            def _hx_local_2(m):
                return (m is not None)
            _this = list(filter(_hx_local_2,arr))
            tmp = "".join([python_Boot.toString1(x1,'') for x1 in _this])
        else:
            pass
        return hx_strings_Pattern(pattern,tmp)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.options = None
        _hx_o.ereg = None
hx_strings_Pattern._hx_class = hx_strings_Pattern


class hx_strings_Matcher:
    _hx_class_name = "hx.strings.Matcher"
    __slots__ = ()
    _hx_methods = ["iterate", "map", "matched", "matchedPos", "matches", "matchesInRegion", "reset", "substringAfterMatch", "substringBeforeMatch"]
    _hx_statics = ["__meta__"]
hx_strings_Matcher._hx_class = hx_strings_Matcher


class hx_strings__Pattern_MatcherImpl:
    _hx_class_name = "hx.strings._Pattern.MatcherImpl"
    __slots__ = ("ereg", "isMatch", "str")
    _hx_fields = ["ereg", "isMatch", "str"]
    _hx_methods = ["reset", "iterate", "map", "matched", "matches", "matchesInRegion", "matchedPos", "substringAfterMatch", "substringBeforeMatch", "_cloneEReg"]
    _hx_interfaces = [hx_strings_Matcher]

    def __init__(self,ereg,pattern,options,_hx_str):
        self.isMatch = None
        clone = Type.createEmptyInstance(EReg)
        value = Reflect.field(ereg,"pattern")
        setattr(clone,(("_hx_" + "pattern") if (("pattern" in python_Boot.keywords)) else (("_hx_" + "pattern") if (((((len("pattern") > 2) and ((ord("pattern"[0]) == 95))) and ((ord("pattern"[1]) == 95))) and ((ord("pattern"[(len("pattern") - 1)]) != 95)))) else "pattern")),value)
        value = Reflect.field(ereg,"global")
        setattr(clone,(("_hx_" + "global") if (("global" in python_Boot.keywords)) else (("_hx_" + "global") if (((((len("global") > 2) and ((ord("global"[0]) == 95))) and ((ord("global"[1]) == 95))) and ((ord("global"[(len("global") - 1)]) != 95)))) else "global")),value)
        self.ereg = clone
        self.str = _hx_str

    def reset(self,_hx_str):
        self.str = _hx_str
        self.isMatch = None
        return self

    def iterate(self,onMatch):
        startAt = 0
        while self.ereg.matchSub(self.str,startAt):
            self.isMatch = True
            _this = self.ereg
            matchedPos_pos = _this.matchObj.start()
            matchedPos_len = (_this.matchObj.end() - _this.matchObj.start())
            onMatch(self)
            startAt = (matchedPos_pos + matchedPos_len)
        self.isMatch = False

    def map(self,mapper):
        _gthis = self
        def _hx_local_1():
            def _hx_local_0(ereg):
                _gthis.isMatch = True
                return mapper(_gthis)
            return self.ereg.map(self.str,_hx_local_0)
        return _hx_local_1()

    def matched(self,n = None):
        if (n is None):
            n = 0
        if (not self.matches()):
            raise haxe_Exception.thrown("No string matched")
        result = self.ereg.matchObj.group(n)
        return result

    def matches(self):
        if (self.isMatch is None):
            _this = self.ereg
            _this.matchObj = python_lib_Re.search(_this.pattern,self.str)
            self.isMatch = (_this.matchObj is not None)
        return self.isMatch

    def matchesInRegion(self,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        def _hx_local_1():
            def _hx_local_0():
                self.isMatch = self.ereg.matchSub(self.str,pos,_hx_len)
                return self.isMatch
            return _hx_local_0()
        return _hx_local_1()

    def matchedPos(self):
        if (not self.matches()):
            raise haxe_Exception.thrown("No string matched")
        _this = self.ereg
        return _hx_AnonObject({'pos': _this.matchObj.start(), 'len': (_this.matchObj.end() - _this.matchObj.start())})

    def substringAfterMatch(self):
        if (not self.matches()):
            return ""
        _this = self.ereg
        return HxString.substr(_this.matchObj.string,_this.matchObj.end(),None)

    def substringBeforeMatch(self):
        if (not self.matches()):
            return ""
        _this = self.ereg
        return HxString.substr(_this.matchObj.string,0,_this.matchObj.start())

    def _cloneEReg(self,_hx_from,pattern,options):
        clone = Type.createEmptyInstance(EReg)
        value = Reflect.field(_hx_from,"pattern")
        setattr(clone,(("_hx_" + "pattern") if (("pattern" in python_Boot.keywords)) else (("_hx_" + "pattern") if (((((len("pattern") > 2) and ((ord("pattern"[0]) == 95))) and ((ord("pattern"[1]) == 95))) and ((ord("pattern"[(len("pattern") - 1)]) != 95)))) else "pattern")),value)
        value = Reflect.field(_hx_from,"global")
        setattr(clone,(("_hx_" + "global") if (("global" in python_Boot.keywords)) else (("_hx_" + "global") if (((((len("global") > 2) and ((ord("global"[0]) == 95))) and ((ord("global"[1]) == 95))) and ((ord("global"[(len("global") - 1)]) != 95)))) else "global")),value)
        return clone

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.ereg = None
        _hx_o.isMatch = None
        _hx_o.str = None
hx_strings__Pattern_MatcherImpl._hx_class = hx_strings__Pattern_MatcherImpl


class hx_strings_StringBuilder:
    _hx_class_name = "hx.strings.StringBuilder"
    __slots__ = ("sb", "pre", "len")
    _hx_fields = ["sb", "pre", "len"]
    _hx_methods = ["get_length", "add", "addChar", "addAll", "clear", "isEmpty", "newLine", "insert", "insertChar", "insertAll", "asOutput", "toString"]
    _hx_statics = ["__meta__"]

    def __init__(self,initialContent = None):
        self.len = 0
        self.pre = None
        self.sb = StringBuf()
        if (initialContent is not None):
            self.add(initialContent)

    def get_length(self):
        return self.len

    def add(self,item):
        _this = self.sb
        s = Std.string(("null" if ((item is None)) else item))
        _this.b.write(s)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.len
        _hx_local_0.len = (_hx_local_1 + (0 if ((item is None)) else len(item)))
        _hx_local_0.len
        return self

    def addChar(self,ch):
        _this = self.sb
        s = "".join(map(chr,[ch]))
        _this.b.write(s)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.len
        _hx_local_0.len = (_hx_local_1 + 1)
        _hx_local_1
        return self

    def addAll(self,items):
        _g = 0
        while (_g < len(items)):
            item = (items[_g] if _g >= 0 and _g < len(items) else None)
            _g = (_g + 1)
            _this = self.sb
            s = Std.string(item)
            _this.b.write(s)
            _hx_local_1 = self
            _hx_local_2 = _hx_local_1.len
            _hx_local_1.len = (_hx_local_2 + (0 if ((item is None)) else len(item)))
            _hx_local_1.len
        return self

    def clear(self):
        self.pre = None
        self.sb = StringBuf()
        self.len = 0
        return self

    def isEmpty(self):
        return (self.len == 0)

    def newLine(self):
        self.sb.b.write("\n")
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.len
        _hx_local_0.len = (_hx_local_1 + 1)
        _hx_local_1
        return self

    def insert(self,pos,item):
        if (pos < 0):
            raise haxe_Exception.thrown("[pos] must not be negative")
        if (pos > self.len):
            raise haxe_Exception.thrown("[pos] must not be greater than this.length")
        if (pos == self.len):
            self.add(item)
            return self
        if (pos == 0):
            if (self.pre is None):
                self.pre = []
            self.pre.insert(0, item)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.len
            _hx_local_0.len = (_hx_local_1 + (0 if ((item is None)) else len(item)))
            _hx_local_0.len
            return self
        pre_len = 0
        if (self.pre is not None):
            pre = self.pre
            i = len(pre)
            _g = 0
            _g1 = len(pre)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _hx_str = (pre[i] if i >= 0 and i < len(pre) else None)
                next_pre_len = (pre_len + ((0 if ((_hx_str is None)) else len(_hx_str))))
                if (next_pre_len == pos):
                    pre.insert((i + 1), item)
                    _hx_local_2 = self
                    _hx_local_3 = _hx_local_2.len
                    _hx_local_2.len = (_hx_local_3 + (0 if ((item is None)) else len(item)))
                    _hx_local_2.len
                    return self
                if (next_pre_len > pos):
                    preSplitted = hx_strings_Strings.splitAt((pre[i] if i >= 0 and i < len(pre) else None),[(pos - pre_len)])
                    python_internal_ArrayImpl._set(pre, i, (preSplitted[0] if 0 < len(preSplitted) else None))
                    pre.insert((i + 1), item)
                    pre.insert((i + 2), (preSplitted[1] if 1 < len(preSplitted) else None))
                    _hx_local_4 = self
                    _hx_local_5 = _hx_local_4.len
                    _hx_local_4.len = (_hx_local_5 + (0 if ((item is None)) else len(item)))
                    _hx_local_4.len
                    return self
                pre_len = next_pre_len
        if (self.sb.get_length() == 0):
            self.add(item)
            return self
        sbSplitted = hx_strings_Strings.splitAt(self.sb.b.getvalue(),[(pos - pre_len)])
        self.sb = StringBuf()
        _this = self.sb
        s = Std.string((sbSplitted[0] if 0 < len(sbSplitted) else None))
        _this.b.write(s)
        _this = self.sb
        s = Std.string(item)
        _this.b.write(s)
        _hx_local_6 = self
        _hx_local_7 = _hx_local_6.len
        _hx_local_6.len = (_hx_local_7 + (0 if ((item is None)) else len(item)))
        _hx_local_6.len
        _this = self.sb
        s = Std.string((sbSplitted[1] if 1 < len(sbSplitted) else None))
        _this.b.write(s)
        return self

    def insertChar(self,pos,ch):
        if (pos < 0):
            raise haxe_Exception.thrown("[pos] must not be negative")
        if (pos > self.len):
            raise haxe_Exception.thrown("[pos] must not be greater than this.length")
        if (pos == self.len):
            self.addChar(ch)
            return self
        if (pos == 0):
            if (self.pre is None):
                self.pre = []
            _this = self.pre
            x = "".join(map(chr,[ch]))
            _this.insert(0, x)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.len
            _hx_local_0.len = (_hx_local_1 + 1)
            _hx_local_1
            return self
        pre_len = 0
        if (self.pre is not None):
            pre = self.pre
            i = len(pre)
            _g = 0
            _g1 = len(pre)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _hx_str = (pre[i] if i >= 0 and i < len(pre) else None)
                next_pre_len = (pre_len + ((0 if ((_hx_str is None)) else len(_hx_str))))
                if (next_pre_len == pos):
                    x = "".join(map(chr,[ch]))
                    pre.insert((i + 1), x)
                    _hx_local_2 = self
                    _hx_local_3 = _hx_local_2.len
                    _hx_local_2.len = (_hx_local_3 + 1)
                    _hx_local_3
                    return self
                if (next_pre_len > pos):
                    preSplitted = hx_strings_Strings.splitAt((pre[i] if i >= 0 and i < len(pre) else None),[(pos - pre_len)])
                    python_internal_ArrayImpl._set(pre, i, (preSplitted[0] if 0 < len(preSplitted) else None))
                    x1 = "".join(map(chr,[ch]))
                    pre.insert((i + 1), x1)
                    pre.insert((i + 2), (preSplitted[1] if 1 < len(preSplitted) else None))
                    _hx_local_4 = self
                    _hx_local_5 = _hx_local_4.len
                    _hx_local_4.len = (_hx_local_5 + 1)
                    _hx_local_5
                    return self
                pre_len = next_pre_len
        if (self.sb.get_length() == 0):
            self.addChar(ch)
            return self
        sbSplitted = hx_strings_Strings.splitAt(self.sb.b.getvalue(),[(pos - pre_len)])
        self.sb = StringBuf()
        _this = self.sb
        s = Std.string((sbSplitted[0] if 0 < len(sbSplitted) else None))
        _this.b.write(s)
        self.addChar(ch)
        _this = self.sb
        s = Std.string((sbSplitted[1] if 1 < len(sbSplitted) else None))
        _this.b.write(s)
        return self

    def insertAll(self,pos,items):
        if (pos < 0):
            raise haxe_Exception.thrown("[pos] must not be negative")
        if (pos > self.len):
            raise haxe_Exception.thrown("[pos] must not be greater than this.length")
        if (pos == self.len):
            self.addAll(items)
            return self
        if (pos == 0):
            if (self.pre is None):
                self.pre = []
            pre = self.pre
            i = len(items)
            while True:
                tmp = i
                i = (i - 1)
                if (not ((tmp > 0))):
                    break
                item = (items[i] if i >= 0 and i < len(items) else None)
                pre.insert(0, item)
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.len
                _hx_local_0.len = (_hx_local_1 + (0 if ((item is None)) else len(item)))
                _hx_local_0.len
            return self
        pre_len = 0
        if (self.pre is not None):
            pre = self.pre
            i = len(pre)
            _g = 0
            _g1 = len(pre)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _hx_str = (pre[i] if i >= 0 and i < len(pre) else None)
                next_pre_len = (pre_len + ((0 if ((_hx_str is None)) else len(_hx_str))))
                if (next_pre_len == pos):
                    j = len(items)
                    while True:
                        tmp = j
                        j = (j - 1)
                        if (not ((tmp > 0))):
                            break
                        item = (items[j] if j >= 0 and j < len(items) else None)
                        pre.insert((i + 1), item)
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.len
                        _hx_local_2.len = (_hx_local_3 + (0 if ((item is None)) else len(item)))
                        _hx_local_2.len
                    return self
                if (next_pre_len > pos):
                    preSplitted = hx_strings_Strings.splitAt((pre[i] if i >= 0 and i < len(pre) else None),[(pos - pre_len)])
                    python_internal_ArrayImpl._set(pre, i, (preSplitted[0] if 0 < len(preSplitted) else None))
                    pre.insert((i + 1), (preSplitted[1] if 1 < len(preSplitted) else None))
                    j1 = len(items)
                    while True:
                        tmp1 = j1
                        j1 = (j1 - 1)
                        if (not ((tmp1 > 0))):
                            break
                        item1 = (items[j1] if j1 >= 0 and j1 < len(items) else None)
                        pre.insert((i + 1), item1)
                        _hx_local_4 = self
                        _hx_local_5 = _hx_local_4.len
                        _hx_local_4.len = (_hx_local_5 + (0 if ((item1 is None)) else len(item1)))
                        _hx_local_4.len
                    return self
                pre_len = next_pre_len
        if (self.sb.get_length() == 0):
            _g = 0
            while (_g < len(items)):
                item = (items[_g] if _g >= 0 and _g < len(items) else None)
                _g = (_g + 1)
                self.add(item)
            return self
        sbSplitted = hx_strings_Strings.splitAt(self.sb.b.getvalue(),[(pos - pre_len)])
        self.sb = StringBuf()
        _this = self.sb
        s = Std.string((sbSplitted[0] if 0 < len(sbSplitted) else None))
        _this.b.write(s)
        _g = 0
        while (_g < len(items)):
            item = (items[_g] if _g >= 0 and _g < len(items) else None)
            _g = (_g + 1)
            _this = self.sb
            s = Std.string(item)
            _this.b.write(s)
            _hx_local_8 = self
            _hx_local_9 = _hx_local_8.len
            _hx_local_8.len = (_hx_local_9 + (0 if ((item is None)) else len(item)))
            _hx_local_8.len
        _this = self.sb
        s = Std.string((sbSplitted[1] if 1 < len(sbSplitted) else None))
        _this.b.write(s)
        return self

    def asOutput(self):
        return hx_strings__StringBuilder_OutputWrapper(self)

    def toString(self):
        if (self.pre is None):
            return self.sb.b.getvalue()
        _this = self.pre
        _hx_str = (HxOverrides.stringOrNull("".join([python_Boot.toString1(x1,'') for x1 in _this])) + HxOverrides.stringOrNull(self.sb.b.getvalue()))
        self.clear()
        self.add(_hx_str)
        return _hx_str

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.sb = None
        _hx_o.pre = None
        _hx_o.len = None
hx_strings_StringBuilder._hx_class = hx_strings_StringBuilder


class hx_strings__StringBuilder_OutputWrapper(haxe_io_Output):
    _hx_class_name = "hx.strings._StringBuilder.OutputWrapper"
    __slots__ = ("sb", "bo")
    _hx_fields = ["sb", "bo"]
    _hx_methods = ["flush", "writeByte", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,sb):
        self.bo = None
        self.sb = sb

    def flush(self):
        if ((self.bo is not None) and ((len(self.bo.b.b) > 0))):
            self.sb.add(self.bo.getBytes().toString())

    def writeByte(self,c):
        if (self.bo is None):
            self.bo = haxe_io_BytesOutput()
        self.bo.writeByte(c)

    def writeString(self,_hx_str,encoding = None):
        self.flush()
        self.sb.add(_hx_str)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.sb = None
        _hx_o.bo = None
hx_strings__StringBuilder_OutputWrapper._hx_class = hx_strings__StringBuilder_OutputWrapper


class hx_strings_internal_OS:
    _hx_class_name = "hx.strings.internal.OS"
    __slots__ = ()
    _hx_statics = ["isWindows"]
hx_strings_internal_OS._hx_class = hx_strings_internal_OS


class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "get_length", "fromCharCode", "substring", "substr"]

    @staticmethod
    def split(s,d):
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            check = s.find(_hx_str, startLeft, len(s))
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        return s

    @staticmethod
    def get_length(s):
        return len(s)

    @staticmethod
    def fromCharCode(code):
        return "".join(map(chr,[code]))

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString


class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "arrayJoin", "safeJoin", "isPyBool", "isPyInt", "isPyFloat", "isClass", "isAnonObject", "_add_dynamic", "toString", "toString1", "isMetaType", "fields", "isString", "isArray", "simpleField", "createClosure", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "unsafeFastCodeAt", "handleKeywords", "prefixLength", "unhandleKeywords", "implementsInterface"]

    @staticmethod
    def arrayJoin(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def safeJoin(x,sep):
        return sep.join([x1 for x1 in x])

    @staticmethod
    def isPyBool(o):
        return isinstance(o,bool)

    @staticmethod
    def isPyInt(o):
        if isinstance(o,int):
            return (not isinstance(o,bool))
        else:
            return False

    @staticmethod
    def isPyFloat(o):
        return isinstance(o,float)

    @staticmethod
    def isClass(o):
        if (o is not None):
            if not HxOverrides.eq(o,str):
                return python_lib_Inspect.isclass(o)
            else:
                return True
        else:
            return False

    @staticmethod
    def isAnonObject(o):
        return isinstance(o,_hx_AnonObject)

    @staticmethod
    def _add_dynamic(a,b):
        if (isinstance(a,str) and isinstance(b,str)):
            return (a + b)
        if (isinstance(a,str) or isinstance(b,str)):
            return (python_Boot.toString1(a,"") + python_Boot.toString1(b,""))
        return (a + b)

    @staticmethod
    def toString(o):
        return python_Boot.toString1(o,"")

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if ((type(o) == type) and (o == str)):
                return "#String"
            if ((type(o) == type) and (o == list)):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def isString(o):
        return isinstance(o,str)

    @staticmethod
    def isArray(o):
        return isinstance(o,list)

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def createClosure(obj,func):
        return python_internal_MethodClosure(obj,func)

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        if (field is None):
            return None
        if isinstance(o,str):
            field1 = field
            _hx_local_0 = len(field1)
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            field1 = field
            _hx_local_1 = len(field1)
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unsafeFastCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def handleKeywords(name):
        if (name in python_Boot.keywords):
            return ("_hx_" + name)
        elif ((((len(name) > 2) and ((ord(name[0]) == 95))) and ((ord(name[1]) == 95))) and ((ord(name[(len(name) - 1)]) != 95))):
            return ("_hx_" + name)
        else:
            return name

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name

    @staticmethod
    def implementsInterface(value,cls):
        loop = None
        def _hx_local_1(intf):
            f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
            if (f is not None):
                _g = 0
                while (_g < len(f)):
                    i = (f[_g] if _g >= 0 and _g < len(f) else None)
                    _g = (_g + 1)
                    if (i == cls):
                        return True
                    else:
                        l = loop(i)
                        if l:
                            return True
                return False
            else:
                return False
        loop = _hx_local_1
        currentClass = value.__class__
        result = False
        while (currentClass is not None):
            if loop(currentClass):
                result = True
                break
            currentClass = python_Boot.getSuperClass(currentClass)
        return result
python_Boot._hx_class = python_Boot

class hx_strings_internal__Either3__Either3(Enum):
    __slots__ = ()
    _hx_class_name = "hx.strings.internal._Either3._Either3"
    _hx_constructs = ["a", "b", "c"]

    @staticmethod
    def a(v):
        return hx_strings_internal__Either3__Either3("a", 0, (v,))

    @staticmethod
    def b(v):
        return hx_strings_internal__Either3__Either3("b", 1, (v,))

    @staticmethod
    def c(v):
        return hx_strings_internal__Either3__Either3("c", 2, (v,))
hx_strings_internal__Either3__Either3._hx_class = hx_strings_internal__Either3__Either3


class hx_strings_Strings:
    _hx_class_name = "hx.strings.Strings"
    __slots__ = ()
    _hx_statics = ["REGEX_ANSI_ESC", "REGEX_HTML_UNESCAPE", "REGEX_SPLIT_LINES", "REGEX_REMOVE_XML_TAGS", "POS_NOT_FOUND", "NEW_LINE_NIX", "NEW_LINE_WIN", "NEW_LINE", "_length", "_getNotFoundDefault", "_charCodeAt8Unsafe", "_splitAsciiWordsUnsafe", "ansiToHtml", "appendIfMissing", "base64Encode", "base64Decode", "charAt8", "charCodeAt8", "compact", "contains", "containsOnly", "containsAll", "containsAllIgnoreCase", "containsAny", "containsAnyIgnoreCase", "containsNone", "containsNoneIgnoreCase", "containsWhitespaces", "countMatches", "countMatchesIgnoreCase", "compare", "compareIgnoreCase", "diff", "diffAt", "ellipsizeLeft", "ellipsizeMiddle", "ellipsizeRight", "endsWith", "endsWithAny", "endsWithAnyIgnoreCase", "endsWithIgnoreCase", "equals", "equalsIgnoreCase", "filter", "filterChars", "getFuzzyDistance", "getLevenshteinDistance", "getLongestCommonSubstring", "hashCode", "htmlDecode", "htmlEncode", "insertAt", "ifBlank", "ifEmpty", "ifNull", "indentLines", "indexOf8", "isBlank", "isDigits", "isEmpty", "isNotBlank", "isNotEmpty", "isLowerCase", "isUpperCase", "iterate", "iterateChars", "lastIndexOf8", "length8", "left", "lpad", "map", "prependIfMissing", "quoteDouble", "quoteSingle", "removeAfter", "removeAfterLast", "removeAfterIgnoreCase", "removeAfterLastIgnoreCase", "removeAt", "removeBefore", "removeBeforeLast", "removeBeforeIgnoreCase", "removeBeforeLastIgnoreCase", "removeAll", "removeFirst", "removeFirstIgnoreCase", "removeAnsi", "removeLeading", "removeTags", "removeTrailing", "repeat", "replaceAll", "replaceFirst", "replaceFirstIgnoreCase", "reverse", "right", "rpad", "split8", "splitAt", "splitEvery", "splitLines", "startsWith", "startsWithAny", "startsWithAnyIgnoreCase", "startsWithIgnoreCase", "substr8", "substring8", "substringAfter", "substringAfterIgnoreCase", "substringBetween", "substringBetweenIgnoreCase", "substringAfterLast", "substringAfterLastIgnoreCase", "substringBefore", "substringBeforeIgnoreCase", "substringBeforeLast", "substringBeforeLastIgnoreCase", "toBool", "toBytes", "toChar", "toCharIterator", "toChars", "toPattern", "toEReg", "toFloat", "toFloatOrNull", "toHex", "toInt", "toIntOrNull", "toLowerCase8", "toLowerCaseFirstChar", "toLowerCamel", "toLowerHyphen", "toLowerUnderscore", "toTitle", "toUpperCamel", "toUpperUnderscore", "toString", "toUpperCase8", "toUpperCaseFirstChar", "trim", "trimRight", "trimLeft", "trimLines", "trimToNull", "trimToEmpty", "truncate", "urlDecode", "urlEncode", "wrap"]

    @staticmethod
    def _length(_hx_str):
        return len(_hx_str)

    @staticmethod
    def _getNotFoundDefault(_hx_str,notFoundDefault):
        notFoundDefault1 = notFoundDefault
        if (notFoundDefault1 == 1):
            return None
        elif (notFoundDefault1 == 2):
            return ""
        elif (notFoundDefault1 == 3):
            return _hx_str
        else:
            pass

    @staticmethod
    def _charCodeAt8Unsafe(_hx_str,pos):
        return HxString.charCodeAt(_hx_str,pos)

    @staticmethod
    def _splitAsciiWordsUnsafe(_hx_str):
        words = list()
        currentWord = hx_strings_StringBuilder()
        chars = hx_strings_Strings.toChars(_hx_str)
        _hx_len = len(chars)
        lastIndex = (_hx_len - 1)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = (chars[i] if i >= 0 and i < len(chars) else None)
            if (((ch > 64) and ((ch < 91))) or (((ch > 96) and ((ch < 123))))):
                chNext = (python_internal_ArrayImpl._get(chars, (i + 1)) if ((i < lastIndex)) else -1)
                currentWord.addChar(ch)
                if ((chNext > 47) and ((chNext < 58))):
                    x = currentWord.toString()
                    words.append(x)
                    currentWord.clear()
                elif (ch in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h):
                    if ((chNext in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h) and ((len(chars) > ((i + 2))))):
                        if (not (python_internal_ArrayImpl._get(chars, (i + 2)) in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h)):
                            x1 = currentWord.toString()
                            words.append(x1)
                            currentWord.clear()
                elif (chNext in hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h):
                    x2 = currentWord.toString()
                    words.append(x2)
                    currentWord.clear()
            elif ((ch > 47) and ((ch < 58))):
                currentWord.addChar(ch)
                chNext1 = (python_internal_ArrayImpl._get(chars, (i + 1)) if ((i < lastIndex)) else -1)
                if (not (((chNext1 > 47) and ((chNext1 < 58))))):
                    x3 = currentWord.toString()
                    words.append(x3)
                    currentWord.clear()
            elif (currentWord.len > 0):
                x4 = currentWord.toString()
                words.append(x4)
                currentWord.clear()
        if (currentWord.len > 0):
            x = currentWord.toString()
            words.append(x)
        return words

    @staticmethod
    def ansiToHtml(_hx_str,renderMethod = None,initialState = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if (renderMethod is None):
            renderMethod = hx_strings_AnsiToHtmlRenderMethod.StyleAttributes
        styleOrClassAttribute = None
        styleOrClassAttribute1 = renderMethod.index
        if (styleOrClassAttribute1 == 0):
            styleOrClassAttribute = "style"
        elif (styleOrClassAttribute1 == 1):
            styleOrClassAttribute = "class"
        elif (styleOrClassAttribute1 == 2):
            cb = renderMethod.params[0]
            styleOrClassAttribute = "class"
        else:
            pass
        sb = hx_strings_StringBuilder()
        if ((initialState is not None) and ((((((initialState.fgcolor is not None) or ((initialState.bgcolor is not None))) or initialState.bold) or initialState.underline) or initialState.blink))):
            sb.add((("<span " + ("null" if styleOrClassAttribute is None else styleOrClassAttribute)) + "=\"")).add(initialState.toCSS(renderMethod)).add("\">")
        effectiveState = hx_strings_AnsiState(initialState)
        strLenMinus1 = (((0 if ((_hx_str is None)) else len(_hx_str))) - 1)
        i = -1
        lookAhead = hx_strings_StringBuilder()
        while (i < strLenMinus1):
            i = (i + 1)
            ch = HxString.charCodeAt(_hx_str,i)
            if (((ch == 27) and ((i < strLenMinus1))) and ((HxString.charCodeAt(_hx_str,(i + 1)) == 91))):
                lookAhead.clear()
                currentState = hx_strings_AnsiState(effectiveState)
                currentGraphicModeParam = 0
                isValidEscapeSequence = False
                i = (i + 1)
                while (i < strLenMinus1):
                    i = (i + 1)
                    ch2 = HxString.charCodeAt(_hx_str,i)
                    lookAhead.addChar(ch2)
                    ch21 = ch2
                    if (ch21 == 48):
                        currentGraphicModeParam = (currentGraphicModeParam * 10)
                    elif (ch21 == 49):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 1)
                    elif (ch21 == 50):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 2)
                    elif (ch21 == 51):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 3)
                    elif (ch21 == 52):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 4)
                    elif (ch21 == 53):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 5)
                    elif (ch21 == 54):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 6)
                    elif (ch21 == 55):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 7)
                    elif (ch21 == 56):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 8)
                    elif (ch21 == 57):
                        currentGraphicModeParam = ((currentGraphicModeParam * 10) + 9)
                    elif (ch21 == 59):
                        currentState.setGraphicModeParameter(currentGraphicModeParam)
                        currentGraphicModeParam = 0
                    elif (ch21 == 109):
                        currentState.setGraphicModeParameter(currentGraphicModeParam)
                        if (((((effectiveState.fgcolor is not None) or ((effectiveState.bgcolor is not None))) or effectiveState.bold) or effectiveState.underline) or effectiveState.blink):
                            sb.add("</span>")
                        if (((((currentState.fgcolor is not None) or ((currentState.bgcolor is not None))) or currentState.bold) or currentState.underline) or currentState.blink):
                            sb.add((("<span " + ("null" if styleOrClassAttribute is None else styleOrClassAttribute)) + "=\"")).add(currentState.toCSS(renderMethod)).add("\">")
                        effectiveState = currentState
                        isValidEscapeSequence = True
                        break
                    else:
                        break
                if (not isValidEscapeSequence):
                    sb.addChar(27).add("[").add(Std.string(lookAhead))
            else:
                sb.addChar(ch)
        if (((((effectiveState.fgcolor is not None) or ((effectiveState.bgcolor is not None))) or effectiveState.bold) or effectiveState.underline) or effectiveState.blink):
            sb.add("</span>")
        return sb.toString()

    @staticmethod
    def appendIfMissing(_hx_str,suffix):
        if (_hx_str is None):
            return None
        if (len(_hx_str) == 0):
            return (Std.string(_hx_str) + Std.string(suffix))
        if hx_strings_Strings.endsWith(_hx_str,suffix):
            return _hx_str
        return (Std.string(_hx_str) + Std.string(suffix))

    @staticmethod
    def base64Encode(plain):
        if (plain is None):
            return None
        return haxe_crypto_Base64.encode((None if ((plain is None)) else haxe_io_Bytes.ofString(plain)))

    @staticmethod
    def base64Decode(encoded):
        if (encoded is None):
            return None
        return haxe_crypto_Base64.decode(encoded).toString()

    @staticmethod
    def charAt8(_hx_str,pos,resultIfOutOfBound = None):
        if (resultIfOutOfBound is None):
            resultIfOutOfBound = ""
        if ((((_hx_str is None) or ((len(_hx_str) == 0))) or ((pos < 0))) or ((pos >= ((0 if ((_hx_str is None)) else len(_hx_str)))))):
            return resultIfOutOfBound
        return ("" if (((pos < 0) or ((pos >= len(_hx_str))))) else _hx_str[pos])

    @staticmethod
    def charCodeAt8(_hx_str,pos,resultIfOutOfBound = None):
        if (resultIfOutOfBound is None):
            resultIfOutOfBound = -1
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (((strLen == 0) or ((pos < 0))) or ((pos >= strLen))):
            return resultIfOutOfBound
        return HxString.charCodeAt(_hx_str,pos)

    @staticmethod
    def compact(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        sb = hx_strings_StringBuilder()
        needWhiteSpace = False
        _g = 0
        _g1 = hx_strings_Strings.toChars(_hx_str)
        while (_g < len(_g1)):
            char = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((char > 8) and ((char < 14))) or ((char == 32))):
                if (sb.len != 0):
                    needWhiteSpace = True
                continue
            elif needWhiteSpace:
                sb.addChar(32)
                needWhiteSpace = False
            sb.addChar(char)
        return sb.toString()

    @staticmethod
    def contains(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        if (searchFor == ""):
            return True
        startIndex = None
        return (((searchIn.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,searchFor,startIndex))) > -1)

    @staticmethod
    def containsOnly(searchIn,allowedChars):
        if ((searchIn is None) or ((len(searchIn) == 0))):
            return True
        if (allowedChars is None):
            return False
        allowedCharsArray = None
        _g = allowedChars
        allowedCharsArray1 = _g.index
        if (allowedCharsArray1 == 0):
            _hx_str = _g.params[0]
            allowedCharsArray = hx_strings_Strings.toChars(_hx_str)
        elif (allowedCharsArray1 == 1):
            chars = _g.params[0]
            allowedCharsArray = chars
        else:
            pass
        _g = 0
        _g1 = hx_strings_Strings.toChars(searchIn)
        while (_g < len(_g1)):
            ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (python_internal_ArrayImpl.indexOf(allowedCharsArray,ch,None) < 0):
                return False
        return True

    @staticmethod
    def containsAll(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            tmp = None
            if ((searchIn is None) or ((candidate is None))):
                tmp = False
            elif (candidate == ""):
                tmp = True
            else:
                startIndex = None
                tmp = (((searchIn.find(candidate) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,candidate,startIndex))) > -1)
            if (not tmp):
                return False
        return True

    @staticmethod
    def containsAllIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        searchIn = searchIn.lower()
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            searchFor1 = candidate.lower()
            tmp = None
            if ((searchIn is None) or ((searchFor1 is None))):
                tmp = False
            elif (searchFor1 == ""):
                tmp = True
            else:
                startIndex = None
                tmp = (((searchIn.find(searchFor1) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,searchFor1,startIndex))) > -1)
            if (not tmp):
                return False
        return True

    @staticmethod
    def containsAny(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            tmp = None
            if ((searchIn is None) or ((candidate is None))):
                tmp = False
            elif (candidate == ""):
                tmp = True
            else:
                startIndex = None
                tmp = (((searchIn.find(candidate) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,candidate,startIndex))) > -1)
            if tmp:
                return True
        return False

    @staticmethod
    def containsAnyIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        searchIn = searchIn.lower()
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            searchFor1 = candidate.lower()
            tmp = None
            if ((searchIn is None) or ((searchFor1 is None))):
                tmp = False
            elif (searchFor1 == ""):
                tmp = True
            else:
                startIndex = None
                tmp = (((searchIn.find(searchFor1) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,searchFor1,startIndex))) > -1)
            if tmp:
                return True
        return False

    @staticmethod
    def containsNone(searchIn,searchFor):
        return (not hx_strings_Strings.containsAny(searchIn,searchFor))

    @staticmethod
    def containsNoneIgnoreCase(searchIn,searchFor):
        return (not hx_strings_Strings.containsAnyIgnoreCase(searchIn,searchFor))

    @staticmethod
    def containsWhitespaces(searchIn):
        if (searchIn is None):
            return False
        _g = 0
        _g1 = hx_strings_Strings.toChars(searchIn)
        while (_g < len(_g1)):
            ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((ch > 8) and ((ch < 14))) or ((ch == 32))):
                return True
        return False

    @staticmethod
    def countMatches(searchIn,searchFor,startAt = None):
        if (startAt is None):
            startAt = 0
        if ((((searchIn is None) or ((len(searchIn) == 0))) or (((searchFor is None) or ((len(searchFor) == 0))))) or ((startAt >= len(searchIn)))):
            return 0
        if (startAt < 0):
            startAt = 0
        count = 0
        foundAt = ((startAt - 1) if ((startAt > -1)) else 0)
        while True:
            startIndex = (foundAt + 1)
            foundAt = (searchIn.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,searchFor,startIndex))
            if (not ((foundAt > -1))):
                break
            count = (count + 1)
        return count

    @staticmethod
    def countMatchesIgnoreCase(searchIn,searchFor,startAt = None):
        if (startAt is None):
            startAt = 0
        if ((((searchIn is None) or ((len(searchIn) == 0))) or (((searchFor is None) or ((len(searchFor) == 0))))) or ((startAt >= len(searchIn)))):
            return 0
        if (startAt < 0):
            startAt = 0
        searchIn = searchIn.lower()
        searchFor = searchFor.lower()
        count = 0
        foundAt = ((startAt - 1) if ((startAt > -1)) else 0)
        while True:
            startIndex = (foundAt + 1)
            foundAt = (searchIn.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(searchIn,searchFor,startIndex))
            if (not ((foundAt > -1))):
                break
            count = (count + 1)
        return count

    @staticmethod
    def compare(_hx_str,other):
        if (_hx_str is None):
            if (other is None):
                return 0
            else:
                return -1
        if (other is None):
            if (_hx_str is None):
                return 0
            else:
                return 1
        if (_hx_str > other):
            return 1
        elif (_hx_str == other):
            return 0
        else:
            return -1

    @staticmethod
    def compareIgnoreCase(_hx_str,other):
        if (_hx_str is None):
            if (other is None):
                return 0
            else:
                return -1
        if (other is None):
            if (_hx_str is None):
                return 0
            else:
                return 1
        str1 = hx_strings_Strings.toLowerCase8(_hx_str)
        other1 = hx_strings_Strings.toLowerCase8(other)
        if (str1 > other1):
            return 1
        elif (str1 == other1):
            return 0
        else:
            return -1

    @staticmethod
    def diff(left,right):
        diff = hx_strings_StringDiff()
        diff.at = hx_strings_Strings.diffAt(left,right)
        diff.left = hx_strings_Strings.substr8(left,diff.at)
        diff.right = hx_strings_Strings.substr8(right,diff.at)
        return diff

    @staticmethod
    def diffAt(_hx_str,other):
        if (_hx_str == other):
            return -1
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        otherLen = (0 if ((other is None)) else len(other))
        if ((strLen == 0) or ((otherLen == 0))):
            return 0
        checkLen = (otherLen if ((strLen > otherLen)) else strLen)
        _g = 0
        _g1 = checkLen
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (HxString.charCodeAt(_hx_str,i) != HxString.charCodeAt(other,i)):
                return i
        return checkLen

    @staticmethod
    def ellipsizeLeft(_hx_str,maxLength,ellipsis = None):
        if (ellipsis is None):
            ellipsis = "..."
        if (((0 if ((_hx_str is None)) else len(_hx_str))) <= maxLength):
            return _hx_str
        ellipsisLen = (0 if ((ellipsis is None)) else len(ellipsis))
        if (maxLength < ellipsisLen):
            raise haxe_Exception.thrown(("[maxLength] must not be smaller than " + Std.string(ellipsisLen)))
        return (("null" if ellipsis is None else ellipsis) + Std.string(hx_strings_Strings.right(_hx_str,(maxLength - ellipsisLen))))

    @staticmethod
    def ellipsizeMiddle(_hx_str,maxLength,ellipsis = None):
        if (ellipsis is None):
            ellipsis = "..."
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (strLen <= maxLength):
            return _hx_str
        ellipsisLen = (0 if ((ellipsis is None)) else len(ellipsis))
        if (maxLength < ellipsisLen):
            raise haxe_Exception.thrown(("[maxLength] must not be smaller than " + Std.string(ellipsisLen)))
        maxStrLen = (maxLength - ellipsisLen)
        leftLen = Math.floor(((maxStrLen / 2) + 0.5))
        rightLen = (maxStrLen - leftLen)
        return ((Std.string((_hx_str if ((((0 if ((_hx_str is None)) else len(_hx_str))) <= leftLen)) else hx_strings_Strings.substring8(_hx_str,0,leftLen))) + ("null" if ellipsis is None else ellipsis)) + Std.string(hx_strings_Strings.right(_hx_str,rightLen)))

    @staticmethod
    def ellipsizeRight(_hx_str,maxLength,ellipsis = None):
        if (ellipsis is None):
            ellipsis = "..."
        if (((0 if ((_hx_str is None)) else len(_hx_str))) <= maxLength):
            return _hx_str
        ellipsisLen = (0 if ((ellipsis is None)) else len(ellipsis))
        if (maxLength < ellipsisLen):
            raise haxe_Exception.thrown(("[maxLength] must not be smaller than " + Std.string(ellipsisLen)))
        _hx_len = (maxLength - ellipsisLen)
        return (Std.string((_hx_str if ((((0 if ((_hx_str is None)) else len(_hx_str))) <= _hx_len)) else hx_strings_Strings.substring8(_hx_str,0,_hx_len))) + ("null" if ellipsis is None else ellipsis))

    @staticmethod
    def endsWith(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        return searchIn.endswith(searchFor)

    @staticmethod
    def endsWithAny(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            if ((candidate is not None) and hx_strings_Strings.endsWith(searchIn,candidate)):
                return True
        return False

    @staticmethod
    def endsWithAnyIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        searchIn = hx_strings_Strings.toLowerCase8(searchIn)
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            if ((candidate is not None) and hx_strings_Strings.endsWith(searchIn,hx_strings_Strings.toLowerCase8(candidate))):
                return True
        return False

    @staticmethod
    def endsWithIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        return hx_strings_Strings.endsWith(searchIn.lower(),searchFor.lower())

    @staticmethod
    def equals(_hx_str,other):
        return (_hx_str == other)

    @staticmethod
    def equalsIgnoreCase(_hx_str,other):
        return (hx_strings_Strings.toLowerCase8(_hx_str) == hx_strings_Strings.toLowerCase8(other))

    @staticmethod
    def filter(_hx_str,_hx_filter,separator = None):
        if (separator is None):
            separator = ""
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        _this = list(filter(_hx_filter,hx_strings_Strings.split8(_hx_str,[separator])))
        return separator.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def filterChars(_hx_str,_hx_filter):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        def _hx_local_0(ch):
            return "".join(map(chr,[ch]))
        _this = list(map(_hx_local_0,list(filter(_hx_filter,hx_strings_Strings.toChars(_hx_str)))))
        return "".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def getFuzzyDistance(left,right):
        if (((left is None) or ((len(left) == 0))) or (((right is None) or ((len(right) == 0))))):
            return 0
        left = hx_strings_Strings.toLowerCase8(left)
        right = hx_strings_Strings.toLowerCase8(right)
        leftChars = hx_strings_Strings.toChars(left)
        rightChars = hx_strings_Strings.toChars(right)
        leftLastMatchAt = -100
        rightLastMatchAt = -100
        score = 0
        _g = 0
        _g1 = len(leftChars)
        while (_g < _g1):
            leftIdx = _g
            _g = (_g + 1)
            leftChar = (leftChars[leftIdx] if leftIdx >= 0 and leftIdx < len(leftChars) else None)
            _g2 = ((rightLastMatchAt + 1) if ((rightLastMatchAt > -1)) else 0)
            _g3 = len(rightChars)
            while (_g2 < _g3):
                rightIdx = _g2
                _g2 = (_g2 + 1)
                rightChar = (rightChars[rightIdx] if rightIdx >= 0 and rightIdx < len(rightChars) else None)
                if (leftChar == rightChar):
                    score = (score + 1)
                    if ((leftLastMatchAt == ((leftIdx - 1))) and ((rightLastMatchAt == ((rightIdx - 1))))):
                        score = (score + 2)
                    leftLastMatchAt = leftIdx
                    rightLastMatchAt = rightIdx
                    break
        return score

    @staticmethod
    def getLevenshteinDistance(left,right):
        leftLen = (0 if ((left is None)) else len(left))
        rightLen = (0 if ((right is None)) else len(right))
        if (leftLen == 0):
            return rightLen
        if (rightLen == 0):
            return leftLen
        if (leftLen > rightLen):
            tmp = left
            left = right
            right = tmp
            tmpLen = leftLen
            leftLen = rightLen
            rightLen = tmpLen
        prevCosts = list()
        costs = list()
        _g = 0
        _g1 = (leftLen + 1)
        while (_g < _g1):
            leftIdx = _g
            _g = (_g + 1)
            prevCosts.append(leftIdx)
            costs.append(0)
        leftChars = hx_strings_Strings.toChars(left)
        rightChars = hx_strings_Strings.toChars(right)
        def _hx_local_0(a,b):
            if (a > b):
                return b
            else:
                return a
        _hx_min = _hx_local_0
        _g = 1
        _g1 = (rightLen + 1)
        while (_g < _g1):
            rightIdx = _g
            _g = (_g + 1)
            rightChar = python_internal_ArrayImpl._get(rightChars, (rightIdx - 1))
            python_internal_ArrayImpl._set(costs, 0, rightIdx)
            _g2 = 1
            _g3 = (leftLen + 1)
            while (_g2 < _g3):
                leftIdx = _g2
                _g2 = (_g2 + 1)
                leftIdxMinus1 = (leftIdx - 1)
                cost = (0 if (((leftChars[leftIdxMinus1] if leftIdxMinus1 >= 0 and leftIdxMinus1 < len(leftChars) else None) == rightChar)) else 1)
                python_internal_ArrayImpl._set(costs, leftIdx, _hx_min(_hx_min(((costs[leftIdxMinus1] if leftIdxMinus1 >= 0 and leftIdxMinus1 < len(costs) else None) + 1),((prevCosts[leftIdx] if leftIdx >= 0 and leftIdx < len(prevCosts) else None) + 1)),((prevCosts[leftIdxMinus1] if leftIdxMinus1 >= 0 and leftIdxMinus1 < len(prevCosts) else None) + cost)))
            tmp = prevCosts
            prevCosts = costs
            costs = tmp
        return (prevCosts[leftLen] if leftLen >= 0 and leftLen < len(prevCosts) else None)

    @staticmethod
    def getLongestCommonSubstring(left,right):
        if ((left is None) or ((right is None))):
            return None
        leftLen = (0 if ((left is None)) else len(left))
        rightLen = (0 if ((right is None)) else len(right))
        if ((leftLen == 0) or ((rightLen == 0))):
            return ""
        leftChars = hx_strings_Strings.toChars(left)
        rightChars = hx_strings_Strings.toChars(right)
        leftSubStartAt = 0
        leftSubLen = 0
        _g = 0
        _g1 = leftLen
        while (_g < _g1):
            leftIdx = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = rightLen
            while (_g2 < _g3):
                rightIdx = _g2
                _g2 = (_g2 + 1)
                currLen = 0
                while (python_internal_ArrayImpl._get(leftChars, (leftIdx + currLen)) == python_internal_ArrayImpl._get(rightChars, (rightIdx + currLen))):
                    currLen = (currLen + 1)
                    if (((leftIdx + currLen) >= leftLen) or (((rightIdx + currLen) >= rightLen))):
                        break
                if (currLen > leftSubLen):
                    leftSubLen = currLen
                    leftSubStartAt = leftIdx
        return hx_strings_Strings.substr8(left,leftSubStartAt,leftSubLen)

    @staticmethod
    def hashCode(_hx_str,algo = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return 0
        if (algo is None):
            algo = hx_strings_HashCodeAlgorithm.PLATFORM_SPECIFIC
        if (algo is None):
            return hash(_hx_str)
        else:
            tmp = algo.index
            if (tmp == 1):
                return haxe_crypto_Adler32.make((None if ((_hx_str is None)) else haxe_io_Bytes.ofString(_hx_str)))
            elif (tmp == 2):
                return haxe_crypto_Crc32.make((None if ((_hx_str is None)) else haxe_io_Bytes.ofString(_hx_str)))
            elif (tmp == 3):
                hc = 5381
                _g = 0
                _g1 = hx_strings_Strings.toChars(_hx_str)
                while (_g < len(_g1)):
                    ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    hc = (((((((((((hc << 5)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + hc) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) ^ ch)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                return hc
            elif (tmp == 4):
                hc = 0
                _g = 0
                _g1 = hx_strings_Strings.toChars(_hx_str)
                while (_g < len(_g1)):
                    ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    hc = ((((((((((hc << 5)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - hc) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + ch) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                return hc
            elif (tmp == 5):
                hc = 0
                _g = 0
                _g1 = hx_strings_Strings.toChars(_hx_str)
                while (_g < len(_g1)):
                    ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                    _g = (_g + 1)
                    hc = (((((((((((((hc << 6)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (((((hc << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - hc) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + ch) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                return hc
            else:
                return hash(_hx_str)

    @staticmethod
    def htmlDecode(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        _this = hx_strings_Strings.REGEX_HTML_UNESCAPE
        def _hx_local_2():
            def _hx_local_1(m):
                match = m.matched()
                match1 = match
                _hx_local_0 = len(match1)
                if (_hx_local_0 == 5):
                    if (match1 == "&amp;"):
                        return "&"
                    else:
                        number = Std.parseInt(hx_strings_Strings.substr8(match,2,(((0 if ((match is None)) else len(match))) - 3)))
                        if (number is None):
                            raise haxe_Exception.thrown(("Invalid HTML value " + ("null" if match is None else match)))
                        return "".join(map(chr,[number]))
                elif (_hx_local_0 == 4):
                    if (match1 == "&gt;"):
                        return ">"
                    elif (match1 == "&lt;"):
                        return "<"
                    else:
                        number = Std.parseInt(hx_strings_Strings.substr8(match,2,(((0 if ((match is None)) else len(match))) - 3)))
                        if (number is None):
                            raise haxe_Exception.thrown(("Invalid HTML value " + ("null" if match is None else match)))
                        return "".join(map(chr,[number]))
                elif (_hx_local_0 == 6):
                    if (match1 == "&apos;"):
                        return "'"
                    elif (match1 == "&nbsp;"):
                        return " "
                    elif (match1 == "&quot;"):
                        return "\""
                    else:
                        number = Std.parseInt(hx_strings_Strings.substr8(match,2,(((0 if ((match is None)) else len(match))) - 3)))
                        if (number is None):
                            raise haxe_Exception.thrown(("Invalid HTML value " + ("null" if match is None else match)))
                        return "".join(map(chr,[number]))
                else:
                    number = Std.parseInt(hx_strings_Strings.substr8(match,2,(((0 if ((match is None)) else len(match))) - 3)))
                    if (number is None):
                        raise haxe_Exception.thrown(("Invalid HTML value " + ("null" if match is None else match)))
                    return "".join(map(chr,[number]))
            return hx_strings__Pattern_MatcherImpl(_this.ereg,_this.pattern,_this.options,_hx_str).map(_hx_local_1)
        return _hx_local_2()

    @staticmethod
    def htmlEncode(_hx_str,escapeQuotes = None):
        if (escapeQuotes is None):
            escapeQuotes = False
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        sb = hx_strings_StringBuilder()
        isFirstSpace = True
        _g = 0
        _g1 = (0 if ((_hx_str is None)) else len(_hx_str))
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            ch = HxString.charCodeAt(_hx_str,i)
            ch1 = ch
            if (ch1 == 32):
                if isFirstSpace:
                    sb.add(" ")
                    isFirstSpace = False
                else:
                    sb.add("&nbsp;")
            elif (ch1 == 34):
                sb.add(("&quot;" if escapeQuotes else "\""))
            elif (ch1 == 38):
                sb.add("&amp;")
            elif (ch1 == 39):
                sb.add(("&#039;" if escapeQuotes else "'"))
            elif (ch1 == 60):
                sb.add("&lt;")
            elif (ch1 == 62):
                sb.add("&gt;")
            elif (ch > 127):
                sb.add("&#").add(Std.string(ch)).add(";")
            else:
                sb.addChar(ch)
            if (ch != 32):
                isFirstSpace = True
        return sb.toString()

    @staticmethod
    def insertAt(_hx_str,pos,insertion):
        if (_hx_str is None):
            return None
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (pos < 0):
            pos = (strLen + pos)
        if ((pos < 0) or ((pos > strLen))):
            raise haxe_Exception.thrown("Absolute value of [pos] must be <= str.length")
        if ((insertion is None) or ((len(insertion) == 0))):
            return _hx_str
        return ((Std.string(hx_strings_Strings.substring8(_hx_str,0,pos)) + Std.string(insertion)) + Std.string(hx_strings_Strings.substring8(_hx_str,pos)))

    @staticmethod
    def ifBlank(_hx_str,fallback):
        if (True if ((_hx_str is None)) else (len(StringTools.trim(_hx_str)) == 0)):
            return fallback
        else:
            return _hx_str

    @staticmethod
    def ifEmpty(_hx_str,fallback):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return fallback
        else:
            return _hx_str

    @staticmethod
    def ifNull(_hx_str,fallback):
        if (_hx_str is None):
            return fallback
        else:
            return _hx_str

    @staticmethod
    def indentLines(_hx_str,indentWith):
        if (_hx_str is None):
            return None
        if ((len(_hx_str) == 0) or (((indentWith is None) or ((len(indentWith) == 0))))):
            return _hx_str
        isFirstLine = True
        sb = hx_strings_StringBuilder()
        _g = 0
        _g1 = hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(_hx_str)
        while (_g < len(_g1)):
            line = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if isFirstLine:
                isFirstLine = False
            else:
                sb.newLine()
            sb.add(indentWith)
            sb.add(line)
        return sb.toString()

    @staticmethod
    def indexOf8(_hx_str,searchFor,startAt = None):
        if (startAt is None):
            startAt = 0
        if ((_hx_str is None) or ((searchFor is None))):
            return -1
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        searchForLen = (0 if ((searchFor is None)) else len(searchFor))
        if (startAt < 0):
            startAt = 0
        if (searchForLen == 0):
            if (startAt == 0):
                return 0
            if ((startAt > 0) and ((startAt < strLen))):
                return startAt
            return strLen
        if (startAt >= strLen):
            return -1
        if (startAt is None):
            return _hx_str.find(searchFor)
        else:
            return HxString.indexOfImpl(_hx_str,searchFor,startAt)

    @staticmethod
    def isBlank(_hx_str):
        if (_hx_str is None):
            return True
        else:
            return (len(StringTools.trim(_hx_str)) == 0)

    @staticmethod
    def isDigits(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return False
        _g = 0
        _g1 = (0 if ((_hx_str is None)) else len(_hx_str))
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            this1 = HxString.charCodeAt(_hx_str,i)
            if (not (((this1 > 47) and ((this1 < 58))))):
                return False
        return True

    @staticmethod
    def isEmpty(_hx_str):
        if (_hx_str is not None):
            return (len(_hx_str) == 0)
        else:
            return True

    @staticmethod
    def isNotBlank(_hx_str):
        if (_hx_str is not None):
            return (len(StringTools.trim(_hx_str)) > 0)
        else:
            return False

    @staticmethod
    def isNotEmpty(_hx_str):
        if (_hx_str is not None):
            return (len(_hx_str) > 0)
        else:
            return False

    @staticmethod
    def isLowerCase(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return False
        return (_hx_str == hx_strings_Strings.toLowerCase8(_hx_str))

    @staticmethod
    def isUpperCase(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return False
        return (_hx_str == hx_strings_Strings.toUpperCase8(_hx_str))

    @staticmethod
    def iterate(_hx_str,callback,separator = None):
        if (separator is None):
            separator = ""
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return
        _g = 0
        _g1 = hx_strings_Strings.split8(_hx_str,[separator])
        while (_g < len(_g1)):
            sub = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            callback(sub)

    @staticmethod
    def iterateChars(_hx_str,callback):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return
        _g = 0
        _g1 = (0 if ((_hx_str is None)) else len(_hx_str))
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            callback(HxString.charCodeAt(_hx_str,i))

    @staticmethod
    def lastIndexOf8(_hx_str,searchFor,startAt = None):
        if ((_hx_str is None) or ((searchFor is None))):
            return -1
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        searchForLen = (0 if ((searchFor is None)) else len(searchFor))
        if (startAt is None):
            startAt = strLen
        if (searchForLen == 0):
            if (startAt < 0):
                return 0
            if (startAt > strLen):
                return strLen
            return startAt
        if (startAt < 0):
            return -1
        elif (startAt >= strLen):
            startAt = (strLen - 1)
        strNeedsUTF8Workaround = (len(_hx_str) != strLen)
        searchForNeedsUTF8Workaround = (len(searchFor) != searchForLen)
        if (searchForNeedsUTF8Workaround and (not strNeedsUTF8Workaround)):
            return -1
        searchForChars = hx_strings_Strings.toChars(searchFor)
        startAt = (startAt + ((searchForLen - 1)))
        searchForPosToCheck = (searchForLen - 1)
        strPos = strLen
        while True:
            tmp = strPos
            strPos = (strPos - 1)
            if (not ((tmp > 0))):
                break
            if (strPos > startAt):
                continue
            strCh = HxString.charCodeAt(_hx_str,strPos)
            if (strCh == (searchForChars[searchForPosToCheck] if searchForPosToCheck >= 0 and searchForPosToCheck < len(searchForChars) else None)):
                if (searchForPosToCheck == 0):
                    return strPos
                searchForPosToCheck = (searchForPosToCheck - 1)
            else:
                searchForPosToCheck = (searchForLen - 1)
        return -1

    @staticmethod
    def length8(_hx_str):
        if (_hx_str is None):
            return 0
        return len(_hx_str)

    @staticmethod
    def left(_hx_str,_hx_len):
        if (((0 if ((_hx_str is None)) else len(_hx_str))) <= _hx_len):
            return _hx_str
        return hx_strings_Strings.substring8(_hx_str,0,_hx_len)

    @staticmethod
    def lpad(_hx_str,targetLength,padStr = None,canOverflow = None):
        if (padStr is None):
            padStr = " "
        if (canOverflow is None):
            canOverflow = True
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if ((_hx_str is None) or ((strLen > targetLength))):
            return _hx_str
        if ((padStr is None) or ((len(padStr) == 0))):
            padStr = " "
        sb = [_hx_str]
        padLen = (0 if ((padStr is None)) else len(padStr))
        while (strLen < targetLength):
            sb.insert(0, padStr)
            strLen = (strLen + padLen)
        if canOverflow:
            return "".join([python_Boot.toString1(x1,'') for x1 in sb])
        return hx_strings_Strings.right("".join([python_Boot.toString1(x1,'') for x1 in sb]),targetLength)

    @staticmethod
    def map(_hx_str,mapper,separator = None):
        if (separator is None):
            separator = ""
        if (_hx_str is None):
            return None
        if (separator is None):
            raise haxe_Exception.thrown("[separator] must not be null")
        return list(map(mapper,hx_strings_Strings.split8(_hx_str,[separator])))

    @staticmethod
    def prependIfMissing(_hx_str,suffix):
        if (_hx_str is None):
            return None
        if (len(_hx_str) == 0):
            return (("null" if suffix is None else suffix) + Std.string(_hx_str))
        if hx_strings_Strings.startsWith(_hx_str,suffix):
            return _hx_str
        return (("null" if suffix is None else suffix) + Std.string(_hx_str))

    @staticmethod
    def quoteDouble(_hx_str):
        if (_hx_str is None):
            return None
        if (len(_hx_str) == 0):
            return "\"\""
        tmp = None
        if (_hx_str is None):
            tmp = False
        else:
            startIndex = None
            tmp = (((_hx_str.find("\"") if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,"\"",startIndex))) > -1)
        if (not tmp):
            return (("\"" + Std.string(_hx_str)) + "\"")
        return (("\"" + Std.string(hx_strings_Strings.replaceAll(_hx_str,"\"","\\\""))) + "\"")

    @staticmethod
    def quoteSingle(_hx_str):
        if (_hx_str is None):
            return None
        if (len(_hx_str) == 0):
            return "''"
        tmp = None
        if (_hx_str is None):
            tmp = False
        else:
            startIndex = None
            tmp = (((_hx_str.find("'") if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,"'",startIndex))) > -1)
        if (not tmp):
            return (("'" + Std.string(_hx_str)) + "'")
        return (("'" + Std.string(hx_strings_Strings.replaceAll(_hx_str,"'","\\'"))) + "'")

    @staticmethod
    def removeAfter(_hx_str,searchFor):
        return hx_strings_Strings.substringBefore(_hx_str,searchFor)

    @staticmethod
    def removeAfterLast(_hx_str,searchFor):
        return hx_strings_Strings.substringBeforeLast(_hx_str,searchFor)

    @staticmethod
    def removeAfterIgnoreCase(_hx_str,searchFor):
        return hx_strings_Strings.substringBeforeIgnoreCase(_hx_str,searchFor)

    @staticmethod
    def removeAfterLastIgnoreCase(_hx_str,searchFor):
        return hx_strings_Strings.substringBeforeLastIgnoreCase(_hx_str,searchFor)

    @staticmethod
    def removeAt(_hx_str,pos,length):
        if (((_hx_str is None) or ((len(_hx_str) == 0))) or ((length < 1))):
            return _hx_str
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (pos < 0):
            pos = (strLen + pos)
        if (pos < 0):
            raise haxe_Exception.thrown("[pos] must be smaller than -1 * str.length")
        if ((pos + length) >= strLen):
            return hx_strings_Strings.substring8(_hx_str,0,pos)
        return (Std.string(hx_strings_Strings.substring8(_hx_str,0,pos)) + Std.string(hx_strings_Strings.substring8(_hx_str,(pos + length))))

    @staticmethod
    def removeBefore(_hx_str,searchFor):
        return hx_strings_Strings.substringAfter(_hx_str,searchFor)

    @staticmethod
    def removeBeforeLast(_hx_str,searchFor):
        return hx_strings_Strings.substringAfterLast(_hx_str,searchFor)

    @staticmethod
    def removeBeforeIgnoreCase(_hx_str,searchFor):
        return hx_strings_Strings.substringAfterIgnoreCase(_hx_str,searchFor)

    @staticmethod
    def removeBeforeLastIgnoreCase(_hx_str,searchFor):
        return hx_strings_Strings.substringAfterLastIgnoreCase(_hx_str,searchFor)

    @staticmethod
    def removeAll(searchIn,searchFor):
        return hx_strings_Strings.replaceAll(searchIn,searchFor,"")

    @staticmethod
    def removeFirst(searchIn,searchFor):
        return hx_strings_Strings.replaceFirst(searchIn,searchFor,"")

    @staticmethod
    def removeFirstIgnoreCase(searchIn,searchFor):
        return hx_strings_Strings.replaceFirstIgnoreCase(searchIn,searchFor,"")

    @staticmethod
    def removeAnsi(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return hx_strings_Strings.REGEX_ANSI_ESC.ereg.replace(_hx_str,"")

    @staticmethod
    def removeLeading(searchIn,searchFor):
        if (((searchIn is None) or ((len(searchIn) == 0))) or (((searchFor is None) or ((len(searchFor) == 0))))):
            return searchIn
        while hx_strings_Strings.startsWith(searchIn,searchFor):
            searchIn = HxString.substring(searchIn,len(searchFor),len(searchIn))
        return searchIn

    @staticmethod
    def removeTags(xml):
        if ((xml is None) or ((len(xml) == 0))):
            return xml
        return hx_strings_Strings.REGEX_REMOVE_XML_TAGS.ereg.replace(xml,"")

    @staticmethod
    def removeTrailing(searchIn,searchFor):
        if (((searchIn is None) or ((len(searchIn) == 0))) or (((searchFor is None) or ((len(searchFor) == 0))))):
            return searchIn
        while hx_strings_Strings.endsWith(searchIn,searchFor):
            searchIn = HxString.substring(searchIn,0,(len(searchIn) - len(searchFor)))
        return searchIn

    @staticmethod
    def repeat(_hx_str,count,separator = None):
        if (separator is None):
            separator = ""
        if (_hx_str is None):
            return None
        if (count < 1):
            return ""
        if (count == 1):
            return _hx_str
        _g = []
        _g1 = 0
        _g2 = count
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            _g.append(_hx_str)
        return separator.join([python_Boot.toString1(x1,'') for x1 in _g])

    @staticmethod
    def replaceAll(searchIn,searchFor,replaceWith):
        if (((searchIn is None) or (((searchIn is None) or ((len(searchIn) == 0))))) or ((searchFor is None))):
            return searchIn
        if (replaceWith is None):
            replaceWith = "null"
        return StringTools.replace(searchIn,searchFor,replaceWith)

    @staticmethod
    def replaceFirst(searchIn,searchFor,replaceWith):
        if (((searchIn is None) or (((searchIn is None) or ((len(searchIn) == 0))))) or ((searchFor is None))):
            return searchIn
        if (replaceWith is None):
            replaceWith = "null"
        foundAt = None
        if (len(searchFor) == 0):
            if (((0 if ((searchIn is None)) else len(searchIn))) > 1):
                foundAt = 1
            else:
                return searchIn
        else:
            foundAt = hx_strings_Strings.indexOf8(searchIn,searchFor)
        return ((Std.string(hx_strings_Strings.substr8(searchIn,0,foundAt)) + ("null" if replaceWith is None else replaceWith)) + Std.string(hx_strings_Strings.substr8(searchIn,(foundAt + ((0 if ((searchFor is None)) else len(searchFor)))))))

    @staticmethod
    def replaceFirstIgnoreCase(searchIn,searchFor,replaceWith):
        if (((searchIn is None) or (((searchIn is None) or ((len(searchIn) == 0))))) or ((searchFor is None))):
            return searchIn
        if (replaceWith is None):
            replaceWith = "null"
        searchFor = searchFor.lower()
        foundAt = None
        if (len(searchFor) == 0):
            if (((0 if ((searchIn is None)) else len(searchIn))) > 1):
                foundAt = 1
            else:
                return searchIn
        else:
            foundAt = hx_strings_Strings.indexOf8(searchIn.lower(),searchFor)
        return ((Std.string(hx_strings_Strings.substr8(searchIn,0,foundAt)) + ("null" if replaceWith is None else replaceWith)) + Std.string(hx_strings_Strings.substr8(searchIn,(foundAt + ((0 if ((searchFor is None)) else len(searchFor)))))))

    @staticmethod
    def reverse(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        chars = hx_strings_Strings.split8(_hx_str,[""])
        chars.reverse()
        return "".join([python_Boot.toString1(x1,'') for x1 in chars])

    @staticmethod
    def right(_hx_str,_hx_len):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return hx_strings_Strings.substring8(_hx_str,(((0 if ((_hx_str is None)) else len(_hx_str))) - _hx_len))

    @staticmethod
    def rpad(_hx_str,targetLength,padStr = None,canOverflow = None):
        if (padStr is None):
            padStr = " "
        if (canOverflow is None):
            canOverflow = True
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if ((_hx_str is None) or ((strLen > targetLength))):
            return _hx_str
        if ((padStr is None) or ((len(padStr) == 0))):
            padStr = " "
        padLen = (0 if ((padStr is None)) else len(padStr))
        sb = hx_strings_StringBuilder(_hx_str)
        while (strLen < targetLength):
            sb.add(padStr)
            strLen = (strLen + padLen)
        if canOverflow:
            return sb.toString()
        _hx_str = sb.toString()
        return (_hx_str if ((((0 if ((_hx_str is None)) else len(_hx_str))) <= targetLength)) else hx_strings_Strings.substring8(_hx_str,0,targetLength))

    @staticmethod
    def split8(_hx_str,separator,maxParts = None):
        if (maxParts is None):
            maxParts = 0
        if ((_hx_str is None) or ((separator is None))):
            return None
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (strLen == 0):
            return []
        def _hx_local_0(s):
            return (s is not None)
        separators = list(filter(_hx_local_0,separator))
        if (len(separators) == 0):
            return None
        if ((maxParts <= 0) and ((len(separators) == 1))):
            delimiter = (separators[0] if 0 < len(separators) else None)
            if (delimiter == ""):
                return list(_hx_str)
            else:
                return _hx_str.split(delimiter)
        if (python_internal_ArrayImpl.indexOf(separators,"",None) > -1):
            if (maxParts <= 0):
                _g = []
                _g1 = 0
                _g2 = strLen
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    x = HxString.substr(_hx_str,i,1)
                    _g.append(x)
                return _g
            if (maxParts > strLen):
                maxParts = strLen
            maxParts = (maxParts - 1)
            _g = []
            _g1 = 0
            _g2 = maxParts
            while (_g1 < _g2):
                i = _g1
                _g1 = (_g1 + 1)
                x = HxString.substr(_hx_str,i,1)
                _g.append(x)
            result = _g
            x = HxString.substr(_hx_str,maxParts,(strLen - maxParts))
            result.append(x)
            return result
        _g = []
        _g1 = 0
        while (_g1 < len(separators)):
            sep = (separators[_g1] if _g1 >= 0 and _g1 < len(separators) else None)
            _g1 = (_g1 + 1)
            x = (0 if ((sep is None)) else len(sep))
            _g.append(x)
        separatorsLengths = _g
        lastFoundAt = 0
        result = []
        resultCount = 0
        while True:
            separatorLen = 0
            foundAt = -1
            _g = 0
            _g1 = len(separators)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                sepFoundAt = hx_strings_Strings.indexOf8(_hx_str,(separators[i] if i >= 0 and i < len(separators) else None),lastFoundAt)
                if (sepFoundAt != -1):
                    if ((foundAt == -1) or ((sepFoundAt < foundAt))):
                        foundAt = sepFoundAt
                        separatorLen = (separatorsLengths[i] if i >= 0 and i < len(separatorsLengths) else None)
            resultCount = (resultCount + 1)
            if ((foundAt == -1) or ((resultCount == maxParts))):
                x = HxString.substr(_hx_str,lastFoundAt,(strLen - lastFoundAt))
                result.append(x)
                break
            x1 = HxString.substr(_hx_str,lastFoundAt,(foundAt - lastFoundAt))
            result.append(x1)
            lastFoundAt = (foundAt + separatorLen)
        return result

    @staticmethod
    def splitAt(_hx_str,splitPos):
        if (_hx_str is None):
            return None
        if ((splitPos is None) or ((len(splitPos) == 0))):
            return [_hx_str]
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (strLen == 0):
            return [_hx_str]
        pos = list()
        _g = 0
        _g1 = splitPos
        while (_g < len(_g1)):
            p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (p < 0):
                p = (strLen + p)
            if ((p < 0) or ((p >= strLen))):
                continue
            if (python_internal_ArrayImpl.indexOf(pos,p,None) > -1):
                continue
            pos.append(p)
        def _hx_local_1(a,b):
            if (a < b):
                return -1
            elif (a > b):
                return 1
            else:
                return 0
        pos.sort(key= python_lib_Functools.cmp_to_key(_hx_local_1))
        result = list()
        lastPos = 0
        _g = 0
        while (_g < len(pos)):
            p = (pos[_g] if _g >= 0 and _g < len(pos) else None)
            _g = (_g + 1)
            chunk = hx_strings_Strings.substring8(_hx_str,lastPos,p)
            if ((chunk is not None) and ((len(chunk) > 0))):
                result.append(chunk)
            lastPos = p
        chunk = hx_strings_Strings.substring8(_hx_str,lastPos)
        if ((chunk is not None) and ((len(chunk) > 0))):
            result.append(chunk)
        return result

    @staticmethod
    def splitEvery(_hx_str,count):
        if (_hx_str is None):
            return None
        if (count < 1):
            raise haxe_Exception.thrown("[count] must be greater than 0")
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if ((strLen == 0) or ((count >= strLen))):
            return [_hx_str]
        result = list()
        pos = 0
        while True:
            chunk = hx_strings_Strings.substr8(_hx_str,pos,count)
            pos = (pos + count)
            if ((chunk is None) or ((len(chunk) == 0))):
                break
            result.append(chunk)
        return result

    @staticmethod
    def splitLines(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return []
        else:
            return hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(_hx_str)

    @staticmethod
    def startsWith(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        if (((searchFor is None) or ((len(searchFor) == 0))) or ((searchIn == searchFor))):
            return True
        return searchIn.startswith(searchFor)

    @staticmethod
    def startsWithAny(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            if ((candidate is not None) and hx_strings_Strings.startsWith(searchIn,candidate)):
                return True
        return False

    @staticmethod
    def startsWithAnyIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        searchIn = hx_strings_Strings.toLowerCase8(searchIn)
        _g = 0
        while (_g < len(searchFor)):
            candidate = (searchFor[_g] if _g >= 0 and _g < len(searchFor) else None)
            _g = (_g + 1)
            if ((candidate is not None) and hx_strings_Strings.startsWith(searchIn,hx_strings_Strings.toLowerCase8(candidate))):
                return True
        return False

    @staticmethod
    def startsWithIgnoreCase(searchIn,searchFor):
        if ((searchIn is None) or ((searchFor is None))):
            return False
        if ((searchFor is None) or ((len(searchFor) == 0))):
            return True
        return hx_strings_Strings.startsWith(searchIn.lower(),searchFor.lower())

    @staticmethod
    def substr8(_hx_str,startAt,_hx_len = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if (_hx_len is None):
            _hx_len = (0 if ((_hx_str is None)) else len(_hx_str))
        if (_hx_len <= 0):
            return ""
        if (startAt < 0):
            startAt = (startAt + (0 if ((_hx_str is None)) else len(_hx_str)))
            if (startAt < 0):
                startAt = 0
        return HxString.substr(_hx_str,startAt,_hx_len)

    @staticmethod
    def substring8(_hx_str,startAt,endAt = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if (endAt is None):
            endAt = (0 if ((_hx_str is None)) else len(_hx_str))
        return HxString.substring(_hx_str,startAt,endAt)

    @staticmethod
    def substringAfter(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return _hx_str
        if ((HxOverrides.eq(_hx_str,"") or ((searchFor is None))) or ((searchFor == ""))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = None
        foundAt = (_hx_str.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,searchFor,startIndex))
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAt + len(searchFor)),None)

    @staticmethod
    def substringAfterIgnoreCase(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        searchFor = searchFor.lower()
        _this = _hx_str.lower()
        startIndex = None
        foundAt = (_this.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(_this,searchFor,startIndex))
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAt + len(searchFor)),None)

    @staticmethod
    def substringBetween(_hx_str,after,before = None,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (before is None):
            before = after
        if ((HxOverrides.eq(_hx_str,"") or (((after is None) or ((len(after) == 0))))) or (((before is None) or ((len(before) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = None
        foundAfterAt = (_hx_str.find(after) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,after,startIndex))
        if (foundAfterAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = (foundAfterAt + len(after))
        foundBeforeAt = (_hx_str.find(before) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,before,startIndex))
        if (foundBeforeAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAfterAt + len(after)),foundBeforeAt)

    @staticmethod
    def substringBetweenIgnoreCase(_hx_str,after,before = None,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (before is None):
            before = after
        if ((HxOverrides.eq(_hx_str,"") or (((after is None) or ((len(after) == 0))))) or (((before is None) or ((len(before) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        strLower = hx_strings_Strings.toLowerCase8(_hx_str)
        after1 = hx_strings_Strings.toLowerCase8(after)
        before1 = hx_strings_Strings.toLowerCase8(before)
        startIndex = None
        foundAfterAt = (strLower.find(after1) if ((startIndex is None)) else HxString.indexOfImpl(strLower,after1,startIndex))
        if (foundAfterAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = (foundAfterAt + len(after1))
        foundBeforeAt = (strLower.find(before1) if ((startIndex is None)) else HxString.indexOfImpl(strLower,before1,startIndex))
        if (foundBeforeAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAfterAt + len(after1)),foundBeforeAt)

    @staticmethod
    def substringAfterLast(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = None
        foundAt = None
        if (startIndex is None):
            foundAt = _hx_str.rfind(searchFor, 0, len(_hx_str))
        elif (searchFor == ""):
            length = len(_hx_str)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            foundAt = (length if ((startIndex > length)) else startIndex)
        else:
            i = _hx_str.rfind(searchFor, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(searchFor))) if ((i == -1)) else (i + 1))
            check = _hx_str.find(searchFor, startLeft, len(_hx_str))
            foundAt = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAt + len(searchFor)),None)

    @staticmethod
    def substringAfterLastIgnoreCase(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        searchFor = searchFor.lower()
        _this = _hx_str.lower()
        startIndex = None
        foundAt = None
        if (startIndex is None):
            foundAt = _this.rfind(searchFor, 0, len(_this))
        elif (searchFor == ""):
            length = len(_this)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            foundAt = (length if ((startIndex > length)) else startIndex)
        else:
            i = _this.rfind(searchFor, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(searchFor))) if ((i == -1)) else (i + 1))
            check = _this.find(searchFor, startLeft, len(_this))
            foundAt = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,(foundAt + len(searchFor)),None)

    @staticmethod
    def substringBefore(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = None
        foundAt = (_hx_str.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(_hx_str,searchFor,startIndex))
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,0,foundAt)

    @staticmethod
    def substringBeforeIgnoreCase(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        searchFor = searchFor.lower()
        _this = _hx_str.lower()
        startIndex = None
        foundAt = (_this.find(searchFor) if ((startIndex is None)) else HxString.indexOfImpl(_this,searchFor,startIndex))
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,0,foundAt)

    @staticmethod
    def substringBeforeLast(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        startIndex = None
        foundAt = None
        if (startIndex is None):
            foundAt = _hx_str.rfind(searchFor, 0, len(_hx_str))
        elif (searchFor == ""):
            length = len(_hx_str)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            foundAt = (length if ((startIndex > length)) else startIndex)
        else:
            i = _hx_str.rfind(searchFor, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(searchFor))) if ((i == -1)) else (i + 1))
            check = _hx_str.find(searchFor, startLeft, len(_hx_str))
            foundAt = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,0,foundAt)

    @staticmethod
    def substringBeforeLastIgnoreCase(_hx_str,searchFor,notFoundDefault = None):
        if (notFoundDefault is None):
            notFoundDefault = 2
        if (_hx_str is None):
            return None
        if (HxOverrides.eq(_hx_str,"") or (((searchFor is None) or ((len(searchFor) == 0))))):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        searchFor = searchFor.lower()
        _this = _hx_str.lower()
        startIndex = None
        foundAt = None
        if (startIndex is None):
            foundAt = _this.rfind(searchFor, 0, len(_this))
        elif (searchFor == ""):
            length = len(_this)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            foundAt = (length if ((startIndex > length)) else startIndex)
        else:
            i = _this.rfind(searchFor, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(searchFor))) if ((i == -1)) else (i + 1))
            check = _this.find(searchFor, startLeft, len(_this))
            foundAt = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (foundAt == -1):
            tmp = None
            notFoundDefault1 = notFoundDefault
            if (notFoundDefault1 == 1):
                tmp = None
            elif (notFoundDefault1 == 2):
                tmp = ""
            elif (notFoundDefault1 == 3):
                tmp = _hx_str
            else:
                pass
            return tmp
        return HxString.substring(_hx_str,0,foundAt)

    @staticmethod
    def toBool(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return False
        _g = _hx_str.lower()
        _hx_local_0 = len(_g)
        if (_hx_local_0 == 1):
            if (_g == "0"):
                return False
            else:
                return True
        elif (_hx_local_0 == 5):
            if (_g == "false"):
                return False
            else:
                return True
        elif (_hx_local_0 == 2):
            if (_g == "no"):
                return False
            else:
                return True
        else:
            return True

    @staticmethod
    def toBytes(_hx_str):
        if (_hx_str is None):
            return None
        return haxe_io_Bytes.ofString(_hx_str)

    @staticmethod
    def toChar(charCode):
        return charCode

    @staticmethod
    def toCharIterator(_hx_str):
        if (_hx_str is None):
            return hx_strings__CharIterator_NullCharIterator.INSTANCE
        else:
            return hx_strings__CharIterator_StringCharIterator(_hx_str,0)

    @staticmethod
    def toChars(_hx_str):
        if (_hx_str is None):
            return None
        strLen = (0 if ((_hx_str is None)) else len(_hx_str))
        if (strLen == 0):
            return []
        _g = []
        _g1 = 0
        _g2 = strLen
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            x = HxString.charCodeAt(_hx_str,i)
            _g.append(x)
        return _g

    @staticmethod
    def toPattern(_hx_str,options = None):
        if (_hx_str is None):
            return None
        return hx_strings_Pattern.compile(_hx_str,options)

    @staticmethod
    def toEReg(_hx_str,opt = None):
        if (opt is None):
            opt = ""
        if (_hx_str is None):
            raise haxe_Exception.thrown("[str] must not be null")
        return EReg(_hx_str,opt)

    @staticmethod
    def toFloat(_hx_str,ifUnparseable):
        if (_hx_str is None):
            return ifUnparseable
        result = Std.parseFloat(_hx_str)
        if python_lib_Math.isnan(result):
            return ifUnparseable
        else:
            return result

    @staticmethod
    def toFloatOrNull(_hx_str,ifUnparseable = None):
        if (_hx_str is None):
            return ifUnparseable
        result = Std.parseFloat(_hx_str)
        if python_lib_Math.isnan(result):
            return ifUnparseable
        else:
            return result

    @staticmethod
    def toHex(num,minDigits = None,upperCase = None):
        if (minDigits is None):
            minDigits = 0
        if (upperCase is None):
            upperCase = True
        hexed = StringTools.hex(num,0)
        if (not upperCase):
            return hexed.lower()
        if (len(hexed) >= minDigits):
            return hexed
        return hx_strings_Strings.lpad(hexed,minDigits,"0")

    @staticmethod
    def toInt(_hx_str,ifUnparseable):
        if (_hx_str is None):
            return ifUnparseable
        result = Std.parseInt(_hx_str)
        if (result is None):
            return ifUnparseable
        else:
            return result

    @staticmethod
    def toIntOrNull(_hx_str,ifUnparseable = None):
        if (_hx_str is None):
            return ifUnparseable
        result = Std.parseInt(_hx_str)
        if (result is None):
            return ifUnparseable
        else:
            return result

    @staticmethod
    def toLowerCase8(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return _hx_str.lower()

    @staticmethod
    def toLowerCaseFirstChar(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        this1 = HxString.charCodeAt(_hx_str,0)
        lowerChar = hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapU2L.h.get(this1,None)
        firstChar = (this1 if ((lowerChar is None)) else lowerChar)
        if (len(_hx_str) == 1):
            return "".join(map(chr,[firstChar]))
        other = hx_strings_Strings.substr8(_hx_str,1)
        return (HxOverrides.stringOrNull("".join(map(chr,[firstChar]))) + ("null" if other is None else other))

    @staticmethod
    def toLowerCamel(_hx_str,keepUppercasedWords = None):
        if (keepUppercasedWords is None):
            keepUppercasedWords = True
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        sb = hx_strings_StringBuilder()
        if keepUppercasedWords:
            _g = 0
            _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)
            while (_g < len(_g1)):
                word = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                sb.add(hx_strings_Strings.toUpperCaseFirstChar(word))
        else:
            _g = 0
            _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)
            while (_g < len(_g1)):
                word = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                sb.add(hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(word)))
        return hx_strings_Strings.toLowerCaseFirstChar(sb.toString())

    @staticmethod
    def toLowerHyphen(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        def _hx_local_0(s):
            return hx_strings_Strings.toLowerCase8(s)
        _this = list(map(_hx_local_0,hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)))
        return "-".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def toLowerUnderscore(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        def _hx_local_0(s):
            return hx_strings_Strings.toLowerCase8(s)
        _this = list(map(_hx_local_0,hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)))
        return "_".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def toTitle(_hx_str,keepUppercasedWords = None):
        if (keepUppercasedWords is None):
            keepUppercasedWords = True
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if keepUppercasedWords:
            def _hx_local_0(s):
                if (hx_strings_Strings.toUpperCase8(s) == s):
                    return s
                else:
                    return hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(s))
            _this = list(map(_hx_local_0,hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)))
            return " ".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_1(s):
            return hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(s))
        _this = list(map(_hx_local_1,hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)))
        return " ".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def toUpperCamel(_hx_str,keepUppercasedWords = None):
        if (keepUppercasedWords is None):
            keepUppercasedWords = True
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        sb = hx_strings_StringBuilder()
        if keepUppercasedWords:
            _g = 0
            _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)
            while (_g < len(_g1)):
                word = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                sb.add(hx_strings_Strings.toUpperCaseFirstChar(word))
        else:
            _g = 0
            _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)
            while (_g < len(_g1)):
                word = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                sb.add(hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(word)))
        return sb.toString()

    @staticmethod
    def toUpperUnderscore(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        def _hx_local_0(s):
            return hx_strings_Strings.toUpperCase8(s)
        _this = list(map(_hx_local_0,hx_strings_Strings._splitAsciiWordsUnsafe(_hx_str)))
        return "_".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def toString(_hx_str):
        if (_hx_str is None):
            return "null"
        else:
            return _hx_str

    @staticmethod
    def toUpperCase8(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return _hx_str.upper()

    @staticmethod
    def toUpperCaseFirstChar(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        this1 = HxString.charCodeAt(_hx_str,0)
        upperChar = hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER.mapL2U.h.get(this1,None)
        firstChar = (this1 if ((upperChar is None)) else upperChar)
        if (len(_hx_str) == 1):
            return "".join(map(chr,[firstChar]))
        other = hx_strings_Strings.substr8(_hx_str,1)
        return (HxOverrides.stringOrNull("".join(map(chr,[firstChar]))) + ("null" if other is None else other))

    @staticmethod
    def trim(_hx_str,charsToRemove = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if (charsToRemove is None):
            return StringTools.trim(_hx_str)
        removableChars = None
        _g = charsToRemove
        removableChars1 = _g.index
        if (removableChars1 == 0):
            str1 = _g.params[0]
            removableChars = hx_strings_Strings.toChars(str1)
        elif (removableChars1 == 1):
            chars = _g.params[0]
            removableChars = chars
        else:
            pass
        this1 = hx_strings_internal__Either2__Either2.b(removableChars)
        this2 = hx_strings_internal__Either2__Either2.b(removableChars)
        return hx_strings_Strings.trimLeft(hx_strings_Strings.trimRight(_hx_str,this1),this2)

    @staticmethod
    def trimRight(_hx_str,charsToRemove = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        if (charsToRemove is None):
            return StringTools.rtrim(_hx_str)
        removableChars = None
        _g = charsToRemove
        removableChars1 = _g.index
        if (removableChars1 == 0):
            str1 = _g.params[0]
            removableChars = hx_strings_Strings.toChars(str1)
        elif (removableChars1 == 1):
            chars = _g.params[0]
            removableChars = chars
        else:
            pass
        if (len(removableChars) == 0):
            return _hx_str
        _hx_len = (0 if ((_hx_str is None)) else len(_hx_str))
        i = (_hx_len - 1)
        while ((i > -1) and ((python_internal_ArrayImpl.indexOf(removableChars,hx_strings_Strings.charCodeAt8(hx_strings_Strings.charAt8(_hx_str,i),0),None) > -1))):
            i = (i - 1)
        if (i < ((_hx_len - 1))):
            return hx_strings_Strings.substring8(_hx_str,0,(i + 1))
        return _hx_str

    @staticmethod
    def trimLeft(_hx_str,charsToRemove = None):
        if (_hx_str is None):
            return _hx_str
        if (charsToRemove is None):
            return StringTools.ltrim(_hx_str)
        removableChars = None
        _g = charsToRemove
        removableChars1 = _g.index
        if (removableChars1 == 0):
            str1 = _g.params[0]
            removableChars = hx_strings_Strings.toChars(str1)
        elif (removableChars1 == 1):
            chars = _g.params[0]
            removableChars = chars
        else:
            pass
        if (len(removableChars) == 0):
            return _hx_str
        _hx_len = (0 if ((_hx_str is None)) else len(_hx_str))
        i = 0
        while ((i < _hx_len) and ((python_internal_ArrayImpl.indexOf(removableChars,hx_strings_Strings.charCodeAt8(hx_strings_Strings.charAt8(_hx_str,i),0),None) > -1))):
            i = (i + 1)
        if (i > 0):
            return hx_strings_Strings.substring8(_hx_str,i,_hx_len)
        return _hx_str

    @staticmethod
    def trimLines(_hx_str,charsToRemove = None):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        def _hx_local_0(line):
            return hx_strings_Strings.trim(line,charsToRemove)
        _this = list(map(_hx_local_0,hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(_hx_str)))
        return "\n".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def trimToNull(_hx_str):
        if (_hx_str is None):
            return None
        trimmed = hx_strings_Strings.trim(_hx_str)
        if ((trimmed is None) or ((len(trimmed) == 0))):
            return None
        return trimmed

    @staticmethod
    def trimToEmpty(_hx_str):
        trimmed = hx_strings_Strings.trim(_hx_str)
        if ((trimmed is None) or ((len(trimmed) == 0))):
            return ""
        return trimmed

    @staticmethod
    def truncate(_hx_str,maxLength):
        if (((0 if ((_hx_str is None)) else len(_hx_str))) <= maxLength):
            return _hx_str
        else:
            return hx_strings_Strings.substring8(_hx_str,0,maxLength)

    @staticmethod
    def urlDecode(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return python_lib_urllib_Parse.unquote(_hx_str)

    @staticmethod
    def urlEncode(_hx_str):
        if ((_hx_str is None) or ((len(_hx_str) == 0))):
            return _hx_str
        return python_lib_urllib_Parse.quote(_hx_str,"")

    @staticmethod
    def wrap(_hx_str,maxLineLength,splitLongWords = None,newLineSeparator = None):
        if (splitLongWords is None):
            splitLongWords = True
        if (newLineSeparator is None):
            newLineSeparator = "\n"
        if ((((0 if ((_hx_str is None)) else len(_hx_str))) <= maxLineLength) or ((maxLineLength < 1))):
            return _hx_str
        sb = hx_strings_StringBuilder()
        wordChars = []
        currLineLength = 0
        _g = 0
        _g1 = hx_strings_Strings.toChars(_hx_str)
        while (_g < len(_g1)):
            ch = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((ch > 8) and ((ch < 14))) or ((ch == 32))):
                if (len(wordChars) > 0):
                    _g2 = 0
                    while (_g2 < len(wordChars)):
                        wordCh = (wordChars[_g2] if _g2 >= 0 and _g2 < len(wordChars) else None)
                        _g2 = (_g2 + 1)
                        if ((currLineLength == maxLineLength) and splitLongWords):
                            sb.add(newLineSeparator)
                            currLineLength = 0
                        currLineLength = (currLineLength + 1)
                        sb.addChar(wordCh)
                    wordChars = []
                if (currLineLength >= maxLineLength):
                    sb.add(newLineSeparator)
                    currLineLength = 0
                sb.addChar(ch)
                currLineLength = (currLineLength + 1)
            else:
                wordChars.append(ch)
        if (len(wordChars) > 0):
            _g = 0
            while (_g < len(wordChars)):
                wordCh = (wordChars[_g] if _g >= 0 and _g < len(wordChars) else None)
                _g = (_g + 1)
                if ((currLineLength == maxLineLength) and splitLongWords):
                    sb.add(newLineSeparator)
                    currLineLength = 0
                currLineLength = (currLineLength + 1)
                sb.addChar(wordCh)
        return sb.toString()
hx_strings_Strings._hx_class = hx_strings_Strings


class hx_strings_StringDiff:
    _hx_class_name = "hx.strings.StringDiff"
    __slots__ = ("at", "left", "right")
    _hx_fields = ["at", "left", "right"]
    _hx_methods = ["toString"]

    def __init__(self):
        self.right = None
        self.left = None
        self.at = -1

    def toString(self):
        return (((((("StringDiff[at=" + Std.string(self.at)) + ", left=") + HxOverrides.stringOrNull(self.left)) + ", right=") + HxOverrides.stringOrNull(self.right)) + "]")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.at = None
        _hx_o.left = None
        _hx_o.right = None
hx_strings_StringDiff._hx_class = hx_strings_StringDiff

class hx_strings_HashCodeAlgorithm(Enum):
    __slots__ = ()
    _hx_class_name = "hx.strings.HashCodeAlgorithm"
    _hx_constructs = ["PLATFORM_SPECIFIC", "ADLER32", "CRC32B", "DJB2A", "JAVA", "SDBM"]
hx_strings_HashCodeAlgorithm.PLATFORM_SPECIFIC = hx_strings_HashCodeAlgorithm("PLATFORM_SPECIFIC", 0, ())
hx_strings_HashCodeAlgorithm.ADLER32 = hx_strings_HashCodeAlgorithm("ADLER32", 1, ())
hx_strings_HashCodeAlgorithm.CRC32B = hx_strings_HashCodeAlgorithm("CRC32B", 2, ())
hx_strings_HashCodeAlgorithm.DJB2A = hx_strings_HashCodeAlgorithm("DJB2A", 3, ())
hx_strings_HashCodeAlgorithm.JAVA = hx_strings_HashCodeAlgorithm("JAVA", 4, ())
hx_strings_HashCodeAlgorithm.SDBM = hx_strings_HashCodeAlgorithm("SDBM", 5, ())
hx_strings_HashCodeAlgorithm._hx_class = hx_strings_HashCodeAlgorithm

class hx_strings_AnsiToHtmlRenderMethod(Enum):
    __slots__ = ()
    _hx_class_name = "hx.strings.AnsiToHtmlRenderMethod"
    _hx_constructs = ["StyleAttributes", "CssClasses", "CssClassesCallback"]

    @staticmethod
    def CssClassesCallback(func):
        return hx_strings_AnsiToHtmlRenderMethod("CssClassesCallback", 2, (func,))
hx_strings_AnsiToHtmlRenderMethod.StyleAttributes = hx_strings_AnsiToHtmlRenderMethod("StyleAttributes", 0, ())
hx_strings_AnsiToHtmlRenderMethod.CssClasses = hx_strings_AnsiToHtmlRenderMethod("CssClasses", 1, ())
hx_strings_AnsiToHtmlRenderMethod._hx_class = hx_strings_AnsiToHtmlRenderMethod


class hx_strings_AnsiState:
    _hx_class_name = "hx.strings.AnsiState"
    __slots__ = ("bgcolor", "blink", "bold", "fgcolor", "underline")
    _hx_fields = ["bgcolor", "blink", "bold", "fgcolor", "underline"]
    _hx_methods = ["isActive", "reset", "copyFrom", "setGraphicModeParameter", "toCSS"]
    _hx_statics = ["defaultCssClassesCallback"]

    def __init__(self,copyFrom = None):
        self.fgcolor = None
        self.bgcolor = None
        self.underline = False
        self.bold = False
        self.blink = False
        if (copyFrom is None):
            self.reset()
        else:
            self.copyFrom(copyFrom)

    def isActive(self):
        if (not (((((self.fgcolor is not None) or ((self.bgcolor is not None))) or self.bold) or self.underline))):
            return self.blink
        else:
            return True

    def reset(self):
        self.fgcolor = None
        self.bgcolor = None
        self.bold = False
        self.underline = False
        self.blink = False

    def copyFrom(self,other):
        self.fgcolor = other.fgcolor
        self.bgcolor = other.bgcolor
        self.bold = other.bold
        self.underline = other.underline
        self.blink = other.blink

    def setGraphicModeParameter(self,param):
        param1 = param
        if (param1 == 0):
            self.reset()
        elif (param1 == 1):
            self.bold = True
        elif (param1 == 4):
            self.underline = True
        elif (param1 == 5):
            self.blink = True
        elif (param1 == 30):
            self.fgcolor = "black"
        elif (param1 == 31):
            self.fgcolor = "red"
        elif (param1 == 32):
            self.fgcolor = "green"
        elif (param1 == 33):
            self.fgcolor = "yellow"
        elif (param1 == 34):
            self.fgcolor = "blue"
        elif (param1 == 35):
            self.fgcolor = "magenta"
        elif (param1 == 36):
            self.fgcolor = "cyan"
        elif (param1 == 37):
            self.fgcolor = "white"
        elif (param1 == 40):
            self.bgcolor = "black"
        elif (param1 == 41):
            self.bgcolor = "red"
        elif (param1 == 42):
            self.bgcolor = "green"
        elif (param1 == 43):
            self.bgcolor = "yellow"
        elif (param1 == 44):
            self.bgcolor = "blue"
        elif (param1 == 45):
            self.bgcolor = "magenta"
        elif (param1 == 46):
            self.bgcolor = "cyan"
        elif (param1 == 47):
            self.bgcolor = "white"
        else:
            pass

    def toCSS(self,renderMethod):
        if (((((self.fgcolor is not None) or ((self.bgcolor is not None))) or self.bold) or self.underline) or self.blink):
            sb = hx_strings_StringBuilder()
            if (renderMethod is None):
                renderMethod = hx_strings_AnsiToHtmlRenderMethod.StyleAttributes
            tmp = renderMethod.index
            if (tmp == 0):
                if (self.fgcolor is not None):
                    sb.add("color:").add(self.fgcolor).add(";")
                if (self.bgcolor is not None):
                    sb.add("background-color:").add(self.bgcolor).add(";")
                if self.bold:
                    sb.add("font-weight:bold;")
                if self.underline:
                    sb.add("text-decoration:underline;")
                if self.blink:
                    sb.add("text-decoration:blink;")
            elif (tmp == 1):
                sb.add(hx_strings_AnsiState.defaultCssClassesCallback(self))
            elif (tmp == 2):
                func = renderMethod.params[0]
                sb.add(func(self))
            else:
                pass
            return sb.toString()
        return ""

    @staticmethod
    def defaultCssClassesCallback(state):
        classes = []
        if (state.fgcolor is not None):
            x = ("ansi_fg_" + HxOverrides.stringOrNull(state.fgcolor))
            classes.append(x)
        if (state.bgcolor is not None):
            x = ("ansi_bg_" + HxOverrides.stringOrNull(state.bgcolor))
            classes.append(x)
        if state.bold:
            classes.append("ansi_bold")
        if state.underline:
            classes.append("ansi_underline")
        if state.blink:
            classes.append("ansi_blink")
        return " ".join([python_Boot.toString1(x1,'') for x1 in classes])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bgcolor = None
        _hx_o.blink = None
        _hx_o.bold = None
        _hx_o.fgcolor = None
        _hx_o.underline = None
hx_strings_AnsiState._hx_class = hx_strings_AnsiState


class hx_strings_internal_Bits:
    _hx_class_name = "hx.strings.internal.Bits"
    __slots__ = ()
    _hx_statics = ["clearBit", "setBit", "toggleBit", "getBit"]

    @staticmethod
    def clearBit(num,bitPos):
        return (num & ~((1 << ((bitPos - 1)))))

    @staticmethod
    def setBit(num,bitPos):
        return (num | ((1 << ((bitPos - 1)))))

    @staticmethod
    def toggleBit(num,bitPos):
        return (num ^ ((1 << ((bitPos - 1)))))

    @staticmethod
    def getBit(num,bitPos):
        return (1 == (((num >> ((bitPos - 1))) & 1)))
hx_strings_internal_Bits._hx_class = hx_strings_internal_Bits


class hx_strings_internal__Either2_Either2_Impl_:
    _hx_class_name = "hx.strings.internal._Either2.Either2_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "get_value", "fromA", "fromB"]
    value = None

    @staticmethod
    def _new(value):
        this1 = value
        return this1

    @staticmethod
    def get_value(this1):
        return this1

    @staticmethod
    def fromA(value):
        this1 = hx_strings_internal__Either2__Either2.a(value)
        return this1

    @staticmethod
    def fromB(value):
        this1 = hx_strings_internal__Either2__Either2.b(value)
        return this1
hx_strings_internal__Either2_Either2_Impl_._hx_class = hx_strings_internal__Either2_Either2_Impl_

class hx_strings_internal__Either2__Either2(Enum):
    __slots__ = ()
    _hx_class_name = "hx.strings.internal._Either2._Either2"
    _hx_constructs = ["a", "b"]

    @staticmethod
    def a(v):
        return hx_strings_internal__Either2__Either2("a", 0, (v,))

    @staticmethod
    def b(v):
        return hx_strings_internal__Either2__Either2("b", 1, (v,))
hx_strings_internal__Either2__Either2._hx_class = hx_strings_internal__Either2__Either2


class hx_strings_internal__Either3_Either3_Impl_:
    _hx_class_name = "hx.strings.internal._Either3.Either3_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "get_value", "fromA", "fromB", "fromC"]
    value = None

    @staticmethod
    def _new(value):
        this1 = value
        return this1

    @staticmethod
    def get_value(this1):
        return this1

    @staticmethod
    def fromA(value):
        this1 = hx_strings_internal__Either3__Either3.a(value)
        return this1

    @staticmethod
    def fromB(value):
        this1 = hx_strings_internal__Either3__Either3.b(value)
        return this1

    @staticmethod
    def fromC(value):
        this1 = hx_strings_internal__Either3__Either3.c(value)
        return this1
hx_strings_internal__Either3_Either3_Impl_._hx_class = hx_strings_internal__Either3_Either3_Impl_


class hx_strings_internal__OneOrMany_OneOrMany_Impl_:
    _hx_class_name = "hx.strings.internal._OneOrMany.OneOrMany_Impl_"
    __slots__ = ()
    _hx_statics = ["fromSingle"]

    @staticmethod
    def fromSingle(value):
        return [value]
hx_strings_internal__OneOrMany_OneOrMany_Impl_._hx_class = hx_strings_internal__OneOrMany_OneOrMany_Impl_


class hx_strings_internal__RingBuffer_RingBuffer_Impl_:
    _hx_class_name = "hx.strings.internal._RingBuffer.RingBuffer_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "get"]

    @staticmethod
    def _new(size):
        this1 = hx_strings_internal__RingBuffer_RingBufferImpl(size)
        return this1

    @staticmethod
    def get(this1,index):
        return this1.get(index)
hx_strings_internal__RingBuffer_RingBuffer_Impl_._hx_class = hx_strings_internal__RingBuffer_RingBuffer_Impl_


class hx_strings_internal__RingBuffer_RingBufferIterator:
    _hx_class_name = "hx.strings.internal._RingBuffer.RingBufferIterator"
    __slots__ = ("buff", "idx")
    _hx_fields = ["buff", "idx"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,buff):
        self.idx = -1
        self.buff = buff

    def hasNext(self):
        return ((self.idx + 1) < self.buff.length)

    def next(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.idx
        _hx_local_0.idx = (_hx_local_1 + 1)
        _hx_local_1
        return self.buff.get(self.idx)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buff = None
        _hx_o.idx = None
hx_strings_internal__RingBuffer_RingBufferIterator._hx_class = hx_strings_internal__RingBuffer_RingBufferIterator


class python_HaxeIterable:
    _hx_class_name = "python.HaxeIterable"
    __slots__ = ("x",)
    _hx_fields = ["x"]
    _hx_methods = ["iterator"]

    def __init__(self,x):
        self.x = x

    def iterator(self):
        return python_HaxeIterator(self.x.__iter__())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.it = None
        _hx_o.x = None
        _hx_o.has = None
        _hx_o.checked = None
python_HaxeIterator._hx_class = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def toDict(this1):
        return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

    @staticmethod
    def toDictHelper(this1,x):
        return this1

    @staticmethod
    def fromDict(d):
        this1 = d
        return this1

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1

    @staticmethod
    def typed(this1):
        return _hx_AnonObject(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

    @staticmethod
    def get(this1,key,_hx_def):
        return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_


class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["lineEnd", "get___name__", "print", "printString", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]
    __name__ = None

    @staticmethod
    def get___name__():
        return __name__

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def printString(_hx_str):
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        python_lib_Sys.stdout.flush()

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None

    @staticmethod
    def dictAsAnon(d):
        return _hx_AnonObject(d)

    @staticmethod
    def toPythonIterable(it):
        def _hx_local_3():
            def _hx_local_2():
                it1 = HxOverrides.iterator(it)
                _hx_self = None
                def _hx_local_0():
                    if it1.hasNext():
                        return it1.next()
                    else:
                        raise haxe_Exception.thrown(StopIteration())
                def _hx_local_1():
                    return _hx_self
                this1 = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
                _hx_self = this1
                return _hx_self
            return _hx_AnonObject({'__iter__': _hx_local_2})
        return _hx_local_3()

    @staticmethod
    def toHaxeIterable(it):
        return python_HaxeIterable(it)

    @staticmethod
    def toHaxeIterator(it):
        return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib


class python__NativeIterable_NativeIterable_Impl_:
    _hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
    __slots__ = ()
    _hx_statics = ["toHaxeIterable", "iterator"]

    @staticmethod
    def toHaxeIterable(this1):
        return python_HaxeIterable(this1)

    @staticmethod
    def iterator(this1):
        return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_


class python__NativeIterator_NativeIterator_Impl_:
    _hx_class_name = "python._NativeIterator.NativeIterator_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toHaxeIterator"]

    @staticmethod
    def _new(p):
        this1 = p
        return this1

    @staticmethod
    def toHaxeIterator(this1):
        return python_HaxeIterator(this1)
python__NativeIterator_NativeIterator_Impl_._hx_class = python__NativeIterator_NativeIterator_Impl_


class python_NativeStringTools:
    _hx_class_name = "python.NativeStringTools"
    __slots__ = ()
    _hx_statics = ["format", "encode", "contains", "strip", "rpartition", "startswith", "endswith"]

    @staticmethod
    def format(s,args):
        return s.format(*args)

    @staticmethod
    def encode(s,encoding = None,errors = None):
        if (encoding is None):
            encoding = "utf-8"
        if (errors is None):
            errors = "strict"
        return s.encode(encoding, errors)

    @staticmethod
    def contains(s,e):
        return (e in s)

    @staticmethod
    def strip(s,chars = None):
        return s.strip(chars)

    @staticmethod
    def rpartition(s,sep):
        return s.rpartition(sep)

    @staticmethod
    def startswith(s,prefix):
        return s.startswith(prefix)

    @staticmethod
    def endswith(s,suffix):
        return s.endswith(suffix)
python_NativeStringTools._hx_class = python_NativeStringTools


class python__VarArgs_VarArgs_Impl_:
    _hx_class_name = "python._VarArgs.VarArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "raw", "toArray", "fromArray"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def raw(this1):
        return this1

    @staticmethod
    def toArray(this1):
        if (not Std.isOfType(this1,list)):
            return list(this1)
        else:
            return this1

    @staticmethod
    def fromArray(d):
        this1 = d
        return this1
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["get_length", "concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set", "unsafeGet", "unsafeSet", "resize"]

    @staticmethod
    def get_length(x):
        return len(x)

    @staticmethod
    def concat(a1,a2):
        return (a1 + a2)

    @staticmethod
    def copy(x):
        return list(x)

    @staticmethod
    def iterator(x):
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        if (l < 0):
            l = 0
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if HxOverrides.eq(a[i],x):
                return i
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        if (l > _hx_len):
            l = _hx_len
        while True:
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            if HxOverrides.eq(a[l],x):
                return l
        return -1

    @staticmethod
    def join(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        x.append(e)
        return len(x)

    @staticmethod
    def unshift(x,e):
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        try:
            x.remove(e)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def contains(x,e):
        return (e in x)

    @staticmethod
    def shift(x):
        if (len(x) == 0):
            return None
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        if (pos < 0):
            pos = (len(x) + pos)
        if (pos < 0):
            pos = 0
        res = x[pos:(pos + _hx_len)]
        del x[pos:(pos + _hx_len)]
        return res

    @staticmethod
    def map(x,f):
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        a.reverse()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v

    @staticmethod
    def unsafeGet(x,idx):
        return x[idx]

    @staticmethod
    def unsafeSet(x,idx,val):
        x[idx] = val
        return val

    @staticmethod
    def resize(x,_hx_len):
        l = len(x)
        if (l < _hx_len):
            idx = (_hx_len - 1)
            v = None
            l1 = len(x)
            while (l1 < idx):
                x.append(None)
                l1 = (l1 + 1)
            if (l1 == idx):
                x.append(v)
            else:
                x[idx] = v
        elif (l > _hx_len):
            pos = _hx_len
            len1 = (l - _hx_len)
            if (pos < 0):
                pos = (len(x) + pos)
            if (pos < 0):
                pos = 0
            res = x[pos:(pos + len1)]
            del x[pos:(pos + len1)]
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "keyValueIterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "split", "length", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def keyValueIterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayKeyValueIterator(x)
        return x.keyValueIterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def shift(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop(0))
        return x.shift()

    @staticmethod
    def pop(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop())
        return x.pop()

    @staticmethod
    def push(x,e):
        if isinstance(x,list):
            _this = x
            _this.append(e)
            return len(_this)
        return x.push(e)

    @staticmethod
    def join(x,sep):
        if isinstance(x,list):
            return sep.join([python_Boot.toString1(x1,'') for x1 in x])
        return x.join(sep)

    @staticmethod
    def filter(x,f):
        if isinstance(x,list):
            return list(filter(f,x))
        return x.filter(f)

    @staticmethod
    def map(x,f):
        if isinstance(x,list):
            return list(map(f,x))
        return x.map(f)

    @staticmethod
    def toUpperCase(x):
        if isinstance(x,str):
            return x.upper()
        return x.toUpperCase()

    @staticmethod
    def toLowerCase(x):
        if isinstance(x,str):
            return x.lower()
        return x.toLowerCase()

    @staticmethod
    def split(x,delimiter):
        if isinstance(x,str):
            _this = x
            if (delimiter == ""):
                return list(_this)
            else:
                return _this.split(delimiter)
        return x.split(delimiter)

    @staticmethod
    def length(x):
        if isinstance(x,str):
            return len(x)
        elif isinstance(x,list):
            return len(x)
        return x.length

    @staticmethod
    def rshift(val,n):
        return ((val % 0x100000000) >> n)

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]

    @staticmethod
    def arraySet(a,i,v):
        if isinstance(a,list):
            x = a
            v1 = v
            l = len(x)
            while (l < i):
                x.append(None)
                l = (l + 1)
            if (l == i):
                x.append(v1)
            else:
                x[i] = v1
            return v1
        else:
            a[i] = v
            return v

    @staticmethod
    def mapKwArgs(a,v):
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1

    @staticmethod
    def reverseMapKwArgs(a,v):
        a1 = a.copy()
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if (val in a1):
                x = a1.get(val,None)
                a1[k1] = x
                del a1[val]
        return a1
HxOverrides._hx_class = HxOverrides


class python_internal_Internal:
    _hx_class_name = "python.internal.Internal"
    __slots__ = ()
python_internal_Internal._hx_class = python_internal_Internal


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.obj = None
        _hx_o.func = None
python_internal_MethodClosure._hx_class = python_internal_MethodClosure


class python_io_NativeInput(haxe_io_Input):
    _hx_class_name = "python.io.NativeInput"
    __slots__ = ("stream", "wasEof")
    _hx_fields = ["stream", "wasEof"]
    _hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        self.wasEof = None
        self.stream = s
        self.set_bigEndian(False)
        self.wasEof = False
        if (not self.stream.readable()):
            raise haxe_Exception.thrown("Write-only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def tell(self):
        return self.stream.tell()

    def throwEof(self):
        self.wasEof = True
        raise haxe_Exception.thrown(haxe_io_Eof())

    def eof(self):
        return self.wasEof

    def readinto(self,b):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def seek(self,p,mode):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def readBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        ba = bytearray(_hx_len)
        ret = self.readinto(ba)
        if (ret == 0):
            self.throwEof()
        s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
        return ret

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
        _hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput


class python_io_IInput:
    _hx_class_name = "python.io.IInput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
python_io_IInput._hx_class = python_io_IInput


class python_io_NativeBytesInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def readinto(self,b):
        return self.stream.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput


class python_io_IFileInput:
    _hx_class_name = "python.io.IFileInput"
    __slots__ = ()
    _hx_methods = ["seek", "tell", "eof"]
    _hx_interfaces = [python_io_IInput]
python_io_IFileInput._hx_class = python_io_IFileInput


class python_io_FileBytesInput(python_io_NativeBytesInput):
    _hx_class_name = "python.io.FileBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeBytesInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesInput._hx_class = python_io_FileBytesInput


class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = ["get_canSeek", "close", "prepare", "flush", "tell"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def flush(self):
        self.stream.flush()

    def tell(self):
        return self.stream.tell()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput


class python_io_NativeBytesOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "prepare", "writeByte", "writeBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)

    def seek(self,p,pos):
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def writeByte(self,c):
        self.stream.write(bytearray([c]))

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.write(s.b[pos:(pos + _hx_len)])

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesOutput._hx_class = python_io_NativeBytesOutput


class python_io_IOutput:
    _hx_class_name = "python.io.IOutput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput


class python_io_IFileOutput:
    _hx_class_name = "python.io.IFileOutput"
    __slots__ = ()
    _hx_methods = ["seek", "tell"]
    _hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput


class python_io_FileBytesOutput(python_io_NativeBytesOutput):
    _hx_class_name = "python.io.FileBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeBytesOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesOutput._hx_class = python_io_FileBytesOutput


class python_io_NativeTextInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.buffer.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def readinto(self,b):
        return self.stream.buffer.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextInput._hx_class = python_io_NativeTextInput


class python_io_FileTextInput(python_io_NativeTextInput):
    _hx_class_name = "python.io.FileTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeTextInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextInput._hx_class = python_io_FileTextInput


class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def seek(self,p,pos):
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.buffer.write(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput


class python_io_FileTextOutput(python_io_NativeTextOutput):
    _hx_class_name = "python.io.FileTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeTextOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput


class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

    @staticmethod
    def createFileInputFromText(t):
        return sys_io_FileInput(python_io_FileTextInput(t))

    @staticmethod
    def createFileInputFromBytes(t):
        return sys_io_FileInput(python_io_FileBytesInput(t))

    @staticmethod
    def createFileOutputFromText(t):
        return sys_io_FileOutput(python_io_FileTextOutput(t))

    @staticmethod
    def createFileOutputFromBytes(t):
        return sys_io_FileOutput(python_io_FileBytesOutput(t))

    @staticmethod
    def seekInTextMode(stream,tell,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            p = (tell() + p)
            pos1 = 0
        elif (pos2 == 2):
            stream.seek(0,2)
            p = (tell() + p)
            pos1 = 0
        else:
            pass
        stream.seek(p,pos1)

    @staticmethod
    def seekInBinaryMode(stream,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            pos1 = 1
        elif (pos2 == 2):
            pos1 = 2
        else:
            pass
        stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools


class python_lib__Re_Choice_Impl_:
    _hx_class_name = "python.lib._Re.Choice_Impl_"
    __slots__ = ()
    _hx_statics = ["fromA", "fromB"]

    @staticmethod
    def fromA(x):
        return x

    @staticmethod
    def fromB(x):
        return x
python_lib__Re_Choice_Impl_._hx_class = python_lib__Re_Choice_Impl_


class python_lib__Re_RegexHelper:
    _hx_class_name = "python.lib._Re.RegexHelper"
    __slots__ = ()
    _hx_statics = ["findallDynamic"]

    @staticmethod
    def findallDynamic(r,string,pos = None,endpos = None):
        if (endpos is None):
            if (pos is None):
                return r.findall(string)
            else:
                return r.findall(string,pos)
        else:
            return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper


class sys_io_File:
    _hx_class_name = "sys.io.File"
    __slots__ = ()
    _hx_statics = ["getContent", "saveContent", "getBytes", "saveBytes", "read", "write", "append", "update", "copy"]

    @staticmethod
    def getContent(path):
        f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
        content = f.read(-1)
        f.close()
        return content

    @staticmethod
    def saveContent(path,content):
        f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
        f.write(content)
        f.close()

    @staticmethod
    def getBytes(path):
        f = python_lib_Builtins.open(path,"rb",-1)
        size = f.read(-1)
        b = haxe_io_Bytes.ofData(size)
        f.close()
        return b

    @staticmethod
    def saveBytes(path,_hx_bytes):
        f = python_lib_Builtins.open(path,"wb",-1)
        f.write(_hx_bytes.b)
        f.close()

    @staticmethod
    def read(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("rb" if binary else "r")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileInputFromBytes(f)
        else:
            return python_io_IoTools.createFileInputFromText(f)

    @staticmethod
    def write(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("wb" if binary else "w")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def append(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("ab" if binary else "a")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def update(path,binary = None):
        if (binary is None):
            binary = True
        if (not sys_FileSystem.exists(path)):
            sys_io_File.write(path).close()
        mode = ("rb+" if binary else "r+")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def copy(srcPath,dstPath):
        python_lib_Shutil.copy(srcPath,dstPath)
sys_io_File._hx_class = sys_io_File


class sys_io_FileInput(haxe_io_Input):
    _hx_class_name = "sys.io.FileInput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def eof(self):
        return self.impl.eof()

    def readByte(self):
        return self.impl.readByte()

    def readBytes(self,s,pos,_hx_len):
        return self.impl.readBytes(s,pos,_hx_len)

    def close(self):
        self.impl.close()

    def readAll(self,bufsize = None):
        return self.impl.readAll(bufsize)

    def readFullBytes(self,s,pos,_hx_len):
        self.impl.readFullBytes(s,pos,_hx_len)

    def read(self,nbytes):
        return self.impl.read(nbytes)

    def readUntil(self,end):
        return self.impl.readUntil(end)

    def readLine(self):
        return self.impl.readLine()

    def readFloat(self):
        return self.impl.readFloat()

    def readDouble(self):
        return self.impl.readDouble()

    def readInt8(self):
        return self.impl.readInt8()

    def readInt16(self):
        return self.impl.readInt16()

    def readUInt16(self):
        return self.impl.readUInt16()

    def readInt24(self):
        return self.impl.readInt24()

    def readUInt24(self):
        return self.impl.readUInt24()

    def readInt32(self):
        return self.impl.readInt32()

    def readString(self,_hx_len,encoding = None):
        return self.impl.readString(_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput


class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def flush(self):
        self.impl.flush()

    def close(self):
        self.impl.close()

    def write(self,s):
        self.impl.write(s)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeFloat(self,x):
        self.impl.writeFloat(x)

    def writeDouble(self,x):
        self.impl.writeDouble(x)

    def writeInt8(self,x):
        self.impl.writeInt8(x)

    def writeInt16(self,x):
        self.impl.writeInt16(x)

    def writeUInt16(self,x):
        self.impl.writeUInt16(x)

    def writeInt24(self,x):
        self.impl.writeInt24(x)

    def writeUInt24(self,x):
        self.impl.writeUInt24(x)

    def writeInt32(self,x):
        self.impl.writeInt32(x)

    def prepare(self,nbytes):
        self.impl.prepare(nbytes)

    def writeInput(self,i,bufsize = None):
        self.impl.writeInput(i,bufsize)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput

class sys_io_FileSeek(Enum):
    __slots__ = ()
    _hx_class_name = "sys.io.FileSeek"
    _hx_constructs = ["SeekBegin", "SeekCur", "SeekEnd"]
sys_io_FileSeek.SeekBegin = sys_io_FileSeek("SeekBegin", 0, ())
sys_io_FileSeek.SeekCur = sys_io_FileSeek("SeekCur", 1, ())
sys_io_FileSeek.SeekEnd = sys_io_FileSeek("SeekEnd", 2, ())
sys_io_FileSeek._hx_class = sys_io_FileSeek

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

haxe_SysTools.winMetaCharacters = [32, 40, 41, 37, 33, 94, 34, 60, 62, 38, 124, 10, 13, 44, 59]
StringTools.winMetaCharacters = haxe_SysTools.winMetaCharacters
Sys._programPath = sys_FileSystem.fullPath(python_lib_Inspect.getsourcefile(Sys))
_Xml_XmlType_Impl_.Element = 0
_Xml_XmlType_Impl_.PCData = 1
_Xml_XmlType_Impl_.CData = 2
_Xml_XmlType_Impl_.Comment = 3
_Xml_XmlType_Impl_.DocType = 4
_Xml_XmlType_Impl_.ProcessingInstruction = 5
_Xml_XmlType_Impl_.Document = 6
Xml.Element = 0
Xml.PCData = 1
Xml.CData = 2
Xml.Comment = 3
Xml.DocType = 4
Xml.ProcessingInstruction = 5
Xml.Document = 6
com_plantuml_mindmap_Tetris.MAX_VALUE = 999999999.0
haxe_crypto_Base64.CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
haxe_crypto_Base64.BYTES = haxe_io_Bytes.ofString(haxe_crypto_Base64.CHARS)
haxe_crypto_Base64.URL_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
haxe_crypto_Base64.URL_BYTES = haxe_io_Bytes.ofString(haxe_crypto_Base64.URL_CHARS)
def _hx_init_haxe_io_FPHelper_i64tmp():
    def _hx_local_0():
        this1 = haxe__Int64____Int64(0,0)
        return this1
    return _hx_local_0()
haxe_io_FPHelper.i64tmp = _hx_init_haxe_io_FPHelper_i64tmp()
haxe_io_FPHelper.LN2 = 0.6931471805599453
def _hx_init_haxe_xml_Parser_escapes():
    def _hx_local_0():
        h = haxe_ds_StringMap()
        h.h["lt"] = "<"
        h.h["gt"] = ">"
        h.h["amp"] = "&"
        h.h["quot"] = "\""
        h.h["apos"] = "'"
        return h
    return _hx_local_0()
haxe_xml_Parser.escapes = _hx_init_haxe_xml_Parser_escapes()
hx_strings__Char_Char_Impl_.CHAR_CASE_MAPPER = hx_strings__Char_CharCaseMapper()
hx_strings__Char_Char_Impl_.BACKSPACE = 8
hx_strings__Char_Char_Impl_.TAB = 9
hx_strings__Char_Char_Impl_.LF = 10
hx_strings__Char_Char_Impl_.CR = 13
hx_strings__Char_Char_Impl_.ESC = 27
hx_strings__Char_Char_Impl_.SPACE = 32
hx_strings__Char_Char_Impl_.EXCLAMATION_MARK = 33
hx_strings__Char_Char_Impl_.DOUBLE_QUOTE = 34
hx_strings__Char_Char_Impl_.HASH = 35
hx_strings__Char_Char_Impl_.DOLLAR = 36
hx_strings__Char_Char_Impl_.AMPERSAND = 38
hx_strings__Char_Char_Impl_.SINGLE_QUOTE = 39
hx_strings__Char_Char_Impl_.BRACKET_ROUND_LEFT = 40
hx_strings__Char_Char_Impl_.BRACKET_ROUND_RIGHT = 41
hx_strings__Char_Char_Impl_.ASTERISK = 42
hx_strings__Char_Char_Impl_.PLUS = 43
hx_strings__Char_Char_Impl_.COMMA = 44
hx_strings__Char_Char_Impl_.MINUS = 45
hx_strings__Char_Char_Impl_.DOT = 46
hx_strings__Char_Char_Impl_.SLASH = 47
hx_strings__Char_Char_Impl_.ZERO = 48
hx_strings__Char_Char_Impl_.ONE = 49
hx_strings__Char_Char_Impl_.TWO = 50
hx_strings__Char_Char_Impl_.TRHEE = 51
hx_strings__Char_Char_Impl_.FOUR = 52
hx_strings__Char_Char_Impl_.FIVE = 53
hx_strings__Char_Char_Impl_.SIX = 54
hx_strings__Char_Char_Impl_.SEVEN = 55
hx_strings__Char_Char_Impl_.EIGHT = 56
hx_strings__Char_Char_Impl_.NINE = 57
hx_strings__Char_Char_Impl_.COLON = 58
hx_strings__Char_Char_Impl_.SEMICOLON = 59
hx_strings__Char_Char_Impl_.LOWER_THAN = 60
hx_strings__Char_Char_Impl_.EQUALS = 61
hx_strings__Char_Char_Impl_.GREATER_THAN = 62
hx_strings__Char_Char_Impl_.QUESTION_MARK = 63
hx_strings__Char_Char_Impl_.BRACKET_SQUARE_LEFT = 91
hx_strings__Char_Char_Impl_.BACKSLASH = 92
hx_strings__Char_Char_Impl_.BRACKET_SQUARE_RIGHT = 93
hx_strings__Char_Char_Impl_.CARET = 94
hx_strings__Char_Char_Impl_.UNDERSCORE = 95
hx_strings__Char_Char_Impl_.BRACKET_CURLY_LEFT = 123
hx_strings__Char_Char_Impl_.PIPE = 124
hx_strings__Char_Char_Impl_.BRACKET_CURLY_RIGHT = 125
hx_strings__CharIterator_NullCharIterator.INSTANCE = hx_strings__CharIterator_NullCharIterator()
hx_strings_Pattern.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'immutable': None, 'threadSafe': None})})
hx_strings_Matcher.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'notThreadSafe': None})})
hx_strings_StringBuilder.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'notThreadSafe': None})})
def _hx_init_hx_strings_internal_OS_isWindows():
    def _hx_local_0():
        os = Sys.systemName()
        _this = EReg("win","i")
        _this.matchObj = python_lib_Re.search(_this.pattern,os)
        return (_this.matchObj is not None)
    return _hx_local_0()
hx_strings_internal_OS.isWindows = _hx_init_hx_strings_internal_OS_isWindows()
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
def _hx_init_hx_strings_Strings_REGEX_ANSI_ESC():
    def _hx_local_0():
        this1 = hx_strings_internal__Either3__Either3.b("g")
        return hx_strings_Pattern.compile((HxOverrides.stringOrNull("".join(map(chr,[27]))) + "\\[[;\\d]*m"),this1)
    return _hx_local_0()
hx_strings_Strings.REGEX_ANSI_ESC = _hx_init_hx_strings_Strings_REGEX_ANSI_ESC()
def _hx_init_hx_strings_Strings_REGEX_HTML_UNESCAPE():
    def _hx_local_0():
        this1 = hx_strings_internal__Either3__Either3.b("g")
        return hx_strings_Pattern.compile("&(#\\d+|amp|nbsp|apos|lt|gt|quot);",this1)
    return _hx_local_0()
hx_strings_Strings.REGEX_HTML_UNESCAPE = _hx_init_hx_strings_Strings_REGEX_HTML_UNESCAPE()
def _hx_init_hx_strings_Strings_REGEX_SPLIT_LINES():
    def _hx_local_0():
        this1 = hx_strings_internal__Either3__Either3.b("g")
        return hx_strings_Pattern.compile("\\r?\\n",this1)
    return _hx_local_0()
hx_strings_Strings.REGEX_SPLIT_LINES = _hx_init_hx_strings_Strings_REGEX_SPLIT_LINES()
def _hx_init_hx_strings_Strings_REGEX_REMOVE_XML_TAGS():
    def _hx_local_0():
        this1 = hx_strings_internal__Either3__Either3.b("g")
        return hx_strings_Pattern.compile("<[!a-zA-Z\\/][^>]*>",this1)
    return _hx_local_0()
hx_strings_Strings.REGEX_REMOVE_XML_TAGS = _hx_init_hx_strings_Strings_REGEX_REMOVE_XML_TAGS()
hx_strings_Strings.POS_NOT_FOUND = -1
hx_strings_Strings.NEW_LINE_NIX = "\n"
hx_strings_Strings.NEW_LINE_WIN = "\r\n"
hx_strings_Strings.NEW_LINE = ("\r\n" if (hx_strings_internal_OS.isWindows) else "\n")
python_Lib.lineEnd = ("\r\n" if ((Sys.systemName() == "Windows")) else "\n")

MainCLI.main()
