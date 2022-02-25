(function ($hx_exports, $global) { "use strict";
$hx_exports["com"] = $hx_exports["com"] || {};
$hx_exports["com"]["plantuml"] = $hx_exports["com"]["plantuml"] || {};
$hx_exports["com"]["plantuml"]["api"] = $hx_exports["com"]["plantuml"]["api"] || {};
$hx_exports["com"]["plantuml"]["api"]["v1"] = $hx_exports["com"]["plantuml"]["api"]["v1"] || {};
var $estr = function() { return js_Boot.__string_rec(this,''); },$hxEnums = $hxEnums || {},$_;
function $extend(from, fields) {
	var proto = Object.create(from);
	for (var name in fields) proto[name] = fields[name];
	if( fields.toString !== Object.prototype.toString ) proto.toString = fields.toString;
	return proto;
}
var EReg = function(r,opt) {
	this.r = new RegExp(r,opt.split("u").join(""));
};
EReg.__name__ = "EReg";
EReg.prototype = {
	r: null
	,match: function(s) {
		if(this.r.global) {
			this.r.lastIndex = 0;
		}
		this.r.m = this.r.exec(s);
		this.r.s = s;
		return this.r.m != null;
	}
	,matched: function(n) {
		if(this.r.m != null && n >= 0 && n < this.r.m.length) {
			return this.r.m[n];
		} else {
			throw haxe_Exception.thrown("EReg::matched");
		}
	}
	,matchedLeft: function() {
		if(this.r.m == null) {
			throw haxe_Exception.thrown("No string matched");
		}
		return HxOverrides.substr(this.r.s,0,this.r.m.index);
	}
	,matchedRight: function() {
		if(this.r.m == null) {
			throw haxe_Exception.thrown("No string matched");
		}
		var sz = this.r.m.index + this.r.m[0].length;
		return HxOverrides.substr(this.r.s,sz,this.r.s.length - sz);
	}
	,matchedPos: function() {
		if(this.r.m == null) {
			throw haxe_Exception.thrown("No string matched");
		}
		return { pos : this.r.m.index, len : this.r.m[0].length};
	}
	,matchSub: function(s,pos,len) {
		if(len == null) {
			len = -1;
		}
		if(this.r.global) {
			this.r.lastIndex = pos;
			this.r.m = this.r.exec(len < 0 ? s : HxOverrides.substr(s,0,pos + len));
			var b = this.r.m != null;
			if(b) {
				this.r.s = s;
			}
			return b;
		} else {
			var b = this.match(len < 0 ? HxOverrides.substr(s,pos,null) : HxOverrides.substr(s,pos,len));
			if(b) {
				this.r.s = s;
				this.r.m.index += pos;
			}
			return b;
		}
	}
	,split: function(s) {
		var d = "#__delim__#";
		return s.replace(this.r,d).split(d);
	}
	,map: function(s,f) {
		var offset = 0;
		var buf_b = "";
		while(true) {
			if(offset >= s.length) {
				break;
			} else if(!this.matchSub(s,offset)) {
				buf_b += Std.string(HxOverrides.substr(s,offset,null));
				break;
			}
			var p = this.matchedPos();
			buf_b += Std.string(HxOverrides.substr(s,offset,p.pos - offset));
			buf_b += Std.string(f(this));
			if(p.len == 0) {
				buf_b += Std.string(HxOverrides.substr(s,p.pos,1));
				offset = p.pos + 1;
			} else {
				offset = p.pos + p.len;
			}
			if(!this.r.global) {
				break;
			}
		}
		if(!this.r.global && offset > 0 && offset < s.length) {
			buf_b += Std.string(HxOverrides.substr(s,offset,null));
		}
		return buf_b;
	}
	,__class__: EReg
};
var HxOverrides = function() { };
HxOverrides.__name__ = "HxOverrides";
HxOverrides.cca = function(s,index) {
	var x = s.charCodeAt(index);
	if(x != x) {
		return undefined;
	}
	return x;
};
HxOverrides.substr = function(s,pos,len) {
	if(len == null) {
		len = s.length;
	} else if(len < 0) {
		if(pos == 0) {
			len = s.length + len;
		} else {
			return "";
		}
	}
	return s.substr(pos,len);
};
HxOverrides.remove = function(a,obj) {
	var i = a.indexOf(obj);
	if(i == -1) {
		return false;
	}
	a.splice(i,1);
	return true;
};
HxOverrides.now = function() {
	return Date.now();
};
var Lambda = function() { };
Lambda.__name__ = "Lambda";
Lambda.array = function(it) {
	var a = [];
	var i = $getIterator(it);
	while(i.hasNext()) {
		var i1 = i.next();
		a.push(i1);
	}
	return a;
};
Lambda.has = function(it,elt) {
	var x = $getIterator(it);
	while(x.hasNext()) {
		var x1 = x.next();
		if(x1 == elt) {
			return true;
		}
	}
	return false;
};
var com_plantuml_api_v1_Plantuml = $hx_exports["com"]["plantuml"]["api"]["v1"]["Plantuml"] = function() {
	this.data = [];
	this.format = "svg";
};
com_plantuml_api_v1_Plantuml.__name__ = "com.plantuml.api.v1.Plantuml";
com_plantuml_api_v1_Plantuml.prototype = {
	format: null
	,data: null
	,addLineSingle: function(line) {
		if(line != "") {
			this.data[this.data.length] = line;
		}
	}
	,addLines: function(lines) {
		var _g = 0;
		var _g1 = lines.split("\n");
		while(_g < _g1.length) {
			var s = _g1[_g];
			++_g;
			this.addLineSingle(s);
		}
	}
	,addLinesArray: function(lines) {
		var _g = 0;
		while(_g < lines.length) {
			var s = lines[_g];
			++_g;
			this.addLineSingle(s);
		}
	}
	,toString: function() {
		return this.data.toString();
	}
	,setFormat: function(arg0) {
	}
	,setSvgLinkTarget: function(arg0) {
	}
	,setWatermark: function(arg0) {
	}
	,setScale: function(arg0) {
	}
	,setStyle: function(arg0) {
	}
	,compile: function() {
		var _g = 0;
		var _g1 = this.data;
		while(_g < _g1.length) {
			var s = _g1[_g];
			++_g;
			haxe_Log.trace(s,{ fileName : "src/com/plantuml/api/v1/Plantuml.hx", lineNumber : 46, className : "com.plantuml.api.v1.Plantuml", methodName : "compile"});
		}
	}
	,getSvg: function() {
		var factory = new com_plantuml_mindmap_MindMapDiagramFactory();
		var lines = new com_plantuml_command_BlocLines(this.data);
		var diagram = factory.createSystem(lines);
		var svg = com_plantuml_ugraphic_UGraphicSvg.create();
		diagram.exportDiagramNow(svg);
		var s = svg.getSvg();
		return s;
	}
	,__class__: com_plantuml_api_v1_Plantuml
};
var Plantuml = $hx_exports["Plantuml"] = function() {
	com_plantuml_api_v1_Plantuml.call(this);
};
Plantuml.__name__ = "Plantuml";
Plantuml.__super__ = com_plantuml_api_v1_Plantuml;
Plantuml.prototype = $extend(com_plantuml_api_v1_Plantuml.prototype,{
	__class__: Plantuml
});
var MainJs = function() { };
MainJs.__name__ = "MainJs";
MainJs.main = function() {
};
Math.__name__ = "Math";
var Reflect = function() { };
Reflect.__name__ = "Reflect";
Reflect.field = function(o,field) {
	try {
		return o[field];
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
		return null;
	}
};
Reflect.getProperty = function(o,field) {
	var tmp;
	if(o == null) {
		return null;
	} else {
		var tmp1;
		if(o.__properties__) {
			tmp = o.__properties__["get_" + field];
			tmp1 = tmp;
		} else {
			tmp1 = false;
		}
		if(tmp1) {
			return o[tmp]();
		} else {
			return o[field];
		}
	}
};
Reflect.fields = function(o) {
	var a = [];
	if(o != null) {
		var hasOwnProperty = Object.prototype.hasOwnProperty;
		for( var f in o ) {
		if(f != "__id__" && f != "hx__closures__" && hasOwnProperty.call(o,f)) {
			a.push(f);
		}
		}
	}
	return a;
};
Reflect.isFunction = function(f) {
	if(typeof(f) == "function") {
		return !(f.__name__ || f.__ename__);
	} else {
		return false;
	}
};
Reflect.compare = function(a,b) {
	if(a == b) {
		return 0;
	} else if(a > b) {
		return 1;
	} else {
		return -1;
	}
};
Reflect.compareMethods = function(f1,f2) {
	if(f1 == f2) {
		return true;
	}
	if(!Reflect.isFunction(f1) || !Reflect.isFunction(f2)) {
		return false;
	}
	if(f1.scope == f2.scope && f1.method == f2.method) {
		return f1.method != null;
	} else {
		return false;
	}
};
Reflect.isObject = function(v) {
	if(v == null) {
		return false;
	}
	var t = typeof(v);
	if(!(t == "string" || t == "object" && v.__enum__ == null)) {
		if(t == "function") {
			return (v.__name__ || v.__ename__) != null;
		} else {
			return false;
		}
	} else {
		return true;
	}
};
Reflect.isEnumValue = function(v) {
	if(v != null) {
		return v.__enum__ != null;
	} else {
		return false;
	}
};
var Std = function() { };
Std.__name__ = "Std";
Std.string = function(s) {
	return js_Boot.__string_rec(s,"");
};
Std.parseInt = function(x) {
	if(x != null) {
		var _g = 0;
		var _g1 = x.length;
		while(_g < _g1) {
			var i = _g++;
			var c = x.charCodeAt(i);
			if(c <= 8 || c >= 14 && c != 32 && c != 45) {
				var nc = x.charCodeAt(i + 1);
				var v = parseInt(x,nc == 120 || nc == 88 ? 16 : 10);
				if(isNaN(v)) {
					return null;
				} else {
					return v;
				}
			}
		}
	}
	return null;
};
var StringBuf = function() {
	this.b = "";
};
StringBuf.__name__ = "StringBuf";
StringBuf.prototype = {
	b: null
	,__class__: StringBuf
};
var StringTools = function() { };
StringTools.__name__ = "StringTools";
StringTools.htmlEscape = function(s,quotes) {
	var buf_b = "";
	var _g_offset = 0;
	var _g_s = s;
	while(_g_offset < _g_s.length) {
		var s = _g_s;
		var index = _g_offset++;
		var c = s.charCodeAt(index);
		if(c >= 55296 && c <= 56319) {
			c = c - 55232 << 10 | s.charCodeAt(index + 1) & 1023;
		}
		var c1 = c;
		if(c1 >= 65536) {
			++_g_offset;
		}
		var code = c1;
		switch(code) {
		case 34:
			if(quotes) {
				buf_b += "&quot;";
			} else {
				buf_b += String.fromCodePoint(code);
			}
			break;
		case 38:
			buf_b += "&amp;";
			break;
		case 39:
			if(quotes) {
				buf_b += "&#039;";
			} else {
				buf_b += String.fromCodePoint(code);
			}
			break;
		case 60:
			buf_b += "&lt;";
			break;
		case 62:
			buf_b += "&gt;";
			break;
		default:
			buf_b += String.fromCodePoint(code);
		}
	}
	return buf_b;
};
StringTools.startsWith = function(s,start) {
	if(s.length >= start.length) {
		return s.lastIndexOf(start,0) == 0;
	} else {
		return false;
	}
};
StringTools.endsWith = function(s,end) {
	var elen = end.length;
	var slen = s.length;
	if(slen >= elen) {
		return s.indexOf(end,slen - elen) == slen - elen;
	} else {
		return false;
	}
};
StringTools.isSpace = function(s,pos) {
	var c = HxOverrides.cca(s,pos);
	if(!(c > 8 && c < 14)) {
		return c == 32;
	} else {
		return true;
	}
};
StringTools.ltrim = function(s) {
	var l = s.length;
	var r = 0;
	while(r < l && StringTools.isSpace(s,r)) ++r;
	if(r > 0) {
		return HxOverrides.substr(s,r,l - r);
	} else {
		return s;
	}
};
StringTools.rtrim = function(s) {
	var l = s.length;
	var r = 0;
	while(r < l && StringTools.isSpace(s,l - r - 1)) ++r;
	if(r > 0) {
		return HxOverrides.substr(s,0,l - r);
	} else {
		return s;
	}
};
StringTools.trim = function(s) {
	return StringTools.ltrim(StringTools.rtrim(s));
};
StringTools.replace = function(s,sub,by) {
	return s.split(sub).join(by);
};
StringTools.hex = function(n,digits) {
	var s = "";
	var hexChars = "0123456789ABCDEF";
	while(true) {
		s = hexChars.charAt(n & 15) + s;
		n >>>= 4;
		if(!(n > 0)) {
			break;
		}
	}
	if(digits != null) {
		while(s.length < digits) s = "0" + s;
	}
	return s;
};
var ValueType = $hxEnums["ValueType"] = { __ename__:"ValueType",__constructs__:null
	,TNull: {_hx_name:"TNull",_hx_index:0,__enum__:"ValueType",toString:$estr}
	,TInt: {_hx_name:"TInt",_hx_index:1,__enum__:"ValueType",toString:$estr}
	,TFloat: {_hx_name:"TFloat",_hx_index:2,__enum__:"ValueType",toString:$estr}
	,TBool: {_hx_name:"TBool",_hx_index:3,__enum__:"ValueType",toString:$estr}
	,TObject: {_hx_name:"TObject",_hx_index:4,__enum__:"ValueType",toString:$estr}
	,TFunction: {_hx_name:"TFunction",_hx_index:5,__enum__:"ValueType",toString:$estr}
	,TClass: ($_=function(c) { return {_hx_index:6,c:c,__enum__:"ValueType",toString:$estr}; },$_._hx_name="TClass",$_.__params__ = ["c"],$_)
	,TEnum: ($_=function(e) { return {_hx_index:7,e:e,__enum__:"ValueType",toString:$estr}; },$_._hx_name="TEnum",$_.__params__ = ["e"],$_)
	,TUnknown: {_hx_name:"TUnknown",_hx_index:8,__enum__:"ValueType",toString:$estr}
};
ValueType.__constructs__ = [ValueType.TNull,ValueType.TInt,ValueType.TFloat,ValueType.TBool,ValueType.TObject,ValueType.TFunction,ValueType.TClass,ValueType.TEnum,ValueType.TUnknown];
var Type = function() { };
Type.__name__ = "Type";
Type.getEnum = function(o) {
	if(o == null) {
		return null;
	}
	return $hxEnums[o.__enum__];
};
Type.getInstanceFields = function(c) {
	var a = [];
	for(var i in c.prototype) a.push(i);
	HxOverrides.remove(a,"__class__");
	HxOverrides.remove(a,"__properties__");
	return a;
};
Type.typeof = function(v) {
	switch(typeof(v)) {
	case "boolean":
		return ValueType.TBool;
	case "function":
		if(v.__name__ || v.__ename__) {
			return ValueType.TObject;
		}
		return ValueType.TFunction;
	case "number":
		if(Math.ceil(v) == v % 2147483648.0) {
			return ValueType.TInt;
		}
		return ValueType.TFloat;
	case "object":
		if(v == null) {
			return ValueType.TNull;
		}
		var e = v.__enum__;
		if(e != null) {
			return ValueType.TEnum($hxEnums[e]);
		}
		var c = js_Boot.getClass(v);
		if(c != null) {
			return ValueType.TClass(c);
		}
		return ValueType.TObject;
	case "string":
		return ValueType.TClass(String);
	case "undefined":
		return ValueType.TNull;
	default:
		return ValueType.TUnknown;
	}
};
Type.enumParameters = function(e) {
	var enm = $hxEnums[e.__enum__];
	var params = enm.__constructs__[e._hx_index].__params__;
	if(params != null) {
		var _g = [];
		var _g1 = 0;
		while(_g1 < params.length) {
			var p = params[_g1];
			++_g1;
			_g.push(e[p]);
		}
		return _g;
	} else {
		return [];
	}
};
var XmlType = {};
XmlType.toString = function(this1) {
	switch(this1) {
	case 0:
		return "Element";
	case 1:
		return "PCData";
	case 2:
		return "CData";
	case 3:
		return "Comment";
	case 4:
		return "DocType";
	case 5:
		return "ProcessingInstruction";
	case 6:
		return "Document";
	}
};
var Xml = function(nodeType) {
	this.nodeType = nodeType;
	this.children = [];
	this.attributeMap = new haxe_ds_StringMap();
};
Xml.__name__ = "Xml";
Xml.createElement = function(name) {
	var xml = new Xml(Xml.Element);
	if(xml.nodeType != Xml.Element) {
		throw haxe_Exception.thrown("Bad node type, expected Element but found " + (xml.nodeType == null ? "null" : XmlType.toString(xml.nodeType)));
	}
	xml.nodeName = name;
	return xml;
};
Xml.createCData = function(data) {
	var xml = new Xml(Xml.CData);
	if(xml.nodeType == Xml.Document || xml.nodeType == Xml.Element) {
		throw haxe_Exception.thrown("Bad node type, unexpected " + (xml.nodeType == null ? "null" : XmlType.toString(xml.nodeType)));
	}
	xml.nodeValue = data;
	return xml;
};
Xml.prototype = {
	nodeType: null
	,nodeName: null
	,nodeValue: null
	,parent: null
	,children: null
	,attributeMap: null
	,get: function(att) {
		if(this.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element but found " + (this.nodeType == null ? "null" : XmlType.toString(this.nodeType)));
		}
		return this.attributeMap.h[att];
	}
	,set: function(att,value) {
		if(this.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element but found " + (this.nodeType == null ? "null" : XmlType.toString(this.nodeType)));
		}
		this.attributeMap.h[att] = value;
	}
	,attributes: function() {
		if(this.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element but found " + (this.nodeType == null ? "null" : XmlType.toString(this.nodeType)));
		}
		return new haxe_ds__$StringMap_StringMapKeyIterator(this.attributeMap.h);
	}
	,addChild: function(x) {
		if(this.nodeType != Xml.Document && this.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element or Document but found " + (this.nodeType == null ? "null" : XmlType.toString(this.nodeType)));
		}
		if(x.parent != null) {
			x.parent.removeChild(x);
		}
		this.children.push(x);
		x.parent = this;
	}
	,removeChild: function(x) {
		if(this.nodeType != Xml.Document && this.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element or Document but found " + (this.nodeType == null ? "null" : XmlType.toString(this.nodeType)));
		}
		if(HxOverrides.remove(this.children,x)) {
			x.parent = null;
			return true;
		}
		return false;
	}
	,toString: function() {
		return haxe_xml_Printer.print(this);
	}
	,__class__: Xml
};
var com_plantuml_Direction = $hxEnums["com.plantuml.Direction"] = { __ename__:"com.plantuml.Direction",__constructs__:null
	,RIGHT: {_hx_name:"RIGHT",_hx_index:0,__enum__:"com.plantuml.Direction",toString:$estr}
	,LEFT: {_hx_name:"LEFT",_hx_index:1,__enum__:"com.plantuml.Direction",toString:$estr}
	,DOWN: {_hx_name:"DOWN",_hx_index:2,__enum__:"com.plantuml.Direction",toString:$estr}
	,UP: {_hx_name:"UP",_hx_index:3,__enum__:"com.plantuml.Direction",toString:$estr}
};
com_plantuml_Direction.__constructs__ = [com_plantuml_Direction.RIGHT,com_plantuml_Direction.LEFT,com_plantuml_Direction.DOWN,com_plantuml_Direction.UP];
var com_plantuml_ISkinParam = function() { };
com_plantuml_ISkinParam.__name__ = "com.plantuml.ISkinParam";
com_plantuml_ISkinParam.__isInterface__ = true;
com_plantuml_ISkinParam.prototype = {
	getCurrentStyleBuilder: null
	,__class__: com_plantuml_ISkinParam
};
var com_plantuml_SkinParam = function() {
};
com_plantuml_SkinParam.__name__ = "com.plantuml.SkinParam";
com_plantuml_SkinParam.__interfaces__ = [com_plantuml_ISkinParam];
com_plantuml_SkinParam.prototype = {
	getCurrentStyleBuilder: function() {
		return new com_plantuml_style_StyleBuilder();
	}
	,__class__: com_plantuml_SkinParam
};
var com_plantuml_awt_geom_Dimension2D = function(width,height) {
	this.width = width;
	this.height = height;
};
com_plantuml_awt_geom_Dimension2D.__name__ = "com.plantuml.awt.geom.Dimension2D";
com_plantuml_awt_geom_Dimension2D.prototype = {
	width: null
	,height: null
	,getHeight: function() {
		return this.height;
	}
	,getWidth: function() {
		return this.width;
	}
	,toString: function() {
		return "" + this.width + " x " + this.height;
	}
	,delta: function(deltaWidth,deltaHeight) {
		return new com_plantuml_awt_geom_Dimension2D(this.width + deltaWidth,this.height + deltaHeight);
	}
	,__class__: com_plantuml_awt_geom_Dimension2D
};
var com_plantuml_awt_geom_Line2D = function(x1,y1,x2,y2) {
	this.x1 = x1;
	this.y1 = y1;
	this.x2 = x2;
	this.y2 = y2;
};
com_plantuml_awt_geom_Line2D.__name__ = "com.plantuml.awt.geom.Line2D";
com_plantuml_awt_geom_Line2D.prototype = {
	x1: null
	,y1: null
	,x2: null
	,y2: null
	,getX1: function() {
		return this.x1;
	}
	,getY1: function() {
		return this.y1;
	}
	,getX2: function() {
		return this.x2;
	}
	,getY2: function() {
		return this.y2;
	}
	,__class__: com_plantuml_awt_geom_Line2D
};
var com_plantuml_awt_geom_Point2D = function(x,y) {
	this.x = x;
	this.y = y;
};
com_plantuml_awt_geom_Point2D.__name__ = "com.plantuml.awt.geom.Point2D";
com_plantuml_awt_geom_Point2D.prototype = {
	x: null
	,y: null
	,getX: function() {
		return this.x;
	}
	,getY: function() {
		return this.y;
	}
	,asTranslate: function() {
		return new com_plantuml_ugraphic_UTranslate(this.x,this.y);
	}
	,__class__: com_plantuml_awt_geom_Point2D
};
var com_plantuml_command_BlocLines = function(lines) {
	this.lines = lines.slice();
};
com_plantuml_command_BlocLines.__name__ = "com.plantuml.command.BlocLines";
com_plantuml_command_BlocLines.single = function(s) {
	return new com_plantuml_command_BlocLines([s]);
};
com_plantuml_command_BlocLines.prototype = {
	lines: null
	,getLines: function() {
		return this.lines;
	}
	,toString: function() {
		return this.lines.toString();
	}
	,size: function() {
		return this.lines.length;
	}
	,__class__: com_plantuml_command_BlocLines
};
var com_plantuml_command_Command = function() { };
com_plantuml_command_Command.__name__ = "com.plantuml.command.Command";
com_plantuml_command_Command.__isInterface__ = true;
com_plantuml_command_Command.prototype = {
	isValid: null
	,execute: null
	,__class__: com_plantuml_command_Command
};
var com_plantuml_command_CommandControl = $hxEnums["com.plantuml.command.CommandControl"] = { __ename__:"com.plantuml.command.CommandControl",__constructs__:null
	,OK: {_hx_name:"OK",_hx_index:0,__enum__:"com.plantuml.command.CommandControl",toString:$estr}
	,NOT_OK: {_hx_name:"NOT_OK",_hx_index:1,__enum__:"com.plantuml.command.CommandControl",toString:$estr}
	,OK_PARTIAL: {_hx_name:"OK_PARTIAL",_hx_index:2,__enum__:"com.plantuml.command.CommandControl",toString:$estr}
};
com_plantuml_command_CommandControl.__constructs__ = [com_plantuml_command_CommandControl.OK,com_plantuml_command_CommandControl.NOT_OK,com_plantuml_command_CommandControl.OK_PARTIAL];
var com_plantuml_command_CommandExecutionResult = $hxEnums["com.plantuml.command.CommandExecutionResult"] = { __ename__:"com.plantuml.command.CommandExecutionResult",__constructs__:null
	,OK: {_hx_name:"OK",_hx_index:0,__enum__:"com.plantuml.command.CommandExecutionResult",toString:$estr}
	,ERROR: ($_=function(msg) { return {_hx_index:1,msg:msg,__enum__:"com.plantuml.command.CommandExecutionResult",toString:$estr}; },$_._hx_name="ERROR",$_.__params__ = ["msg"],$_)
};
com_plantuml_command_CommandExecutionResult.__constructs__ = [com_plantuml_command_CommandExecutionResult.OK,com_plantuml_command_CommandExecutionResult.ERROR];
var com_plantuml_command_SingleLineCommand = function() { };
com_plantuml_command_SingleLineCommand.__name__ = "com.plantuml.command.SingleLineCommand";
com_plantuml_command_SingleLineCommand.__interfaces__ = [com_plantuml_command_Command];
com_plantuml_command_SingleLineCommand.prototype = {
	regex: null
	,_init: function(array) {
		this.regex = new com_plantuml_command_regex_RegexConcat(array);
	}
	,getPattern: function() {
		return this.regex.getPattern();
	}
	,isValid: function(lines) {
		if(lines.size() != 1) {
			return com_plantuml_command_CommandControl.NOT_OK;
		}
		var s = lines.getLines()[0];
		if(this.regex.match(s)) {
			return com_plantuml_command_CommandControl.OK;
		}
		return com_plantuml_command_CommandControl.NOT_OK;
	}
	,execute: function(diagram,lines) {
		var map = this.regex.matcher(lines.getLines()[0]);
		return this.executeArg(diagram,lines,map);
	}
	,executeArg: null
	,__class__: com_plantuml_command_SingleLineCommand
};
var com_plantuml_command_regex_IRegex = function() { };
com_plantuml_command_regex_IRegex.__name__ = "com.plantuml.command.regex.IRegex";
com_plantuml_command_regex_IRegex.__isInterface__ = true;
com_plantuml_command_regex_IRegex.prototype = {
	getSize: null
	,getPattern: null
	,match: null
	,eat: null
	,__class__: com_plantuml_command_regex_IRegex
};
var com_plantuml_command_regex_AbstractRegex = function() { };
com_plantuml_command_regex_AbstractRegex.__name__ = "com.plantuml.command.regex.AbstractRegex";
com_plantuml_command_regex_AbstractRegex.__interfaces__ = [com_plantuml_command_regex_IRegex];
com_plantuml_command_regex_AbstractRegex.prototype = {
	getSize: null
	,eat: null
	,pattern: null
	,getPattern: function() {
		return this.pattern;
	}
	,match: function(full) {
		var r = new EReg(this.pattern,"i");
		return r.match(full);
	}
	,matchArray: function(full) {
		var r = new EReg(this.pattern,"i");
		if(r.match(full) == false) {
			return null;
		}
		var result = [];
		var i = 1;
		try {
			while(true) {
				result.push(r.matched(i));
				++i;
			}
		} catch( _g ) {
			return result;
		}
	}
	,__class__: com_plantuml_command_regex_AbstractRegex
};
var com_plantuml_command_regex_MyPattern = function() { };
com_plantuml_command_regex_MyPattern.__name__ = "com.plantuml.command.regex.MyPattern";
com_plantuml_command_regex_MyPattern.transform = function(p) {
	p = StringTools.replace(p,"%s","\\s ");
	return p;
};
var com_plantuml_command_regex_RegexConcat = function(all) {
	this.all = all;
	var tmp = "";
	var _g = 0;
	while(_g < all.length) {
		var r = all[_g];
		++_g;
		tmp += r.getPattern();
	}
	this.pattern = tmp;
};
com_plantuml_command_regex_RegexConcat.__name__ = "com.plantuml.command.regex.RegexConcat";
com_plantuml_command_regex_RegexConcat.__interfaces__ = [com_plantuml_command_regex_IRegex];
com_plantuml_command_regex_RegexConcat.__super__ = com_plantuml_command_regex_AbstractRegex;
com_plantuml_command_regex_RegexConcat.prototype = $extend(com_plantuml_command_regex_AbstractRegex.prototype,{
	all: null
	,getSize: function() {
		var size = 0;
		var _g = 0;
		var _g1 = this.all;
		while(_g < _g1.length) {
			var r = _g1[_g];
			++_g;
			size += r.getSize();
		}
		return size;
	}
	,matcher: function(full) {
		var array = this.matchArray(full);
		array.reverse();
		var map = new haxe_ds_StringMap();
		this.eat(array,map);
		return map;
	}
	,eat: function(array,map) {
		var _g = 0;
		var _g1 = this.all;
		while(_g < _g1.length) {
			var r = _g1[_g];
			++_g;
			r.eat(array,map);
		}
	}
	,__class__: com_plantuml_command_regex_RegexConcat
});
var com_plantuml_command_regex_RegexLeaf = function(size,pattern,name) {
	this.name = name;
	this.pattern = com_plantuml_command_regex_MyPattern.transform(pattern);
	this.size = size;
};
com_plantuml_command_regex_RegexLeaf.__name__ = "com.plantuml.command.regex.RegexLeaf";
com_plantuml_command_regex_RegexLeaf.__interfaces__ = [com_plantuml_command_regex_IRegex];
com_plantuml_command_regex_RegexLeaf.start = function() {
	return new com_plantuml_command_regex_RegexLeaf(0,"^");
};
com_plantuml_command_regex_RegexLeaf.end = function() {
	return new com_plantuml_command_regex_RegexLeaf(0,"$");
};
com_plantuml_command_regex_RegexLeaf.spaceZeroOrMore = function() {
	return new com_plantuml_command_regex_RegexLeaf(0,"[%s]*");
};
com_plantuml_command_regex_RegexLeaf.spaceOneOrMore = function() {
	return new com_plantuml_command_regex_RegexLeaf(0,"[%s]+");
};
com_plantuml_command_regex_RegexLeaf.__super__ = com_plantuml_command_regex_AbstractRegex;
com_plantuml_command_regex_RegexLeaf.prototype = $extend(com_plantuml_command_regex_AbstractRegex.prototype,{
	name: null
	,size: null
	,getSize: function() {
		return this.size;
	}
	,toString: function() {
		return this.name + "=" + this.pattern;
	}
	,eat: function(array,map) {
		if(this.size == 1) {
			var s = array.pop();
			map.h[this.name] = s;
		} else {
			var _g = 0;
			var _g1 = this.size;
			while(_g < _g1) {
				var i = _g++;
				var s = array.pop();
				map.h[this.name + i] = s;
			}
		}
	}
	,__class__: com_plantuml_command_regex_RegexLeaf
});
var com_plantuml_command_regex_RegexOptional = function(orig) {
	this.orig = orig;
	this.pattern = "(?:" + orig.getPattern() + ")?";
};
com_plantuml_command_regex_RegexOptional.__name__ = "com.plantuml.command.regex.RegexOptional";
com_plantuml_command_regex_RegexOptional.__interfaces__ = [com_plantuml_command_regex_IRegex];
com_plantuml_command_regex_RegexOptional.__super__ = com_plantuml_command_regex_AbstractRegex;
com_plantuml_command_regex_RegexOptional.prototype = $extend(com_plantuml_command_regex_AbstractRegex.prototype,{
	orig: null
	,getSize: function() {
		return this.orig.getSize();
	}
	,eat: function(array,map) {
		var s = array[0];
		if(s == null) {
			array.pop();
		}
		this.orig.eat(array,map);
	}
	,__class__: com_plantuml_command_regex_RegexOptional
});
var com_plantuml_core_Diagram = function() { };
com_plantuml_core_Diagram.__name__ = "com.plantuml.core.Diagram";
com_plantuml_core_Diagram.prototype = {
	exportDiagramNow: null
	,__class__: com_plantuml_core_Diagram
};
var com_plantuml_cucadiagram_Display = function(label) {
	this.label = label;
};
com_plantuml_cucadiagram_Display.__name__ = "com.plantuml.cucadiagram.Display";
com_plantuml_cucadiagram_Display.getWithNewlines = function(label) {
	return new com_plantuml_cucadiagram_Display(label);
};
com_plantuml_cucadiagram_Display.prototype = {
	label: null
	,getEndingStereotype: function() {
		return null;
	}
	,removeEndingStereotype: function() {
		return this;
	}
	,get: function(i) {
		return this.label;
	}
	,toString: function() {
		return this.label;
	}
	,__class__: com_plantuml_cucadiagram_Display
};
var com_plantuml_graphic_StringBounder = function() { };
com_plantuml_graphic_StringBounder.__name__ = "com.plantuml.graphic.StringBounder";
com_plantuml_graphic_StringBounder.__isInterface__ = true;
com_plantuml_graphic_StringBounder.prototype = {
	calculateDimension: null
	,__class__: com_plantuml_graphic_StringBounder
};
var com_plantuml_ugraphic_UShape = function() { };
com_plantuml_ugraphic_UShape.__name__ = "com.plantuml.ugraphic.UShape";
com_plantuml_ugraphic_UShape.__isInterface__ = true;
var com_plantuml_graphic_UDrawable = function() { };
com_plantuml_graphic_UDrawable.__name__ = "com.plantuml.graphic.UDrawable";
com_plantuml_graphic_UDrawable.__isInterface__ = true;
com_plantuml_graphic_UDrawable.prototype = {
	drawU: null
	,__class__: com_plantuml_graphic_UDrawable
};
var com_plantuml_graphic_TextBlock = function() { };
com_plantuml_graphic_TextBlock.__name__ = "com.plantuml.graphic.TextBlock";
com_plantuml_graphic_TextBlock.__isInterface__ = true;
com_plantuml_graphic_TextBlock.__interfaces__ = [com_plantuml_ugraphic_UShape,com_plantuml_graphic_UDrawable];
com_plantuml_graphic_TextBlock.prototype = {
	calculateDimension: null
	,__class__: com_plantuml_graphic_TextBlock
};
var com_plantuml_graphic_TextBlockMarged = function(textBlock,top,right,bottom,left) {
	this.textBlock = textBlock;
	this.top = top;
	this.right = right;
	this.bottom = bottom;
	this.left = left;
};
com_plantuml_graphic_TextBlockMarged.__name__ = "com.plantuml.graphic.TextBlockMarged";
com_plantuml_graphic_TextBlockMarged.__interfaces__ = [com_plantuml_graphic_TextBlock];
com_plantuml_graphic_TextBlockMarged.prototype = {
	textBlock: null
	,top: null
	,right: null
	,bottom: null
	,left: null
	,drawU: function(ug) {
		var translate = new com_plantuml_ugraphic_UTranslate(this.left,this.top);
		this.textBlock.drawU(ug.apply(translate));
	}
	,calculateDimension: function(stringBounder) {
		var dim = this.textBlock.calculateDimension(stringBounder);
		return dim.delta(this.left + this.right,this.top + this.bottom);
	}
	,__class__: com_plantuml_graphic_TextBlockMarged
};
var com_plantuml_mindmap_Branch = function() {
};
com_plantuml_mindmap_Branch.__name__ = "com.plantuml.mindmap.Branch";
com_plantuml_mindmap_Branch.__interfaces__ = [com_plantuml_graphic_UDrawable];
com_plantuml_mindmap_Branch.prototype = {
	root: null
	,last: null
	,finger: null
	,hasRoot: function() {
		return this.root != null;
	}
	,initRoot: function(styleBuilder,backColor,label,shape,stereotype) {
		this.root = com_plantuml_mindmap_Idea.createIdeaSimple(styleBuilder,backColor,label,shape,stereotype);
		this.last = this.root;
	}
	,add: function(styleBuilder,backColor,level,label,shape,stereotype) {
		if(this.last == null) {
			return com_plantuml_command_CommandExecutionResult.ERROR("Check your indentation ?");
		}
		if(level == this.last.getLevel() + 1) {
			var newIdea = this.last.createIdea(styleBuilder,backColor,level,label,shape,stereotype);
			this.last = newIdea;
			return com_plantuml_command_CommandExecutionResult.OK;
		}
		if(level <= this.last.getLevel()) {
			var diff = this.last.getLevel() - level + 1;
			var newIdea = this.getParentOfLast(diff).createIdea(styleBuilder,backColor,level,label,shape,stereotype);
			this.last = newIdea;
			return com_plantuml_command_CommandExecutionResult.OK;
		}
		return com_plantuml_command_CommandExecutionResult.ERROR("error42L");
	}
	,getParentOfLast: function(nb) {
		var result = this.last;
		var _g = 0;
		var _g1 = nb;
		while(_g < _g1) {
			var i = _g++;
			result = result.getParent();
		}
		return result;
	}
	,hasFinger: function() {
		return this.finger != null;
	}
	,hasChildren: function() {
		return this.root.hasChildren();
	}
	,initFinger: function(skinParam,direction) {
		this.finger = com_plantuml_mindmap_FingerImpl.build(this.root,skinParam,direction);
	}
	,doNotDrawFirstPhalanx: function() {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/Branch.hx", lineNumber : 66, className : "com.plantuml.mindmap.Branch", methodName : "doNotDrawFirstPhalanx"});
	}
	,drawU: function(ug) {
		if(this.finger != null) {
			this.finger.drawU(ug);
		}
	}
	,getHalfThickness: function(stringBounder) {
		if(this.finger == null) {
			return 0;
		}
		return this.finger.getFullThickness(stringBounder) / 2;
	}
	,getFullElongation: function(stringBounder) {
		if(this.finger == null) {
			return 0;
		}
		return this.finger.getFullElongation(stringBounder);
	}
	,getX12: function(stringBounder) {
		if(this.finger == null) {
			return 0;
		}
		return this.finger.getFullElongation(stringBounder) + (js_Boot.__cast(this.finger , com_plantuml_mindmap_FingerImpl)).getX12();
	}
	,__class__: com_plantuml_mindmap_Branch
};
var com_plantuml_mindmap_CommandMindMapDirection = function() {
	this._init([com_plantuml_command_regex_RegexLeaf.start(),new com_plantuml_command_regex_RegexLeaf(0,"[^*]*"),new com_plantuml_command_regex_RegexLeaf(0,"\\b"),new com_plantuml_command_regex_RegexLeaf(1,"(left|right)","DIRECTION"),new com_plantuml_command_regex_RegexLeaf(0,"\\b"),new com_plantuml_command_regex_RegexLeaf(0,"[^*]*"),com_plantuml_command_regex_RegexLeaf.end()]);
};
com_plantuml_mindmap_CommandMindMapDirection.__name__ = "com.plantuml.mindmap.CommandMindMapDirection";
com_plantuml_mindmap_CommandMindMapDirection.__super__ = com_plantuml_command_SingleLineCommand;
com_plantuml_mindmap_CommandMindMapDirection.prototype = $extend(com_plantuml_command_SingleLineCommand.prototype,{
	executeArg: function(diagram,lines,map) {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/CommandMindMapDirection.hx", lineNumber : 21, className : "com.plantuml.mindmap.CommandMindMapDirection", methodName : "executeArg"});
	}
	,__class__: com_plantuml_mindmap_CommandMindMapDirection
});
var com_plantuml_mindmap_CommandMindMapOrgmode = function() {
	this._init([com_plantuml_command_regex_RegexLeaf.start(),new com_plantuml_command_regex_RegexLeaf(1,"([ \t]*[*]+)","TYPE"),new com_plantuml_command_regex_RegexOptional(new com_plantuml_command_regex_RegexLeaf(1,"\\[(#\\w+)\\]","BACKCOLOR")),new com_plantuml_command_regex_RegexLeaf(1,"(_)?","SHAPE"),com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(),new com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"),com_plantuml_command_regex_RegexLeaf.end()]);
};
com_plantuml_mindmap_CommandMindMapOrgmode.__name__ = "com.plantuml.mindmap.CommandMindMapOrgmode";
com_plantuml_mindmap_CommandMindMapOrgmode.__super__ = com_plantuml_command_SingleLineCommand;
com_plantuml_mindmap_CommandMindMapOrgmode.prototype = $extend(com_plantuml_command_SingleLineCommand.prototype,{
	executeArg: function(diagram_,lines,arg) {
		var diagram = js_Boot.__cast(diagram_ , com_plantuml_mindmap_MindMapDiagram);
		var type = arg.h["TYPE"];
		var label = arg.h["LABEL"];
		var stringColor = arg.h["BACKCOLOR"];
		var backColor = null;
		var shape = com_plantuml_mindmap_IdeaShapeUtils.fromDesc(arg.h["SHAPE"]);
		return diagram.addIdea(backColor,diagram.getSmartLevel(type),com_plantuml_cucadiagram_Display.getWithNewlines(label),shape);
	}
	,__class__: com_plantuml_mindmap_CommandMindMapOrgmode
});
var com_plantuml_mindmap_CommandMindMapPlus = function() {
	this._init([com_plantuml_command_regex_RegexLeaf.start(),new com_plantuml_command_regex_RegexLeaf(1,"([+-]+)","TYPE"),new com_plantuml_command_regex_RegexOptional(new com_plantuml_command_regex_RegexLeaf(1,"\\[(#\\w+)\\]","BACKCOLOR")),new com_plantuml_command_regex_RegexLeaf(1,"(_)?","SHAPE"),com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(),new com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"),com_plantuml_command_regex_RegexLeaf.end()]);
};
com_plantuml_mindmap_CommandMindMapPlus.__name__ = "com.plantuml.mindmap.CommandMindMapPlus";
com_plantuml_mindmap_CommandMindMapPlus.__super__ = com_plantuml_command_SingleLineCommand;
com_plantuml_mindmap_CommandMindMapPlus.prototype = $extend(com_plantuml_command_SingleLineCommand.prototype,{
	executeArg: function(diagram,lines,map) {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/CommandMindMapPlus.hx", lineNumber : 21, className : "com.plantuml.mindmap.CommandMindMapPlus", methodName : "executeArg"});
	}
	,__class__: com_plantuml_mindmap_CommandMindMapPlus
});
var com_plantuml_mindmap_CommandMindMapRoot = function() {
	this._init([com_plantuml_command_regex_RegexLeaf.start(),new com_plantuml_command_regex_RegexLeaf(1,"(0)","TYPE"),com_plantuml_command_regex_RegexLeaf.spaceOneOrMore(),new com_plantuml_command_regex_RegexLeaf(1,"([^%s].*)","LABEL"),com_plantuml_command_regex_RegexLeaf.end()]);
};
com_plantuml_mindmap_CommandMindMapRoot.__name__ = "com.plantuml.mindmap.CommandMindMapRoot";
com_plantuml_mindmap_CommandMindMapRoot.__super__ = com_plantuml_command_SingleLineCommand;
com_plantuml_mindmap_CommandMindMapRoot.prototype = $extend(com_plantuml_command_SingleLineCommand.prototype,{
	executeArg: function(diagram,lines,map) {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/CommandMindMapRoot.hx", lineNumber : 19, className : "com.plantuml.mindmap.CommandMindMapRoot", methodName : "executeArg"});
	}
	,__class__: com_plantuml_mindmap_CommandMindMapRoot
});
var com_plantuml_mindmap_Finger = function() { };
com_plantuml_mindmap_Finger.__name__ = "com.plantuml.mindmap.Finger";
com_plantuml_mindmap_Finger.__isInterface__ = true;
com_plantuml_mindmap_Finger.__interfaces__ = [com_plantuml_graphic_UDrawable];
com_plantuml_mindmap_Finger.prototype = {
	getPhalanxThickness: null
	,getNailThickness: null
	,getFullThickness: null
	,getPhalanxElongation: null
	,getNailElongation: null
	,getFullElongation: null
	,doNotDrawFirstPhalanx: null
	,__class__: com_plantuml_mindmap_Finger
};
var com_plantuml_mindmap_FingerImpl = function(styleBuilder,backColor,label,skinParam,shape,direction,level,stereotype) {
	this.nail = [];
	this.marginBottom = 10.0;
	this.marginTop = 10.0;
	this.marginRight = 10.0;
	this.marginLeft = 10.0;
	this.drawPhalanx = true;
	this.backColor = backColor;
	this.stereotype = stereotype;
	this.level = level;
	this.label = label;
	this.skinParam = skinParam;
	this.styleBuilder = styleBuilder;
	this.shape = shape;
	this.direction = direction;
};
com_plantuml_mindmap_FingerImpl.__name__ = "com.plantuml.mindmap.FingerImpl";
com_plantuml_mindmap_FingerImpl.__interfaces__ = [com_plantuml_graphic_UDrawable,com_plantuml_mindmap_Finger];
com_plantuml_mindmap_FingerImpl.build = function(idea,skinParam,direction) {
	var result = new com_plantuml_mindmap_FingerImpl(idea.getStyleBuilder(),idea.getBackColor(),idea.getLabel(),skinParam,idea.getShape(),direction,idea.getLevel(),idea.getStereotype());
	var _g = 0;
	var _g1 = idea.getChildren();
	while(_g < _g1.length) {
		var child = _g1[_g];
		++_g;
		result.addInNail(com_plantuml_mindmap_FingerImpl.build(child,skinParam,direction));
	}
	return result;
};
com_plantuml_mindmap_FingerImpl.prototype = {
	label: null
	,backColor: null
	,stereotype: null
	,skinParam: null
	,styleBuilder: null
	,shape: null
	,direction: null
	,level: null
	,drawPhalanx: null
	,marginLeft: null
	,marginRight: null
	,marginTop: null
	,marginBottom: null
	,nail: null
	,tetris: null
	,drawU: function(ug) {
		var stringBounder = ug.getStringBounder();
		var phalanx = this.getPhalanx();
		var dimPhalanx = phalanx.calculateDimension(stringBounder);
		if(this.drawPhalanx) {
			var posY = -this.getPhalanxThickness(stringBounder) / 2;
			var posX = this.direction == com_plantuml_Direction.RIGHT ? 0 : -dimPhalanx.getWidth();
			phalanx.drawU(ug.apply(new com_plantuml_ugraphic_UTranslate(posX,posY)));
		}
		var p1 = new com_plantuml_awt_geom_Point2D(this.direction == com_plantuml_Direction.RIGHT ? dimPhalanx.getWidth() : -dimPhalanx.getWidth(),0);
		var _g = 0;
		var _g1 = this.nail.length;
		while(_g < _g1) {
			var i = _g++;
			var child = this.nail[i];
			var stp = this.getTetris(stringBounder).getElements()[i];
			var x = this.direction == com_plantuml_Direction.RIGHT ? dimPhalanx.getWidth() + this.getX12() : -dimPhalanx.getWidth() - this.getX12();
			var p2 = new com_plantuml_awt_geom_Point2D(x,stp.getY());
			child.drawU(ug.apply(p2.asTranslate()));
			this.drawLine(ug,p1,p2);
		}
	}
	,getPhalanxThickness: function(stringBounder) {
		return this.getPhalanx().calculateDimension(stringBounder).getHeight();
	}
	,getNailThickness: function(stringBounder) {
		return this.getTetris(stringBounder).getHeight();
	}
	,getFullThickness: function(stringBounder) {
		var thickness1 = this.getPhalanxThickness(stringBounder);
		var thickness2 = this.getNailThickness(stringBounder);
		return Math.max(thickness1,thickness2);
	}
	,getPhalanxElongation: function(stringBounder) {
		return this.getPhalanx().calculateDimension(stringBounder).getWidth();
	}
	,getNailElongation: function(stringBounder) {
		return this.getTetris(stringBounder).getWidth();
	}
	,getFullElongation: function(stringBounder) {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/FingerImpl.hx", lineNumber : 80, className : "com.plantuml.mindmap.FingerImpl", methodName : "getFullElongation"});
	}
	,doNotDrawFirstPhalanx: function() {
	}
	,getX12: function() {
		return this.getX1() + this.getX2();
	}
	,addInNail: function(child) {
		this.nail.push(child);
	}
	,getPhalanx: function() {
		if(this.drawPhalanx == false) {
			return com_plantuml_ugraphic_TextBlockUtils.empty(0,0);
		}
		if(this.shape == com_plantuml_mindmap_IdeaShape.BOX) {
			var box = com_plantuml_mindmap_FtileBoxOld.createMindMap(this.styleBuilder,this.label);
			return com_plantuml_ugraphic_TextBlockUtils.withMargin(box,0,0,this.marginTop,this.marginBottom);
		}
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/FingerImpl.hx", lineNumber : 121, className : "com.plantuml.mindmap.FingerImpl", methodName : "getPhalanx"});
	}
	,getTetris: function(stringBounder) {
		if(this.tetris == null) {
			this.tetris = new com_plantuml_mindmap_Tetris(this.label.get(0));
			var _g = 0;
			var _g1 = this.nail;
			while(_g < _g1.length) {
				var child = _g1[_g];
				++_g;
				this.tetris.add(child.asSymetricalTee(stringBounder));
			}
			this.tetris.balance();
		}
		return this.tetris;
	}
	,asSymetricalTee: function(stringBounder) {
		var thickness1 = this.getPhalanxThickness(stringBounder);
		var elongation1 = this.getPhalanxElongation(stringBounder);
		if(this.nail.length == 0) {
			return new com_plantuml_mindmap_SymetricalTee(thickness1,elongation1,0,0);
		}
		var thickness2 = this.getNailThickness(stringBounder);
		var elongation2 = this.getNailElongation(stringBounder);
		return new com_plantuml_mindmap_SymetricalTee(thickness1,elongation1 + this.getX1(),thickness2,this.getX2() + elongation2);
	}
	,getX1: function() {
		return this.marginLeft;
	}
	,getX2: function() {
		return this.marginRight + 30;
	}
	,drawLine: function(ug,p1,p2) {
		var path = new com_plantuml_ugraphic_UPath();
		var delta1 = this.direction == com_plantuml_Direction.RIGHT ? 10 : -10;
		var delta2 = this.direction == com_plantuml_Direction.RIGHT ? 25 : -25;
		path.moveToPoint(p1);
		path.lineTo(p1.getX() + delta1,p1.getY());
		path.cubicTo(p1.getX() + delta2,p1.getY(),p2.getX() - delta2,p2.getY(),p2.getX() - delta1,p2.getY());
		path.lineToPoint(p2);
		ug.draw(path);
	}
	,__class__: com_plantuml_mindmap_FingerImpl
};
var com_plantuml_mindmap_FtileBoxOld = function(label) {
	this.label = label;
	this.padding = com_plantuml_style_ClockwiseTopRightBottomLeft.same(10);
};
com_plantuml_mindmap_FtileBoxOld.__name__ = "com.plantuml.mindmap.FtileBoxOld";
com_plantuml_mindmap_FtileBoxOld.__interfaces__ = [com_plantuml_graphic_TextBlock];
com_plantuml_mindmap_FtileBoxOld.createMindMap = function(styleBuilder,label) {
	return new com_plantuml_mindmap_FtileBoxOld(label);
};
com_plantuml_mindmap_FtileBoxOld.prototype = {
	padding: null
	,label: null
	,drawU: function(ug) {
		var dim2 = this.calculateDimension(ug.getStringBounder());
		ug.draw(new com_plantuml_ugraphic_URectangle(dim2.getWidth(),dim2.getHeight()));
		ug = ug.apply(new com_plantuml_ugraphic_UTranslate(this.padding.getLeft(),this.padding.getTop()));
		var dim = this.getDimRaw(ug.getStringBounder());
		ug.draw(new com_plantuml_ugraphic_UText(this.label.get(0)));
	}
	,getDimRaw: function(stringBounder) {
		return stringBounder.calculateDimension(new com_plantuml_ugraphic_UFont(),this.label.get(0));
	}
	,calculateDimension: function(stringBounder) {
		var dimRaw = this.getDimRaw(stringBounder);
		dimRaw = dimRaw.delta(this.padding.getLeft() + this.padding.getRight(),this.padding.getBottom() + this.padding.getTop());
		return dimRaw;
	}
	,__class__: com_plantuml_mindmap_FtileBoxOld
};
var com_plantuml_mindmap_Idea = function(styleBuilder,backColor,level,parent,label,shape,stereotype) {
	this.children = [];
	this.backColor = backColor;
	this.styleBuilder = styleBuilder;
	this.label = label;
	this.level = level;
	this.parent = parent;
	this.shape = shape;
	this.stereotype = stereotype;
};
com_plantuml_mindmap_Idea.__name__ = "com.plantuml.mindmap.Idea";
com_plantuml_mindmap_Idea.createIdeaSimple = function(styleBuilder,backColor,label,shape,stereotype) {
	return new com_plantuml_mindmap_Idea(styleBuilder,backColor,0,null,label,shape,stereotype);
};
com_plantuml_mindmap_Idea.prototype = {
	label: null
	,level: null
	,parent: null
	,children: null
	,shape: null
	,backColor: null
	,styleBuilder: null
	,stereotype: null
	,getLevel: function() {
		return this.level;
	}
	,createIdea: function(styleBuilder,backColor,newLevel,newDisplay,newShape,stereotype) {
		var result = new com_plantuml_mindmap_Idea(styleBuilder,backColor,newLevel,this,newDisplay,newShape,stereotype);
		this.children.push(result);
		return result;
	}
	,getParent: function() {
		return this.parent;
	}
	,hasChildren: function() {
		return this.children.length > 0;
	}
	,getStyleBuilder: function() {
		return this.styleBuilder;
	}
	,getBackColor: function() {
		return this.backColor;
	}
	,getLabel: function() {
		return this.label;
	}
	,getShape: function() {
		return this.shape;
	}
	,getStereotype: function() {
		return this.stereotype;
	}
	,getChildren: function() {
		return this.children;
	}
	,__class__: com_plantuml_mindmap_Idea
};
var com_plantuml_mindmap_IdeaShape = $hxEnums["com.plantuml.mindmap.IdeaShape"] = { __ename__:"com.plantuml.mindmap.IdeaShape",__constructs__:null
	,BOX: {_hx_name:"BOX",_hx_index:0,__enum__:"com.plantuml.mindmap.IdeaShape",toString:$estr}
	,NONE: {_hx_name:"NONE",_hx_index:1,__enum__:"com.plantuml.mindmap.IdeaShape",toString:$estr}
};
com_plantuml_mindmap_IdeaShape.__constructs__ = [com_plantuml_mindmap_IdeaShape.BOX,com_plantuml_mindmap_IdeaShape.NONE];
var com_plantuml_mindmap_IdeaShapeUtils = function() { };
com_plantuml_mindmap_IdeaShapeUtils.__name__ = "com.plantuml.mindmap.IdeaShapeUtils";
com_plantuml_mindmap_IdeaShapeUtils.fromDesc = function(s) {
	if("_" == s) {
		return com_plantuml_mindmap_IdeaShape.NONE;
	}
	return com_plantuml_mindmap_IdeaShape.BOX;
};
var com_plantuml_mindmap_MindMap = function(skinParam) {
	this.right = new com_plantuml_mindmap_Branch();
	this.left = new com_plantuml_mindmap_Branch();
	this.skinParam = skinParam;
};
com_plantuml_mindmap_MindMap.__name__ = "com.plantuml.mindmap.MindMap";
com_plantuml_mindmap_MindMap.prototype = {
	left: null
	,right: null
	,skinParam: null
	,isFull: function(level) {
		if(level == 0) {
			return this.right.hasRoot();
		} else {
			return false;
		}
	}
	,addIdeaInternal: function(stereotype,backColor,level,label,shape,direction) {
		if(this.left.hasRoot() == false && this.right.hasRoot() == false) {
			level = 0;
		}
		if(level == 0) {
			this.right.initRoot(this.skinParam.getCurrentStyleBuilder(),backColor,label,shape,stereotype);
			this.left.initRoot(this.skinParam.getCurrentStyleBuilder(),backColor,label,shape,stereotype);
			return com_plantuml_command_CommandExecutionResult.OK;
		}
		if(direction == com_plantuml_Direction.LEFT) {
			return this.left.add(this.skinParam.getCurrentStyleBuilder(),backColor,level,label,shape,stereotype);
		}
		return this.right.add(this.skinParam.getCurrentStyleBuilder(),backColor,level,label,shape,stereotype);
	}
	,drawU: function(ug) {
		if(this.left.hasRoot() == false && this.right.hasRoot() == false) {
			return;
		}
		this.computeFinger();
		var stringBounder = ug.getStringBounder();
		var y1 = this.right.getHalfThickness(stringBounder);
		var y2 = this.left.getHalfThickness(stringBounder);
		var y = Math.max(y1,y2);
		var x = this.left.getX12(stringBounder);
		this.right.drawU(ug.apply(new com_plantuml_ugraphic_UTranslate(x,y)));
		this.left.drawU(ug.apply(new com_plantuml_ugraphic_UTranslate(x,y)));
	}
	,computeFinger: function() {
		if(this.left.hasFinger() == false && this.right.hasFinger() == false) {
			if(this.left.hasChildren()) {
				this.left.initFinger(this.skinParam,com_plantuml_Direction.LEFT);
			}
			if(this.left.hasFinger() == false || this.right.hasChildren()) {
				this.right.initFinger(this.skinParam,com_plantuml_Direction.RIGHT);
			}
			if(this.left.hasFinger() && this.right.hasFinger()) {
				this.left.doNotDrawFirstPhalanx();
			}
		}
	}
	,__class__: com_plantuml_mindmap_MindMap
};
var com_plantuml_mindmap_MindMapDiagram = function() {
	this.defaultDirection = com_plantuml_Direction.RIGHT;
	this.mindmaps = [new com_plantuml_mindmap_MindMap(this.getSkinParam())];
};
com_plantuml_mindmap_MindMapDiagram.__name__ = "com.plantuml.mindmap.MindMapDiagram";
com_plantuml_mindmap_MindMapDiagram.__super__ = com_plantuml_core_Diagram;
com_plantuml_mindmap_MindMapDiagram.prototype = $extend(com_plantuml_core_Diagram.prototype,{
	first: null
	,mindmaps: null
	,defaultDirection: null
	,getSmartLevel: function(type) {
		if(this.first == null) {
			this.first = type;
		}
		if(hx_strings_Strings.endsWith(type,"**")) {
			type = hx_strings_Strings.trim(hx_strings_Strings.replaceAll(type,"\t"," "));
		}
		type = hx_strings_Strings.replaceAll(type,"\t"," ");
		if((type == null ? false : type.indexOf(" ") > -1) == false) {
			return type.length - 1;
		}
		if(hx_strings_Strings.endsWith(type,this.first)) {
			return type.length - this.first.length;
		}
		if(hx_strings_Strings.trim(type).length == 1) {
			return type.length - 1;
		}
		if(hx_strings_Strings.startsWith(type,this.first)) {
			return type.length - this.first.length;
		}
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/MindMapDiagram.hx", lineNumber : 41, className : "com.plantuml.mindmap.MindMapDiagram", methodName : "getSmartLevel"});
	}
	,last: function() {
		return this.mindmaps[this.mindmaps.length - 1];
	}
	,getSkinParam: function() {
		return new com_plantuml_SkinParam();
	}
	,addIdea: function(backColor,level,label,shape,direction) {
		var stereotype = label.getEndingStereotype();
		if(stereotype != null) {
			label = label.removeEndingStereotype();
		}
		if(this.last().isFull(level)) {
			this.mindmaps.push(new com_plantuml_mindmap_MindMap(this.getSkinParam()));
		}
		if(direction == null) {
			direction = this.defaultDirection;
		}
		return this.last().addIdeaInternal(stereotype,backColor,level,label,shape,direction);
	}
	,exportDiagramNow: function(ug) {
		var _g = 0;
		var _g1 = this.mindmaps;
		while(_g < _g1.length) {
			var mindmap = _g1[_g];
			++_g;
			mindmap.drawU(ug);
		}
	}
	,__class__: com_plantuml_mindmap_MindMapDiagram
});
var com_plantuml_mindmap_MindMapDiagramFactory = function() {
	this.cmds = this.createCommands();
};
com_plantuml_mindmap_MindMapDiagramFactory.__name__ = "com.plantuml.mindmap.MindMapDiagramFactory";
com_plantuml_mindmap_MindMapDiagramFactory.prototype = {
	cmds: null
	,createCommands: function() {
		var cmds = [];
		cmds.push(new com_plantuml_mindmap_CommandMindMapOrgmode());
		cmds.push(new com_plantuml_mindmap_CommandMindMapRoot());
		cmds.push(new com_plantuml_mindmap_CommandMindMapPlus());
		cmds.push(new com_plantuml_mindmap_CommandMindMapDirection());
		return cmds;
	}
	,getCandidate: function(s) {
		var _g = 0;
		var _g1 = this.cmds;
		while(_g < _g1.length) {
			var cmd = _g1[_g];
			++_g;
			if(cmd.isValid(com_plantuml_command_BlocLines.single(s)) == com_plantuml_command_CommandControl.OK) {
				return cmd;
			}
		}
		return null;
	}
	,createSystem: function(lines) {
		var diagram = new com_plantuml_mindmap_MindMapDiagram();
		var _g = 0;
		var _g1 = lines.getLines();
		while(_g < _g1.length) {
			var s = _g1[_g];
			++_g;
			if(s == "" || hx_strings_Strings.startsWith(s,"@start") || hx_strings_Strings.startsWith(s,"@end")) {
				continue;
			}
			var cmd = this.getCandidate(s);
			if(cmd == null) {
				throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/MindMapDiagramFactory.hx", lineNumber : 44, className : "com.plantuml.mindmap.MindMapDiagramFactory", methodName : "createSystem"});
			}
			var exec = cmd.execute(diagram,com_plantuml_command_BlocLines.single(s));
		}
		return diagram;
	}
	,__class__: com_plantuml_mindmap_MindMapDiagramFactory
};
var haxe_IMap = function() { };
haxe_IMap.__name__ = "haxe.IMap";
haxe_IMap.__isInterface__ = true;
haxe_IMap.prototype = {
	get: null
	,keys: null
	,__class__: haxe_IMap
};
var haxe_ds_BalancedTree = function() {
};
haxe_ds_BalancedTree.__name__ = "haxe.ds.BalancedTree";
haxe_ds_BalancedTree.__interfaces__ = [haxe_IMap];
haxe_ds_BalancedTree.prototype = {
	root: null
	,set: function(key,value) {
		this.root = this.setLoop(key,value,this.root);
	}
	,get: function(key) {
		var node = this.root;
		while(node != null) {
			var c = this.compare(key,node.key);
			if(c == 0) {
				return node.value;
			}
			if(c < 0) {
				node = node.left;
			} else {
				node = node.right;
			}
		}
		return null;
	}
	,remove: function(key) {
		try {
			this.root = this.removeLoop(key,this.root);
			return true;
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			if(typeof(haxe_Exception.caught(_g).unwrap()) == "string") {
				return false;
			} else {
				throw _g;
			}
		}
	}
	,keys: function() {
		var ret = [];
		this.keysLoop(this.root,ret);
		return new haxe_iterators_ArrayIterator(ret);
	}
	,setLoop: function(k,v,node) {
		if(node == null) {
			return new haxe_ds_TreeNode(null,k,v,null);
		}
		var c = this.compare(k,node.key);
		if(c == 0) {
			return new haxe_ds_TreeNode(node.left,k,v,node.right,node == null ? 0 : node._height);
		} else if(c < 0) {
			var nl = this.setLoop(k,v,node.left);
			return this.balance(nl,node.key,node.value,node.right);
		} else {
			var nr = this.setLoop(k,v,node.right);
			return this.balance(node.left,node.key,node.value,nr);
		}
	}
	,removeLoop: function(k,node) {
		if(node == null) {
			throw haxe_Exception.thrown("Not_found");
		}
		var c = this.compare(k,node.key);
		if(c == 0) {
			return this.merge(node.left,node.right);
		} else if(c < 0) {
			return this.balance(this.removeLoop(k,node.left),node.key,node.value,node.right);
		} else {
			return this.balance(node.left,node.key,node.value,this.removeLoop(k,node.right));
		}
	}
	,keysLoop: function(node,acc) {
		if(node != null) {
			this.keysLoop(node.left,acc);
			acc.push(node.key);
			this.keysLoop(node.right,acc);
		}
	}
	,merge: function(t1,t2) {
		if(t1 == null) {
			return t2;
		}
		if(t2 == null) {
			return t1;
		}
		var t = this.minBinding(t2);
		return this.balance(t1,t.key,t.value,this.removeMinBinding(t2));
	}
	,minBinding: function(t) {
		if(t == null) {
			throw haxe_Exception.thrown("Not_found");
		} else if(t.left == null) {
			return t;
		} else {
			return this.minBinding(t.left);
		}
	}
	,removeMinBinding: function(t) {
		if(t.left == null) {
			return t.right;
		} else {
			return this.balance(this.removeMinBinding(t.left),t.key,t.value,t.right);
		}
	}
	,balance: function(l,k,v,r) {
		var hl = l == null ? 0 : l._height;
		var hr = r == null ? 0 : r._height;
		if(hl > hr + 2) {
			var _this = l.left;
			var _this1 = l.right;
			if((_this == null ? 0 : _this._height) >= (_this1 == null ? 0 : _this1._height)) {
				return new haxe_ds_TreeNode(l.left,l.key,l.value,new haxe_ds_TreeNode(l.right,k,v,r));
			} else {
				return new haxe_ds_TreeNode(new haxe_ds_TreeNode(l.left,l.key,l.value,l.right.left),l.right.key,l.right.value,new haxe_ds_TreeNode(l.right.right,k,v,r));
			}
		} else if(hr > hl + 2) {
			var _this = r.right;
			var _this1 = r.left;
			if((_this == null ? 0 : _this._height) > (_this1 == null ? 0 : _this1._height)) {
				return new haxe_ds_TreeNode(new haxe_ds_TreeNode(l,k,v,r.left),r.key,r.value,r.right);
			} else {
				return new haxe_ds_TreeNode(new haxe_ds_TreeNode(l,k,v,r.left.left),r.left.key,r.left.value,new haxe_ds_TreeNode(r.left.right,r.key,r.value,r.right));
			}
		} else {
			return new haxe_ds_TreeNode(l,k,v,r,(hl > hr ? hl : hr) + 1);
		}
	}
	,compare: function(k1,k2) {
		return Reflect.compare(k1,k2);
	}
	,__class__: haxe_ds_BalancedTree
};
var com_plantuml_mindmap_BalancedTreeStripe = function() {
	haxe_ds_BalancedTree.call(this);
};
com_plantuml_mindmap_BalancedTreeStripe.__name__ = "com.plantuml.mindmap.BalancedTreeStripe";
com_plantuml_mindmap_BalancedTreeStripe.__super__ = haxe_ds_BalancedTree;
com_plantuml_mindmap_BalancedTreeStripe.prototype = $extend(haxe_ds_BalancedTree.prototype,{
	compare: function(k1,k2) {
		return Reflect.compare(k1.getStart(),k2.getStart());
	}
	,size: function() {
		var cpt = 0;
		var k = this.keys();
		while(k.hasNext()) {
			var k1 = k.next();
			++cpt;
		}
		return cpt;
	}
	,add: function(key) {
		this.set(key,true);
	}
	,__class__: com_plantuml_mindmap_BalancedTreeStripe
});
var com_plantuml_mindmap_Stripe = function(x1,x2,value) {
	if(x2 <= x1) {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/Stripe.hx", lineNumber : 29, className : "com.plantuml.mindmap.Stripe", methodName : "new"});
	}
	this.x1 = x1;
	this.x2 = x2;
	this.value = value;
};
com_plantuml_mindmap_Stripe.__name__ = "com.plantuml.mindmap.Stripe";
com_plantuml_mindmap_Stripe.prototype = {
	x1: null
	,x2: null
	,value: null
	,contains: function(x) {
		if(x >= this.x1) {
			return x <= this.x2;
		} else {
			return false;
		}
	}
	,toString: function() {
		return "" + this.x1 + "->" + this.x2 + " (" + this.value + ")";
	}
	,getValue: function() {
		return this.value;
	}
	,getStart: function() {
		return this.x1;
	}
	,getEnd: function() {
		return this.x2;
	}
	,__class__: com_plantuml_mindmap_Stripe
};
var com_plantuml_mindmap_StripeFrontier = function() {
	this.stripes = new com_plantuml_mindmap_BalancedTreeStripe();
	this.stripes.set(new com_plantuml_mindmap_Stripe(-com_plantuml_mindmap_Tetris.MAX_VALUE,com_plantuml_mindmap_Tetris.MAX_VALUE,-com_plantuml_mindmap_Tetris.MAX_VALUE),true);
};
com_plantuml_mindmap_StripeFrontier.__name__ = "com.plantuml.mindmap.StripeFrontier";
com_plantuml_mindmap_StripeFrontier.prototype = {
	stripes: null
	,isEmpty: function() {
		return this.stripes.size() == 1;
	}
	,addSegment: function(x1,x2,value) {
		if(x2 <= x1) {
			haxe_Log.trace("x1=" + x1,{ fileName : "src/com/plantuml/mindmap/StripeFrontier.hx", lineNumber : 19, className : "com.plantuml.mindmap.StripeFrontier", methodName : "addSegment"});
			haxe_Log.trace("x2=" + x2,{ fileName : "src/com/plantuml/mindmap/StripeFrontier.hx", lineNumber : 20, className : "com.plantuml.mindmap.StripeFrontier", methodName : "addSegment"});
			throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/StripeFrontier.hx", lineNumber : 21, className : "com.plantuml.mindmap.StripeFrontier", methodName : "addSegment"});
		}
		var collisions = this.collisionning(x1,x2);
		if(collisions.size() > 1) {
			var it = collisions.keys();
			it.next();
			var x = x1;
			while(it.hasNext()) {
				var tmp = it.next();
				this.addSegment(x,tmp.getStart(),value);
				x = tmp.getStart();
			}
			this.addSegment(x,x2,value);
		} else {
			var touch = collisions.keys().next();
			this.addSingleInternal(x1,x2,value,touch);
		}
	}
	,collisionning: function(x1,x2) {
		var result = new com_plantuml_mindmap_BalancedTreeStripe();
		var stripe = this.stripes.keys();
		while(stripe.hasNext()) {
			var stripe1 = stripe.next();
			if(x1 >= stripe1.getEnd()) {
				continue;
			}
			result.add(stripe1);
			if(x2 <= stripe1.getEnd()) {
				return result;
			}
		}
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/StripeFrontier.hx", lineNumber : 49, className : "com.plantuml.mindmap.StripeFrontier", methodName : "collisionning"});
	}
	,addSingleInternal: function(x1,x2,value,touch) {
		if(value <= touch.getValue()) {
			return;
		}
		var ok = this.stripes.remove(touch);
		if(!ok) {
			throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/StripeFrontier.hx", lineNumber : 58, className : "com.plantuml.mindmap.StripeFrontier", methodName : "addSingleInternal"});
		}
		if(touch.getStart() != x1) {
			this.stripes.add(new com_plantuml_mindmap_Stripe(touch.getStart(),x1,touch.getValue()));
		}
		this.stripes.add(new com_plantuml_mindmap_Stripe(x1,x2,value));
		if(x2 != touch.getEnd()) {
			this.stripes.add(new com_plantuml_mindmap_Stripe(x2,touch.getEnd(),touch.getValue()));
		}
	}
	,getContact: function(x1,x2) {
		var collisions = this.collisionning(x1,x2);
		var result = -com_plantuml_mindmap_Tetris.MAX_VALUE;
		var strip = collisions.keys();
		while(strip.hasNext()) {
			var strip1 = strip.next();
			result = Math.max(result,strip1.getValue());
		}
		return result;
	}
	,__class__: com_plantuml_mindmap_StripeFrontier
};
var com_plantuml_mindmap_SymetricalTee = function(thickness1,elongation1,thickness2,elongation2) {
	this.thickness1 = thickness1;
	this.elongation1 = elongation1;
	this.thickness2 = thickness2;
	this.elongation2 = elongation2;
};
com_plantuml_mindmap_SymetricalTee.__name__ = "com.plantuml.mindmap.SymetricalTee";
com_plantuml_mindmap_SymetricalTee.prototype = {
	thickness1: null
	,elongation1: null
	,thickness2: null
	,elongation2: null
	,getThickness1: function() {
		return this.thickness1;
	}
	,getElongation1: function() {
		return this.elongation1;
	}
	,getThickness2: function() {
		return this.thickness2;
	}
	,getElongation2: function() {
		return this.elongation2;
	}
	,getFullElongation: function() {
		return this.elongation1 + this.elongation2;
	}
	,getFullThickness: function() {
		return Math.max(this.thickness1,this.thickness2);
	}
	,__class__: com_plantuml_mindmap_SymetricalTee
};
var com_plantuml_mindmap_SymetricalTeePositioned = function(tee,y) {
	this.tee = tee;
	this.y = y;
};
com_plantuml_mindmap_SymetricalTeePositioned.__name__ = "com.plantuml.mindmap.SymetricalTeePositioned";
com_plantuml_mindmap_SymetricalTeePositioned.create = function(tee) {
	return new com_plantuml_mindmap_SymetricalTeePositioned(tee,0);
};
com_plantuml_mindmap_SymetricalTeePositioned.prototype = {
	tee: null
	,y: null
	,getSegmentA1: function() {
		return new com_plantuml_awt_geom_Line2D(0,this.y - this.tee.getThickness1() / 2,this.tee.getElongation1(),this.y - this.tee.getThickness1() / 2);
	}
	,getSegmentB1: function() {
		return new com_plantuml_awt_geom_Line2D(0,this.y + this.tee.getThickness1() / 2,this.tee.getElongation1(),this.y + this.tee.getThickness1() / 2);
	}
	,getSegmentA2: function() {
		return new com_plantuml_awt_geom_Line2D(this.tee.getElongation1(),this.y - this.tee.getThickness2() / 2,this.tee.getElongation1() + this.tee.getElongation2(),this.y - this.tee.getThickness2() / 2);
	}
	,getSegmentB2: function() {
		return new com_plantuml_awt_geom_Line2D(this.tee.getElongation1(),this.y + this.tee.getThickness2() / 2,this.tee.getElongation1() + this.tee.getElongation2(),this.y + this.tee.getThickness2() / 2);
	}
	,moveSoThatSegmentA1isOn: function(newY) {
		var current = this.getSegmentA1().getY1();
		this.y += newY - current;
	}
	,moveSoThatSegmentA2isOn: function(newY) {
		var current = this.getSegmentA2().getY1();
		this.y += newY - current;
	}
	,getMax: function(other) {
		if(this.tee != other.tee) {
			throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/SymetricalTeePositioned.hx", lineNumber : 52, className : "com.plantuml.mindmap.SymetricalTeePositioned", methodName : "getMax"});
		}
		if(other.y > this.y) {
			return other;
		}
		return this;
	}
	,getMaxY: function() {
		return this.y + Math.max(this.tee.getThickness1() / 2,this.tee.getThickness2() / 2);
	}
	,getMinY: function() {
		return this.y - Math.max(this.tee.getThickness1() / 2,this.tee.getThickness2() / 2);
	}
	,getY: function() {
		return this.y;
	}
	,move: function(delta) {
		this.y += delta;
	}
	,getMaxX: function() {
		return this.tee.getElongation1() + this.tee.getElongation2();
	}
	,__class__: com_plantuml_mindmap_SymetricalTeePositioned
};
var com_plantuml_mindmap_Tetris = function(name) {
	this.maxY = -com_plantuml_mindmap_Tetris.MAX_VALUE;
	this.minY = com_plantuml_mindmap_Tetris.MAX_VALUE;
	this.elements = [];
	this.frontier = new com_plantuml_mindmap_StripeFrontier();
	this.name = name;
};
com_plantuml_mindmap_Tetris.__name__ = "com.plantuml.mindmap.Tetris";
com_plantuml_mindmap_Tetris.prototype = {
	frontier: null
	,elements: null
	,minY: null
	,maxY: null
	,name: null
	,add: function(tee) {
		if(this.frontier.isEmpty()) {
			var p1 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee);
			this.addInternal(p1);
			return;
		}
		var c1 = this.frontier.getContact(0,tee.getElongation1());
		var c2 = this.frontier.getContact(tee.getElongation1(),tee.getElongation1() + tee.getElongation2());
		var p1 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee);
		p1.moveSoThatSegmentA1isOn(c1);
		var p2 = com_plantuml_mindmap_SymetricalTeePositioned.create(tee);
		p2.moveSoThatSegmentA2isOn(c2);
		var result = p1.getMax(p2);
		this.addInternal(result);
	}
	,getHeight: function() {
		if(this.elements.length == 0) {
			return 0;
		}
		return this.maxY - this.minY;
	}
	,balance: function() {
		if(this.elements.length == 0) {
			return;
		}
		if(this.minY != com_plantuml_mindmap_Tetris.MAX_VALUE) {
			throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/mindmap/Tetris.hx", lineNumber : 55, className : "com.plantuml.mindmap.Tetris", methodName : "balance"});
		}
		var _g = 0;
		var _g1 = this.elements;
		while(_g < _g1.length) {
			var element = _g1[_g];
			++_g;
			this.minY = Math.min(this.minY,element.getMinY());
			this.maxY = Math.max(this.maxY,element.getMaxY());
		}
		var mean = (this.minY + this.maxY) / 2;
		var _g = 0;
		var _g1 = this.elements;
		while(_g < _g1.length) {
			var stp = _g1[_g];
			++_g;
			stp.move(-mean);
		}
	}
	,addInternal: function(result) {
		this.elements.push(result);
		var b1 = result.getSegmentB1();
		this.frontier.addSegment(b1.getX1(),b1.getX2(),b1.getY1());
		var b2 = result.getSegmentB2();
		if(b2.getX1() != b2.getX2()) {
			this.frontier.addSegment(b2.getX1(),b2.getX2(),b2.getY1());
		}
	}
	,getElements: function() {
		return this.elements;
	}
	,getWidth: function() {
		var result = 0;
		var _g = 0;
		var _g1 = this.elements;
		while(_g < _g1.length) {
			var tee = _g1[_g];
			++_g;
			result = Math.max(result,tee.getMaxX());
		}
		return result;
	}
	,__class__: com_plantuml_mindmap_Tetris
};
var com_plantuml_style_ClockwiseTopRightBottomLeft = function(top,right,bottom,left) {
	this.top = top;
	this.right = right;
	this.bottom = bottom;
	this.left = left;
};
com_plantuml_style_ClockwiseTopRightBottomLeft.__name__ = "com.plantuml.style.ClockwiseTopRightBottomLeft";
com_plantuml_style_ClockwiseTopRightBottomLeft.same = function(value) {
	return new com_plantuml_style_ClockwiseTopRightBottomLeft(value,value,value,value);
};
com_plantuml_style_ClockwiseTopRightBottomLeft.none = function() {
	return new com_plantuml_style_ClockwiseTopRightBottomLeft(0,0,0,0);
};
com_plantuml_style_ClockwiseTopRightBottomLeft.prototype = {
	top: null
	,right: null
	,bottom: null
	,left: null
	,getTop: function() {
		return this.top;
	}
	,getRight: function() {
		return this.right;
	}
	,getBottom: function() {
		return this.bottom;
	}
	,getLeft: function() {
		return this.left;
	}
	,__class__: com_plantuml_style_ClockwiseTopRightBottomLeft
};
var com_plantuml_style_StyleBuilder = function() {
};
com_plantuml_style_StyleBuilder.__name__ = "com.plantuml.style.StyleBuilder";
com_plantuml_style_StyleBuilder.prototype = {
	__class__: com_plantuml_style_StyleBuilder
};
var com_plantuml_ugraphic_UDriver = function() { };
com_plantuml_ugraphic_UDriver.__name__ = "com.plantuml.ugraphic.UDriver";
com_plantuml_ugraphic_UDriver.__isInterface__ = true;
com_plantuml_ugraphic_UDriver.prototype = {
	draw: null
	,__class__: com_plantuml_ugraphic_UDriver
};
var com_plantuml_svg_DriverPathSvg = function() {
};
com_plantuml_svg_DriverPathSvg.__name__ = "com.plantuml.svg.DriverPathSvg";
com_plantuml_svg_DriverPathSvg.__interfaces__ = [com_plantuml_ugraphic_UDriver];
com_plantuml_svg_DriverPathSvg.prototype = {
	draw: function(shape2,x,y,mapper,param,object) {
		var shape = js_Boot.__cast(shape2 , com_plantuml_ugraphic_UPath);
		object.svgPath(x,y,shape,shape.getDeltaShadow());
	}
	,__class__: com_plantuml_svg_DriverPathSvg
};
var com_plantuml_svg_DriverRectangleSvg = function() {
};
com_plantuml_svg_DriverRectangleSvg.__name__ = "com.plantuml.svg.DriverRectangleSvg";
com_plantuml_svg_DriverRectangleSvg.__interfaces__ = [com_plantuml_ugraphic_UDriver];
com_plantuml_svg_DriverRectangleSvg.prototype = {
	draw: function(shape,x,y,mapper,param,object) {
		var rect = js_Boot.__cast(shape , com_plantuml_ugraphic_URectangle);
		var width = rect.getWidth();
		var height = rect.getHeight();
		var rx = 0;
		var ry = 0;
		object.svgRectangle(x,y,width,height,rx / 2,ry / 2,rect.getDeltaShadow(),rect.getComment(),rect.getCodeLine());
	}
	,__class__: com_plantuml_svg_DriverRectangleSvg
};
var com_plantuml_svg_DriverTextSvg = function() {
};
com_plantuml_svg_DriverTextSvg.__name__ = "com.plantuml.svg.DriverTextSvg";
com_plantuml_svg_DriverTextSvg.__interfaces__ = [com_plantuml_ugraphic_UDriver];
com_plantuml_svg_DriverTextSvg.prototype = {
	draw: function(shape,x,y,mapper,param,object) {
		var text = js_Boot.__cast(shape , com_plantuml_ugraphic_UText);
		object.text(text.getText(),x,y + 12,"",16,"","plain","",100,new haxe_ds_StringMap(),"");
	}
	,__class__: com_plantuml_svg_DriverTextSvg
};
var com_plantuml_svg_SvgGraphics = function() {
	this.gRoot = Xml.createElement("g");
	this.defs = Xml.createElement("defs");
	this.root = Xml.createElement("svg");
	this.root.set("xmlns","http://www.w3.org/2000/svg");
	this.root.set("xmlns:xlink","http://www.w3.org/1999/xlink");
	this.root.set("version","1.1");
	var maxXscaled = 800;
	var maxYscaled = 800;
	var style = "width:" + maxXscaled + " px;height: " + maxYscaled + " + px;";
	this.root.set("style",style);
	this.root.set("width","" + maxXscaled + "px");
	this.root.set("height","" + maxYscaled + "px");
	this.root.addChild(this.defs);
	this.root.addChild(this.gRoot);
};
com_plantuml_svg_SvgGraphics.__name__ = "com.plantuml.svg.SvgGraphics";
com_plantuml_svg_SvgGraphics.prototype = {
	root: null
	,defs: null
	,gRoot: null
	,text: function(text,x,y,fontFamily,fontSize,fontWeight,fontStyle,textDecoration,textLength,attributes,textBackColor) {
		var elt = Xml.createElement("text");
		elt.set("x",this.format(x));
		elt.set("y",this.format(y));
		elt.set("font-size",this.format(fontSize));
		elt.addChild(Xml.createCData(text));
		this.getG().addChild(elt);
	}
	,svgRectangle: function(x,y,width,height,rx,ry,deltaShadow,id,codeLine) {
		var elt = this.createRectangleInternal(x,y,width,height);
		this.getG().addChild(elt);
	}
	,createRectangleInternal: function(x,y,width,height) {
		var elt = Xml.createElement("rect");
		elt.set("x",this.format(x));
		elt.set("y",this.format(y));
		elt.set("width",this.format(width));
		elt.set("height",this.format(height));
		this.fillMe(elt);
		elt.set("style",this.getStyleSpecial());
		return elt;
	}
	,getG: function() {
		return this.gRoot;
	}
	,format: function(x) {
		if(x == null) {
			return "null";
		} else {
			return "" + x;
		}
	}
	,toSvg: function() {
		return haxe_xml_Printer.print(this.root);
	}
	,fillMe: function(elt) {
		elt.set("fill","white");
	}
	,getStyleSpecial: function() {
		var style = new hx_strings_StringBuilder();
		style.add("stroke:black;");
		return style.toString();
	}
	,getStyle: function() {
		var style = new hx_strings_StringBuilder();
		style.add("stroke:black;");
		style.add("fill:none;");
		return style.toString();
	}
	,svgPath: function(x,y,path,deltaShadow) {
		var sb = new hx_strings_StringBuilder();
		var _g = 0;
		var _g1 = path.getSegments();
		while(_g < _g1.length) {
			var seg = _g1[_g];
			++_g;
			var type = seg.getSegmentType();
			var coord = seg.getCoord();
			if(type == com_plantuml_ugraphic_USegmentType.SEG_MOVETO) {
				sb.add("M" + this.format(coord[0] + x) + "," + this.format(coord[1] + y) + " ");
			} else if(type == com_plantuml_ugraphic_USegmentType.SEG_LINETO) {
				sb.add("L" + this.format(coord[0] + x) + "," + this.format(coord[1] + y) + " ");
			} else if(type == com_plantuml_ugraphic_USegmentType.SEG_CUBICTO) {
				sb.add("C" + this.format(coord[0] + x) + "," + this.format(coord[1] + y) + " " + this.format(coord[2] + x) + "," + this.format(coord[3] + y) + " " + this.format(coord[4] + x) + "," + this.format(coord[5] + y) + " ");
			} else {
				haxe_Log.trace(type,{ fileName : "src/com/plantuml/svg/SvgGraphics.hx", lineNumber : 109, className : "com.plantuml.svg.SvgGraphics", methodName : "svgPath"});
				throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/svg/SvgGraphics.hx", lineNumber : 110, className : "com.plantuml.svg.SvgGraphics", methodName : "svgPath"});
			}
		}
		var elt = Xml.createElement("path");
		elt.set("d",sb.toString());
		elt.set("style",this.getStyle());
		this.getG().addChild(elt);
	}
	,__class__: com_plantuml_svg_SvgGraphics
};
var com_plantuml_ugraphic_UGraphic = function() { };
com_plantuml_ugraphic_UGraphic.__name__ = "com.plantuml.ugraphic.UGraphic";
com_plantuml_ugraphic_UGraphic.__isInterface__ = true;
com_plantuml_ugraphic_UGraphic.prototype = {
	getStringBounder: null
	,apply: null
	,draw: null
	,__class__: com_plantuml_ugraphic_UGraphic
};
var com_plantuml_ugraphic_AbstractCommonUGraphic = function() {
	this.drivers = new haxe_ds_StringMap();
	this.translate = new com_plantuml_ugraphic_UTranslate(0,0);
};
com_plantuml_ugraphic_AbstractCommonUGraphic.__name__ = "com.plantuml.ugraphic.AbstractCommonUGraphic";
com_plantuml_ugraphic_AbstractCommonUGraphic.__interfaces__ = [com_plantuml_ugraphic_UGraphic];
com_plantuml_ugraphic_AbstractCommonUGraphic.prototype = {
	getStringBounder: null
	,draw: null
	,translate: null
	,drivers: null
	,getTranslateX: function() {
		return this.translate.getDx();
	}
	,getTranslateY: function() {
		return this.translate.getDy();
	}
	,apply: function(change) {
		var result = this.copyUGraphic();
		if(((change) instanceof com_plantuml_ugraphic_UTranslate)) {
			var translate = js_Boot.__cast(change , com_plantuml_ugraphic_UTranslate);
			result.translate = result.translate.compose(translate);
			return result;
		}
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/ugraphic/AbstractCommonUGraphic.hx", lineNumber : 23, className : "com.plantuml.ugraphic.AbstractCommonUGraphic", methodName : "apply"});
	}
	,copyUGraphic: null
	,__class__: com_plantuml_ugraphic_AbstractCommonUGraphic
};
var com_plantuml_ugraphic_Empty = function(width,height) {
	this.width = width;
	this.height = height;
};
com_plantuml_ugraphic_Empty.__name__ = "com.plantuml.ugraphic.Empty";
com_plantuml_ugraphic_Empty.__interfaces__ = [com_plantuml_graphic_TextBlock];
com_plantuml_ugraphic_Empty.prototype = {
	width: null
	,height: null
	,drawU: function(ug) {
	}
	,calculateDimension: function(stringBounder) {
		return new com_plantuml_awt_geom_Dimension2D(this.width,this.height);
	}
	,__class__: com_plantuml_ugraphic_Empty
};
var com_plantuml_ugraphic_TextBlockUtils = function() { };
com_plantuml_ugraphic_TextBlockUtils.__name__ = "com.plantuml.ugraphic.TextBlockUtils";
com_plantuml_ugraphic_TextBlockUtils.empty = function(width,height) {
	return new com_plantuml_ugraphic_Empty(width,height);
};
com_plantuml_ugraphic_TextBlockUtils.withMargin = function(textBlock,marginX1,marginX2,marginY1,marginY2) {
	return new com_plantuml_graphic_TextBlockMarged(textBlock,marginY1,marginX2,marginY2,marginX1);
};
var com_plantuml_ugraphic_UChange = function() { };
com_plantuml_ugraphic_UChange.__name__ = "com.plantuml.ugraphic.UChange";
com_plantuml_ugraphic_UChange.__isInterface__ = true;
var com_plantuml_ugraphic_UFont = function() {
};
com_plantuml_ugraphic_UFont.__name__ = "com.plantuml.ugraphic.UFont";
com_plantuml_ugraphic_UFont.prototype = {
	__class__: com_plantuml_ugraphic_UFont
};
var com_plantuml_ugraphic_StringBounderSvg = function() {
};
com_plantuml_ugraphic_StringBounderSvg.__name__ = "com.plantuml.ugraphic.StringBounderSvg";
com_plantuml_ugraphic_StringBounderSvg.__interfaces__ = [com_plantuml_graphic_StringBounder];
com_plantuml_ugraphic_StringBounderSvg.prototype = {
	calculateDimension: function(font,text) {
		var width = text.length;
		var height = 16;
		return new com_plantuml_awt_geom_Dimension2D(width * 12,height);
	}
	,__class__: com_plantuml_ugraphic_StringBounderSvg
};
var com_plantuml_ugraphic_UGraphicSvg = function(core) {
	com_plantuml_ugraphic_AbstractCommonUGraphic.call(this);
	this.core = core;
	var this1 = this.drivers;
	var key = com_plantuml_ugraphic_UText.__name__;
	var value = new com_plantuml_svg_DriverTextSvg();
	this1.h[key] = value;
	var this1 = this.drivers;
	var key = com_plantuml_ugraphic_URectangle.__name__;
	var value = new com_plantuml_svg_DriverRectangleSvg();
	this1.h[key] = value;
	var this1 = this.drivers;
	var key = com_plantuml_ugraphic_UPath.__name__;
	var value = new com_plantuml_svg_DriverPathSvg();
	this1.h[key] = value;
};
com_plantuml_ugraphic_UGraphicSvg.__name__ = "com.plantuml.ugraphic.UGraphicSvg";
com_plantuml_ugraphic_UGraphicSvg.__interfaces__ = [com_plantuml_ugraphic_UGraphic];
com_plantuml_ugraphic_UGraphicSvg.create = function() {
	return new com_plantuml_ugraphic_UGraphicSvg(new com_plantuml_svg_SvgGraphics());
};
com_plantuml_ugraphic_UGraphicSvg.__super__ = com_plantuml_ugraphic_AbstractCommonUGraphic;
com_plantuml_ugraphic_UGraphicSvg.prototype = $extend(com_plantuml_ugraphic_AbstractCommonUGraphic.prototype,{
	core: null
	,getStringBounder: function() {
		return new com_plantuml_ugraphic_StringBounderSvg();
	}
	,draw: function(shape) {
		var cl = js_Boot.getClass(shape);
		var this1 = this.drivers;
		var key = cl.__name__;
		var driver = this1.h[key];
		if(driver == null) {
			haxe_Log.trace(shape,{ fileName : "src/com/plantuml/ugraphic/UGraphicSvg.hx", lineNumber : 45, className : "com.plantuml.ugraphic.UGraphicSvg", methodName : "draw"});
			throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/ugraphic/UGraphicSvg.hx", lineNumber : 46, className : "com.plantuml.ugraphic.UGraphicSvg", methodName : "draw"});
		} else {
			driver.draw(shape,this.getTranslateX(),this.getTranslateY(),null,null,this.core);
		}
	}
	,getSvg: function() {
		return this.core.toSvg();
	}
	,copyUGraphic: function() {
		var result = new com_plantuml_ugraphic_UGraphicSvg(this.core);
		result.translate = this.translate.copy();
		return result;
	}
	,__class__: com_plantuml_ugraphic_UGraphicSvg
});
var com_plantuml_ugraphic_UParam = function() { };
com_plantuml_ugraphic_UParam.__name__ = "com.plantuml.ugraphic.UParam";
com_plantuml_ugraphic_UParam.__isInterface__ = true;
var com_plantuml_ugraphic_UPath = function() {
	this.segments = [];
};
com_plantuml_ugraphic_UPath.__name__ = "com.plantuml.ugraphic.UPath";
com_plantuml_ugraphic_UPath.__interfaces__ = [com_plantuml_ugraphic_UShape];
com_plantuml_ugraphic_UPath.prototype = {
	segments: null
	,getSegments: function() {
		return this.segments;
	}
	,moveToPoint: function(p1) {
		var x = p1.getX();
		var y = p1.getY();
		this.add([x,y],com_plantuml_ugraphic_USegmentType.SEG_MOVETO);
	}
	,lineToPoint: function(p1) {
		var x = p1.getX();
		var y = p1.getY();
		this.lineTo(x,y);
	}
	,lineTo: function(x,y) {
		this.add([x,y],com_plantuml_ugraphic_USegmentType.SEG_LINETO);
	}
	,cubicTo: function(ctrlx1,ctrly1,ctrlx2,ctrly2,x2,y2) {
		this.add([ctrlx1,ctrly1,ctrlx2,ctrly2,x2,y2],com_plantuml_ugraphic_USegmentType.SEG_CUBICTO);
	}
	,addInternal: function(segment) {
		this.segments.push(segment);
	}
	,add: function(coord,pathType) {
		this.addInternal(new com_plantuml_ugraphic_USegment(coord,pathType));
	}
	,getDeltaShadow: function() {
		return 0;
	}
	,__class__: com_plantuml_ugraphic_UPath
};
var com_plantuml_ugraphic_URectangle = function(width,height) {
	this.width = width;
	this.height = height;
};
com_plantuml_ugraphic_URectangle.__name__ = "com.plantuml.ugraphic.URectangle";
com_plantuml_ugraphic_URectangle.__interfaces__ = [com_plantuml_ugraphic_UShape];
com_plantuml_ugraphic_URectangle.prototype = {
	width: null
	,height: null
	,getWidth: function() {
		return this.width;
	}
	,getHeight: function() {
		return this.height;
	}
	,getDeltaShadow: function() {
		return 0;
	}
	,getComment: function() {
		return "";
	}
	,getCodeLine: function() {
		return "";
	}
	,__class__: com_plantuml_ugraphic_URectangle
};
var com_plantuml_ugraphic_USegment = function(coord,pathType) {
	this.coord = coord;
	this.pathType = pathType;
};
com_plantuml_ugraphic_USegment.__name__ = "com.plantuml.ugraphic.USegment";
com_plantuml_ugraphic_USegment.prototype = {
	coord: null
	,pathType: null
	,getSegmentType: function() {
		return this.pathType;
	}
	,getCoord: function() {
		return this.coord;
	}
	,__class__: com_plantuml_ugraphic_USegment
};
var com_plantuml_ugraphic_USegmentType = $hxEnums["com.plantuml.ugraphic.USegmentType"] = { __ename__:"com.plantuml.ugraphic.USegmentType",__constructs__:null
	,SEG_MOVETO: {_hx_name:"SEG_MOVETO",_hx_index:0,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
	,SEG_LINETO: {_hx_name:"SEG_LINETO",_hx_index:1,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
	,SEG_QUADTO: {_hx_name:"SEG_QUADTO",_hx_index:2,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
	,SEG_CUBICTO: {_hx_name:"SEG_CUBICTO",_hx_index:3,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
	,SEG_CLOSE: {_hx_name:"SEG_CLOSE",_hx_index:4,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
	,SEG_ARCTO: {_hx_name:"SEG_ARCTO",_hx_index:5,__enum__:"com.plantuml.ugraphic.USegmentType",toString:$estr}
};
com_plantuml_ugraphic_USegmentType.__constructs__ = [com_plantuml_ugraphic_USegmentType.SEG_MOVETO,com_plantuml_ugraphic_USegmentType.SEG_LINETO,com_plantuml_ugraphic_USegmentType.SEG_QUADTO,com_plantuml_ugraphic_USegmentType.SEG_CUBICTO,com_plantuml_ugraphic_USegmentType.SEG_CLOSE,com_plantuml_ugraphic_USegmentType.SEG_ARCTO];
var com_plantuml_ugraphic_USegmentType_$ = function() { };
com_plantuml_ugraphic_USegmentType_$.__name__ = "com.plantuml.ugraphic.USegmentType_";
com_plantuml_ugraphic_USegmentType_$.getNbPoints = function(me) {
	switch(me._hx_index) {
	case 0:
		return 1;
	case 1:
		return 1;
	case 3:
		return 3;
	case 4:
		return 0;
	default:
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "src/com/plantuml/ugraphic/USegmentType.hx", lineNumber : 24, className : "com.plantuml.ugraphic.USegmentType_", methodName : "getNbPoints"});
	}
};
var com_plantuml_ugraphic_UText = function(text) {
	this.text = text;
};
com_plantuml_ugraphic_UText.__name__ = "com.plantuml.ugraphic.UText";
com_plantuml_ugraphic_UText.__interfaces__ = [com_plantuml_ugraphic_UShape];
com_plantuml_ugraphic_UText.prototype = {
	text: null
	,getText: function() {
		return this.text;
	}
	,__class__: com_plantuml_ugraphic_UText
};
var com_plantuml_ugraphic_UTranslate = function(dx,dy) {
	this.dx = dx;
	this.dy = dy;
};
com_plantuml_ugraphic_UTranslate.__name__ = "com.plantuml.ugraphic.UTranslate";
com_plantuml_ugraphic_UTranslate.__interfaces__ = [com_plantuml_ugraphic_UChange];
com_plantuml_ugraphic_UTranslate.prototype = {
	dx: null
	,dy: null
	,getDx: function() {
		return this.dx;
	}
	,getDy: function() {
		return this.dy;
	}
	,copy: function() {
		return new com_plantuml_ugraphic_UTranslate(this.dx,this.dy);
	}
	,compose: function(other) {
		return new com_plantuml_ugraphic_UTranslate(this.dx + other.dx,this.dy + other.dy);
	}
	,__class__: com_plantuml_ugraphic_UTranslate
};
var com_plantuml_ugraphic_color_ColorMapper = function() { };
com_plantuml_ugraphic_color_ColorMapper.__name__ = "com.plantuml.ugraphic.color.ColorMapper";
com_plantuml_ugraphic_color_ColorMapper.__isInterface__ = true;
var com_plantuml_ugraphic_color_HColor = function() { };
com_plantuml_ugraphic_color_HColor.__name__ = "com.plantuml.ugraphic.color.HColor";
com_plantuml_ugraphic_color_HColor.__isInterface__ = true;
com_plantuml_ugraphic_color_HColor.__interfaces__ = [com_plantuml_ugraphic_UChange];
var haxe_StackItem = $hxEnums["haxe.StackItem"] = { __ename__:"haxe.StackItem",__constructs__:null
	,CFunction: {_hx_name:"CFunction",_hx_index:0,__enum__:"haxe.StackItem",toString:$estr}
	,Module: ($_=function(m) { return {_hx_index:1,m:m,__enum__:"haxe.StackItem",toString:$estr}; },$_._hx_name="Module",$_.__params__ = ["m"],$_)
	,FilePos: ($_=function(s,file,line,column) { return {_hx_index:2,s:s,file:file,line:line,column:column,__enum__:"haxe.StackItem",toString:$estr}; },$_._hx_name="FilePos",$_.__params__ = ["s","file","line","column"],$_)
	,Method: ($_=function(classname,method) { return {_hx_index:3,classname:classname,method:method,__enum__:"haxe.StackItem",toString:$estr}; },$_._hx_name="Method",$_.__params__ = ["classname","method"],$_)
	,LocalFunction: ($_=function(v) { return {_hx_index:4,v:v,__enum__:"haxe.StackItem",toString:$estr}; },$_._hx_name="LocalFunction",$_.__params__ = ["v"],$_)
};
haxe_StackItem.__constructs__ = [haxe_StackItem.CFunction,haxe_StackItem.Module,haxe_StackItem.FilePos,haxe_StackItem.Method,haxe_StackItem.LocalFunction];
var haxe_CallStack = {};
haxe_CallStack.callStack = function() {
	return haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.callStack());
};
haxe_CallStack.exceptionStack = function(fullStack) {
	if(fullStack == null) {
		fullStack = false;
	}
	var eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack());
	return fullStack ? eStack : haxe_CallStack.subtract(eStack,haxe_CallStack.callStack());
};
haxe_CallStack.toString = function(stack) {
	var b = new StringBuf();
	var _g = 0;
	var _g1 = stack;
	while(_g < _g1.length) {
		var s = _g1[_g];
		++_g;
		b.b += "\nCalled from ";
		haxe_CallStack.itemToString(b,s);
	}
	return b.b;
};
haxe_CallStack.subtract = function(this1,stack) {
	var startIndex = -1;
	var i = -1;
	while(++i < this1.length) {
		var _g = 0;
		var _g1 = stack.length;
		while(_g < _g1) {
			var j = _g++;
			if(haxe_CallStack.equalItems(this1[i],stack[j])) {
				if(startIndex < 0) {
					startIndex = i;
				}
				++i;
				if(i >= this1.length) {
					break;
				}
			} else {
				startIndex = -1;
			}
		}
		if(startIndex >= 0) {
			break;
		}
	}
	if(startIndex >= 0) {
		return this1.slice(0,startIndex);
	} else {
		return this1;
	}
};
haxe_CallStack.equalItems = function(item1,item2) {
	if(item1 == null) {
		if(item2 == null) {
			return true;
		} else {
			return false;
		}
	} else {
		switch(item1._hx_index) {
		case 0:
			if(item2 == null) {
				return false;
			} else if(item2._hx_index == 0) {
				return true;
			} else {
				return false;
			}
			break;
		case 1:
			if(item2 == null) {
				return false;
			} else if(item2._hx_index == 1) {
				var m2 = item2.m;
				var m1 = item1.m;
				return m1 == m2;
			} else {
				return false;
			}
			break;
		case 2:
			if(item2 == null) {
				return false;
			} else if(item2._hx_index == 2) {
				var item21 = item2.s;
				var file2 = item2.file;
				var line2 = item2.line;
				var col2 = item2.column;
				var col1 = item1.column;
				var line1 = item1.line;
				var file1 = item1.file;
				var item11 = item1.s;
				if(file1 == file2 && line1 == line2 && col1 == col2) {
					return haxe_CallStack.equalItems(item11,item21);
				} else {
					return false;
				}
			} else {
				return false;
			}
			break;
		case 3:
			if(item2 == null) {
				return false;
			} else if(item2._hx_index == 3) {
				var class2 = item2.classname;
				var method2 = item2.method;
				var method1 = item1.method;
				var class1 = item1.classname;
				if(class1 == class2) {
					return method1 == method2;
				} else {
					return false;
				}
			} else {
				return false;
			}
			break;
		case 4:
			if(item2 == null) {
				return false;
			} else if(item2._hx_index == 4) {
				var v2 = item2.v;
				var v1 = item1.v;
				return v1 == v2;
			} else {
				return false;
			}
			break;
		}
	}
};
haxe_CallStack.itemToString = function(b,s) {
	switch(s._hx_index) {
	case 0:
		b.b += "a C function";
		break;
	case 1:
		var m = s.m;
		b.b += "module ";
		b.b += m == null ? "null" : "" + m;
		break;
	case 2:
		var s1 = s.s;
		var file = s.file;
		var line = s.line;
		var col = s.column;
		if(s1 != null) {
			haxe_CallStack.itemToString(b,s1);
			b.b += " (";
		}
		b.b += file == null ? "null" : "" + file;
		b.b += " line ";
		b.b += line == null ? "null" : "" + line;
		if(col != null) {
			b.b += " column ";
			b.b += col == null ? "null" : "" + col;
		}
		if(s1 != null) {
			b.b += ")";
		}
		break;
	case 3:
		var cname = s.classname;
		var meth = s.method;
		b.b += Std.string(cname == null ? "<unknown>" : cname);
		b.b += ".";
		b.b += meth == null ? "null" : "" + meth;
		break;
	case 4:
		var n = s.v;
		b.b += "local function #";
		b.b += n == null ? "null" : "" + n;
		break;
	}
};
var haxe_Exception = function(message,previous,native) {
	Error.call(this,message);
	this.message = message;
	this.__previousException = previous;
	this.__nativeException = native != null ? native : this;
	this.__skipStack = 0;
	var old = Error.prepareStackTrace;
	Error.prepareStackTrace = function(e) { return e.stack; }
	if(((native) instanceof Error)) {
		this.stack = native.stack;
	} else {
		var e = null;
		if(Error.captureStackTrace) {
			Error.captureStackTrace(this,haxe_Exception);
			e = this;
		} else {
			e = new Error();
			if(typeof(e.stack) == "undefined") {
				try { throw e; } catch(_) {}
				this.__skipStack++;
			}
		}
		this.stack = e.stack;
	}
	Error.prepareStackTrace = old;
};
haxe_Exception.__name__ = "haxe.Exception";
haxe_Exception.caught = function(value) {
	if(((value) instanceof haxe_Exception)) {
		return value;
	} else if(((value) instanceof Error)) {
		return new haxe_Exception(value.message,null,value);
	} else {
		return new haxe_ValueException(value,null,value);
	}
};
haxe_Exception.thrown = function(value) {
	if(((value) instanceof haxe_Exception)) {
		return value.get_native();
	} else if(((value) instanceof Error)) {
		return value;
	} else {
		var e = new haxe_ValueException(value);
		e.__skipStack++;
		return e;
	}
};
haxe_Exception.__super__ = Error;
haxe_Exception.prototype = $extend(Error.prototype,{
	__skipStack: null
	,__nativeException: null
	,__previousException: null
	,unwrap: function() {
		return this.__nativeException;
	}
	,toString: function() {
		return this.get_message();
	}
	,__shiftStack: function() {
		this.__skipStack++;
	}
	,get_message: function() {
		return this.message;
	}
	,get_native: function() {
		return this.__nativeException;
	}
	,get_stack: function() {
		var _g = this.__exceptionStack;
		if(_g == null) {
			var value = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.normalize(this.stack),this.__skipStack);
			this.setProperty("__exceptionStack",value);
			return value;
		} else {
			var s = _g;
			return s;
		}
	}
	,setProperty: function(name,value) {
		try {
			Object.defineProperty(this,name,{ value : value});
		} catch( _g ) {
			this[name] = value;
		}
	}
	,__class__: haxe_Exception
	,__properties__: {get_native:"get_native",get_stack:"get_stack",get_message:"get_message"}
});
var haxe_Log = function() { };
haxe_Log.__name__ = "haxe.Log";
haxe_Log.formatOutput = function(v,infos) {
	var str = Std.string(v);
	if(infos == null) {
		return str;
	}
	var pstr = infos.fileName + ":" + infos.lineNumber;
	if(infos.customParams != null) {
		var _g = 0;
		var _g1 = infos.customParams;
		while(_g < _g1.length) {
			var v = _g1[_g];
			++_g;
			str += ", " + Std.string(v);
		}
	}
	return pstr + ": " + str;
};
haxe_Log.trace = function(v,infos) {
	var str = haxe_Log.formatOutput(v,infos);
	if(typeof(console) != "undefined" && console.log != null) {
		console.log(str);
	}
};
var haxe_NativeStackTrace = function() { };
haxe_NativeStackTrace.__name__ = "haxe.NativeStackTrace";
haxe_NativeStackTrace.saveStack = function(e) {
	haxe_NativeStackTrace.lastError = e;
};
haxe_NativeStackTrace.callStack = function() {
	var e = new Error("");
	var stack = haxe_NativeStackTrace.tryHaxeStack(e);
	if(typeof(stack) == "undefined") {
		try {
			throw e;
		} catch( _g ) {
		}
		stack = e.stack;
	}
	return haxe_NativeStackTrace.normalize(stack,2);
};
haxe_NativeStackTrace.exceptionStack = function() {
	return haxe_NativeStackTrace.normalize(haxe_NativeStackTrace.tryHaxeStack(haxe_NativeStackTrace.lastError));
};
haxe_NativeStackTrace.toHaxe = function(s,skip) {
	if(skip == null) {
		skip = 0;
	}
	if(s == null) {
		return [];
	} else if(typeof(s) == "string") {
		var stack = s.split("\n");
		if(stack[0] == "Error") {
			stack.shift();
		}
		var m = [];
		var _g = 0;
		var _g1 = stack.length;
		while(_g < _g1) {
			var i = _g++;
			if(skip > i) {
				continue;
			}
			var line = stack[i];
			var matched = line.match(/^    at ([A-Za-z0-9_. ]+) \(([^)]+):([0-9]+):([0-9]+)\)$/);
			if(matched != null) {
				var path = matched[1].split(".");
				if(path[0] == "$hxClasses") {
					path.shift();
				}
				var meth = path.pop();
				var file = matched[2];
				var line1 = Std.parseInt(matched[3]);
				var column = Std.parseInt(matched[4]);
				m.push(haxe_StackItem.FilePos(meth == "Anonymous function" ? haxe_StackItem.LocalFunction() : meth == "Global code" ? null : haxe_StackItem.Method(path.join("."),meth),file,line1,column));
			} else {
				m.push(haxe_StackItem.Module(StringTools.trim(line)));
			}
		}
		return m;
	} else if(skip > 0 && Array.isArray(s)) {
		return s.slice(skip);
	} else {
		return s;
	}
};
haxe_NativeStackTrace.tryHaxeStack = function(e) {
	if(e == null) {
		return [];
	}
	var oldValue = Error.prepareStackTrace;
	Error.prepareStackTrace = haxe_NativeStackTrace.prepareHxStackTrace;
	var stack = e.stack;
	Error.prepareStackTrace = oldValue;
	return stack;
};
haxe_NativeStackTrace.prepareHxStackTrace = function(e,callsites) {
	var stack = [];
	var _g = 0;
	while(_g < callsites.length) {
		var site = callsites[_g];
		++_g;
		if(haxe_NativeStackTrace.wrapCallSite != null) {
			site = haxe_NativeStackTrace.wrapCallSite(site);
		}
		var method = null;
		var fullName = site.getFunctionName();
		if(fullName != null) {
			var idx = fullName.lastIndexOf(".");
			if(idx >= 0) {
				var className = fullName.substring(0,idx);
				var methodName = fullName.substring(idx + 1);
				method = haxe_StackItem.Method(className,methodName);
			} else {
				method = haxe_StackItem.Method(null,fullName);
			}
		}
		var fileName = site.getFileName();
		var fileAddr = fileName == null ? -1 : fileName.indexOf("file:");
		if(haxe_NativeStackTrace.wrapCallSite != null && fileAddr > 0) {
			fileName = fileName.substring(fileAddr + 6);
		}
		stack.push(haxe_StackItem.FilePos(method,fileName,site.getLineNumber(),site.getColumnNumber()));
	}
	return stack;
};
haxe_NativeStackTrace.normalize = function(stack,skipItems) {
	if(skipItems == null) {
		skipItems = 0;
	}
	if(Array.isArray(stack) && skipItems > 0) {
		return stack.slice(skipItems);
	} else if(typeof(stack) == "string") {
		switch(stack.substring(0,6)) {
		case "Error\n":case "Error:":
			++skipItems;
			break;
		default:
		}
		return haxe_NativeStackTrace.skipLines(stack,skipItems);
	} else {
		return stack;
	}
};
haxe_NativeStackTrace.skipLines = function(stack,skip,pos) {
	if(pos == null) {
		pos = 0;
	}
	if(skip > 0) {
		pos = stack.indexOf("\n",pos);
		if(pos < 0) {
			return "";
		} else {
			return haxe_NativeStackTrace.skipLines(stack,--skip,pos + 1);
		}
	} else {
		return stack.substring(pos);
	}
};
var haxe_Timer = function(time_ms) {
	var me = this;
	this.id = setInterval(function() {
		me.run();
	},time_ms);
};
haxe_Timer.__name__ = "haxe.Timer";
haxe_Timer.delay = function(f,time_ms) {
	var t = new haxe_Timer(time_ms);
	t.run = function() {
		t.stop();
		f();
	};
	return t;
};
haxe_Timer.prototype = {
	id: null
	,stop: function() {
		if(this.id == null) {
			return;
		}
		clearInterval(this.id);
		this.id = null;
	}
	,run: function() {
	}
	,__class__: haxe_Timer
};
var haxe_ValueException = function(value,previous,native) {
	haxe_Exception.call(this,String(value),previous,native);
	this.value = value;
	this.__skipStack++;
};
haxe_ValueException.__name__ = "haxe.ValueException";
haxe_ValueException.__super__ = haxe_Exception;
haxe_ValueException.prototype = $extend(haxe_Exception.prototype,{
	value: null
	,unwrap: function() {
		return this.value;
	}
	,__class__: haxe_ValueException
});
var haxe_crypto_Adler32 = function() {
	this.a1 = 1;
	this.a2 = 0;
};
haxe_crypto_Adler32.__name__ = "haxe.crypto.Adler32";
haxe_crypto_Adler32.make = function(b) {
	var a = new haxe_crypto_Adler32();
	a.update(b,0,b.length);
	return a.get();
};
haxe_crypto_Adler32.prototype = {
	a1: null
	,a2: null
	,get: function() {
		return this.a2 << 16 | this.a1;
	}
	,update: function(b,pos,len) {
		var a1 = this.a1;
		var a2 = this.a2;
		var _g = pos;
		var _g1 = pos + len;
		while(_g < _g1) {
			var p = _g++;
			var c = b.b[p];
			a1 = (a1 + c) % 65521;
			a2 = (a2 + a1) % 65521;
		}
		this.a1 = a1;
		this.a2 = a2;
	}
	,__class__: haxe_crypto_Adler32
};
var haxe_io_Bytes = function(data) {
	this.length = data.byteLength;
	this.b = new Uint8Array(data);
	this.b.bufferValue = data;
	data.hxBytes = this;
	data.bytes = this.b;
};
haxe_io_Bytes.__name__ = "haxe.io.Bytes";
haxe_io_Bytes.ofString = function(s,encoding) {
	if(encoding == haxe_io_Encoding.RawNative) {
		var buf = new Uint8Array(s.length << 1);
		var _g = 0;
		var _g1 = s.length;
		while(_g < _g1) {
			var i = _g++;
			var c = s.charCodeAt(i);
			buf[i << 1] = c & 255;
			buf[i << 1 | 1] = c >> 8;
		}
		return new haxe_io_Bytes(buf.buffer);
	}
	var a = [];
	var i = 0;
	while(i < s.length) {
		var c = s.charCodeAt(i++);
		if(55296 <= c && c <= 56319) {
			c = c - 55232 << 10 | s.charCodeAt(i++) & 1023;
		}
		if(c <= 127) {
			a.push(c);
		} else if(c <= 2047) {
			a.push(192 | c >> 6);
			a.push(128 | c & 63);
		} else if(c <= 65535) {
			a.push(224 | c >> 12);
			a.push(128 | c >> 6 & 63);
			a.push(128 | c & 63);
		} else {
			a.push(240 | c >> 18);
			a.push(128 | c >> 12 & 63);
			a.push(128 | c >> 6 & 63);
			a.push(128 | c & 63);
		}
	}
	return new haxe_io_Bytes(new Uint8Array(a).buffer);
};
haxe_io_Bytes.prototype = {
	length: null
	,b: null
	,getString: function(pos,len,encoding) {
		if(pos < 0 || len < 0 || pos + len > this.length) {
			throw haxe_Exception.thrown(haxe_io_Error.OutsideBounds);
		}
		if(encoding == null) {
			encoding = haxe_io_Encoding.UTF8;
		}
		var s = "";
		var b = this.b;
		var i = pos;
		var max = pos + len;
		switch(encoding._hx_index) {
		case 0:
			var debug = pos > 0;
			while(i < max) {
				var c = b[i++];
				if(c < 128) {
					if(c == 0) {
						break;
					}
					s += String.fromCodePoint(c);
				} else if(c < 224) {
					var code = (c & 63) << 6 | b[i++] & 127;
					s += String.fromCodePoint(code);
				} else if(c < 240) {
					var c2 = b[i++];
					var code1 = (c & 31) << 12 | (c2 & 127) << 6 | b[i++] & 127;
					s += String.fromCodePoint(code1);
				} else {
					var c21 = b[i++];
					var c3 = b[i++];
					var u = (c & 15) << 18 | (c21 & 127) << 12 | (c3 & 127) << 6 | b[i++] & 127;
					s += String.fromCodePoint(u);
				}
			}
			break;
		case 1:
			while(i < max) {
				var c = b[i++] | b[i++] << 8;
				s += String.fromCodePoint(c);
			}
			break;
		}
		return s;
	}
	,toString: function() {
		return this.getString(0,this.length);
	}
	,__class__: haxe_io_Bytes
};
var haxe_io_Encoding = $hxEnums["haxe.io.Encoding"] = { __ename__:"haxe.io.Encoding",__constructs__:null
	,UTF8: {_hx_name:"UTF8",_hx_index:0,__enum__:"haxe.io.Encoding",toString:$estr}
	,RawNative: {_hx_name:"RawNative",_hx_index:1,__enum__:"haxe.io.Encoding",toString:$estr}
};
haxe_io_Encoding.__constructs__ = [haxe_io_Encoding.UTF8,haxe_io_Encoding.RawNative];
var haxe_crypto_Base64 = function() { };
haxe_crypto_Base64.__name__ = "haxe.crypto.Base64";
haxe_crypto_Base64.encode = function(bytes,complement) {
	if(complement == null) {
		complement = true;
	}
	var str = new haxe_crypto_BaseCode(haxe_crypto_Base64.BYTES).encodeBytes(bytes).toString();
	if(complement) {
		switch(bytes.length % 3) {
		case 1:
			str += "==";
			break;
		case 2:
			str += "=";
			break;
		default:
		}
	}
	return str;
};
haxe_crypto_Base64.decode = function(str,complement) {
	if(complement == null) {
		complement = true;
	}
	if(complement) {
		while(HxOverrides.cca(str,str.length - 1) == 61) str = HxOverrides.substr(str,0,-1);
	}
	return new haxe_crypto_BaseCode(haxe_crypto_Base64.BYTES).decodeBytes(haxe_io_Bytes.ofString(str));
};
var haxe_crypto_BaseCode = function(base) {
	var len = base.length;
	var nbits = 1;
	while(len > 1 << nbits) ++nbits;
	if(nbits > 8 || len != 1 << nbits) {
		throw haxe_Exception.thrown("BaseCode : base length must be a power of two.");
	}
	this.base = base;
	this.nbits = nbits;
};
haxe_crypto_BaseCode.__name__ = "haxe.crypto.BaseCode";
haxe_crypto_BaseCode.prototype = {
	base: null
	,nbits: null
	,tbl: null
	,encodeBytes: function(b) {
		var nbits = this.nbits;
		var base = this.base;
		var size = b.length * 8 / nbits | 0;
		var out = new haxe_io_Bytes(new ArrayBuffer(size + (b.length * 8 % nbits == 0 ? 0 : 1)));
		var buf = 0;
		var curbits = 0;
		var mask = (1 << nbits) - 1;
		var pin = 0;
		var pout = 0;
		while(pout < size) {
			while(curbits < nbits) {
				curbits += 8;
				buf <<= 8;
				buf |= b.b[pin++];
			}
			curbits -= nbits;
			out.b[pout++] = base.b[buf >> curbits & mask];
		}
		if(curbits > 0) {
			out.b[pout++] = base.b[buf << nbits - curbits & mask];
		}
		return out;
	}
	,initTable: function() {
		var tbl = [];
		var _g = 0;
		while(_g < 256) {
			var i = _g++;
			tbl[i] = -1;
		}
		var _g = 0;
		var _g1 = this.base.length;
		while(_g < _g1) {
			var i = _g++;
			tbl[this.base.b[i]] = i;
		}
		this.tbl = tbl;
	}
	,decodeBytes: function(b) {
		var nbits = this.nbits;
		var base = this.base;
		if(this.tbl == null) {
			this.initTable();
		}
		var tbl = this.tbl;
		var size = b.length * nbits >> 3;
		var out = new haxe_io_Bytes(new ArrayBuffer(size));
		var buf = 0;
		var curbits = 0;
		var pin = 0;
		var pout = 0;
		while(pout < size) {
			while(curbits < 8) {
				curbits += nbits;
				buf <<= nbits;
				var i = tbl[b.b[pin++]];
				if(i == -1) {
					throw haxe_Exception.thrown("BaseCode : invalid encoded char");
				}
				buf |= i;
			}
			curbits -= 8;
			out.b[pout++] = buf >> curbits & 255;
		}
		return out;
	}
	,__class__: haxe_crypto_BaseCode
};
var haxe_crypto_Crc32 = function() { };
haxe_crypto_Crc32.__name__ = "haxe.crypto.Crc32";
haxe_crypto_Crc32.make = function(data) {
	var c_crc = -1;
	var b = data.b.bufferValue;
	var _g = 0;
	var _g1 = data.length;
	while(_g < _g1) {
		var i = _g++;
		var tmp = (c_crc ^ b.bytes[i]) & 255;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		tmp = tmp >>> 1 ^ -(tmp & 1) & -306674912;
		c_crc = c_crc >>> 8 ^ tmp;
	}
	return c_crc ^ -1;
};
var haxe_ds_TreeNode = function(l,k,v,r,h) {
	if(h == null) {
		h = -1;
	}
	this.left = l;
	this.key = k;
	this.value = v;
	this.right = r;
	if(h == -1) {
		var tmp;
		var _this = this.left;
		var _this1 = this.right;
		if((_this == null ? 0 : _this._height) > (_this1 == null ? 0 : _this1._height)) {
			var _this = this.left;
			tmp = _this == null ? 0 : _this._height;
		} else {
			var _this = this.right;
			tmp = _this == null ? 0 : _this._height;
		}
		this._height = tmp + 1;
	} else {
		this._height = h;
	}
};
haxe_ds_TreeNode.__name__ = "haxe.ds.TreeNode";
haxe_ds_TreeNode.prototype = {
	left: null
	,right: null
	,key: null
	,value: null
	,_height: null
	,__class__: haxe_ds_TreeNode
};
var haxe_ds_EnumValueMap = function() {
	haxe_ds_BalancedTree.call(this);
};
haxe_ds_EnumValueMap.__name__ = "haxe.ds.EnumValueMap";
haxe_ds_EnumValueMap.__interfaces__ = [haxe_IMap];
haxe_ds_EnumValueMap.__super__ = haxe_ds_BalancedTree;
haxe_ds_EnumValueMap.prototype = $extend(haxe_ds_BalancedTree.prototype,{
	compare: function(k1,k2) {
		var d = k1._hx_index - k2._hx_index;
		if(d != 0) {
			return d;
		}
		var p1 = Type.enumParameters(k1);
		var p2 = Type.enumParameters(k2);
		if(p1.length == 0 && p2.length == 0) {
			return 0;
		}
		return this.compareArgs(p1,p2);
	}
	,compareArgs: function(a1,a2) {
		var ld = a1.length - a2.length;
		if(ld != 0) {
			return ld;
		}
		var _g = 0;
		var _g1 = a1.length;
		while(_g < _g1) {
			var i = _g++;
			var d = this.compareArg(a1[i],a2[i]);
			if(d != 0) {
				return d;
			}
		}
		return 0;
	}
	,compareArg: function(v1,v2) {
		if(Reflect.isEnumValue(v1) && Reflect.isEnumValue(v2)) {
			return this.compare(v1,v2);
		} else if(((v1) instanceof Array) && ((v2) instanceof Array)) {
			return this.compareArgs(v1,v2);
		} else {
			return Reflect.compare(v1,v2);
		}
	}
	,__class__: haxe_ds_EnumValueMap
});
var haxe_ds_IntMap = function() {
	this.h = { };
};
haxe_ds_IntMap.__name__ = "haxe.ds.IntMap";
haxe_ds_IntMap.__interfaces__ = [haxe_IMap];
haxe_ds_IntMap.prototype = {
	h: null
	,get: function(key) {
		return this.h[key];
	}
	,keys: function() {
		var a = [];
		for( var key in this.h ) if(this.h.hasOwnProperty(key)) a.push(+key);
		return new haxe_iterators_ArrayIterator(a);
	}
	,__class__: haxe_ds_IntMap
};
var haxe_ds_List = function() {
	this.length = 0;
};
haxe_ds_List.__name__ = "haxe.ds.List";
haxe_ds_List.prototype = {
	h: null
	,q: null
	,length: null
	,add: function(item) {
		var x = new haxe_ds__$List_ListNode(item,null);
		if(this.h == null) {
			this.h = x;
		} else {
			this.q.next = x;
		}
		this.q = x;
		this.length++;
	}
	,remove: function(v) {
		var prev = null;
		var l = this.h;
		while(l != null) {
			if(l.item == v) {
				if(prev == null) {
					this.h = l.next;
				} else {
					prev.next = l.next;
				}
				if(this.q == l) {
					this.q = prev;
				}
				this.length--;
				return true;
			}
			prev = l;
			l = l.next;
		}
		return false;
	}
	,iterator: function() {
		return new haxe_ds__$List_ListIterator(this.h);
	}
	,__class__: haxe_ds_List
};
var haxe_ds__$List_ListNode = function(item,next) {
	this.item = item;
	this.next = next;
};
haxe_ds__$List_ListNode.__name__ = "haxe.ds._List.ListNode";
haxe_ds__$List_ListNode.prototype = {
	item: null
	,next: null
	,__class__: haxe_ds__$List_ListNode
};
var haxe_ds__$List_ListIterator = function(head) {
	this.head = head;
};
haxe_ds__$List_ListIterator.__name__ = "haxe.ds._List.ListIterator";
haxe_ds__$List_ListIterator.prototype = {
	head: null
	,hasNext: function() {
		return this.head != null;
	}
	,next: function() {
		var val = this.head.item;
		this.head = this.head.next;
		return val;
	}
	,__class__: haxe_ds__$List_ListIterator
};
var haxe_ds_StringMap = function() {
	this.h = Object.create(null);
};
haxe_ds_StringMap.__name__ = "haxe.ds.StringMap";
haxe_ds_StringMap.__interfaces__ = [haxe_IMap];
haxe_ds_StringMap.prototype = {
	h: null
	,get: function(key) {
		return this.h[key];
	}
	,keys: function() {
		return new haxe_ds__$StringMap_StringMapKeyIterator(this.h);
	}
	,__class__: haxe_ds_StringMap
};
var haxe_ds__$StringMap_StringMapKeyIterator = function(h) {
	this.h = h;
	this.keys = Object.keys(h);
	this.length = this.keys.length;
	this.current = 0;
};
haxe_ds__$StringMap_StringMapKeyIterator.__name__ = "haxe.ds._StringMap.StringMapKeyIterator";
haxe_ds__$StringMap_StringMapKeyIterator.prototype = {
	h: null
	,keys: null
	,length: null
	,current: null
	,hasNext: function() {
		return this.current < this.length;
	}
	,next: function() {
		return this.keys[this.current++];
	}
	,__class__: haxe_ds__$StringMap_StringMapKeyIterator
};
var haxe_exceptions_PosException = function(message,previous,pos) {
	haxe_Exception.call(this,message,previous);
	if(pos == null) {
		this.posInfos = { fileName : "(unknown)", lineNumber : 0, className : "(unknown)", methodName : "(unknown)"};
	} else {
		this.posInfos = pos;
	}
	this.__skipStack++;
};
haxe_exceptions_PosException.__name__ = "haxe.exceptions.PosException";
haxe_exceptions_PosException.__super__ = haxe_Exception;
haxe_exceptions_PosException.prototype = $extend(haxe_Exception.prototype,{
	posInfos: null
	,toString: function() {
		return "" + haxe_Exception.prototype.toString.call(this) + " in " + this.posInfos.className + "." + this.posInfos.methodName + " at " + this.posInfos.fileName + ":" + this.posInfos.lineNumber;
	}
	,__class__: haxe_exceptions_PosException
});
var haxe_exceptions_NotImplementedException = function(message,previous,pos) {
	if(message == null) {
		message = "Not implemented";
	}
	haxe_exceptions_PosException.call(this,message,previous,pos);
	this.__skipStack++;
};
haxe_exceptions_NotImplementedException.__name__ = "haxe.exceptions.NotImplementedException";
haxe_exceptions_NotImplementedException.__super__ = haxe_exceptions_PosException;
haxe_exceptions_NotImplementedException.prototype = $extend(haxe_exceptions_PosException.prototype,{
	__class__: haxe_exceptions_NotImplementedException
});
var haxe_io_BytesBuffer = function() {
	this.pos = 0;
	this.size = 0;
};
haxe_io_BytesBuffer.__name__ = "haxe.io.BytesBuffer";
haxe_io_BytesBuffer.prototype = {
	buffer: null
	,view: null
	,u8: null
	,pos: null
	,size: null
	,addByte: function(byte) {
		if(this.pos == this.size) {
			this.grow(1);
		}
		this.view.setUint8(this.pos++,byte);
	}
	,grow: function(delta) {
		var req = this.pos + delta;
		var nsize = this.size == 0 ? 16 : this.size;
		while(nsize < req) nsize = nsize * 3 >> 1;
		var nbuf = new ArrayBuffer(nsize);
		var nu8 = new Uint8Array(nbuf);
		if(this.size > 0) {
			nu8.set(this.u8);
		}
		this.size = nsize;
		this.buffer = nbuf;
		this.u8 = nu8;
		this.view = new DataView(this.buffer);
	}
	,getBytes: function() {
		if(this.size == 0) {
			return new haxe_io_Bytes(new ArrayBuffer(0));
		}
		var b = new haxe_io_Bytes(this.buffer);
		b.length = this.pos;
		return b;
	}
	,__class__: haxe_io_BytesBuffer
};
var haxe_io_Output = function() { };
haxe_io_Output.__name__ = "haxe.io.Output";
var haxe_io_BytesOutput = function() {
	this.b = new haxe_io_BytesBuffer();
};
haxe_io_BytesOutput.__name__ = "haxe.io.BytesOutput";
haxe_io_BytesOutput.__super__ = haxe_io_Output;
haxe_io_BytesOutput.prototype = $extend(haxe_io_Output.prototype,{
	b: null
	,writeByte: function(c) {
		this.b.addByte(c);
	}
	,getBytes: function() {
		return this.b.getBytes();
	}
	,__class__: haxe_io_BytesOutput
});
var haxe_io_Eof = function() {
};
haxe_io_Eof.__name__ = "haxe.io.Eof";
haxe_io_Eof.prototype = {
	toString: function() {
		return "Eof";
	}
	,__class__: haxe_io_Eof
};
var haxe_io_Error = $hxEnums["haxe.io.Error"] = { __ename__:"haxe.io.Error",__constructs__:null
	,Blocked: {_hx_name:"Blocked",_hx_index:0,__enum__:"haxe.io.Error",toString:$estr}
	,Overflow: {_hx_name:"Overflow",_hx_index:1,__enum__:"haxe.io.Error",toString:$estr}
	,OutsideBounds: {_hx_name:"OutsideBounds",_hx_index:2,__enum__:"haxe.io.Error",toString:$estr}
	,Custom: ($_=function(e) { return {_hx_index:3,e:e,__enum__:"haxe.io.Error",toString:$estr}; },$_._hx_name="Custom",$_.__params__ = ["e"],$_)
};
haxe_io_Error.__constructs__ = [haxe_io_Error.Blocked,haxe_io_Error.Overflow,haxe_io_Error.OutsideBounds,haxe_io_Error.Custom];
var haxe_io_Input = function() { };
haxe_io_Input.__name__ = "haxe.io.Input";
haxe_io_Input.prototype = {
	readByte: function() {
		throw new haxe_exceptions_NotImplementedException(null,null,{ fileName : "haxe/io/Input.hx", lineNumber : 53, className : "haxe.io.Input", methodName : "readByte"});
	}
	,__class__: haxe_io_Input
};
var haxe_iterators_ArrayIterator = function(array) {
	this.current = 0;
	this.array = array;
};
haxe_iterators_ArrayIterator.__name__ = "haxe.iterators.ArrayIterator";
haxe_iterators_ArrayIterator.prototype = {
	array: null
	,current: null
	,hasNext: function() {
		return this.current < this.array.length;
	}
	,next: function() {
		return this.array[this.current++];
	}
	,__class__: haxe_iterators_ArrayIterator
};
var haxe_rtti_Meta = function() { };
haxe_rtti_Meta.__name__ = "haxe.rtti.Meta";
haxe_rtti_Meta.getMeta = function(t) {
	return t.__meta__;
};
haxe_rtti_Meta.getFields = function(t) {
	var meta = haxe_rtti_Meta.getMeta(t);
	if(meta == null || meta.fields == null) {
		return { };
	} else {
		return meta.fields;
	}
};
var haxe_xml_Printer = function(pretty) {
	this.output = new StringBuf();
	this.pretty = pretty;
};
haxe_xml_Printer.__name__ = "haxe.xml.Printer";
haxe_xml_Printer.print = function(xml,pretty) {
	if(pretty == null) {
		pretty = false;
	}
	var printer = new haxe_xml_Printer(pretty);
	printer.writeNode(xml,"");
	return printer.output.b;
};
haxe_xml_Printer.prototype = {
	output: null
	,pretty: null
	,writeNode: function(value,tabs) {
		switch(value.nodeType) {
		case 0:
			this.output.b += Std.string(tabs + "<");
			if(value.nodeType != Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, expected Element but found " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			this.output.b += Std.string(value.nodeName);
			var attribute = value.attributes();
			while(attribute.hasNext()) {
				var attribute1 = attribute.next();
				this.output.b += Std.string(" " + attribute1 + "=\"");
				var input = StringTools.htmlEscape(value.get(attribute1),true);
				this.output.b += Std.string(input);
				this.output.b += "\"";
			}
			if(this.hasChildren(value)) {
				this.output.b += ">";
				if(this.pretty) {
					this.output.b += "\n";
				}
				if(value.nodeType != Xml.Document && value.nodeType != Xml.Element) {
					throw haxe_Exception.thrown("Bad node type, expected Element or Document but found " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
				}
				var _g_current = 0;
				var _g_array = value.children;
				while(_g_current < _g_array.length) {
					var child = _g_array[_g_current++];
					this.writeNode(child,this.pretty ? tabs + "\t" : tabs);
				}
				this.output.b += Std.string(tabs + "</");
				if(value.nodeType != Xml.Element) {
					throw haxe_Exception.thrown("Bad node type, expected Element but found " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
				}
				this.output.b += Std.string(value.nodeName);
				this.output.b += ">";
				if(this.pretty) {
					this.output.b += "\n";
				}
			} else {
				this.output.b += "/>";
				if(this.pretty) {
					this.output.b += "\n";
				}
			}
			break;
		case 1:
			if(value.nodeType == Xml.Document || value.nodeType == Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, unexpected " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			var nodeValue = value.nodeValue;
			if(nodeValue.length != 0) {
				var input = tabs + StringTools.htmlEscape(nodeValue);
				this.output.b += Std.string(input);
				if(this.pretty) {
					this.output.b += "\n";
				}
			}
			break;
		case 2:
			this.output.b += Std.string(tabs + "<![CDATA[");
			if(value.nodeType == Xml.Document || value.nodeType == Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, unexpected " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			this.output.b += Std.string(value.nodeValue);
			this.output.b += "]]>";
			if(this.pretty) {
				this.output.b += "\n";
			}
			break;
		case 3:
			if(value.nodeType == Xml.Document || value.nodeType == Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, unexpected " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			var commentContent = value.nodeValue;
			var _this_r = new RegExp("[\n\r\t]+","g".split("u").join(""));
			commentContent = commentContent.replace(_this_r,"");
			commentContent = "<!--" + commentContent + "-->";
			this.output.b += tabs == null ? "null" : "" + tabs;
			var input = StringTools.trim(commentContent);
			this.output.b += Std.string(input);
			if(this.pretty) {
				this.output.b += "\n";
			}
			break;
		case 4:
			if(value.nodeType == Xml.Document || value.nodeType == Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, unexpected " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			this.output.b += Std.string("<!DOCTYPE " + value.nodeValue + ">");
			if(this.pretty) {
				this.output.b += "\n";
			}
			break;
		case 5:
			if(value.nodeType == Xml.Document || value.nodeType == Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, unexpected " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			this.output.b += Std.string("<?" + value.nodeValue + "?>");
			if(this.pretty) {
				this.output.b += "\n";
			}
			break;
		case 6:
			if(value.nodeType != Xml.Document && value.nodeType != Xml.Element) {
				throw haxe_Exception.thrown("Bad node type, expected Element or Document but found " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
			}
			var _g_current = 0;
			var _g_array = value.children;
			while(_g_current < _g_array.length) {
				var child = _g_array[_g_current++];
				this.writeNode(child,tabs);
			}
			break;
		}
	}
	,hasChildren: function(value) {
		if(value.nodeType != Xml.Document && value.nodeType != Xml.Element) {
			throw haxe_Exception.thrown("Bad node type, expected Element or Document but found " + (value.nodeType == null ? "null" : XmlType.toString(value.nodeType)));
		}
		var _g_current = 0;
		var _g_array = value.children;
		while(_g_current < _g_array.length) {
			var child = _g_array[_g_current++];
			switch(child.nodeType) {
			case 0:case 1:
				return true;
			case 2:case 3:
				if(child.nodeType == Xml.Document || child.nodeType == Xml.Element) {
					throw haxe_Exception.thrown("Bad node type, unexpected " + (child.nodeType == null ? "null" : XmlType.toString(child.nodeType)));
				}
				if(StringTools.ltrim(child.nodeValue).length != 0) {
					return true;
				}
				break;
			default:
			}
		}
		return false;
	}
	,__class__: haxe_xml_Printer
};
var hx_strings_AnyAsString = {};
hx_strings_AnyAsString.fromBool = function(value) {
	if(value) {
		return "true";
	} else {
		return "false";
	}
};
hx_strings_AnyAsString.fromAny = function(value) {
	return Std.string(value);
};
var hx_strings__$Char_CharCaseMapper = function() {
	this.mapL2U = new haxe_ds_IntMap();
	this.mapU2L = new haxe_ds_IntMap();
	this._addCaseMapping(97,65);
	this._addCaseMapping(98,66);
	this._addCaseMapping(99,67);
	this._addCaseMapping(100,68);
	this._addCaseMapping(101,69);
	this._addCaseMapping(102,70);
	this._addCaseMapping(103,71);
	this._addCaseMapping(104,72);
	this._addCaseMapping(105,73);
	this._addCaseMapping(106,74);
	this._addCaseMapping(107,75);
	this._addCaseMapping(108,76);
	this._addCaseMapping(109,77);
	this._addCaseMapping(110,78);
	this._addCaseMapping(111,79);
	this._addCaseMapping(112,80);
	this._addCaseMapping(113,81);
	this._addCaseMapping(114,82);
	this._addCaseMapping(115,83);
	this._addCaseMapping(116,84);
	this._addCaseMapping(117,85);
	this._addCaseMapping(118,86);
	this._addCaseMapping(119,87);
	this._addCaseMapping(120,88);
	this._addCaseMapping(121,89);
	this._addCaseMapping(122,90);
	this._addCaseMapping(224,192);
	this._addCaseMapping(225,193);
	this._addCaseMapping(226,194);
	this._addCaseMapping(227,195);
	this._addCaseMapping(228,196);
	this._addCaseMapping(229,197);
	this._addCaseMapping(230,198);
	this._addCaseMapping(231,199);
	this._addCaseMapping(232,200);
	this._addCaseMapping(233,201);
	this._addCaseMapping(234,202);
	this._addCaseMapping(235,203);
	this._addCaseMapping(236,204);
	this._addCaseMapping(237,205);
	this._addCaseMapping(238,206);
	this._addCaseMapping(239,207);
	this._addCaseMapping(240,208);
	this._addCaseMapping(241,209);
	this._addCaseMapping(242,210);
	this._addCaseMapping(243,211);
	this._addCaseMapping(244,212);
	this._addCaseMapping(245,213);
	this._addCaseMapping(246,214);
	this._addCaseMapping(248,216);
	this._addCaseMapping(249,217);
	this._addCaseMapping(250,218);
	this._addCaseMapping(251,219);
	this._addCaseMapping(252,220);
	this._addCaseMapping(253,221);
	this._addCaseMapping(254,222);
	this._addCaseMapping(255,376);
	this._addCaseMapping(257,256);
	this._addCaseMapping(259,258);
	this._addCaseMapping(261,260);
	this._addCaseMapping(263,262);
	this._addCaseMapping(265,264);
	this._addCaseMapping(267,266);
	this._addCaseMapping(269,268);
	this._addCaseMapping(271,270);
	this._addCaseMapping(273,272);
	this._addCaseMapping(275,274);
	this._addCaseMapping(277,276);
	this._addCaseMapping(279,278);
	this._addCaseMapping(281,280);
	this._addCaseMapping(283,282);
	this._addCaseMapping(285,284);
	this._addCaseMapping(287,286);
	this._addCaseMapping(289,288);
	this._addCaseMapping(291,290);
	this._addCaseMapping(293,292);
	this._addCaseMapping(295,294);
	this._addCaseMapping(297,296);
	this._addCaseMapping(299,298);
	this._addCaseMapping(301,300);
	this._addCaseMapping(303,302);
	this._addCaseMapping(305,73);
	this._addCaseMapping(307,306);
	this._addCaseMapping(309,308);
	this._addCaseMapping(311,310);
	this._addCaseMapping(314,313);
	this._addCaseMapping(316,315);
	this._addCaseMapping(318,317);
	this._addCaseMapping(320,319);
	this._addCaseMapping(322,321);
	this._addCaseMapping(324,323);
	this._addCaseMapping(326,325);
	this._addCaseMapping(328,327);
	this._addCaseMapping(331,330);
	this._addCaseMapping(333,332);
	this._addCaseMapping(335,334);
	this._addCaseMapping(337,336);
	this._addCaseMapping(339,338);
	this._addCaseMapping(341,340);
	this._addCaseMapping(343,342);
	this._addCaseMapping(345,344);
	this._addCaseMapping(347,346);
	this._addCaseMapping(349,348);
	this._addCaseMapping(351,350);
	this._addCaseMapping(353,352);
	this._addCaseMapping(355,354);
	this._addCaseMapping(357,356);
	this._addCaseMapping(359,358);
	this._addCaseMapping(361,360);
	this._addCaseMapping(363,362);
	this._addCaseMapping(365,364);
	this._addCaseMapping(367,366);
	this._addCaseMapping(369,368);
	this._addCaseMapping(371,370);
	this._addCaseMapping(373,372);
	this._addCaseMapping(375,374);
	this._addCaseMapping(378,377);
	this._addCaseMapping(380,379);
	this._addCaseMapping(382,381);
	this._addCaseMapping(387,386);
	this._addCaseMapping(389,388);
	this._addCaseMapping(392,391);
	this._addCaseMapping(396,395);
	this._addCaseMapping(402,401);
	this._addCaseMapping(409,408);
	this._addCaseMapping(417,416);
	this._addCaseMapping(419,418);
	this._addCaseMapping(421,420);
	this._addCaseMapping(424,423);
	this._addCaseMapping(429,428);
	this._addCaseMapping(432,431);
	this._addCaseMapping(436,435);
	this._addCaseMapping(438,437);
	this._addCaseMapping(441,440);
	this._addCaseMapping(445,444);
	this._addCaseMapping(454,452);
	this._addCaseMapping(457,455);
	this._addCaseMapping(460,458);
	this._addCaseMapping(462,461);
	this._addCaseMapping(464,463);
	this._addCaseMapping(466,465);
	this._addCaseMapping(468,467);
	this._addCaseMapping(470,469);
	this._addCaseMapping(472,471);
	this._addCaseMapping(474,473);
	this._addCaseMapping(476,475);
	this._addCaseMapping(479,478);
	this._addCaseMapping(481,480);
	this._addCaseMapping(483,482);
	this._addCaseMapping(485,484);
	this._addCaseMapping(487,486);
	this._addCaseMapping(489,488);
	this._addCaseMapping(491,490);
	this._addCaseMapping(493,492);
	this._addCaseMapping(495,494);
	this._addCaseMapping(499,497);
	this._addCaseMapping(501,500);
	this._addCaseMapping(507,506);
	this._addCaseMapping(509,508);
	this._addCaseMapping(511,510);
	this._addCaseMapping(513,512);
	this._addCaseMapping(515,514);
	this._addCaseMapping(517,516);
	this._addCaseMapping(519,518);
	this._addCaseMapping(521,520);
	this._addCaseMapping(523,522);
	this._addCaseMapping(525,524);
	this._addCaseMapping(527,526);
	this._addCaseMapping(529,528);
	this._addCaseMapping(531,530);
	this._addCaseMapping(533,532);
	this._addCaseMapping(535,534);
	this._addCaseMapping(595,385);
	this._addCaseMapping(596,390);
	this._addCaseMapping(599,394);
	this._addCaseMapping(600,398);
	this._addCaseMapping(601,399);
	this._addCaseMapping(603,400);
	this._addCaseMapping(608,403);
	this._addCaseMapping(611,404);
	this._addCaseMapping(616,407);
	this._addCaseMapping(617,406);
	this._addCaseMapping(623,412);
	this._addCaseMapping(626,413);
	this._addCaseMapping(629,415);
	this._addCaseMapping(643,425);
	this._addCaseMapping(648,430);
	this._addCaseMapping(650,433);
	this._addCaseMapping(651,434);
	this._addCaseMapping(658,439);
	this._addCaseMapping(924,181);
	this._addCaseMapping(940,902);
	this._addCaseMapping(941,904);
	this._addCaseMapping(942,905);
	this._addCaseMapping(943,906);
	this._addCaseMapping(945,913);
	this._addCaseMapping(946,914);
	this._addCaseMapping(947,915);
	this._addCaseMapping(948,916);
	this._addCaseMapping(949,917);
	this._addCaseMapping(950,918);
	this._addCaseMapping(951,919);
	this._addCaseMapping(952,920);
	this._addCaseMapping(953,921);
	this._addCaseMapping(954,922);
	this._addCaseMapping(955,923);
	this._addCaseMapping(956,924);
	this._addCaseMapping(957,925);
	this._addCaseMapping(958,926);
	this._addCaseMapping(959,927);
	this._addCaseMapping(960,928);
	this._addCaseMapping(961,929);
	this._addCaseMapping(963,931);
	this._addCaseMapping(964,932);
	this._addCaseMapping(965,933);
	this._addCaseMapping(966,934);
	this._addCaseMapping(967,935);
	this._addCaseMapping(968,936);
	this._addCaseMapping(969,937);
	this._addCaseMapping(970,938);
	this._addCaseMapping(971,939);
	this._addCaseMapping(972,908);
	this._addCaseMapping(973,910);
	this._addCaseMapping(974,911);
	this._addCaseMapping(995,994);
	this._addCaseMapping(997,996);
	this._addCaseMapping(999,998);
	this._addCaseMapping(1001,1000);
	this._addCaseMapping(1003,1002);
	this._addCaseMapping(1005,1004);
	this._addCaseMapping(1007,1006);
	this._addCaseMapping(1072,1040);
	this._addCaseMapping(1073,1041);
	this._addCaseMapping(1074,1042);
	this._addCaseMapping(1075,1043);
	this._addCaseMapping(1076,1044);
	this._addCaseMapping(1077,1045);
	this._addCaseMapping(1078,1046);
	this._addCaseMapping(1079,1047);
	this._addCaseMapping(1080,1048);
	this._addCaseMapping(1081,1049);
	this._addCaseMapping(1082,1050);
	this._addCaseMapping(1083,1051);
	this._addCaseMapping(1084,1052);
	this._addCaseMapping(1085,1053);
	this._addCaseMapping(1086,1054);
	this._addCaseMapping(1087,1055);
	this._addCaseMapping(1088,1056);
	this._addCaseMapping(1089,1057);
	this._addCaseMapping(1090,1058);
	this._addCaseMapping(1091,1059);
	this._addCaseMapping(1092,1060);
	this._addCaseMapping(1093,1061);
	this._addCaseMapping(1094,1062);
	this._addCaseMapping(1095,1063);
	this._addCaseMapping(1096,1064);
	this._addCaseMapping(1097,1065);
	this._addCaseMapping(1098,1066);
	this._addCaseMapping(1099,1067);
	this._addCaseMapping(1100,1068);
	this._addCaseMapping(1101,1069);
	this._addCaseMapping(1102,1070);
	this._addCaseMapping(1103,1071);
	this._addCaseMapping(1105,1025);
	this._addCaseMapping(1106,1026);
	this._addCaseMapping(1107,1027);
	this._addCaseMapping(1108,1028);
	this._addCaseMapping(1109,1029);
	this._addCaseMapping(1110,1030);
	this._addCaseMapping(1111,1031);
	this._addCaseMapping(1112,1032);
	this._addCaseMapping(1113,1033);
	this._addCaseMapping(1114,1034);
	this._addCaseMapping(1115,1035);
	this._addCaseMapping(1116,1036);
	this._addCaseMapping(1118,1038);
	this._addCaseMapping(1119,1039);
	this._addCaseMapping(1121,1120);
	this._addCaseMapping(1123,1122);
	this._addCaseMapping(1125,1124);
	this._addCaseMapping(1127,1126);
	this._addCaseMapping(1129,1128);
	this._addCaseMapping(1131,1130);
	this._addCaseMapping(1133,1132);
	this._addCaseMapping(1135,1134);
	this._addCaseMapping(1137,1136);
	this._addCaseMapping(1139,1138);
	this._addCaseMapping(1141,1140);
	this._addCaseMapping(1143,1142);
	this._addCaseMapping(1145,1144);
	this._addCaseMapping(1147,1146);
	this._addCaseMapping(1149,1148);
	this._addCaseMapping(1151,1150);
	this._addCaseMapping(1153,1152);
	this._addCaseMapping(1169,1168);
	this._addCaseMapping(1171,1170);
	this._addCaseMapping(1173,1172);
	this._addCaseMapping(1175,1174);
	this._addCaseMapping(1177,1176);
	this._addCaseMapping(1179,1178);
	this._addCaseMapping(1181,1180);
	this._addCaseMapping(1183,1182);
	this._addCaseMapping(1185,1184);
	this._addCaseMapping(1187,1186);
	this._addCaseMapping(1189,1188);
	this._addCaseMapping(1191,1190);
	this._addCaseMapping(1193,1192);
	this._addCaseMapping(1195,1194);
	this._addCaseMapping(1197,1196);
	this._addCaseMapping(1199,1198);
	this._addCaseMapping(1201,1200);
	this._addCaseMapping(1203,1202);
	this._addCaseMapping(1205,1204);
	this._addCaseMapping(1207,1206);
	this._addCaseMapping(1209,1208);
	this._addCaseMapping(1211,1210);
	this._addCaseMapping(1213,1212);
	this._addCaseMapping(1215,1214);
	this._addCaseMapping(1218,1217);
	this._addCaseMapping(1220,1219);
	this._addCaseMapping(1224,1223);
	this._addCaseMapping(1228,1227);
	this._addCaseMapping(1233,1232);
	this._addCaseMapping(1235,1234);
	this._addCaseMapping(1237,1236);
	this._addCaseMapping(1239,1238);
	this._addCaseMapping(1241,1240);
	this._addCaseMapping(1243,1242);
	this._addCaseMapping(1245,1244);
	this._addCaseMapping(1247,1246);
	this._addCaseMapping(1249,1248);
	this._addCaseMapping(1251,1250);
	this._addCaseMapping(1253,1252);
	this._addCaseMapping(1255,1254);
	this._addCaseMapping(1257,1256);
	this._addCaseMapping(1259,1258);
	this._addCaseMapping(1263,1262);
	this._addCaseMapping(1265,1264);
	this._addCaseMapping(1267,1266);
	this._addCaseMapping(1269,1268);
	this._addCaseMapping(1273,1272);
	this._addCaseMapping(1377,1329);
	this._addCaseMapping(1378,1330);
	this._addCaseMapping(1379,1331);
	this._addCaseMapping(1380,1332);
	this._addCaseMapping(1381,1333);
	this._addCaseMapping(1382,1334);
	this._addCaseMapping(1383,1335);
	this._addCaseMapping(1384,1336);
	this._addCaseMapping(1385,1337);
	this._addCaseMapping(1386,1338);
	this._addCaseMapping(1387,1339);
	this._addCaseMapping(1388,1340);
	this._addCaseMapping(1389,1341);
	this._addCaseMapping(1390,1342);
	this._addCaseMapping(1391,1343);
	this._addCaseMapping(1392,1344);
	this._addCaseMapping(1393,1345);
	this._addCaseMapping(1394,1346);
	this._addCaseMapping(1395,1347);
	this._addCaseMapping(1396,1348);
	this._addCaseMapping(1397,1349);
	this._addCaseMapping(1398,1350);
	this._addCaseMapping(1399,1351);
	this._addCaseMapping(1400,1352);
	this._addCaseMapping(1401,1353);
	this._addCaseMapping(1402,1354);
	this._addCaseMapping(1403,1355);
	this._addCaseMapping(1404,1356);
	this._addCaseMapping(1405,1357);
	this._addCaseMapping(1406,1358);
	this._addCaseMapping(1407,1359);
	this._addCaseMapping(1408,1360);
	this._addCaseMapping(1409,1361);
	this._addCaseMapping(1410,1362);
	this._addCaseMapping(1411,1363);
	this._addCaseMapping(1412,1364);
	this._addCaseMapping(1413,1365);
	this._addCaseMapping(1414,1366);
	this._addCaseMapping(4304,4256);
	this._addCaseMapping(4305,4257);
	this._addCaseMapping(4306,4258);
	this._addCaseMapping(4307,4259);
	this._addCaseMapping(4308,4260);
	this._addCaseMapping(4309,4261);
	this._addCaseMapping(4310,4262);
	this._addCaseMapping(4311,4263);
	this._addCaseMapping(4312,4264);
	this._addCaseMapping(4313,4265);
	this._addCaseMapping(4314,4266);
	this._addCaseMapping(4315,4267);
	this._addCaseMapping(4316,4268);
	this._addCaseMapping(4317,4269);
	this._addCaseMapping(4318,4270);
	this._addCaseMapping(4319,4271);
	this._addCaseMapping(4320,4272);
	this._addCaseMapping(4321,4273);
	this._addCaseMapping(4322,4274);
	this._addCaseMapping(4323,4275);
	this._addCaseMapping(4324,4276);
	this._addCaseMapping(4325,4277);
	this._addCaseMapping(4326,4278);
	this._addCaseMapping(4327,4279);
	this._addCaseMapping(4328,4280);
	this._addCaseMapping(4329,4281);
	this._addCaseMapping(4330,4282);
	this._addCaseMapping(4331,4283);
	this._addCaseMapping(4332,4284);
	this._addCaseMapping(4333,4285);
	this._addCaseMapping(4334,4286);
	this._addCaseMapping(4335,4287);
	this._addCaseMapping(4336,4288);
	this._addCaseMapping(4337,4289);
	this._addCaseMapping(4338,4290);
	this._addCaseMapping(4339,4291);
	this._addCaseMapping(4340,4292);
	this._addCaseMapping(4341,4293);
	this._addCaseMapping(7681,7680);
	this._addCaseMapping(7683,7682);
	this._addCaseMapping(7685,7684);
	this._addCaseMapping(7687,7686);
	this._addCaseMapping(7689,7688);
	this._addCaseMapping(7691,7690);
	this._addCaseMapping(7693,7692);
	this._addCaseMapping(7695,7694);
	this._addCaseMapping(7697,7696);
	this._addCaseMapping(7699,7698);
	this._addCaseMapping(7701,7700);
	this._addCaseMapping(7703,7702);
	this._addCaseMapping(7705,7704);
	this._addCaseMapping(7707,7706);
	this._addCaseMapping(7709,7708);
	this._addCaseMapping(7711,7710);
	this._addCaseMapping(7713,7712);
	this._addCaseMapping(7715,7714);
	this._addCaseMapping(7717,7716);
	this._addCaseMapping(7719,7718);
	this._addCaseMapping(7721,7720);
	this._addCaseMapping(7723,7722);
	this._addCaseMapping(7725,7724);
	this._addCaseMapping(7727,7726);
	this._addCaseMapping(7729,7728);
	this._addCaseMapping(7731,7730);
	this._addCaseMapping(7733,7732);
	this._addCaseMapping(7735,7734);
	this._addCaseMapping(7737,7736);
	this._addCaseMapping(7739,7738);
	this._addCaseMapping(7741,7740);
	this._addCaseMapping(7743,7742);
	this._addCaseMapping(7745,7744);
	this._addCaseMapping(7747,7746);
	this._addCaseMapping(7749,7748);
	this._addCaseMapping(7751,7750);
	this._addCaseMapping(7753,7752);
	this._addCaseMapping(7755,7754);
	this._addCaseMapping(7757,7756);
	this._addCaseMapping(7759,7758);
	this._addCaseMapping(7761,7760);
	this._addCaseMapping(7763,7762);
	this._addCaseMapping(7765,7764);
	this._addCaseMapping(7767,7766);
	this._addCaseMapping(7769,7768);
	this._addCaseMapping(7771,7770);
	this._addCaseMapping(7773,7772);
	this._addCaseMapping(7775,7774);
	this._addCaseMapping(7777,7776);
	this._addCaseMapping(7779,7778);
	this._addCaseMapping(7781,7780);
	this._addCaseMapping(7783,7782);
	this._addCaseMapping(7785,7784);
	this._addCaseMapping(7787,7786);
	this._addCaseMapping(7789,7788);
	this._addCaseMapping(7791,7790);
	this._addCaseMapping(7793,7792);
	this._addCaseMapping(7795,7794);
	this._addCaseMapping(7797,7796);
	this._addCaseMapping(7799,7798);
	this._addCaseMapping(7801,7800);
	this._addCaseMapping(7803,7802);
	this._addCaseMapping(7805,7804);
	this._addCaseMapping(7807,7806);
	this._addCaseMapping(7809,7808);
	this._addCaseMapping(7811,7810);
	this._addCaseMapping(7813,7812);
	this._addCaseMapping(7815,7814);
	this._addCaseMapping(7817,7816);
	this._addCaseMapping(7819,7818);
	this._addCaseMapping(7821,7820);
	this._addCaseMapping(7823,7822);
	this._addCaseMapping(7825,7824);
	this._addCaseMapping(7827,7826);
	this._addCaseMapping(7829,7828);
	this._addCaseMapping(7841,7840);
	this._addCaseMapping(7843,7842);
	this._addCaseMapping(7845,7844);
	this._addCaseMapping(7847,7846);
	this._addCaseMapping(7849,7848);
	this._addCaseMapping(7851,7850);
	this._addCaseMapping(7853,7852);
	this._addCaseMapping(7855,7854);
	this._addCaseMapping(7857,7856);
	this._addCaseMapping(7859,7858);
	this._addCaseMapping(7861,7860);
	this._addCaseMapping(7863,7862);
	this._addCaseMapping(7865,7864);
	this._addCaseMapping(7867,7866);
	this._addCaseMapping(7869,7868);
	this._addCaseMapping(7871,7870);
	this._addCaseMapping(7873,7872);
	this._addCaseMapping(7875,7874);
	this._addCaseMapping(7877,7876);
	this._addCaseMapping(7879,7878);
	this._addCaseMapping(7881,7880);
	this._addCaseMapping(7883,7882);
	this._addCaseMapping(7885,7884);
	this._addCaseMapping(7887,7886);
	this._addCaseMapping(7889,7888);
	this._addCaseMapping(7891,7890);
	this._addCaseMapping(7893,7892);
	this._addCaseMapping(7895,7894);
	this._addCaseMapping(7897,7896);
	this._addCaseMapping(7899,7898);
	this._addCaseMapping(7901,7900);
	this._addCaseMapping(7903,7902);
	this._addCaseMapping(7905,7904);
	this._addCaseMapping(7907,7906);
	this._addCaseMapping(7909,7908);
	this._addCaseMapping(7911,7910);
	this._addCaseMapping(7913,7912);
	this._addCaseMapping(7915,7914);
	this._addCaseMapping(7917,7916);
	this._addCaseMapping(7919,7918);
	this._addCaseMapping(7921,7920);
	this._addCaseMapping(7923,7922);
	this._addCaseMapping(7925,7924);
	this._addCaseMapping(7927,7926);
	this._addCaseMapping(7929,7928);
	this._addCaseMapping(7936,7944);
	this._addCaseMapping(7937,7945);
	this._addCaseMapping(7938,7946);
	this._addCaseMapping(7939,7947);
	this._addCaseMapping(7940,7948);
	this._addCaseMapping(7941,7949);
	this._addCaseMapping(7942,7950);
	this._addCaseMapping(7943,7951);
	this._addCaseMapping(7952,7960);
	this._addCaseMapping(7953,7961);
	this._addCaseMapping(7954,7962);
	this._addCaseMapping(7955,7963);
	this._addCaseMapping(7956,7964);
	this._addCaseMapping(7957,7965);
	this._addCaseMapping(7968,7976);
	this._addCaseMapping(7969,7977);
	this._addCaseMapping(7970,7978);
	this._addCaseMapping(7971,7979);
	this._addCaseMapping(7972,7980);
	this._addCaseMapping(7973,7981);
	this._addCaseMapping(7974,7982);
	this._addCaseMapping(7975,7983);
	this._addCaseMapping(7984,7992);
	this._addCaseMapping(7985,7993);
	this._addCaseMapping(7986,7994);
	this._addCaseMapping(7987,7995);
	this._addCaseMapping(7988,7996);
	this._addCaseMapping(7989,7997);
	this._addCaseMapping(7990,7998);
	this._addCaseMapping(7991,7999);
	this._addCaseMapping(8000,8008);
	this._addCaseMapping(8001,8009);
	this._addCaseMapping(8002,8010);
	this._addCaseMapping(8003,8011);
	this._addCaseMapping(8004,8012);
	this._addCaseMapping(8005,8013);
	this._addCaseMapping(8017,8025);
	this._addCaseMapping(8019,8027);
	this._addCaseMapping(8021,8029);
	this._addCaseMapping(8023,8031);
	this._addCaseMapping(8032,8040);
	this._addCaseMapping(8033,8041);
	this._addCaseMapping(8034,8042);
	this._addCaseMapping(8035,8043);
	this._addCaseMapping(8036,8044);
	this._addCaseMapping(8037,8045);
	this._addCaseMapping(8038,8046);
	this._addCaseMapping(8039,8047);
	this._addCaseMapping(8064,8072);
	this._addCaseMapping(8065,8073);
	this._addCaseMapping(8066,8074);
	this._addCaseMapping(8067,8075);
	this._addCaseMapping(8068,8076);
	this._addCaseMapping(8069,8077);
	this._addCaseMapping(8070,8078);
	this._addCaseMapping(8071,8079);
	this._addCaseMapping(8080,8088);
	this._addCaseMapping(8081,8089);
	this._addCaseMapping(8082,8090);
	this._addCaseMapping(8083,8091);
	this._addCaseMapping(8084,8092);
	this._addCaseMapping(8085,8093);
	this._addCaseMapping(8086,8094);
	this._addCaseMapping(8087,8095);
	this._addCaseMapping(8096,8104);
	this._addCaseMapping(8097,8105);
	this._addCaseMapping(8098,8106);
	this._addCaseMapping(8099,8107);
	this._addCaseMapping(8100,8108);
	this._addCaseMapping(8101,8109);
	this._addCaseMapping(8102,8110);
	this._addCaseMapping(8103,8111);
	this._addCaseMapping(8112,8120);
	this._addCaseMapping(8113,8121);
	this._addCaseMapping(8144,8152);
	this._addCaseMapping(8145,8153);
	this._addCaseMapping(8160,8168);
	this._addCaseMapping(8161,8169);
	this._addCaseMapping(9424,9398);
	this._addCaseMapping(9425,9399);
	this._addCaseMapping(9426,9400);
	this._addCaseMapping(9427,9401);
	this._addCaseMapping(9428,9402);
	this._addCaseMapping(9429,9403);
	this._addCaseMapping(9430,9404);
	this._addCaseMapping(9431,9405);
	this._addCaseMapping(9432,9406);
	this._addCaseMapping(9433,9407);
	this._addCaseMapping(9434,9408);
	this._addCaseMapping(9435,9409);
	this._addCaseMapping(9436,9410);
	this._addCaseMapping(9437,9411);
	this._addCaseMapping(9438,9412);
	this._addCaseMapping(9439,9413);
	this._addCaseMapping(9440,9414);
	this._addCaseMapping(9441,9415);
	this._addCaseMapping(9442,9416);
	this._addCaseMapping(9443,9417);
	this._addCaseMapping(9444,9418);
	this._addCaseMapping(9445,9419);
	this._addCaseMapping(9446,9420);
	this._addCaseMapping(9447,9421);
	this._addCaseMapping(9448,9422);
	this._addCaseMapping(9449,9423);
	this._addCaseMapping(65345,65313);
	this._addCaseMapping(65346,65314);
	this._addCaseMapping(65347,65315);
	this._addCaseMapping(65348,65316);
	this._addCaseMapping(65349,65317);
	this._addCaseMapping(65350,65318);
	this._addCaseMapping(65351,65319);
	this._addCaseMapping(65352,65320);
	this._addCaseMapping(65353,65321);
	this._addCaseMapping(65354,65322);
	this._addCaseMapping(65355,65323);
	this._addCaseMapping(65356,65324);
	this._addCaseMapping(65357,65325);
	this._addCaseMapping(65358,65326);
	this._addCaseMapping(65359,65327);
	this._addCaseMapping(65360,65328);
	this._addCaseMapping(65361,65329);
	this._addCaseMapping(65362,65330);
	this._addCaseMapping(65363,65331);
	this._addCaseMapping(65364,65332);
	this._addCaseMapping(65365,65333);
	this._addCaseMapping(65366,65334);
	this._addCaseMapping(65367,65335);
	this._addCaseMapping(65368,65336);
	this._addCaseMapping(65369,65337);
	this._addCaseMapping(65370,65338);
};
hx_strings__$Char_CharCaseMapper.__name__ = "hx.strings._Char.CharCaseMapper";
hx_strings__$Char_CharCaseMapper.prototype = {
	mapU2L: null
	,mapL2U: null
	,_addCaseMapping: function(lowerChar,upperChar) {
		if(!this.mapU2L.h.hasOwnProperty(upperChar)) {
			this.mapU2L.h[upperChar] = lowerChar;
		}
		if(!this.mapL2U.h.hasOwnProperty(lowerChar)) {
			this.mapL2U.h[lowerChar] = upperChar;
		}
	}
	,isLowerCase: function(ch) {
		return this.mapL2U.h.hasOwnProperty(ch);
	}
	,isUpperCase: function(ch) {
		return this.mapU2L.h.hasOwnProperty(ch);
	}
	,toLowerCase: function(ch) {
		var lowerChar = this.mapU2L.h[ch];
		if(lowerChar == null) {
			return ch;
		} else {
			return lowerChar;
		}
	}
	,toUpperCase: function(ch) {
		var upperChar = this.mapL2U.h[ch];
		if(upperChar == null) {
			return ch;
		} else {
			return upperChar;
		}
	}
	,__class__: hx_strings__$Char_CharCaseMapper
};
var hx_strings_Char = {};
hx_strings_Char.fromString = function(str) {
	return hx_strings_Strings.charCodeAt8(str,0);
};
hx_strings_Char.of = function(ch) {
	return ch;
};
hx_strings_Char.op_plus_string = function(ch,other) {
	return String.fromCodePoint(ch) + other;
};
hx_strings_Char.op_plus_string2 = function(str,ch) {
	return str + String.fromCodePoint(ch);
};
hx_strings_Char.op_plus = function(ch,other) {
	return ch + other;
};
hx_strings_Char.isAscii = function(this1) {
	if(this1 > -1) {
		return this1 < 128;
	} else {
		return false;
	}
};
hx_strings_Char.isAsciiAlpha = function(this1) {
	if(!(this1 > 64 && this1 < 91)) {
		if(this1 > 96) {
			return this1 < 123;
		} else {
			return false;
		}
	} else {
		return true;
	}
};
hx_strings_Char.isAsciiAlphanumeric = function(this1) {
	if(!(this1 > 64 && this1 < 91 || this1 > 96 && this1 < 123)) {
		if(this1 > 47) {
			return this1 < 58;
		} else {
			return false;
		}
	} else {
		return true;
	}
};
hx_strings_Char.isAsciiControl = function(this1) {
	if(!(this1 > -1 && this1 < 32)) {
		return this1 == 127;
	} else {
		return true;
	}
};
hx_strings_Char.isAsciiPrintable = function(this1) {
	if(this1 > 31) {
		return this1 < 127;
	} else {
		return false;
	}
};
hx_strings_Char.isDigit = function(this1) {
	if(this1 > 47) {
		return this1 < 58;
	} else {
		return false;
	}
};
hx_strings_Char.isEOF = function(this1) {
	return this1 != this1;
};
hx_strings_Char.isSpace = function(this1) {
	return this1 == 32;
};
hx_strings_Char.isUTF8 = function(this1) {
	if(this1 > -1) {
		return this1 < 1114112;
	} else {
		return false;
	}
};
hx_strings_Char.isWhitespace = function(this1) {
	if(!(this1 > 8 && this1 < 14)) {
		return this1 == 32;
	} else {
		return true;
	}
};
hx_strings_Char.isLowerCase = function(this1) {
	return hx_strings_Char.CHAR_CASE_MAPPER.mapL2U.h.hasOwnProperty(this1);
};
hx_strings_Char.isUpperCase = function(this1) {
	return hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h.hasOwnProperty(this1);
};
hx_strings_Char.toLowerCase = function(this1) {
	var lowerChar = hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h[this1];
	if(lowerChar == null) {
		return this1;
	} else {
		return lowerChar;
	}
};
hx_strings_Char.toUpperCase = function(this1) {
	var upperChar = hx_strings_Char.CHAR_CASE_MAPPER.mapL2U.h[this1];
	if(upperChar == null) {
		return this1;
	} else {
		return upperChar;
	}
};
hx_strings_Char.toInt = function(this1) {
	return this1;
};
hx_strings_Char.toString = function(this1) {
	return String.fromCodePoint(this1);
};
var hx_strings_CharIterator = function(prevBufferSize) {
	this.prevBufferNextIdx = -1;
	this.prevBufferPrevIdx = -1;
	this.currChar = -1;
	this.col = 0;
	this.line = 0;
	this.index = -1;
	var tmp;
	if(prevBufferSize > 0) {
		var this1 = new hx_strings_internal__$RingBuffer_RingBufferImpl(prevBufferSize + 1);
		tmp = this1;
	} else {
		tmp = null;
	}
	this.prevBuffer = tmp;
};
hx_strings_CharIterator.__name__ = "hx.strings.CharIterator";
hx_strings_CharIterator.fromString = function(chars,prevBufferSize) {
	if(prevBufferSize == null) {
		prevBufferSize = 0;
	}
	if(chars == null) {
		return hx_strings__$CharIterator_NullCharIterator.INSTANCE;
	}
	return new hx_strings__$CharIterator_StringCharIterator(chars,prevBufferSize);
};
hx_strings_CharIterator.fromArray = function(chars,prevBufferSize) {
	if(prevBufferSize == null) {
		prevBufferSize = 0;
	}
	if(chars == null) {
		return hx_strings__$CharIterator_NullCharIterator.INSTANCE;
	}
	return new hx_strings__$CharIterator_ArrayCharIterator(chars,prevBufferSize);
};
hx_strings_CharIterator.fromInput = function(chars,prevBufferSize) {
	if(prevBufferSize == null) {
		prevBufferSize = 0;
	}
	if(chars == null) {
		return hx_strings__$CharIterator_NullCharIterator.INSTANCE;
	}
	return new hx_strings__$CharIterator_InputCharIterator(chars,prevBufferSize);
};
hx_strings_CharIterator.fromIterator = function(chars,prevBufferSize) {
	if(prevBufferSize == null) {
		prevBufferSize = 0;
	}
	if(chars == null) {
		return hx_strings__$CharIterator_NullCharIterator.INSTANCE;
	}
	return new hx_strings__$CharIterator_IteratorCharIterator(chars,prevBufferSize);
};
hx_strings_CharIterator.prototype = {
	index: null
	,line: null
	,col: null
	,currChar: null
	,prevBuffer: null
	,prevBufferPrevIdx: null
	,prevBufferNextIdx: null
	,get_current: function() {
		if(this.index > -1) {
			return this.currChar;
		} else {
			return null;
		}
	}
	,get_pos: function() {
		return new hx_strings_CharPos(this.index,this.line,this.col);
	}
	,hasPrev: function() {
		return this.prevBufferPrevIdx > -1;
	}
	,prev: function() {
		if(this.prevBufferPrevIdx <= -1) {
			throw haxe_Exception.thrown(new haxe_io_Eof());
		}
		var prevChar = this.prevBuffer.get(this.prevBufferPrevIdx);
		this.currChar = prevChar.char;
		this.index = prevChar.index;
		this.line = prevChar.line;
		this.col = prevChar.col;
		this.prevBufferNextIdx = this.prevBufferPrevIdx + 1 < this.prevBuffer.length ? this.prevBufferPrevIdx + 1 : -1;
		this.prevBufferPrevIdx--;
		return this.currChar;
	}
	,hasNext: function() {
		if(this.prevBufferNextIdx > -1) {
			return true;
		} else {
			return !this.isEOF();
		}
	}
	,next: function() {
		if(this.prevBufferNextIdx > -1) {
			var prevChar = this.prevBuffer.get(this.prevBufferNextIdx);
			this.currChar = prevChar.char;
			this.index = prevChar.index;
			this.line = prevChar.line;
			this.col = prevChar.col;
			this.prevBufferPrevIdx = this.prevBufferNextIdx - 1;
			this.prevBufferNextIdx = this.prevBufferNextIdx + 1 < this.prevBuffer.length ? this.prevBufferNextIdx + 1 : -1;
			return this.currChar;
		}
		if(this.isEOF()) {
			throw haxe_Exception.thrown(new haxe_io_Eof());
		}
		if(this.currChar == 10 || this.currChar < 0) {
			this.line++;
			this.col = 0;
		}
		this.index++;
		this.col++;
		this.currChar = this.getChar();
		if(this.prevBuffer != null) {
			this.prevBuffer.add(new hx_strings__$CharIterator_CharWithPos(this.currChar,this.index,this.col,this.line));
			this.prevBufferPrevIdx = this.prevBuffer.length - 2;
			this.prevBufferNextIdx = -1;
		}
		return this.currChar;
	}
	,getChar: function() {
		throw haxe_Exception.thrown("Not implemented");
	}
	,isEOF: function() {
		throw haxe_Exception.thrown("Not implemented");
	}
	,__class__: hx_strings_CharIterator
	,__properties__: {get_pos:"get_pos",get_current:"get_current"}
};
var hx_strings_CharPos = function(index,line,col) {
	this.index = index;
	this.line = line;
	this.col = col;
};
hx_strings_CharPos.__name__ = "hx.strings.CharPos";
hx_strings_CharPos.prototype = {
	index: null
	,line: null
	,col: null
	,toString: function() {
		return "CharPos[index=" + this.index + ", line=" + this.line + ", col=" + this.col + "]";
	}
	,__class__: hx_strings_CharPos
};
var hx_strings__$CharIterator_CharWithPos = function(char,index,line,col) {
	hx_strings_CharPos.call(this,index,line,col);
	this.char = char;
};
hx_strings__$CharIterator_CharWithPos.__name__ = "hx.strings._CharIterator.CharWithPos";
hx_strings__$CharIterator_CharWithPos.__super__ = hx_strings_CharPos;
hx_strings__$CharIterator_CharWithPos.prototype = $extend(hx_strings_CharPos.prototype,{
	char: null
	,__class__: hx_strings__$CharIterator_CharWithPos
});
var hx_strings_internal__$RingBuffer_RingBufferImpl = function(size) {
	this.length = 0;
	this.bufferEndIdx = -1;
	this.bufferStartIdx = 0;
	if(size < 1) {
		throw haxe_Exception.thrown("[size] must be > 0");
	}
	var this1 = new Array(size);
	this.buffer = this1;
	this.size = size;
	this.bufferMaxIdx = size - 1;
};
hx_strings_internal__$RingBuffer_RingBufferImpl.__name__ = "hx.strings.internal._RingBuffer.RingBufferImpl";
hx_strings_internal__$RingBuffer_RingBufferImpl.prototype = {
	buffer: null
	,bufferStartIdx: null
	,bufferEndIdx: null
	,bufferMaxIdx: null
	,length: null
	,size: null
	,add: function(item) {
		if(this.length == this.size) {
			this.bufferEndIdx = this.bufferStartIdx;
			this.bufferStartIdx++;
			if(this.bufferStartIdx > this.bufferMaxIdx) {
				this.bufferStartIdx = 0;
			}
		} else {
			this.bufferEndIdx++;
			this.length++;
		}
		this.buffer[this.bufferEndIdx] = item;
	}
	,get: function(index) {
		if(index < 0 || index > this.bufferMaxIdx) {
			throw haxe_Exception.thrown("[index] " + index + " is out of bound");
		}
		var realIdx = this.bufferStartIdx + index;
		if(realIdx > this.bufferMaxIdx) {
			realIdx -= this.length;
		}
		return this.buffer[realIdx];
	}
	,iterator: function() {
		return new hx_strings_internal__$RingBuffer_RingBufferIterator(this);
	}
	,toArray: function() {
		var arr = [];
		var i = this.iterator();
		while(i.hasNext()) {
			var i1 = i.next();
			arr.push(i1);
		}
		return arr;
	}
	,__class__: hx_strings_internal__$RingBuffer_RingBufferImpl
};
var hx_strings__$CharIterator_NullCharIterator = function() {
	hx_strings_CharIterator.call(this,0);
};
hx_strings__$CharIterator_NullCharIterator.__name__ = "hx.strings._CharIterator.NullCharIterator";
hx_strings__$CharIterator_NullCharIterator.__super__ = hx_strings_CharIterator;
hx_strings__$CharIterator_NullCharIterator.prototype = $extend(hx_strings_CharIterator.prototype,{
	isEOF: function() {
		return true;
	}
	,__class__: hx_strings__$CharIterator_NullCharIterator
});
var hx_strings__$CharIterator_ArrayCharIterator = function(chars,prevBufferSize) {
	hx_strings_CharIterator.call(this,prevBufferSize);
	this.chars = chars;
	this.charsMaxIndex = chars.length - 1;
};
hx_strings__$CharIterator_ArrayCharIterator.__name__ = "hx.strings._CharIterator.ArrayCharIterator";
hx_strings__$CharIterator_ArrayCharIterator.__super__ = hx_strings_CharIterator;
hx_strings__$CharIterator_ArrayCharIterator.prototype = $extend(hx_strings_CharIterator.prototype,{
	chars: null
	,charsMaxIndex: null
	,isEOF: function() {
		return this.index >= this.charsMaxIndex;
	}
	,getChar: function() {
		return this.chars[this.index];
	}
	,__class__: hx_strings__$CharIterator_ArrayCharIterator
});
var hx_strings__$CharIterator_IteratorCharIterator = function(chars,prevBufferSize) {
	hx_strings_CharIterator.call(this,prevBufferSize);
	this.chars = chars;
};
hx_strings__$CharIterator_IteratorCharIterator.__name__ = "hx.strings._CharIterator.IteratorCharIterator";
hx_strings__$CharIterator_IteratorCharIterator.__super__ = hx_strings_CharIterator;
hx_strings__$CharIterator_IteratorCharIterator.prototype = $extend(hx_strings_CharIterator.prototype,{
	chars: null
	,isEOF: function() {
		return !this.chars.hasNext();
	}
	,getChar: function() {
		return this.chars.next();
	}
	,__class__: hx_strings__$CharIterator_IteratorCharIterator
});
var hx_strings__$CharIterator_InputCharIterator = function(chars,prevBufferSize) {
	this.nextCharAvailable = null;
	this.nextChar = -1;
	this.currCharIndex = -1;
	this.byteIndex = 0;
	hx_strings_CharIterator.call(this,prevBufferSize);
	this.input = chars;
};
hx_strings__$CharIterator_InputCharIterator.__name__ = "hx.strings._CharIterator.InputCharIterator";
hx_strings__$CharIterator_InputCharIterator.__super__ = hx_strings_CharIterator;
hx_strings__$CharIterator_InputCharIterator.prototype = $extend(hx_strings_CharIterator.prototype,{
	byteIndex: null
	,input: null
	,currCharIndex: null
	,nextChar: null
	,nextCharAvailable: null
	,isEOF: function() {
		if(this.nextCharAvailable == null) {
			try {
				var byte1 = this.input.readByte();
				this.byteIndex++;
				var tmp;
				if(byte1 <= 127) {
					tmp = byte1;
				} else {
					byte1 &= -129;
					byte1 &= -65;
					var totalBytes = 2;
					var isBit6Set = 1 == (byte1 >> 5 & 1);
					var isBit5Set = false;
					if(isBit6Set) {
						byte1 &= -33;
						++totalBytes;
						isBit5Set = 1 == (byte1 >> 4 & 1);
						if(isBit5Set) {
							byte1 &= -17;
							++totalBytes;
							if(1 == (byte1 >> 3 & 1)) {
								throw haxe_Exception.thrown("Valid UTF-8 byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte1 + "]!");
							}
						}
					}
					var result = byte1 << 6 * (totalBytes - 1);
					var byte = this.input.readByte();
					this.byteIndex++;
					if(1 != (byte >> 7 & 1)) {
						throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
					}
					if(1 == (byte >> 6 & 1)) {
						throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
					}
					var byte2 = byte & -129;
					result += byte2 << 6 * (totalBytes - 2);
					if(isBit6Set) {
						var byte = this.input.readByte();
						this.byteIndex++;
						if(1 != (byte >> 7 & 1)) {
							throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
						}
						if(1 == (byte >> 6 & 1)) {
							throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
						}
						var byte3 = byte & -129;
						result += byte3 << 6 * (totalBytes - 3);
						if(isBit5Set) {
							var byte = this.input.readByte();
							this.byteIndex++;
							if(1 != (byte >> 7 & 1)) {
								throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
							}
							if(1 == (byte >> 6 & 1)) {
								throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
							}
							var byte4 = byte & -129;
							result += byte4 << 6 * (totalBytes - 4);
						}
					}
					if(this.index == 0 && result == 65279) {
						var byte1 = this.input.readByte();
						this.byteIndex++;
						if(byte1 <= 127) {
							tmp = byte1;
						} else {
							byte1 &= -129;
							byte1 &= -65;
							var totalBytes = 2;
							var isBit6Set = 1 == (byte1 >> 5 & 1);
							var isBit5Set = false;
							if(isBit6Set) {
								byte1 &= -33;
								++totalBytes;
								isBit5Set = 1 == (byte1 >> 4 & 1);
								if(isBit5Set) {
									byte1 &= -17;
									++totalBytes;
									if(1 == (byte1 >> 3 & 1)) {
										throw haxe_Exception.thrown("Valid UTF-8 byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte1 + "]!");
									}
								}
							}
							var result1 = byte1 << 6 * (totalBytes - 1);
							var byte = this.input.readByte();
							this.byteIndex++;
							if(1 != (byte >> 7 & 1)) {
								throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
							}
							if(1 == (byte >> 6 & 1)) {
								throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
							}
							var byte2 = byte & -129;
							result1 += byte2 << 6 * (totalBytes - 2);
							if(isBit6Set) {
								var byte = this.input.readByte();
								this.byteIndex++;
								if(1 != (byte >> 7 & 1)) {
									throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
								}
								if(1 == (byte >> 6 & 1)) {
									throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
								}
								var byte3 = byte & -129;
								result1 += byte3 << 6 * (totalBytes - 3);
								if(isBit5Set) {
									var byte = this.input.readByte();
									this.byteIndex++;
									if(1 != (byte >> 7 & 1)) {
										throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
									}
									if(1 == (byte >> 6 & 1)) {
										throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
									}
									var byte4 = byte & -129;
									result1 += byte4 << 6 * (totalBytes - 4);
								}
							}
							tmp = this.index == 0 && result1 == 65279 ? this.readUtf8Char() : result1;
						}
					} else {
						tmp = result;
					}
				}
				this.nextChar = tmp;
				this.nextCharAvailable = true;
			} catch( _g ) {
				haxe_NativeStackTrace.lastError = _g;
				if(((haxe_Exception.caught(_g).unwrap()) instanceof haxe_io_Eof)) {
					this.nextCharAvailable = false;
				} else {
					throw _g;
				}
			}
		}
		return this.nextCharAvailable != true;
	}
	,getChar: function() {
		if(this.index != this.currCharIndex) {
			this.currCharIndex = this.index;
			this.nextCharAvailable = null;
			return this.nextChar;
		}
		return this.currChar;
	}
	,readUtf8Char: function() {
		var byte1 = this.input.readByte();
		this.byteIndex++;
		if(byte1 <= 127) {
			return byte1;
		}
		byte1 &= -129;
		byte1 &= -65;
		var totalBytes = 2;
		var isBit6Set = 1 == (byte1 >> 5 & 1);
		var isBit5Set = false;
		if(isBit6Set) {
			byte1 &= -33;
			++totalBytes;
			isBit5Set = 1 == (byte1 >> 4 & 1);
			if(isBit5Set) {
				byte1 &= -17;
				++totalBytes;
				if(1 == (byte1 >> 3 & 1)) {
					throw haxe_Exception.thrown("Valid UTF-8 byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte1 + "]!");
				}
			}
		}
		var result = byte1 << 6 * (totalBytes - 1);
		var byte = this.input.readByte();
		this.byteIndex++;
		if(1 != (byte >> 7 & 1)) {
			throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
		}
		if(1 == (byte >> 6 & 1)) {
			throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
		}
		var byte2 = byte & -129;
		result += byte2 << 6 * (totalBytes - 2);
		if(isBit6Set) {
			var byte = this.input.readByte();
			this.byteIndex++;
			if(1 != (byte >> 7 & 1)) {
				throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
			}
			if(1 == (byte >> 6 & 1)) {
				throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
			}
			var byte3 = byte & -129;
			result += byte3 << 6 * (totalBytes - 3);
			if(isBit5Set) {
				var byte = this.input.readByte();
				this.byteIndex++;
				if(1 != (byte >> 7 & 1)) {
					throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
				}
				if(1 == (byte >> 6 & 1)) {
					throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
				}
				var byte4 = byte & -129;
				result += byte4 << 6 * (totalBytes - 4);
			}
		}
		if(this.index == 0 && result == 65279) {
			return this.readUtf8Char();
		}
		return result;
	}
	,readUtf8MultiSequenceByte: function() {
		var byte = this.input.readByte();
		this.byteIndex++;
		if(1 != (byte >> 7 & 1)) {
			throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
		}
		if(1 == (byte >> 6 & 1)) {
			throw haxe_Exception.thrown("Valid UTF-8 multi-sequence byte expected at position [" + this.byteIndex + "] but found byte with value [" + byte + "]!");
		}
		return byte & -129;
	}
	,__class__: hx_strings__$CharIterator_InputCharIterator
});
var hx_strings__$CharIterator_StringCharIterator = function(chars,prevBufferSize) {
	hx_strings_CharIterator.call(this,prevBufferSize);
	this.chars = chars;
	this.charsMaxIndex = (chars == null ? 0 : chars.length) - 1;
};
hx_strings__$CharIterator_StringCharIterator.__name__ = "hx.strings._CharIterator.StringCharIterator";
hx_strings__$CharIterator_StringCharIterator.__super__ = hx_strings_CharIterator;
hx_strings__$CharIterator_StringCharIterator.prototype = $extend(hx_strings_CharIterator.prototype,{
	chars: null
	,charsMaxIndex: null
	,isEOF: function() {
		return this.index >= this.charsMaxIndex;
	}
	,getChar: function() {
		return HxOverrides.cca(this.chars,this.index);
	}
	,__class__: hx_strings__$CharIterator_StringCharIterator
});
var hx_strings_Pattern = function(pattern,options) {
	this.pattern = pattern;
	this.options = options;
	this.ereg = new EReg(pattern,options);
	this.options += "u";
};
hx_strings_Pattern.__name__ = "hx.strings.Pattern";
hx_strings_Pattern.compile = function(pattern,options) {
	if(options == null) {
		return new hx_strings_Pattern(pattern,"");
	}
	var _g = options;
	var tmp;
	switch(_g._hx_index) {
	case 0:
		var str = _g.v;
		var str1 = hx_strings_Strings.toLowerCase8(str);
		if(str1 == null || str1.length == 0) {
			tmp = str1;
		} else {
			var _g1 = [];
			var _g2 = 0;
			var _g3 = hx_strings_Strings.toChars(str1);
			while(_g2 < _g3.length) {
				var v = _g3[_g2];
				++_g2;
				if(v == hx_strings_Strings.charCodeAt8("i",0) || v == hx_strings_Strings.charCodeAt8("m",0) || v == hx_strings_Strings.charCodeAt8("g",0)) {
					_g1.push(v);
				}
			}
			var _this = _g1;
			var result = new Array(_this.length);
			var _g1 = 0;
			var _g2 = _this.length;
			while(_g1 < _g2) {
				var i = _g1++;
				result[i] = String.fromCodePoint(_this[i]);
			}
			tmp = result.join("");
		}
		break;
	case 1:
		var opt = _g.v;
		tmp = Std.string(opt);
		break;
	case 2:
		var arr = _g.v;
		var _g = [];
		var _g1 = 0;
		var _g2 = arr;
		while(_g1 < _g2.length) {
			var v = _g2[_g1];
			++_g1;
			if(v != null) {
				_g.push(v);
			}
		}
		tmp = _g.join("");
		break;
	}
	return new hx_strings_Pattern(pattern,tmp);
};
hx_strings_Pattern.prototype = {
	pattern: null
	,options: null
	,ereg: null
	,matcher: function(str) {
		return new hx_strings__$Pattern_MatcherImpl(this.ereg,this.pattern,this.options,str);
	}
	,replace: function(str,replaceWith) {
		return str.replace(this.ereg.r,replaceWith);
	}
	,remove: function(str) {
		return str.replace(this.ereg.r,"");
	}
	,split: function(str) {
		return this.ereg.split(str);
	}
	,__class__: hx_strings_Pattern
};
var hx_strings_Matcher = function() { };
hx_strings_Matcher.__name__ = "hx.strings.Matcher";
hx_strings_Matcher.__isInterface__ = true;
hx_strings_Matcher.prototype = {
	iterate: null
	,map: null
	,matched: null
	,matchedPos: null
	,matches: null
	,matchesInRegion: null
	,reset: null
	,substringAfterMatch: null
	,substringBeforeMatch: null
	,__class__: hx_strings_Matcher
};
var hx_strings__$Pattern_MatcherImpl = function(ereg,pattern,options,str) {
	var clone = new EReg(pattern,options);
	this.ereg = clone;
	this.str = str;
};
hx_strings__$Pattern_MatcherImpl.__name__ = "hx.strings._Pattern.MatcherImpl";
hx_strings__$Pattern_MatcherImpl.__interfaces__ = [hx_strings_Matcher];
hx_strings__$Pattern_MatcherImpl.prototype = {
	ereg: null
	,isMatch: null
	,str: null
	,reset: function(str) {
		this.str = str;
		this.isMatch = null;
		return this;
	}
	,iterate: function(onMatch) {
		var startAt = 0;
		while(this.ereg.matchSub(this.str,startAt)) {
			this.isMatch = true;
			var matchedPos = this.ereg.matchedPos();
			onMatch(this);
			startAt = matchedPos.pos + matchedPos.len;
		}
		this.isMatch = false;
	}
	,map: function(mapper) {
		var _gthis = this;
		return this.ereg.map(this.str,function(ereg) {
			_gthis.isMatch = true;
			return mapper(_gthis);
		});
	}
	,matched: function(n) {
		if(n == null) {
			n = 0;
		}
		if(!this.matches()) {
			throw haxe_Exception.thrown("No string matched");
		}
		var result = this.ereg.matched(n);
		return result;
	}
	,matches: function() {
		if(this.isMatch == null) {
			this.isMatch = this.ereg.match(this.str);
		}
		return this.isMatch;
	}
	,matchesInRegion: function(pos,len) {
		if(len == null) {
			len = -1;
		}
		return this.isMatch = this.ereg.matchSub(this.str,pos,len);
	}
	,matchedPos: function() {
		if(!this.matches()) {
			throw haxe_Exception.thrown("No string matched");
		}
		return this.ereg.matchedPos();
	}
	,substringAfterMatch: function() {
		if(!this.matches()) {
			return "";
		}
		return this.ereg.matchedRight();
	}
	,substringBeforeMatch: function() {
		if(!this.matches()) {
			return "";
		}
		return this.ereg.matchedLeft();
	}
	,_cloneEReg: function(from,pattern,options) {
		var clone = new EReg(pattern,options);
		return clone;
	}
	,__class__: hx_strings__$Pattern_MatcherImpl
};
var hx_strings_StringBuilder = function(initialContent) {
	this.len = 0;
	this.pre = null;
	this.sb = new StringBuf();
	if(initialContent != null) {
		this.add(initialContent);
	}
};
hx_strings_StringBuilder.__name__ = "hx.strings.StringBuilder";
hx_strings_StringBuilder.prototype = {
	sb: null
	,pre: null
	,len: null
	,get_length: function() {
		return this.len;
	}
	,add: function(item) {
		this.sb.b += Std.string(item == null ? "null" : item);
		this.len += item == null ? 0 : item.length;
		return this;
	}
	,addChar: function(ch) {
		if(ch > -1 && ch < 128) {
			this.sb.b += String.fromCodePoint(ch);
		} else {
			var _this = this.sb;
			var x = String.fromCodePoint(ch);
			_this.b += Std.string(x);
		}
		this.len++;
		return this;
	}
	,addAll: function(items) {
		var _g = 0;
		while(_g < items.length) {
			var item = items[_g];
			++_g;
			this.sb.b += Std.string(item);
			this.len += item == null ? 0 : item.length;
		}
		return this;
	}
	,clear: function() {
		this.pre = null;
		this.sb = new StringBuf();
		this.len = 0;
		return this;
	}
	,isEmpty: function() {
		return this.len == 0;
	}
	,newLine: function() {
		this.sb.b += "\n";
		this.len++;
		return this;
	}
	,insert: function(pos,item) {
		if(pos < 0) {
			throw haxe_Exception.thrown("[pos] must not be negative");
		}
		if(pos > this.len) {
			throw haxe_Exception.thrown("[pos] must not be greater than this.length");
		}
		if(pos == this.len) {
			this.add(item);
			return this;
		}
		if(pos == 0) {
			if(this.pre == null) {
				this.pre = [];
			}
			this.pre.unshift(item);
			this.len += item == null ? 0 : item.length;
			return this;
		}
		var pre_len = 0;
		if(this.pre != null) {
			var pre = this.pre;
			var i = pre.length;
			var _g = 0;
			var _g1 = pre.length;
			while(_g < _g1) {
				var i = _g++;
				var str = pre[i];
				var next_pre_len = pre_len + (str == null ? 0 : str.length);
				if(next_pre_len == pos) {
					pre.splice(i + 1,0,item);
					this.len += item == null ? 0 : item.length;
					return this;
				}
				if(next_pre_len > pos) {
					var preSplitted = hx_strings_Strings.splitAt(pre[i],[pos - pre_len]);
					pre[i] = preSplitted[0];
					pre.splice(i + 1,0,item);
					pre.splice(i + 2,0,preSplitted[1]);
					this.len += item == null ? 0 : item.length;
					return this;
				}
				pre_len = next_pre_len;
			}
		}
		if(this.sb.b.length == 0) {
			this.add(item);
			return this;
		}
		var sbSplitted = hx_strings_Strings.splitAt(this.sb.b,[pos - pre_len]);
		this.sb = new StringBuf();
		this.sb.b += Std.string(sbSplitted[0]);
		this.sb.b += Std.string(item);
		this.len += item == null ? 0 : item.length;
		this.sb.b += Std.string(sbSplitted[1]);
		return this;
	}
	,insertChar: function(pos,ch) {
		if(pos < 0) {
			throw haxe_Exception.thrown("[pos] must not be negative");
		}
		if(pos > this.len) {
			throw haxe_Exception.thrown("[pos] must not be greater than this.length");
		}
		if(pos == this.len) {
			this.addChar(ch);
			return this;
		}
		if(pos == 0) {
			if(this.pre == null) {
				this.pre = [];
			}
			this.pre.unshift(String.fromCodePoint(ch));
			this.len++;
			return this;
		}
		var pre_len = 0;
		if(this.pre != null) {
			var pre = this.pre;
			var i = pre.length;
			var _g = 0;
			var _g1 = pre.length;
			while(_g < _g1) {
				var i = _g++;
				var str = pre[i];
				var next_pre_len = pre_len + (str == null ? 0 : str.length);
				if(next_pre_len == pos) {
					var x = String.fromCodePoint(ch);
					pre.splice(i + 1,0,x);
					this.len++;
					return this;
				}
				if(next_pre_len > pos) {
					var preSplitted = hx_strings_Strings.splitAt(pre[i],[pos - pre_len]);
					pre[i] = preSplitted[0];
					var x1 = String.fromCodePoint(ch);
					pre.splice(i + 1,0,x1);
					pre.splice(i + 2,0,preSplitted[1]);
					this.len++;
					return this;
				}
				pre_len = next_pre_len;
			}
		}
		if(this.sb.b.length == 0) {
			this.addChar(ch);
			return this;
		}
		var sbSplitted = hx_strings_Strings.splitAt(this.sb.b,[pos - pre_len]);
		this.sb = new StringBuf();
		this.sb.b += Std.string(sbSplitted[0]);
		this.addChar(ch);
		this.sb.b += Std.string(sbSplitted[1]);
		return this;
	}
	,insertAll: function(pos,items) {
		if(pos < 0) {
			throw haxe_Exception.thrown("[pos] must not be negative");
		}
		if(pos > this.len) {
			throw haxe_Exception.thrown("[pos] must not be greater than this.length");
		}
		if(pos == this.len) {
			this.addAll(items);
			return this;
		}
		if(pos == 0) {
			if(this.pre == null) {
				this.pre = [];
			}
			var pre = this.pre;
			var i = items.length;
			while(i-- > 0) {
				var item = items[i];
				pre.unshift(item);
				this.len += item == null ? 0 : item.length;
			}
			return this;
		}
		var pre_len = 0;
		if(this.pre != null) {
			var pre = this.pre;
			var i = pre.length;
			var _g = 0;
			var _g1 = pre.length;
			while(_g < _g1) {
				var i = _g++;
				var str = pre[i];
				var next_pre_len = pre_len + (str == null ? 0 : str.length);
				if(next_pre_len == pos) {
					var j = items.length;
					while(j-- > 0) {
						var item = items[j];
						pre.splice(i + 1,0,item);
						this.len += item == null ? 0 : item.length;
					}
					return this;
				}
				if(next_pre_len > pos) {
					var preSplitted = hx_strings_Strings.splitAt(pre[i],[pos - pre_len]);
					pre[i] = preSplitted[0];
					pre.splice(i + 1,0,preSplitted[1]);
					var j1 = items.length;
					while(j1-- > 0) {
						var item1 = items[j1];
						pre.splice(i + 1,0,item1);
						this.len += item1 == null ? 0 : item1.length;
					}
					return this;
				}
				pre_len = next_pre_len;
			}
		}
		if(this.sb.b.length == 0) {
			var _g = 0;
			while(_g < items.length) {
				var item = items[_g];
				++_g;
				this.add(item);
			}
			return this;
		}
		var sbSplitted = hx_strings_Strings.splitAt(this.sb.b,[pos - pre_len]);
		this.sb = new StringBuf();
		this.sb.b += Std.string(sbSplitted[0]);
		var _g = 0;
		while(_g < items.length) {
			var item = items[_g];
			++_g;
			this.sb.b += Std.string(item);
			this.len += item == null ? 0 : item.length;
		}
		this.sb.b += Std.string(sbSplitted[1]);
		return this;
	}
	,asOutput: function() {
		return new hx_strings__$StringBuilder_OutputWrapper(this);
	}
	,toString: function() {
		if(this.pre == null) {
			return this.sb.b;
		}
		var str = this.pre.join("") + this.sb.b;
		this.clear();
		this.add(str);
		return str;
	}
	,__class__: hx_strings_StringBuilder
	,__properties__: {get_length:"get_length"}
};
var hx_strings__$StringBuilder_OutputWrapper = function(sb) {
	this.sb = sb;
};
hx_strings__$StringBuilder_OutputWrapper.__name__ = "hx.strings._StringBuilder.OutputWrapper";
hx_strings__$StringBuilder_OutputWrapper.__super__ = haxe_io_Output;
hx_strings__$StringBuilder_OutputWrapper.prototype = $extend(haxe_io_Output.prototype,{
	sb: null
	,bo: null
	,flush: function() {
		if(this.bo != null && this.bo.b.pos > 0) {
			this.sb.add(this.bo.getBytes().toString());
		}
	}
	,writeByte: function(c) {
		if(this.bo == null) {
			this.bo = new haxe_io_BytesOutput();
		}
		this.bo.writeByte(c);
	}
	,writeString: function(str,encoding) {
		this.flush();
		this.sb.add(str);
	}
	,__class__: hx_strings__$StringBuilder_OutputWrapper
});
var hx_strings_internal_OS = function() { };
hx_strings_internal_OS.__name__ = "hx.strings.internal.OS";
var js_Boot = function() { };
js_Boot.__name__ = "js.Boot";
js_Boot.getClass = function(o) {
	if(o == null) {
		return null;
	} else if(((o) instanceof Array)) {
		return Array;
	} else {
		var cl = o.__class__;
		if(cl != null) {
			return cl;
		}
		var name = js_Boot.__nativeClassName(o);
		if(name != null) {
			return js_Boot.__resolveNativeClass(name);
		}
		return null;
	}
};
js_Boot.__string_rec = function(o,s) {
	if(o == null) {
		return "null";
	}
	if(s.length >= 5) {
		return "<...>";
	}
	var t = typeof(o);
	if(t == "function" && (o.__name__ || o.__ename__)) {
		t = "object";
	}
	switch(t) {
	case "function":
		return "<function>";
	case "object":
		if(o.__enum__) {
			var e = $hxEnums[o.__enum__];
			var con = e.__constructs__[o._hx_index];
			var n = con._hx_name;
			if(con.__params__) {
				s = s + "\t";
				return n + "(" + ((function($this) {
					var $r;
					var _g = [];
					{
						var _g1 = 0;
						var _g2 = con.__params__;
						while(true) {
							if(!(_g1 < _g2.length)) {
								break;
							}
							var p = _g2[_g1];
							_g1 = _g1 + 1;
							_g.push(js_Boot.__string_rec(o[p],s));
						}
					}
					$r = _g;
					return $r;
				}(this))).join(",") + ")";
			} else {
				return n;
			}
		}
		if(((o) instanceof Array)) {
			var str = "[";
			s += "\t";
			var _g = 0;
			var _g1 = o.length;
			while(_g < _g1) {
				var i = _g++;
				str += (i > 0 ? "," : "") + js_Boot.__string_rec(o[i],s);
			}
			str += "]";
			return str;
		}
		var tostr;
		try {
			tostr = o.toString;
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			return "???";
		}
		if(tostr != null && tostr != Object.toString && typeof(tostr) == "function") {
			var s2 = o.toString();
			if(s2 != "[object Object]") {
				return s2;
			}
		}
		var str = "{\n";
		s += "\t";
		var hasp = o.hasOwnProperty != null;
		var k = null;
		for( k in o ) {
		if(hasp && !o.hasOwnProperty(k)) {
			continue;
		}
		if(k == "prototype" || k == "__class__" || k == "__super__" || k == "__interfaces__" || k == "__properties__") {
			continue;
		}
		if(str.length != 2) {
			str += ", \n";
		}
		str += s + k + " : " + js_Boot.__string_rec(o[k],s);
		}
		s = s.substring(1);
		str += "\n" + s + "}";
		return str;
	case "string":
		return o;
	default:
		return String(o);
	}
};
js_Boot.__interfLoop = function(cc,cl) {
	if(cc == null) {
		return false;
	}
	if(cc == cl) {
		return true;
	}
	var intf = cc.__interfaces__;
	if(intf != null) {
		var _g = 0;
		var _g1 = intf.length;
		while(_g < _g1) {
			var i = _g++;
			var i1 = intf[i];
			if(i1 == cl || js_Boot.__interfLoop(i1,cl)) {
				return true;
			}
		}
	}
	return js_Boot.__interfLoop(cc.__super__,cl);
};
js_Boot.__instanceof = function(o,cl) {
	if(cl == null) {
		return false;
	}
	switch(cl) {
	case Array:
		return ((o) instanceof Array);
	case Bool:
		return typeof(o) == "boolean";
	case Dynamic:
		return o != null;
	case Float:
		return typeof(o) == "number";
	case Int:
		if(typeof(o) == "number") {
			return ((o | 0) === o);
		} else {
			return false;
		}
		break;
	case String:
		return typeof(o) == "string";
	default:
		if(o != null) {
			if(typeof(cl) == "function") {
				if(js_Boot.__downcastCheck(o,cl)) {
					return true;
				}
			} else if(typeof(cl) == "object" && js_Boot.__isNativeObj(cl)) {
				if(((o) instanceof cl)) {
					return true;
				}
			}
		} else {
			return false;
		}
		if(cl == Class ? o.__name__ != null : false) {
			return true;
		}
		if(cl == Enum ? o.__ename__ != null : false) {
			return true;
		}
		return o.__enum__ != null ? $hxEnums[o.__enum__] == cl : false;
	}
};
js_Boot.__downcastCheck = function(o,cl) {
	if(!((o) instanceof cl)) {
		if(cl.__isInterface__) {
			return js_Boot.__interfLoop(js_Boot.getClass(o),cl);
		} else {
			return false;
		}
	} else {
		return true;
	}
};
js_Boot.__implements = function(o,iface) {
	return js_Boot.__interfLoop(js_Boot.getClass(o),iface);
};
js_Boot.__cast = function(o,t) {
	if(o == null || js_Boot.__instanceof(o,t)) {
		return o;
	} else {
		throw haxe_Exception.thrown("Cannot cast " + Std.string(o) + " to " + Std.string(t));
	}
};
js_Boot.__nativeClassName = function(o) {
	var name = js_Boot.__toStr.call(o).slice(8,-1);
	if(name == "Object" || name == "Function" || name == "Math" || name == "JSON") {
		return null;
	}
	return name;
};
js_Boot.__isNativeObj = function(o) {
	return js_Boot.__nativeClassName(o) != null;
};
js_Boot.__resolveNativeClass = function(name) {
	return $global[name];
};
var hx_strings_internal__$Either3__$Either3 = $hxEnums["hx.strings.internal._Either3._Either3"] = { __ename__:"hx.strings.internal._Either3._Either3",__constructs__:null
	,a: ($_=function(v) { return {_hx_index:0,v:v,__enum__:"hx.strings.internal._Either3._Either3",toString:$estr}; },$_._hx_name="a",$_.__params__ = ["v"],$_)
	,b: ($_=function(v) { return {_hx_index:1,v:v,__enum__:"hx.strings.internal._Either3._Either3",toString:$estr}; },$_._hx_name="b",$_.__params__ = ["v"],$_)
	,c: ($_=function(v) { return {_hx_index:2,v:v,__enum__:"hx.strings.internal._Either3._Either3",toString:$estr}; },$_._hx_name="c",$_.__params__ = ["v"],$_)
};
hx_strings_internal__$Either3__$Either3.__constructs__ = [hx_strings_internal__$Either3__$Either3.a,hx_strings_internal__$Either3__$Either3.b,hx_strings_internal__$Either3__$Either3.c];
var hx_strings_Strings = function() { };
hx_strings_Strings.__name__ = "hx.strings.Strings";
hx_strings_Strings._length = function(str) {
	return str.length;
};
hx_strings_Strings._getNotFoundDefault = function(str,notFoundDefault) {
	switch(notFoundDefault) {
	case 1:
		return null;
	case 2:
		return "";
	case 3:
		return str;
	}
};
hx_strings_Strings._charCodeAt8Unsafe = function(str,pos) {
	return HxOverrides.cca(str,pos);
};
hx_strings_Strings._splitAsciiWordsUnsafe = function(str) {
	var words = [];
	var currentWord = new hx_strings_StringBuilder();
	var chars = hx_strings_Strings.toChars(str);
	var len = chars.length;
	var lastIndex = len - 1;
	var _g = 0;
	var _g1 = len;
	while(_g < _g1) {
		var i = _g++;
		var ch = chars[i];
		if(ch > 64 && ch < 91 || ch > 96 && ch < 123) {
			var chNext = i < lastIndex ? chars[i + 1] : -1;
			currentWord.addChar(ch);
			if(chNext > 47 && chNext < 58) {
				words.push(currentWord.toString());
				currentWord.clear();
			} else if(hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h.hasOwnProperty(ch)) {
				if(hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h.hasOwnProperty(chNext) && chars.length > i + 2) {
					if(!hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h.hasOwnProperty(chars[i + 2])) {
						words.push(currentWord.toString());
						currentWord.clear();
					}
				}
			} else if(hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h.hasOwnProperty(chNext)) {
				words.push(currentWord.toString());
				currentWord.clear();
			}
		} else if(ch > 47 && ch < 58) {
			currentWord.addChar(ch);
			var chNext1 = i < lastIndex ? chars[i + 1] : -1;
			if(!(chNext1 > 47 && chNext1 < 58)) {
				words.push(currentWord.toString());
				currentWord.clear();
			}
		} else if(currentWord.len > 0) {
			words.push(currentWord.toString());
			currentWord.clear();
		}
	}
	if(currentWord.len > 0) {
		words.push(currentWord.toString());
	}
	return words;
};
hx_strings_Strings.ansiToHtml = function(str,renderMethod,initialState) {
	if(str == null || str.length == 0) {
		return str;
	}
	if(renderMethod == null) {
		renderMethod = hx_strings_AnsiToHtmlRenderMethod.StyleAttributes;
	}
	var styleOrClassAttribute;
	switch(renderMethod._hx_index) {
	case 0:
		styleOrClassAttribute = "style";
		break;
	case 1:
		styleOrClassAttribute = "class";
		break;
	case 2:
		var cb = renderMethod.func;
		styleOrClassAttribute = "class";
		break;
	}
	var sb = new hx_strings_StringBuilder();
	if(initialState != null && (initialState.fgcolor != null || initialState.bgcolor != null || initialState.bold || initialState.underline || initialState.blink)) {
		sb.add("<span " + styleOrClassAttribute + "=\"").add(initialState.toCSS(renderMethod)).add("\">");
	}
	var effectiveState = new hx_strings_AnsiState(initialState);
	var strLenMinus1 = (str == null ? 0 : str.length) - 1;
	var i = -1;
	var lookAhead = new hx_strings_StringBuilder();
	while(i < strLenMinus1) {
		++i;
		var ch = HxOverrides.cca(str,i);
		if(ch == 27 && i < strLenMinus1 && HxOverrides.cca(str,i + 1) == 91) {
			lookAhead.clear();
			var currentState = new hx_strings_AnsiState(effectiveState);
			var currentGraphicModeParam = 0;
			var isValidEscapeSequence = false;
			++i;
			_hx_loop2: while(i < strLenMinus1) {
				++i;
				var ch2 = HxOverrides.cca(str,i);
				lookAhead.addChar(ch2);
				switch(ch2) {
				case 48:
					currentGraphicModeParam *= 10;
					break;
				case 49:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 1;
					break;
				case 50:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 2;
					break;
				case 51:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 3;
					break;
				case 52:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 4;
					break;
				case 53:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 5;
					break;
				case 54:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 6;
					break;
				case 55:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 7;
					break;
				case 56:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 8;
					break;
				case 57:
					currentGraphicModeParam = currentGraphicModeParam * 10 + 9;
					break;
				case 59:
					currentState.setGraphicModeParameter(currentGraphicModeParam);
					currentGraphicModeParam = 0;
					break;
				case 109:
					currentState.setGraphicModeParameter(currentGraphicModeParam);
					if(effectiveState.fgcolor != null || effectiveState.bgcolor != null || effectiveState.bold || effectiveState.underline || effectiveState.blink) {
						sb.add("</span>");
					}
					if(currentState.fgcolor != null || currentState.bgcolor != null || currentState.bold || currentState.underline || currentState.blink) {
						sb.add("<span " + styleOrClassAttribute + "=\"").add(currentState.toCSS(renderMethod)).add("\">");
					}
					effectiveState = currentState;
					isValidEscapeSequence = true;
					break _hx_loop2;
				default:
					break _hx_loop2;
				}
			}
			if(!isValidEscapeSequence) {
				sb.addChar(27).add("[").add(Std.string(lookAhead));
			}
		} else {
			sb.addChar(ch);
		}
	}
	if(effectiveState.fgcolor != null || effectiveState.bgcolor != null || effectiveState.bold || effectiveState.underline || effectiveState.blink) {
		sb.add("</span>");
	}
	return sb.toString();
};
hx_strings_Strings.appendIfMissing = function(str,suffix) {
	if(str == null) {
		return null;
	}
	if(str.length == 0) {
		return Std.string(str) + Std.string(suffix);
	}
	if(hx_strings_Strings.endsWith(str,suffix)) {
		return str;
	}
	return Std.string(str) + Std.string(suffix);
};
hx_strings_Strings.base64Encode = function(plain) {
	if(plain == null) {
		return null;
	}
	return haxe_crypto_Base64.encode(plain == null ? null : haxe_io_Bytes.ofString(plain));
};
hx_strings_Strings.base64Decode = function(encoded) {
	if(encoded == null) {
		return null;
	}
	return haxe_crypto_Base64.decode(encoded).toString();
};
hx_strings_Strings.charAt8 = function(str,pos,resultIfOutOfBound) {
	if(resultIfOutOfBound == null) {
		resultIfOutOfBound = "";
	}
	if(str == null || str.length == 0 || pos < 0 || pos >= (str == null ? 0 : str.length)) {
		return resultIfOutOfBound;
	}
	return str.charAt(pos);
};
hx_strings_Strings.charCodeAt8 = function(str,pos,resultIfOutOfBound) {
	if(resultIfOutOfBound == null) {
		resultIfOutOfBound = -1;
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen == 0 || pos < 0 || pos >= strLen) {
		return resultIfOutOfBound;
	}
	return HxOverrides.cca(str,pos);
};
hx_strings_Strings.compact = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	var needWhiteSpace = false;
	var _g = 0;
	var _g1 = hx_strings_Strings.toChars(str);
	while(_g < _g1.length) {
		var char = _g1[_g];
		++_g;
		if(char > 8 && char < 14 || char == 32) {
			if(sb.len != 0) {
				needWhiteSpace = true;
			}
			continue;
		} else if(needWhiteSpace) {
			sb.addChar(32);
			needWhiteSpace = false;
		}
		sb.addChar(char);
	}
	return sb.toString();
};
hx_strings_Strings.contains = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	if(searchFor == "") {
		return true;
	}
	return searchIn.indexOf(searchFor) > -1;
};
hx_strings_Strings.containsOnly = function(searchIn,allowedChars) {
	if(searchIn == null || searchIn.length == 0) {
		return true;
	}
	if(allowedChars == null) {
		return false;
	}
	var allowedCharsArray;
	var _g = allowedChars;
	switch(_g._hx_index) {
	case 0:
		var str = _g.v;
		allowedCharsArray = hx_strings_Strings.toChars(str);
		break;
	case 1:
		var chars = _g.v;
		allowedCharsArray = chars;
		break;
	}
	var _g = 0;
	var _g1 = hx_strings_Strings.toChars(searchIn);
	while(_g < _g1.length) {
		var ch = _g1[_g];
		++_g;
		if(allowedCharsArray.indexOf(ch) < 0) {
			return false;
		}
	}
	return true;
};
hx_strings_Strings.containsAll = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(!(searchIn == null || candidate == null ? false : candidate == "" ? true : searchIn.indexOf(candidate) > -1)) {
			return false;
		}
	}
	return true;
};
hx_strings_Strings.containsAllIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	searchIn = searchIn.toLowerCase();
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		var searchFor1 = candidate.toLowerCase();
		if(!(searchIn == null || searchFor1 == null ? false : searchFor1 == "" ? true : searchIn.indexOf(searchFor1) > -1)) {
			return false;
		}
	}
	return true;
};
hx_strings_Strings.containsAny = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(searchIn == null || candidate == null ? false : candidate == "" ? true : searchIn.indexOf(candidate) > -1) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.containsAnyIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	searchIn = searchIn.toLowerCase();
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		var searchFor1 = candidate.toLowerCase();
		if(searchIn == null || searchFor1 == null ? false : searchFor1 == "" ? true : searchIn.indexOf(searchFor1) > -1) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.containsNone = function(searchIn,searchFor) {
	return !hx_strings_Strings.containsAny(searchIn,searchFor);
};
hx_strings_Strings.containsNoneIgnoreCase = function(searchIn,searchFor) {
	return !hx_strings_Strings.containsAnyIgnoreCase(searchIn,searchFor);
};
hx_strings_Strings.containsWhitespaces = function(searchIn) {
	if(searchIn == null) {
		return false;
	}
	var _g = 0;
	var _g1 = hx_strings_Strings.toChars(searchIn);
	while(_g < _g1.length) {
		var ch = _g1[_g];
		++_g;
		if(ch > 8 && ch < 14 || ch == 32) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.countMatches = function(searchIn,searchFor,startAt) {
	if(startAt == null) {
		startAt = 0;
	}
	if(searchIn == null || searchIn.length == 0 || (searchFor == null || searchFor.length == 0) || startAt >= searchIn.length) {
		return 0;
	}
	if(startAt < 0) {
		startAt = 0;
	}
	var count = 0;
	var foundAt = startAt > -1 ? startAt - 1 : 0;
	while(true) {
		foundAt = searchIn.indexOf(searchFor,foundAt + 1);
		if(!(foundAt > -1)) {
			break;
		}
		++count;
	}
	return count;
};
hx_strings_Strings.countMatchesIgnoreCase = function(searchIn,searchFor,startAt) {
	if(startAt == null) {
		startAt = 0;
	}
	if(searchIn == null || searchIn.length == 0 || (searchFor == null || searchFor.length == 0) || startAt >= searchIn.length) {
		return 0;
	}
	if(startAt < 0) {
		startAt = 0;
	}
	searchIn = searchIn.toLowerCase();
	searchFor = searchFor.toLowerCase();
	var count = 0;
	var foundAt = startAt > -1 ? startAt - 1 : 0;
	while(true) {
		foundAt = searchIn.indexOf(searchFor,foundAt + 1);
		if(!(foundAt > -1)) {
			break;
		}
		++count;
	}
	return count;
};
hx_strings_Strings.compare = function(str,other) {
	if(str == null) {
		if(other == null) {
			return 0;
		} else {
			return -1;
		}
	}
	if(other == null) {
		if(str == null) {
			return 0;
		} else {
			return 1;
		}
	}
	if(str > other) {
		return 1;
	} else if(str == other) {
		return 0;
	} else {
		return -1;
	}
};
hx_strings_Strings.compareIgnoreCase = function(str,other) {
	if(str == null) {
		if(other == null) {
			return 0;
		} else {
			return -1;
		}
	}
	if(other == null) {
		if(str == null) {
			return 0;
		} else {
			return 1;
		}
	}
	var str1 = hx_strings_Strings.toLowerCase8(str);
	var other1 = hx_strings_Strings.toLowerCase8(other);
	if(str1 > other1) {
		return 1;
	} else if(str1 == other1) {
		return 0;
	} else {
		return -1;
	}
};
hx_strings_Strings.diff = function(left,right) {
	var diff = new hx_strings_StringDiff();
	diff.at = hx_strings_Strings.diffAt(left,right);
	diff.left = hx_strings_Strings.substr8(left,diff.at);
	diff.right = hx_strings_Strings.substr8(right,diff.at);
	return diff;
};
hx_strings_Strings.diffAt = function(str,other) {
	if(str == other) {
		return -1;
	}
	var strLen = str == null ? 0 : str.length;
	var otherLen = other == null ? 0 : other.length;
	if(strLen == 0 || otherLen == 0) {
		return 0;
	}
	var checkLen = strLen > otherLen ? otherLen : strLen;
	var _g = 0;
	var _g1 = checkLen;
	while(_g < _g1) {
		var i = _g++;
		if(HxOverrides.cca(str,i) != HxOverrides.cca(other,i)) {
			return i;
		}
	}
	return checkLen;
};
hx_strings_Strings.ellipsizeLeft = function(str,maxLength,ellipsis) {
	if(ellipsis == null) {
		ellipsis = "...";
	}
	if((str == null ? 0 : str.length) <= maxLength) {
		return str;
	}
	var ellipsisLen = ellipsis == null ? 0 : ellipsis.length;
	if(maxLength < ellipsisLen) {
		throw haxe_Exception.thrown("[maxLength] must not be smaller than " + ellipsisLen);
	}
	return ellipsis + Std.string(hx_strings_Strings.right(str,maxLength - ellipsisLen));
};
hx_strings_Strings.ellipsizeMiddle = function(str,maxLength,ellipsis) {
	if(ellipsis == null) {
		ellipsis = "...";
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen <= maxLength) {
		return str;
	}
	var ellipsisLen = ellipsis == null ? 0 : ellipsis.length;
	if(maxLength < ellipsisLen) {
		throw haxe_Exception.thrown("[maxLength] must not be smaller than " + ellipsisLen);
	}
	var maxStrLen = maxLength - ellipsisLen;
	var leftLen = Math.round(maxStrLen / 2);
	var rightLen = maxStrLen - leftLen;
	return Std.string((str == null ? 0 : str.length) <= leftLen ? str : hx_strings_Strings.substring8(str,0,leftLen)) + ellipsis + Std.string(hx_strings_Strings.right(str,rightLen));
};
hx_strings_Strings.ellipsizeRight = function(str,maxLength,ellipsis) {
	if(ellipsis == null) {
		ellipsis = "...";
	}
	if((str == null ? 0 : str.length) <= maxLength) {
		return str;
	}
	var ellipsisLen = ellipsis == null ? 0 : ellipsis.length;
	if(maxLength < ellipsisLen) {
		throw haxe_Exception.thrown("[maxLength] must not be smaller than " + ellipsisLen);
	}
	var len = maxLength - ellipsisLen;
	return Std.string((str == null ? 0 : str.length) <= len ? str : hx_strings_Strings.substring8(str,0,len)) + ellipsis;
};
hx_strings_Strings.endsWith = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	return StringTools.endsWith(searchIn,searchFor);
};
hx_strings_Strings.endsWithAny = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(candidate != null && hx_strings_Strings.endsWith(searchIn,candidate)) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.endsWithAnyIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	searchIn = hx_strings_Strings.toLowerCase8(searchIn);
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(candidate != null && hx_strings_Strings.endsWith(searchIn,hx_strings_Strings.toLowerCase8(candidate))) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.endsWithIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	return hx_strings_Strings.endsWith(searchIn.toLowerCase(),searchFor.toLowerCase());
};
hx_strings_Strings.equals = function(str,other) {
	return str == other;
};
hx_strings_Strings.equalsIgnoreCase = function(str,other) {
	return hx_strings_Strings.toLowerCase8(str) == hx_strings_Strings.toLowerCase8(other);
};
hx_strings_Strings.filter = function(str,filter,separator) {
	if(separator == null) {
		separator = "";
	}
	if(str == null || str.length == 0) {
		return str;
	}
	var _g = [];
	var _g1 = 0;
	var _g2 = hx_strings_Strings.split8(str,[separator]);
	while(_g1 < _g2.length) {
		var v = _g2[_g1];
		++_g1;
		if(filter(v)) {
			_g.push(v);
		}
	}
	return _g.join(separator);
};
hx_strings_Strings.filterChars = function(str,filter) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _g = [];
	var _g1 = 0;
	var _g2 = hx_strings_Strings.toChars(str);
	while(_g1 < _g2.length) {
		var v = _g2[_g1];
		++_g1;
		if(filter(v)) {
			_g.push(v);
		}
	}
	var _this = _g;
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = String.fromCodePoint(_this[i]);
	}
	return result.join("");
};
hx_strings_Strings.getFuzzyDistance = function(left,right) {
	if(left == null || left.length == 0 || (right == null || right.length == 0)) {
		return 0;
	}
	left = hx_strings_Strings.toLowerCase8(left);
	right = hx_strings_Strings.toLowerCase8(right);
	var leftChars = hx_strings_Strings.toChars(left);
	var rightChars = hx_strings_Strings.toChars(right);
	var leftLastMatchAt = -100;
	var rightLastMatchAt = -100;
	var score = 0;
	var _g = 0;
	var _g1 = leftChars.length;
	while(_g < _g1) {
		var leftIdx = _g++;
		var leftChar = leftChars[leftIdx];
		var _g2 = rightLastMatchAt > -1 ? rightLastMatchAt + 1 : 0;
		var _g3 = rightChars.length;
		while(_g2 < _g3) {
			var rightIdx = _g2++;
			var rightChar = rightChars[rightIdx];
			if(leftChar == rightChar) {
				++score;
				if(leftLastMatchAt == leftIdx - 1 && rightLastMatchAt == rightIdx - 1) {
					score += 2;
				}
				leftLastMatchAt = leftIdx;
				rightLastMatchAt = rightIdx;
				break;
			}
		}
	}
	return score;
};
hx_strings_Strings.getLevenshteinDistance = function(left,right) {
	var leftLen = left == null ? 0 : left.length;
	var rightLen = right == null ? 0 : right.length;
	if(leftLen == 0) {
		return rightLen;
	}
	if(rightLen == 0) {
		return leftLen;
	}
	if(leftLen > rightLen) {
		var tmp = left;
		left = right;
		right = tmp;
		var tmpLen = leftLen;
		leftLen = rightLen;
		rightLen = tmpLen;
	}
	var prevCosts = [];
	var costs = [];
	var _g = 0;
	var _g1 = leftLen + 1;
	while(_g < _g1) {
		var leftIdx = _g++;
		prevCosts.push(leftIdx);
		costs.push(0);
	}
	var leftChars = hx_strings_Strings.toChars(left);
	var rightChars = hx_strings_Strings.toChars(right);
	var min = function(a,b) {
		if(a > b) {
			return b;
		} else {
			return a;
		}
	};
	var _g = 1;
	var _g1 = rightLen + 1;
	while(_g < _g1) {
		var rightIdx = _g++;
		var rightChar = rightChars[rightIdx - 1];
		costs[0] = rightIdx;
		var _g2 = 1;
		var _g3 = leftLen + 1;
		while(_g2 < _g3) {
			var leftIdx = _g2++;
			var leftIdxMinus1 = leftIdx - 1;
			var cost = leftChars[leftIdxMinus1] == rightChar ? 0 : 1;
			costs[leftIdx] = min(min(costs[leftIdxMinus1] + 1,prevCosts[leftIdx] + 1),prevCosts[leftIdxMinus1] + cost);
		}
		var tmp = prevCosts;
		prevCosts = costs;
		costs = tmp;
	}
	return prevCosts[leftLen];
};
hx_strings_Strings.getLongestCommonSubstring = function(left,right) {
	if(left == null || right == null) {
		return null;
	}
	var leftLen = left == null ? 0 : left.length;
	var rightLen = right == null ? 0 : right.length;
	if(leftLen == 0 || rightLen == 0) {
		return "";
	}
	var leftChars = hx_strings_Strings.toChars(left);
	var rightChars = hx_strings_Strings.toChars(right);
	var leftSubStartAt = 0;
	var leftSubLen = 0;
	var _g = 0;
	var _g1 = leftLen;
	while(_g < _g1) {
		var leftIdx = _g++;
		var _g2 = 0;
		var _g3 = rightLen;
		while(_g2 < _g3) {
			var rightIdx = _g2++;
			var currLen = 0;
			while(leftChars[leftIdx + currLen] == rightChars[rightIdx + currLen]) {
				++currLen;
				if(leftIdx + currLen >= leftLen || rightIdx + currLen >= rightLen) {
					break;
				}
			}
			if(currLen > leftSubLen) {
				leftSubLen = currLen;
				leftSubStartAt = leftIdx;
			}
		}
	}
	return hx_strings_Strings.substr8(left,leftSubStartAt,leftSubLen);
};
hx_strings_Strings.hashCode = function(str,algo) {
	if(str == null || str.length == 0) {
		return 0;
	}
	if(algo == null) {
		algo = hx_strings_HashCodeAlgorithm.PLATFORM_SPECIFIC;
	}
	if(algo == null) {
		return haxe_crypto_Crc32.make(str == null ? null : haxe_io_Bytes.ofString(str));
	} else {
		switch(algo._hx_index) {
		case 1:
			return haxe_crypto_Adler32.make(str == null ? null : haxe_io_Bytes.ofString(str));
		case 2:
			return haxe_crypto_Crc32.make(str == null ? null : haxe_io_Bytes.ofString(str));
		case 3:
			var hc = 5381;
			var _g = 0;
			var _g1 = hx_strings_Strings.toChars(str);
			while(_g < _g1.length) {
				var ch = _g1[_g];
				++_g;
				hc = ((hc << 5) + hc | 0) ^ ch;
			}
			return hc;
		case 4:
			var hc = 0;
			var _g = 0;
			var _g1 = hx_strings_Strings.toChars(str);
			while(_g < _g1.length) {
				var ch = _g1[_g];
				++_g;
				hc = ((hc << 5) - hc | 0) + ch | 0;
			}
			return hc;
		case 5:
			var hc = 0;
			var _g = 0;
			var _g1 = hx_strings_Strings.toChars(str);
			while(_g < _g1.length) {
				var ch = _g1[_g];
				++_g;
				hc = (((hc << 6) + (hc << 16) | 0) - hc | 0) + ch | 0;
			}
			return hc;
		default:
			return haxe_crypto_Crc32.make(str == null ? null : haxe_io_Bytes.ofString(str));
		}
	}
};
hx_strings_Strings.htmlDecode = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _this = hx_strings_Strings.REGEX_HTML_UNESCAPE;
	return new hx_strings__$Pattern_MatcherImpl(_this.ereg,_this.pattern,_this.options,str).map(function(m) {
		var match = m.matched();
		switch(match) {
		case "&amp;":
			return "&";
		case "&apos;":
			return "'";
		case "&gt;":
			return ">";
		case "&lt;":
			return "<";
		case "&nbsp;":
			return " ";
		case "&quot;":
			return "\"";
		default:
			var number = Std.parseInt(hx_strings_Strings.substr8(match,2,(match == null ? 0 : match.length) - 3));
			if(number == null) {
				throw haxe_Exception.thrown("Invalid HTML value " + match);
			}
			var this1 = number;
			return String.fromCodePoint(this1);
		}
	});
};
hx_strings_Strings.htmlEncode = function(str,escapeQuotes) {
	if(escapeQuotes == null) {
		escapeQuotes = false;
	}
	if(str == null || str.length == 0) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	var isFirstSpace = true;
	var _g = 0;
	var _g1 = str == null ? 0 : str.length;
	while(_g < _g1) {
		var i = _g++;
		var ch = HxOverrides.cca(str,i);
		switch(ch) {
		case 32:
			if(isFirstSpace) {
				sb.add(" ");
				isFirstSpace = false;
			} else {
				sb.add("&nbsp;");
			}
			break;
		case 34:
			sb.add(escapeQuotes ? "&quot;" : "\"");
			break;
		case 38:
			sb.add("&amp;");
			break;
		case 39:
			sb.add(escapeQuotes ? "&#039;" : "'");
			break;
		case 60:
			sb.add("&lt;");
			break;
		case 62:
			sb.add("&gt;");
			break;
		default:
			if(ch > 127) {
				sb.add("&#").add(Std.string(ch)).add(";");
			} else {
				sb.addChar(ch);
			}
		}
		if(ch != 32) {
			isFirstSpace = true;
		}
	}
	return sb.toString();
};
hx_strings_Strings.insertAt = function(str,pos,insertion) {
	if(str == null) {
		return null;
	}
	var strLen = str == null ? 0 : str.length;
	if(pos < 0) {
		pos = strLen + pos;
	}
	if(pos < 0 || pos > strLen) {
		throw haxe_Exception.thrown("Absolute value of [pos] must be <= str.length");
	}
	if(insertion == null || insertion.length == 0) {
		return str;
	}
	return Std.string(hx_strings_Strings.substring8(str,0,pos)) + insertion + Std.string(hx_strings_Strings.substring8(str,pos));
};
hx_strings_Strings.ifBlank = function(str,fallback) {
	if(str == null ? true : StringTools.trim(str).length == 0) {
		return fallback;
	} else {
		return str;
	}
};
hx_strings_Strings.ifEmpty = function(str,fallback) {
	if(str == null || str.length == 0) {
		return fallback;
	} else {
		return str;
	}
};
hx_strings_Strings.ifNull = function(str,fallback) {
	if(str == null) {
		return fallback;
	} else {
		return str;
	}
};
hx_strings_Strings.indentLines = function(str,indentWith) {
	if(str == null) {
		return null;
	}
	if(str.length == 0 || (indentWith == null || indentWith.length == 0)) {
		return str;
	}
	var isFirstLine = true;
	var sb = new hx_strings_StringBuilder();
	var _g = 0;
	var _g1 = hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(str);
	while(_g < _g1.length) {
		var line = _g1[_g];
		++_g;
		if(isFirstLine) {
			isFirstLine = false;
		} else {
			sb.newLine();
		}
		sb.add(indentWith);
		sb.add(line);
	}
	return sb.toString();
};
hx_strings_Strings.indexOf8 = function(str,searchFor,startAt) {
	if(startAt == null) {
		startAt = 0;
	}
	if(str == null || searchFor == null) {
		return -1;
	}
	var strLen = str == null ? 0 : str.length;
	var searchForLen = searchFor == null ? 0 : searchFor.length;
	if(startAt < 0) {
		startAt = 0;
	}
	if(searchForLen == 0) {
		if(startAt == 0) {
			return 0;
		}
		if(startAt > 0 && startAt < strLen) {
			return startAt;
		}
		return strLen;
	}
	if(startAt >= strLen) {
		return -1;
	}
	return str.indexOf(searchFor,startAt);
};
hx_strings_Strings.isBlank = function(str) {
	if(str == null) {
		return true;
	} else {
		return StringTools.trim(str).length == 0;
	}
};
hx_strings_Strings.isDigits = function(str) {
	if(str == null || str.length == 0) {
		return false;
	}
	var _g = 0;
	var _g1 = str == null ? 0 : str.length;
	while(_g < _g1) {
		var i = _g++;
		var this1 = HxOverrides.cca(str,i);
		if(!(this1 > 47 && this1 < 58)) {
			return false;
		}
	}
	return true;
};
hx_strings_Strings.isEmpty = function(str) {
	if(str != null) {
		return str.length == 0;
	} else {
		return true;
	}
};
hx_strings_Strings.isNotBlank = function(str) {
	if(str != null) {
		return StringTools.trim(str).length > 0;
	} else {
		return false;
	}
};
hx_strings_Strings.isNotEmpty = function(str) {
	if(str != null) {
		return str.length > 0;
	} else {
		return false;
	}
};
hx_strings_Strings.isLowerCase = function(str) {
	if(str == null || str.length == 0) {
		return false;
	}
	return str == hx_strings_Strings.toLowerCase8(str);
};
hx_strings_Strings.isUpperCase = function(str) {
	if(str == null || str.length == 0) {
		return false;
	}
	return str == hx_strings_Strings.toUpperCase8(str);
};
hx_strings_Strings.iterate = function(str,callback,separator) {
	if(separator == null) {
		separator = "";
	}
	if(str == null || str.length == 0) {
		return;
	}
	var _g = 0;
	var _g1 = hx_strings_Strings.split8(str,[separator]);
	while(_g < _g1.length) {
		var sub = _g1[_g];
		++_g;
		callback(sub);
	}
};
hx_strings_Strings.iterateChars = function(str,callback) {
	if(str == null || str.length == 0) {
		return;
	}
	var _g = 0;
	var _g1 = str == null ? 0 : str.length;
	while(_g < _g1) {
		var i = _g++;
		callback(HxOverrides.cca(str,i));
	}
};
hx_strings_Strings.lastIndexOf8 = function(str,searchFor,startAt) {
	if(str == null || searchFor == null) {
		return -1;
	}
	var strLen = str == null ? 0 : str.length;
	var searchForLen = searchFor == null ? 0 : searchFor.length;
	if(startAt == null) {
		startAt = strLen;
	}
	if(searchForLen == 0) {
		if(startAt < 0) {
			return 0;
		}
		if(startAt > strLen) {
			return strLen;
		}
		return startAt;
	}
	if(startAt < 0) {
		return -1;
	} else if(startAt >= strLen) {
		startAt = strLen - 1;
	}
	var strNeedsUTF8Workaround = str.length != strLen;
	var searchForNeedsUTF8Workaround = searchFor.length != searchForLen;
	if(!strNeedsUTF8Workaround && !searchForNeedsUTF8Workaround) {
		return str.lastIndexOf(searchFor,startAt);
	}
	if(searchForNeedsUTF8Workaround && !strNeedsUTF8Workaround) {
		return -1;
	}
	var searchForChars = hx_strings_Strings.toChars(searchFor);
	startAt += searchForLen - 1;
	var searchForPosToCheck = searchForLen - 1;
	var strPos = strLen;
	while(strPos-- > 0) {
		if(strPos > startAt) {
			continue;
		}
		var strCh = HxOverrides.cca(str,strPos);
		if(strCh == searchForChars[searchForPosToCheck]) {
			if(searchForPosToCheck == 0) {
				return strPos;
			}
			--searchForPosToCheck;
		} else {
			searchForPosToCheck = searchForLen - 1;
		}
	}
	return -1;
};
hx_strings_Strings.length8 = function(str) {
	if(str == null) {
		return 0;
	}
	return str.length;
};
hx_strings_Strings.left = function(str,len) {
	if((str == null ? 0 : str.length) <= len) {
		return str;
	}
	return hx_strings_Strings.substring8(str,0,len);
};
hx_strings_Strings.lpad = function(str,targetLength,padStr,canOverflow) {
	if(canOverflow == null) {
		canOverflow = true;
	}
	if(padStr == null) {
		padStr = " ";
	}
	var strLen = str == null ? 0 : str.length;
	if(str == null || strLen > targetLength) {
		return str;
	}
	if(padStr == null || padStr.length == 0) {
		padStr = " ";
	}
	var sb = [str];
	var padLen = padStr == null ? 0 : padStr.length;
	while(strLen < targetLength) {
		sb.unshift(padStr);
		strLen += padLen;
	}
	if(canOverflow) {
		return sb.join("");
	}
	return hx_strings_Strings.right(sb.join(""),targetLength);
};
hx_strings_Strings.map = function(str,mapper,separator) {
	if(separator == null) {
		separator = "";
	}
	if(str == null) {
		return null;
	}
	if(separator == null) {
		throw haxe_Exception.thrown("[separator] must not be null");
	}
	var _this = hx_strings_Strings.split8(str,[separator]);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = mapper(_this[i]);
	}
	return result;
};
hx_strings_Strings.prependIfMissing = function(str,suffix) {
	if(str == null) {
		return null;
	}
	if(str.length == 0) {
		return suffix + Std.string(str);
	}
	if(hx_strings_Strings.startsWith(str,suffix)) {
		return str;
	}
	return suffix + Std.string(str);
};
hx_strings_Strings.quoteDouble = function(str) {
	if(str == null) {
		return null;
	}
	if(str.length == 0) {
		return "\"\"";
	}
	if(!(str == null ? false : str.indexOf("\"") > -1)) {
		return "\"" + Std.string(str) + "\"";
	}
	return "\"" + Std.string(hx_strings_Strings.replaceAll(str,"\"","\\\"")) + "\"";
};
hx_strings_Strings.quoteSingle = function(str) {
	if(str == null) {
		return null;
	}
	if(str.length == 0) {
		return "''";
	}
	if(!(str == null ? false : str.indexOf("'") > -1)) {
		return "'" + Std.string(str) + "'";
	}
	return "'" + Std.string(hx_strings_Strings.replaceAll(str,"'","\\'")) + "'";
};
hx_strings_Strings.removeAfter = function(str,searchFor) {
	return hx_strings_Strings.substringBefore(str,searchFor);
};
hx_strings_Strings.removeAfterLast = function(str,searchFor) {
	return hx_strings_Strings.substringBeforeLast(str,searchFor);
};
hx_strings_Strings.removeAfterIgnoreCase = function(str,searchFor) {
	return hx_strings_Strings.substringBeforeIgnoreCase(str,searchFor);
};
hx_strings_Strings.removeAfterLastIgnoreCase = function(str,searchFor) {
	return hx_strings_Strings.substringBeforeLastIgnoreCase(str,searchFor);
};
hx_strings_Strings.removeAt = function(str,pos,length) {
	if(str == null || str.length == 0 || length < 1) {
		return str;
	}
	var strLen = str == null ? 0 : str.length;
	if(pos < 0) {
		pos = strLen + pos;
	}
	if(pos < 0) {
		throw haxe_Exception.thrown("[pos] must be smaller than -1 * str.length");
	}
	if(pos + length >= strLen) {
		return hx_strings_Strings.substring8(str,0,pos);
	}
	return Std.string(hx_strings_Strings.substring8(str,0,pos)) + Std.string(hx_strings_Strings.substring8(str,pos + length));
};
hx_strings_Strings.removeBefore = function(str,searchFor) {
	return hx_strings_Strings.substringAfter(str,searchFor);
};
hx_strings_Strings.removeBeforeLast = function(str,searchFor) {
	return hx_strings_Strings.substringAfterLast(str,searchFor);
};
hx_strings_Strings.removeBeforeIgnoreCase = function(str,searchFor) {
	return hx_strings_Strings.substringAfterIgnoreCase(str,searchFor);
};
hx_strings_Strings.removeBeforeLastIgnoreCase = function(str,searchFor) {
	return hx_strings_Strings.substringAfterLastIgnoreCase(str,searchFor);
};
hx_strings_Strings.removeAll = function(searchIn,searchFor) {
	return hx_strings_Strings.replaceAll(searchIn,searchFor,"");
};
hx_strings_Strings.removeFirst = function(searchIn,searchFor) {
	return hx_strings_Strings.replaceFirst(searchIn,searchFor,"");
};
hx_strings_Strings.removeFirstIgnoreCase = function(searchIn,searchFor) {
	return hx_strings_Strings.replaceFirstIgnoreCase(searchIn,searchFor,"");
};
hx_strings_Strings.removeAnsi = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	return str.replace(hx_strings_Strings.REGEX_ANSI_ESC.ereg.r,"");
};
hx_strings_Strings.removeLeading = function(searchIn,searchFor) {
	if(searchIn == null || searchIn.length == 0 || (searchFor == null || searchFor.length == 0)) {
		return searchIn;
	}
	while(hx_strings_Strings.startsWith(searchIn,searchFor)) searchIn = searchIn.substring(searchFor.length,searchIn.length);
	return searchIn;
};
hx_strings_Strings.removeTags = function(xml) {
	if(xml == null || xml.length == 0) {
		return xml;
	}
	return xml.replace(hx_strings_Strings.REGEX_REMOVE_XML_TAGS.ereg.r,"");
};
hx_strings_Strings.removeTrailing = function(searchIn,searchFor) {
	if(searchIn == null || searchIn.length == 0 || (searchFor == null || searchFor.length == 0)) {
		return searchIn;
	}
	while(hx_strings_Strings.endsWith(searchIn,searchFor)) searchIn = searchIn.substring(0,searchIn.length - searchFor.length);
	return searchIn;
};
hx_strings_Strings.repeat = function(str,count,separator) {
	if(separator == null) {
		separator = "";
	}
	if(str == null) {
		return null;
	}
	if(count < 1) {
		return "";
	}
	if(count == 1) {
		return str;
	}
	var _g = [];
	var _g1 = 0;
	var _g2 = count;
	while(_g1 < _g2) {
		var i = _g1++;
		_g.push(str);
	}
	return _g.join(separator);
};
hx_strings_Strings.replaceAll = function(searchIn,searchFor,replaceWith) {
	if(searchIn == null || (searchIn == null || searchIn.length == 0) || searchFor == null) {
		return searchIn;
	}
	if(replaceWith == null) {
		replaceWith = "null";
	}
	return StringTools.replace(searchIn,searchFor,replaceWith);
};
hx_strings_Strings.replaceFirst = function(searchIn,searchFor,replaceWith) {
	if(searchIn == null || (searchIn == null || searchIn.length == 0) || searchFor == null) {
		return searchIn;
	}
	if(replaceWith == null) {
		replaceWith = "null";
	}
	var foundAt;
	if(searchFor.length == 0) {
		if((searchIn == null ? 0 : searchIn.length) > 1) {
			foundAt = 1;
		} else {
			return searchIn;
		}
	} else {
		foundAt = hx_strings_Strings.indexOf8(searchIn,searchFor);
	}
	return Std.string(hx_strings_Strings.substr8(searchIn,0,foundAt)) + replaceWith + Std.string(hx_strings_Strings.substr8(searchIn,foundAt + (searchFor == null ? 0 : searchFor.length)));
};
hx_strings_Strings.replaceFirstIgnoreCase = function(searchIn,searchFor,replaceWith) {
	if(searchIn == null || (searchIn == null || searchIn.length == 0) || searchFor == null) {
		return searchIn;
	}
	if(replaceWith == null) {
		replaceWith = "null";
	}
	searchFor = searchFor.toLowerCase();
	var foundAt;
	if(searchFor.length == 0) {
		if((searchIn == null ? 0 : searchIn.length) > 1) {
			foundAt = 1;
		} else {
			return searchIn;
		}
	} else {
		foundAt = hx_strings_Strings.indexOf8(searchIn.toLowerCase(),searchFor);
	}
	return Std.string(hx_strings_Strings.substr8(searchIn,0,foundAt)) + replaceWith + Std.string(hx_strings_Strings.substr8(searchIn,foundAt + (searchFor == null ? 0 : searchFor.length)));
};
hx_strings_Strings.reverse = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var chars = hx_strings_Strings.split8(str,[""]);
	chars.reverse();
	return chars.join("");
};
hx_strings_Strings.right = function(str,len) {
	if(str == null || str.length == 0) {
		return str;
	}
	return hx_strings_Strings.substring8(str,(str == null ? 0 : str.length) - len);
};
hx_strings_Strings.rpad = function(str,targetLength,padStr,canOverflow) {
	if(canOverflow == null) {
		canOverflow = true;
	}
	if(padStr == null) {
		padStr = " ";
	}
	var strLen = str == null ? 0 : str.length;
	if(str == null || strLen > targetLength) {
		return str;
	}
	if(padStr == null || padStr.length == 0) {
		padStr = " ";
	}
	var padLen = padStr == null ? 0 : padStr.length;
	var sb = new hx_strings_StringBuilder(str);
	while(strLen < targetLength) {
		sb.add(padStr);
		strLen += padLen;
	}
	if(canOverflow) {
		return sb.toString();
	}
	var str = sb.toString();
	return (str == null ? 0 : str.length) <= targetLength ? str : hx_strings_Strings.substring8(str,0,targetLength);
};
hx_strings_Strings.split8 = function(str,separator,maxParts) {
	if(maxParts == null) {
		maxParts = 0;
	}
	if(str == null || separator == null) {
		return null;
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen == 0) {
		return [];
	}
	var _g = [];
	var _g1 = 0;
	var _g2 = separator;
	while(_g1 < _g2.length) {
		var v = _g2[_g1];
		++_g1;
		if(v != null) {
			_g.push(v);
		}
	}
	var separators = _g;
	if(separators.length == 0) {
		return null;
	}
	if(maxParts <= 0 && separators.length == 1) {
		return str.split(separators[0]);
	}
	if(separators.indexOf("") > -1) {
		if(maxParts <= 0) {
			var _g = [];
			var _g1 = 0;
			var _g2 = strLen;
			while(_g1 < _g2) {
				var i = _g1++;
				_g.push(HxOverrides.substr(str,i,1));
			}
			return _g;
		}
		if(maxParts > strLen) {
			maxParts = strLen;
		}
		--maxParts;
		var _g = [];
		var _g1 = 0;
		var _g2 = maxParts;
		while(_g1 < _g2) {
			var i = _g1++;
			_g.push(HxOverrides.substr(str,i,1));
		}
		var result = _g;
		result.push(HxOverrides.substr(str,maxParts,strLen - maxParts));
		return result;
	}
	var _g = [];
	var _g1 = 0;
	while(_g1 < separators.length) {
		var sep = separators[_g1];
		++_g1;
		_g.push(sep == null ? 0 : sep.length);
	}
	var separatorsLengths = _g;
	var lastFoundAt = 0;
	var result = [];
	var resultCount = 0;
	while(true) {
		var separatorLen = 0;
		var foundAt = -1;
		var _g = 0;
		var _g1 = separators.length;
		while(_g < _g1) {
			var i = _g++;
			var sepFoundAt = hx_strings_Strings.indexOf8(str,separators[i],lastFoundAt);
			if(sepFoundAt != -1) {
				if(foundAt == -1 || sepFoundAt < foundAt) {
					foundAt = sepFoundAt;
					separatorLen = separatorsLengths[i];
				}
			}
		}
		++resultCount;
		if(foundAt == -1 || resultCount == maxParts) {
			result.push(HxOverrides.substr(str,lastFoundAt,strLen - lastFoundAt));
			break;
		}
		result.push(HxOverrides.substr(str,lastFoundAt,foundAt - lastFoundAt));
		lastFoundAt = foundAt + separatorLen;
	}
	return result;
};
hx_strings_Strings.splitAt = function(str,splitPos) {
	if(str == null) {
		return null;
	}
	if(splitPos == null || splitPos.length == 0) {
		return [str];
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen == 0) {
		return [str];
	}
	var pos = [];
	var _g = 0;
	var _g1 = splitPos;
	while(_g < _g1.length) {
		var p = _g1[_g];
		++_g;
		if(p < 0) {
			p = strLen + p;
		}
		if(p < 0 || p >= strLen) {
			continue;
		}
		if(pos.indexOf(p) > -1) {
			continue;
		}
		pos.push(p);
	}
	pos.sort(function(a,b) {
		if(a < b) {
			return -1;
		} else if(a > b) {
			return 1;
		} else {
			return 0;
		}
	});
	var result = [];
	var lastPos = 0;
	var _g = 0;
	while(_g < pos.length) {
		var p = pos[_g];
		++_g;
		var chunk = hx_strings_Strings.substring8(str,lastPos,p);
		if(chunk != null && chunk.length > 0) {
			result.push(chunk);
		}
		lastPos = p;
	}
	var chunk = hx_strings_Strings.substring8(str,lastPos);
	if(chunk != null && chunk.length > 0) {
		result.push(chunk);
	}
	return result;
};
hx_strings_Strings.splitEvery = function(str,count) {
	if(str == null) {
		return null;
	}
	if(count < 1) {
		throw haxe_Exception.thrown("[count] must be greater than 0");
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen == 0 || count >= strLen) {
		return [str];
	}
	var result = [];
	var pos = 0;
	while(true) {
		var chunk = hx_strings_Strings.substr8(str,pos,count);
		pos += count;
		if(chunk == null || chunk.length == 0) {
			break;
		}
		result.push(chunk);
	}
	return result;
};
hx_strings_Strings.splitLines = function(str) {
	if(str == null || str.length == 0) {
		return [];
	} else {
		return hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(str);
	}
};
hx_strings_Strings.startsWith = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	if(searchFor == null || searchFor.length == 0 || searchIn == searchFor) {
		return true;
	}
	return StringTools.startsWith(searchIn,searchFor);
};
hx_strings_Strings.startsWithAny = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(candidate != null && hx_strings_Strings.startsWith(searchIn,candidate)) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.startsWithAnyIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	searchIn = hx_strings_Strings.toLowerCase8(searchIn);
	var _g = 0;
	while(_g < searchFor.length) {
		var candidate = searchFor[_g];
		++_g;
		if(candidate != null && hx_strings_Strings.startsWith(searchIn,hx_strings_Strings.toLowerCase8(candidate))) {
			return true;
		}
	}
	return false;
};
hx_strings_Strings.startsWithIgnoreCase = function(searchIn,searchFor) {
	if(searchIn == null || searchFor == null) {
		return false;
	}
	if(searchFor == null || searchFor.length == 0) {
		return true;
	}
	return hx_strings_Strings.startsWith(searchIn.toLowerCase(),searchFor.toLowerCase());
};
hx_strings_Strings.substr8 = function(str,startAt,len) {
	if(str == null || str.length == 0) {
		return str;
	}
	if(len == null) {
		len = str == null ? 0 : str.length;
	}
	if(len <= 0) {
		return "";
	}
	if(startAt < 0) {
		startAt += str == null ? 0 : str.length;
		if(startAt < 0) {
			startAt = 0;
		}
	}
	return HxOverrides.substr(str,startAt,len);
};
hx_strings_Strings.substring8 = function(str,startAt,endAt) {
	if(str == null || str.length == 0) {
		return str;
	}
	if(endAt == null) {
		endAt = str == null ? 0 : str.length;
	}
	return str.substring(startAt,endAt);
};
hx_strings_Strings.substringAfter = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return str;
	}
	if(str == "" || searchFor == null || searchFor == "") {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundAt = str.indexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAt + searchFor.length);
};
hx_strings_Strings.substringAfterIgnoreCase = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	searchFor = searchFor.toLowerCase();
	var foundAt = str.toLowerCase().indexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAt + searchFor.length);
};
hx_strings_Strings.substringBetween = function(str,after,before,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(before == null) {
		before = after;
	}
	if(str == "" || (after == null || after.length == 0) || (before == null || before.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundAfterAt = str.indexOf(after);
	if(foundAfterAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundBeforeAt = str.indexOf(before,foundAfterAt + after.length);
	if(foundBeforeAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAfterAt + after.length,foundBeforeAt);
};
hx_strings_Strings.substringBetweenIgnoreCase = function(str,after,before,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(before == null) {
		before = after;
	}
	if(str == "" || (after == null || after.length == 0) || (before == null || before.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var strLower = hx_strings_Strings.toLowerCase8(str);
	var after1 = hx_strings_Strings.toLowerCase8(after);
	var before1 = hx_strings_Strings.toLowerCase8(before);
	var foundAfterAt = strLower.indexOf(after1);
	if(foundAfterAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundBeforeAt = strLower.indexOf(before1,foundAfterAt + after1.length);
	if(foundBeforeAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAfterAt + after1.length,foundBeforeAt);
};
hx_strings_Strings.substringAfterLast = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundAt = str.lastIndexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAt + searchFor.length);
};
hx_strings_Strings.substringAfterLastIgnoreCase = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	searchFor = searchFor.toLowerCase();
	var foundAt = str.toLowerCase().lastIndexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(foundAt + searchFor.length);
};
hx_strings_Strings.substringBefore = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundAt = str.indexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(0,foundAt);
};
hx_strings_Strings.substringBeforeIgnoreCase = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	searchFor = searchFor.toLowerCase();
	var foundAt = str.toLowerCase().indexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(0,foundAt);
};
hx_strings_Strings.substringBeforeLast = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	var foundAt = str.lastIndexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(0,foundAt);
};
hx_strings_Strings.substringBeforeLastIgnoreCase = function(str,searchFor,notFoundDefault) {
	if(notFoundDefault == null) {
		notFoundDefault = 2;
	}
	if(str == null) {
		return null;
	}
	if(str == "" || (searchFor == null || searchFor.length == 0)) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	searchFor = searchFor.toLowerCase();
	var foundAt = str.toLowerCase().lastIndexOf(searchFor);
	if(foundAt == -1) {
		var tmp;
		switch(notFoundDefault) {
		case 1:
			tmp = null;
			break;
		case 2:
			tmp = "";
			break;
		case 3:
			tmp = str;
			break;
		}
		return tmp;
	}
	return str.substring(0,foundAt);
};
hx_strings_Strings.toBool = function(str) {
	if(str == null || str.length == 0) {
		return false;
	}
	switch(str.toLowerCase()) {
	case "0":case "false":case "no":
		return false;
	default:
		return true;
	}
};
hx_strings_Strings.toBytes = function(str) {
	if(str == null) {
		return null;
	}
	return haxe_io_Bytes.ofString(str);
};
hx_strings_Strings.toChar = function(charCode) {
	return charCode;
};
hx_strings_Strings.toCharIterator = function(str) {
	if(str == null) {
		return hx_strings__$CharIterator_NullCharIterator.INSTANCE;
	} else {
		return new hx_strings__$CharIterator_StringCharIterator(str,0);
	}
};
hx_strings_Strings.toChars = function(str) {
	if(str == null) {
		return null;
	}
	var strLen = str == null ? 0 : str.length;
	if(strLen == 0) {
		return [];
	}
	var _g = [];
	var _g1 = 0;
	var _g2 = strLen;
	while(_g1 < _g2) {
		var i = _g1++;
		_g.push(HxOverrides.cca(str,i));
	}
	return _g;
};
hx_strings_Strings.toPattern = function(str,options) {
	if(str == null) {
		return null;
	}
	return hx_strings_Pattern.compile(str,options);
};
hx_strings_Strings.toEReg = function(str,opt) {
	if(opt == null) {
		opt = "";
	}
	if(str == null) {
		throw haxe_Exception.thrown("[str] must not be null");
	}
	return new EReg(str,opt);
};
hx_strings_Strings.toFloat = function(str,ifUnparseable) {
	if(str == null) {
		return ifUnparseable;
	}
	var result = parseFloat(str);
	if(isNaN(result)) {
		return ifUnparseable;
	} else {
		return result;
	}
};
hx_strings_Strings.toFloatOrNull = function(str,ifUnparseable) {
	if(str == null) {
		return ifUnparseable;
	}
	var result = parseFloat(str);
	if(isNaN(result)) {
		return ifUnparseable;
	} else {
		return result;
	}
};
hx_strings_Strings.toHex = function(num,minDigits,upperCase) {
	if(upperCase == null) {
		upperCase = true;
	}
	if(minDigits == null) {
		minDigits = 0;
	}
	var hexed = StringTools.hex(num,0);
	if(!upperCase) {
		return hexed.toLowerCase();
	}
	if(hexed.length >= minDigits) {
		return hexed;
	}
	return hx_strings_Strings.lpad(hexed,minDigits,"0");
};
hx_strings_Strings.toInt = function(str,ifUnparseable) {
	if(str == null) {
		return ifUnparseable;
	}
	var result = Std.parseInt(str);
	if(result == null) {
		return ifUnparseable;
	} else {
		return result;
	}
};
hx_strings_Strings.toIntOrNull = function(str,ifUnparseable) {
	if(str == null) {
		return ifUnparseable;
	}
	var result = Std.parseInt(str);
	if(result == null) {
		return ifUnparseable;
	} else {
		return result;
	}
};
hx_strings_Strings.toLowerCase8 = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	return str.toLowerCase();
};
hx_strings_Strings.toLowerCaseFirstChar = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var this1 = HxOverrides.cca(str,0);
	var lowerChar = hx_strings_Char.CHAR_CASE_MAPPER.mapU2L.h[this1];
	var firstChar = lowerChar == null ? this1 : lowerChar;
	if(str.length == 1) {
		return String.fromCodePoint(firstChar);
	}
	var other = hx_strings_Strings.substr8(str,1);
	return String.fromCodePoint(firstChar) + other;
};
hx_strings_Strings.toLowerCamel = function(str,keepUppercasedWords) {
	if(keepUppercasedWords == null) {
		keepUppercasedWords = true;
	}
	if(str == null || str.length == 0) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	if(keepUppercasedWords) {
		var _g = 0;
		var _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(str);
		while(_g < _g1.length) {
			var word = _g1[_g];
			++_g;
			sb.add(hx_strings_Strings.toUpperCaseFirstChar(word));
		}
	} else {
		var _g = 0;
		var _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(str);
		while(_g < _g1.length) {
			var word = _g1[_g];
			++_g;
			sb.add(hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(word)));
		}
	}
	return hx_strings_Strings.toLowerCaseFirstChar(sb.toString());
};
hx_strings_Strings.toLowerHyphen = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _this = hx_strings_Strings._splitAsciiWordsUnsafe(str);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = hx_strings_Strings.toLowerCase8(_this[i]);
	}
	return result.join("-");
};
hx_strings_Strings.toLowerUnderscore = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _this = hx_strings_Strings._splitAsciiWordsUnsafe(str);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = hx_strings_Strings.toLowerCase8(_this[i]);
	}
	return result.join("_");
};
hx_strings_Strings.toTitle = function(str,keepUppercasedWords) {
	if(keepUppercasedWords == null) {
		keepUppercasedWords = true;
	}
	if(str == null || str.length == 0) {
		return str;
	}
	if(keepUppercasedWords) {
		var _this = hx_strings_Strings._splitAsciiWordsUnsafe(str);
		var result = new Array(_this.length);
		var _g = 0;
		var _g1 = _this.length;
		while(_g < _g1) {
			var i = _g++;
			var s = _this[i];
			result[i] = hx_strings_Strings.toUpperCase8(s) == s ? s : hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(s));
		}
		return result.join(" ");
	}
	var _this = hx_strings_Strings._splitAsciiWordsUnsafe(str);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(_this[i]));
	}
	return result.join(" ");
};
hx_strings_Strings.toUpperCamel = function(str,keepUppercasedWords) {
	if(keepUppercasedWords == null) {
		keepUppercasedWords = true;
	}
	if(str == null || str.length == 0) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	if(keepUppercasedWords) {
		var _g = 0;
		var _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(str);
		while(_g < _g1.length) {
			var word = _g1[_g];
			++_g;
			sb.add(hx_strings_Strings.toUpperCaseFirstChar(word));
		}
	} else {
		var _g = 0;
		var _g1 = hx_strings_Strings._splitAsciiWordsUnsafe(str);
		while(_g < _g1.length) {
			var word = _g1[_g];
			++_g;
			sb.add(hx_strings_Strings.toUpperCaseFirstChar(hx_strings_Strings.toLowerCase8(word)));
		}
	}
	return sb.toString();
};
hx_strings_Strings.toUpperUnderscore = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _this = hx_strings_Strings._splitAsciiWordsUnsafe(str);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = hx_strings_Strings.toUpperCase8(_this[i]);
	}
	return result.join("_");
};
hx_strings_Strings.toString = function(str) {
	if(str == null) {
		return "null";
	} else {
		return str;
	}
};
hx_strings_Strings.toUpperCase8 = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	var _g = 0;
	var _g1 = str == null ? 0 : str.length;
	while(_g < _g1) {
		var i = _g++;
		var this1 = HxOverrides.cca(str,i);
		var upperChar = hx_strings_Char.CHAR_CASE_MAPPER.mapL2U.h[this1];
		sb.addChar(upperChar == null ? this1 : upperChar);
	}
	return sb.toString();
};
hx_strings_Strings.toUpperCaseFirstChar = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	var this1 = HxOverrides.cca(str,0);
	var upperChar = hx_strings_Char.CHAR_CASE_MAPPER.mapL2U.h[this1];
	var firstChar = upperChar == null ? this1 : upperChar;
	if(str.length == 1) {
		return String.fromCodePoint(firstChar);
	}
	var other = hx_strings_Strings.substr8(str,1);
	return String.fromCodePoint(firstChar) + other;
};
hx_strings_Strings.trim = function(str,charsToRemove) {
	if(str == null || str.length == 0) {
		return str;
	}
	if(charsToRemove == null) {
		return StringTools.trim(str);
	}
	var removableChars;
	var _g = charsToRemove;
	switch(_g._hx_index) {
	case 0:
		var str1 = _g.v;
		removableChars = hx_strings_Strings.toChars(str1);
		break;
	case 1:
		var chars = _g.v;
		removableChars = chars;
		break;
	}
	var this1 = hx_strings_internal__$Either2__$Either2.b(removableChars);
	var this2 = hx_strings_internal__$Either2__$Either2.b(removableChars);
	return hx_strings_Strings.trimLeft(hx_strings_Strings.trimRight(str,this1),this2);
};
hx_strings_Strings.trimRight = function(str,charsToRemove) {
	if(str == null || str.length == 0) {
		return str;
	}
	if(charsToRemove == null) {
		return StringTools.rtrim(str);
	}
	var removableChars;
	var _g = charsToRemove;
	switch(_g._hx_index) {
	case 0:
		var str1 = _g.v;
		removableChars = hx_strings_Strings.toChars(str1);
		break;
	case 1:
		var chars = _g.v;
		removableChars = chars;
		break;
	}
	if(removableChars.length == 0) {
		return str;
	}
	var len = str == null ? 0 : str.length;
	var i = len - 1;
	while(i > -1 && removableChars.indexOf(hx_strings_Strings.charCodeAt8(hx_strings_Strings.charAt8(str,i),0)) > -1) --i;
	if(i < len - 1) {
		return hx_strings_Strings.substring8(str,0,i + 1);
	}
	return str;
};
hx_strings_Strings.trimLeft = function(str,charsToRemove) {
	if(str == null) {
		return str;
	}
	if(charsToRemove == null) {
		return StringTools.ltrim(str);
	}
	var removableChars;
	var _g = charsToRemove;
	switch(_g._hx_index) {
	case 0:
		var str1 = _g.v;
		removableChars = hx_strings_Strings.toChars(str1);
		break;
	case 1:
		var chars = _g.v;
		removableChars = chars;
		break;
	}
	if(removableChars.length == 0) {
		return str;
	}
	var len = str == null ? 0 : str.length;
	var i = 0;
	while(i < len && removableChars.indexOf(hx_strings_Strings.charCodeAt8(hx_strings_Strings.charAt8(str,i),0)) > -1) ++i;
	if(i > 0) {
		return hx_strings_Strings.substring8(str,i,len);
	}
	return str;
};
hx_strings_Strings.trimLines = function(str,charsToRemove) {
	if(str == null || str.length == 0) {
		return str;
	}
	var _this = hx_strings_Strings.REGEX_SPLIT_LINES.ereg.split(str);
	var result = new Array(_this.length);
	var _g = 0;
	var _g1 = _this.length;
	while(_g < _g1) {
		var i = _g++;
		result[i] = hx_strings_Strings.trim(_this[i],charsToRemove);
	}
	return result.join("\n");
};
hx_strings_Strings.trimToNull = function(str) {
	if(str == null) {
		return null;
	}
	var trimmed = hx_strings_Strings.trim(str);
	if(trimmed == null || trimmed.length == 0) {
		return null;
	}
	return trimmed;
};
hx_strings_Strings.trimToEmpty = function(str) {
	var trimmed = hx_strings_Strings.trim(str);
	if(trimmed == null || trimmed.length == 0) {
		return "";
	}
	return trimmed;
};
hx_strings_Strings.truncate = function(str,maxLength) {
	if((str == null ? 0 : str.length) <= maxLength) {
		return str;
	} else {
		return hx_strings_Strings.substring8(str,0,maxLength);
	}
};
hx_strings_Strings.urlDecode = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	return decodeURIComponent(str.split("+").join(" "));
};
hx_strings_Strings.urlEncode = function(str) {
	if(str == null || str.length == 0) {
		return str;
	}
	return encodeURIComponent(str);
};
hx_strings_Strings.wrap = function(str,maxLineLength,splitLongWords,newLineSeparator) {
	if(newLineSeparator == null) {
		newLineSeparator = "\n";
	}
	if(splitLongWords == null) {
		splitLongWords = true;
	}
	if((str == null ? 0 : str.length) <= maxLineLength || maxLineLength < 1) {
		return str;
	}
	var sb = new hx_strings_StringBuilder();
	var wordChars = [];
	var currLineLength = 0;
	var _g = 0;
	var _g1 = hx_strings_Strings.toChars(str);
	while(_g < _g1.length) {
		var ch = _g1[_g];
		++_g;
		if(ch > 8 && ch < 14 || ch == 32) {
			if(wordChars.length > 0) {
				var _g2 = 0;
				while(_g2 < wordChars.length) {
					var wordCh = wordChars[_g2];
					++_g2;
					if(currLineLength == maxLineLength && splitLongWords) {
						sb.add(newLineSeparator);
						currLineLength = 0;
					}
					++currLineLength;
					sb.addChar(wordCh);
				}
				wordChars = [];
			}
			if(currLineLength >= maxLineLength) {
				sb.add(newLineSeparator);
				currLineLength = 0;
			}
			sb.addChar(ch);
			++currLineLength;
		} else {
			wordChars.push(ch);
		}
	}
	if(wordChars.length > 0) {
		var _g = 0;
		while(_g < wordChars.length) {
			var wordCh = wordChars[_g];
			++_g;
			if(currLineLength == maxLineLength && splitLongWords) {
				sb.add(newLineSeparator);
				currLineLength = 0;
			}
			++currLineLength;
			sb.addChar(wordCh);
		}
	}
	return sb.toString();
};
var hx_strings_StringDiff = function() {
	this.at = -1;
};
hx_strings_StringDiff.__name__ = "hx.strings.StringDiff";
hx_strings_StringDiff.prototype = {
	at: null
	,left: null
	,right: null
	,toString: function() {
		return "StringDiff[at=" + this.at + ", left=" + this.left + ", right=" + this.right + "]";
	}
	,__class__: hx_strings_StringDiff
};
var hx_strings_HashCodeAlgorithm = $hxEnums["hx.strings.HashCodeAlgorithm"] = { __ename__:"hx.strings.HashCodeAlgorithm",__constructs__:null
	,PLATFORM_SPECIFIC: {_hx_name:"PLATFORM_SPECIFIC",_hx_index:0,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
	,ADLER32: {_hx_name:"ADLER32",_hx_index:1,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
	,CRC32B: {_hx_name:"CRC32B",_hx_index:2,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
	,DJB2A: {_hx_name:"DJB2A",_hx_index:3,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
	,JAVA: {_hx_name:"JAVA",_hx_index:4,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
	,SDBM: {_hx_name:"SDBM",_hx_index:5,__enum__:"hx.strings.HashCodeAlgorithm",toString:$estr}
};
hx_strings_HashCodeAlgorithm.__constructs__ = [hx_strings_HashCodeAlgorithm.PLATFORM_SPECIFIC,hx_strings_HashCodeAlgorithm.ADLER32,hx_strings_HashCodeAlgorithm.CRC32B,hx_strings_HashCodeAlgorithm.DJB2A,hx_strings_HashCodeAlgorithm.JAVA,hx_strings_HashCodeAlgorithm.SDBM];
var hx_strings_AnsiToHtmlRenderMethod = $hxEnums["hx.strings.AnsiToHtmlRenderMethod"] = { __ename__:"hx.strings.AnsiToHtmlRenderMethod",__constructs__:null
	,StyleAttributes: {_hx_name:"StyleAttributes",_hx_index:0,__enum__:"hx.strings.AnsiToHtmlRenderMethod",toString:$estr}
	,CssClasses: {_hx_name:"CssClasses",_hx_index:1,__enum__:"hx.strings.AnsiToHtmlRenderMethod",toString:$estr}
	,CssClassesCallback: ($_=function(func) { return {_hx_index:2,func:func,__enum__:"hx.strings.AnsiToHtmlRenderMethod",toString:$estr}; },$_._hx_name="CssClassesCallback",$_.__params__ = ["func"],$_)
};
hx_strings_AnsiToHtmlRenderMethod.__constructs__ = [hx_strings_AnsiToHtmlRenderMethod.StyleAttributes,hx_strings_AnsiToHtmlRenderMethod.CssClasses,hx_strings_AnsiToHtmlRenderMethod.CssClassesCallback];
var hx_strings_AnsiState = function(copyFrom) {
	this.underline = false;
	this.bold = false;
	this.blink = false;
	if(copyFrom == null) {
		this.reset();
	} else {
		this.copyFrom(copyFrom);
	}
};
hx_strings_AnsiState.__name__ = "hx.strings.AnsiState";
hx_strings_AnsiState.defaultCssClassesCallback = function(state) {
	var classes = [];
	if(state.fgcolor != null) {
		classes.push("ansi_fg_" + state.fgcolor);
	}
	if(state.bgcolor != null) {
		classes.push("ansi_bg_" + state.bgcolor);
	}
	if(state.bold) {
		classes.push("ansi_bold");
	}
	if(state.underline) {
		classes.push("ansi_underline");
	}
	if(state.blink) {
		classes.push("ansi_blink");
	}
	return classes.join(" ");
};
hx_strings_AnsiState.prototype = {
	bgcolor: null
	,blink: null
	,bold: null
	,fgcolor: null
	,underline: null
	,isActive: function() {
		if(!(this.fgcolor != null || this.bgcolor != null || this.bold || this.underline)) {
			return this.blink;
		} else {
			return true;
		}
	}
	,reset: function() {
		this.fgcolor = null;
		this.bgcolor = null;
		this.bold = false;
		this.underline = false;
		this.blink = false;
	}
	,copyFrom: function(other) {
		this.fgcolor = other.fgcolor;
		this.bgcolor = other.bgcolor;
		this.bold = other.bold;
		this.underline = other.underline;
		this.blink = other.blink;
	}
	,setGraphicModeParameter: function(param) {
		switch(param) {
		case 0:
			this.reset();
			break;
		case 1:
			this.bold = true;
			break;
		case 4:
			this.underline = true;
			break;
		case 5:
			this.blink = true;
			break;
		case 30:
			this.fgcolor = "black";
			break;
		case 31:
			this.fgcolor = "red";
			break;
		case 32:
			this.fgcolor = "green";
			break;
		case 33:
			this.fgcolor = "yellow";
			break;
		case 34:
			this.fgcolor = "blue";
			break;
		case 35:
			this.fgcolor = "magenta";
			break;
		case 36:
			this.fgcolor = "cyan";
			break;
		case 37:
			this.fgcolor = "white";
			break;
		case 40:
			this.bgcolor = "black";
			break;
		case 41:
			this.bgcolor = "red";
			break;
		case 42:
			this.bgcolor = "green";
			break;
		case 43:
			this.bgcolor = "yellow";
			break;
		case 44:
			this.bgcolor = "blue";
			break;
		case 45:
			this.bgcolor = "magenta";
			break;
		case 46:
			this.bgcolor = "cyan";
			break;
		case 47:
			this.bgcolor = "white";
			break;
		}
	}
	,toCSS: function(renderMethod) {
		if(this.fgcolor != null || this.bgcolor != null || this.bold || this.underline || this.blink) {
			var sb = new hx_strings_StringBuilder();
			if(renderMethod == null) {
				renderMethod = hx_strings_AnsiToHtmlRenderMethod.StyleAttributes;
			}
			switch(renderMethod._hx_index) {
			case 0:
				if(this.fgcolor != null) {
					sb.add("color:").add(this.fgcolor).add(";");
				}
				if(this.bgcolor != null) {
					sb.add("background-color:").add(this.bgcolor).add(";");
				}
				if(this.bold) {
					sb.add("font-weight:bold;");
				}
				if(this.underline) {
					sb.add("text-decoration:underline;");
				}
				if(this.blink) {
					sb.add("text-decoration:blink;");
				}
				break;
			case 1:
				sb.add(hx_strings_AnsiState.defaultCssClassesCallback(this));
				break;
			case 2:
				var func = renderMethod.func;
				sb.add(func(this));
				break;
			}
			return sb.toString();
		}
		return "";
	}
	,__class__: hx_strings_AnsiState
};
var hx_strings_internal_Bits = function() { };
hx_strings_internal_Bits.__name__ = "hx.strings.internal.Bits";
hx_strings_internal_Bits.clearBit = function(num,bitPos) {
	return num & ~(1 << bitPos - 1);
};
hx_strings_internal_Bits.setBit = function(num,bitPos) {
	return num | 1 << bitPos - 1;
};
hx_strings_internal_Bits.toggleBit = function(num,bitPos) {
	return num ^ 1 << bitPos - 1;
};
hx_strings_internal_Bits.getBit = function(num,bitPos) {
	return 1 == (num >> bitPos - 1 & 1);
};
var hx_strings_internal_Either2 = {};
hx_strings_internal_Either2.__properties__ = {get_value:"get_value"};
hx_strings_internal_Either2._new = function(value) {
	var this1 = value;
	return this1;
};
hx_strings_internal_Either2.get_value = function(this1) {
	return this1;
};
hx_strings_internal_Either2.fromA = function(value) {
	var this1 = hx_strings_internal__$Either2__$Either2.a(value);
	return this1;
};
hx_strings_internal_Either2.fromB = function(value) {
	var this1 = hx_strings_internal__$Either2__$Either2.b(value);
	return this1;
};
var hx_strings_internal__$Either2__$Either2 = $hxEnums["hx.strings.internal._Either2._Either2"] = { __ename__:"hx.strings.internal._Either2._Either2",__constructs__:null
	,a: ($_=function(v) { return {_hx_index:0,v:v,__enum__:"hx.strings.internal._Either2._Either2",toString:$estr}; },$_._hx_name="a",$_.__params__ = ["v"],$_)
	,b: ($_=function(v) { return {_hx_index:1,v:v,__enum__:"hx.strings.internal._Either2._Either2",toString:$estr}; },$_._hx_name="b",$_.__params__ = ["v"],$_)
};
hx_strings_internal__$Either2__$Either2.__constructs__ = [hx_strings_internal__$Either2__$Either2.a,hx_strings_internal__$Either2__$Either2.b];
var hx_strings_internal_Either3 = {};
hx_strings_internal_Either3.__properties__ = {get_value:"get_value"};
hx_strings_internal_Either3._new = function(value) {
	var this1 = value;
	return this1;
};
hx_strings_internal_Either3.get_value = function(this1) {
	return this1;
};
hx_strings_internal_Either3.fromA = function(value) {
	var this1 = hx_strings_internal__$Either3__$Either3.a(value);
	return this1;
};
hx_strings_internal_Either3.fromB = function(value) {
	var this1 = hx_strings_internal__$Either3__$Either3.b(value);
	return this1;
};
hx_strings_internal_Either3.fromC = function(value) {
	var this1 = hx_strings_internal__$Either3__$Either3.c(value);
	return this1;
};
var hx_strings_internal_OneOrMany = {};
hx_strings_internal_OneOrMany.fromSingle = function(value) {
	return [value];
};
var hx_strings_internal_RingBuffer = {};
hx_strings_internal_RingBuffer._new = function(size) {
	var this1 = new hx_strings_internal__$RingBuffer_RingBufferImpl(size);
	return this1;
};
hx_strings_internal_RingBuffer.get = function(this1,index) {
	return this1.get(index);
};
var hx_strings_internal__$RingBuffer_RingBufferIterator = function(buff) {
	this.idx = -1;
	this.buff = buff;
};
hx_strings_internal__$RingBuffer_RingBufferIterator.__name__ = "hx.strings.internal._RingBuffer.RingBufferIterator";
hx_strings_internal__$RingBuffer_RingBufferIterator.prototype = {
	buff: null
	,idx: null
	,hasNext: function() {
		return this.idx + 1 < this.buff.length;
	}
	,next: function() {
		this.idx++;
		return this.buff.get(this.idx);
	}
	,__class__: hx_strings_internal__$RingBuffer_RingBufferIterator
};
var utest_Assert = function() { };
utest_Assert.__name__ = "utest.Assert";
utest_Assert.processResult = function(cond,getMessage,pos) {
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(getMessage(),pos));
	}
	return cond;
};
utest_Assert.isTrue = function(cond,msg,pos) {
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected true",pos));
	}
	return cond;
};
utest_Assert.isFalse = function(value,msg,pos) {
	var cond = value == false;
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected false",pos));
	}
	return cond;
};
utest_Assert.isNull = function(value,msg,pos) {
	var cond = value == null;
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected null but it is " + utest_Assert.q(value),pos));
	}
	return cond;
};
utest_Assert.notNull = function(value,msg,pos) {
	var cond = value != null;
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected not null",pos));
	}
	return cond;
};
utest_Assert.is = function(value,type,msg,pos) {
	return utest_Assert.isOfType(value,type,msg,pos);
};
utest_Assert.isOfType = function(value,type,msg,pos) {
	var cond = js_Boot.__instanceof(value,type);
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected type " + utest_Assert.typeToString(type) + " but it is " + utest_Assert.typeToString(value),pos));
	}
	return cond;
};
utest_Assert.notEquals = function(expected,value,msg,pos) {
	var cond = expected != value;
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected " + utest_Assert.q(expected) + " and test value " + utest_Assert.q(value) + " should be different",pos));
	}
	return cond;
};
utest_Assert.equals = function(expected,value,msg,pos) {
	var cond = expected == value;
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value),pos));
	}
	return cond;
};
utest_Assert.match = function(pattern,value,msg,pos) {
	var cond = pattern.match(value);
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "the value " + utest_Assert.q(value) + " does not match the provided pattern",pos));
	}
	return cond;
};
utest_Assert.floatEquals = function(expected,value,approx,msg,pos) {
	var cond = utest_Assert._floatEquals(expected,value,approx);
	if(utest_Assert.results == null) {
		throw haxe_Exception.thrown("Assert at " + pos.fileName + ":" + pos.lineNumber + " out of context. Most likely you are trying to assert after a test timeout.");
	}
	if(cond) {
		utest_Assert.results.add(utest_Assertation.Success(pos));
	} else {
		utest_Assert.results.add(utest_Assertation.Failure(msg != null ? msg : "expected " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value),pos));
	}
	return cond;
};
utest_Assert._floatEquals = function(expected,value,approx) {
	if(isNaN(expected)) {
		return isNaN(value);
	} else if(isNaN(value)) {
		return false;
	} else if(!isFinite(expected) && !isFinite(value)) {
		return expected > 0 == value > 0;
	}
	if(null == approx) {
		approx = 1e-5;
	}
	return Math.abs(value - expected) <= approx;
};
utest_Assert.getTypeName = function(v) {
	var _g = Type.typeof(v);
	switch(_g._hx_index) {
	case 0:
		return "`null`";
	case 1:
		return "Int";
	case 2:
		return "Float";
	case 3:
		return "Bool";
	case 4:
		return "Object";
	case 5:
		return "function";
	case 6:
		var c = _g.c;
		return c.__name__;
	case 7:
		var e = _g.e;
		return e.__ename__;
	case 8:
		return "`Unknown`";
	}
};
utest_Assert.isIterable = function(v,isAnonym) {
	var fields = isAnonym ? Reflect.fields(v) : Type.getInstanceFields(js_Boot.getClass(v));
	if(!Lambda.has(fields,"iterator")) {
		return false;
	}
	return Reflect.isFunction(Reflect.field(v,"iterator"));
};
utest_Assert.isIterator = function(v,isAnonym) {
	var fields = isAnonym ? Reflect.fields(v) : Type.getInstanceFields(js_Boot.getClass(v));
	if(!Lambda.has(fields,"next") || !Lambda.has(fields,"hasNext")) {
		return false;
	}
	if(Reflect.isFunction(Reflect.field(v,"next"))) {
		return Reflect.isFunction(Reflect.field(v,"hasNext"));
	} else {
		return false;
	}
};
utest_Assert.sameAs = function(expected,value,status,approx) {
	var texpected = utest_Assert.getTypeName(expected);
	var tvalue = utest_Assert.getTypeName(value);
	status.expectedValue = expected;
	status.actualValue = value;
	if(texpected != tvalue && !(texpected == "Int" && tvalue == "Float" || texpected == "Float" && tvalue == "Int")) {
		status.error = "expected type " + texpected + " but it is " + tvalue + (status.path == "" ? "" : " for field " + status.path);
		return false;
	}
	var _g = Type.typeof(expected);
	switch(_g._hx_index) {
	case 1:case 2:
		if(!utest_Assert._floatEquals(expected,value,approx)) {
			status.error = "expected " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value) + (status.path == "" ? "" : " for field " + status.path);
			return false;
		}
		return true;
	case 0:case 3:
		if(expected != value) {
			status.error = "expected " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value) + (status.path == "" ? "" : " for field " + status.path);
			return false;
		}
		return true;
	case 4:
		if(status.recursive || status.path == "") {
			var tfields = Reflect.fields(value);
			var fields = Reflect.fields(expected);
			var path = status.path;
			var _g1 = 0;
			while(_g1 < fields.length) {
				var field = fields[_g1];
				++_g1;
				HxOverrides.remove(tfields,field);
				status.path = path == "" ? field : path + "." + field;
				if(!Object.prototype.hasOwnProperty.call(value,field)) {
					status.error = "expected field " + status.path + " does not exist in " + utest_Assert.q(value);
					return false;
				}
				var e = Reflect.field(expected,field);
				if(Reflect.isFunction(e)) {
					continue;
				}
				var v = Reflect.field(value,field);
				if(!utest_Assert.sameAs(e,v,status,approx)) {
					return false;
				}
			}
			if(tfields.length > 0) {
				status.error = "the tested object has extra field(s) (" + tfields.join(", ") + ") not included in the expected ones";
				return false;
			}
		}
		if(utest_Assert.isIterator(expected,true)) {
			if(!utest_Assert.isIterator(value,true)) {
				status.error = "expected Iterable but it is not " + (status.path == "" ? "" : " for field " + status.path);
				return false;
			}
			if(status.recursive || status.path == "") {
				var evalues = Lambda.array({ iterator : function() {
					return expected;
				}});
				var vvalues = Lambda.array({ iterator : function() {
					return value;
				}});
				if(evalues.length != vvalues.length) {
					status.error = "expected " + evalues.length + " values in Iterator but they are " + vvalues.length + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				var _g2 = evalues.length;
				while(_g1 < _g2) {
					var i = _g1++;
					status.path = path == "" ? "iterator[" + i + "]" : path + "[" + i + "]";
					if(!utest_Assert.sameAs(evalues[i],vvalues[i],status,approx)) {
						status.error = "expected " + utest_Assert.q(status.expectedValue) + " but it is " + utest_Assert.q(status.actualValue) + (status.path == "" ? "" : " for field " + status.path);
						return false;
					}
				}
			}
			return true;
		}
		if(utest_Assert.isIterable(expected,true)) {
			if(!utest_Assert.isIterable(value,true)) {
				status.error = "expected Iterator but it is not " + (status.path == "" ? "" : " for field " + status.path);
				return false;
			}
			if(status.recursive || status.path == "") {
				var evalues = Lambda.array(expected);
				var vvalues = Lambda.array(value);
				if(evalues.length != vvalues.length) {
					status.error = "expected " + evalues.length + " values in Iterable but they are " + vvalues.length + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				var _g2 = evalues.length;
				while(_g1 < _g2) {
					var i = _g1++;
					status.path = path == "" ? "iterable[" + i + "]" : path + "[" + i + "]";
					if(!utest_Assert.sameAs(evalues[i],vvalues[i],status,approx)) {
						return false;
					}
				}
			}
			return true;
		}
		return true;
	case 5:
		if(!Reflect.compareMethods(expected,value)) {
			status.error = "expected same function reference" + (status.path == "" ? "" : " for field " + status.path);
			return false;
		}
		return true;
	case 6:
		var c = _g.c;
		var cexpected = c.__name__;
		var c = js_Boot.getClass(value);
		var cvalue = c.__name__;
		if(cexpected != cvalue) {
			status.error = "expected instance of " + utest_Assert.q(cexpected) + " but it is " + utest_Assert.q(cvalue) + (status.path == "" ? "" : " for field " + status.path);
			return false;
		}
		if(typeof(expected) == "string") {
			if(expected == value) {
				return true;
			} else {
				status.error = "expected string '" + Std.string(expected) + "' but it is '" + Std.string(value) + "'";
				return false;
			}
		}
		if(((expected) instanceof Array)) {
			if(status.recursive || status.path == "") {
				if(expected.length != value.length) {
					status.error = "expected " + Std.string(expected.length) + " elements but they are " + Std.string(value.length) + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				var _g2 = expected.length;
				while(_g1 < _g2) {
					var i = _g1++;
					status.path = path == "" ? "array[" + i + "]" : path + "[" + i + "]";
					if(!utest_Assert.sameAs(expected[i],value[i],status,approx)) {
						status.error = "expected array element at [" + i + "] to have " + utest_Assert.q(status.expectedValue) + " but it is " + utest_Assert.q(status.actualValue) + (status.path == "" ? "" : " for field " + status.path);
						return false;
					}
				}
			}
			return true;
		}
		if(((expected) instanceof Date)) {
			if(expected.getTime() != value.getTime()) {
				status.error = "expected " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value) + (status.path == "" ? "" : " for field " + status.path);
				return false;
			}
			return true;
		}
		if(((expected) instanceof haxe_io_Bytes)) {
			if(status.recursive || status.path == "") {
				var ebytes = expected;
				var vbytes = value;
				if(ebytes.length != vbytes.length) {
					status.error = "expected " + ebytes.length + " bytes length but it is " + vbytes.length;
					return false;
				}
				var _g1 = 0;
				var _g2 = ebytes.length;
				while(_g1 < _g2) {
					var i = _g1++;
					if(ebytes.b[i] != vbytes.b[i]) {
						status.error = "expected byte #" + i + " to be " + ebytes.b[i] + " but it is " + vbytes.b[i] + (status.path == "" ? "" : " for field " + status.path);
						return false;
					}
				}
			}
			return true;
		}
		if(js_Boot.__implements(expected,haxe_IMap)) {
			if(status.recursive || status.path == "") {
				var map = js_Boot.__cast(expected , haxe_IMap);
				var vmap = js_Boot.__cast(value , haxe_IMap);
				var _g1 = [];
				var k = map.keys();
				while(k.hasNext()) {
					var k1 = k.next();
					_g1.push(k1);
				}
				var keys = _g1;
				var _g1 = [];
				var k = vmap.keys();
				while(k.hasNext()) {
					var k1 = k.next();
					_g1.push(k1);
				}
				var vkeys = _g1;
				if(keys.length != vkeys.length) {
					status.error = "expected " + keys.length + " keys but they are " + vkeys.length + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				while(_g1 < keys.length) {
					var key = keys[_g1];
					++_g1;
					status.path = path == "" ? "hash[" + Std.string(key) + "]" : path + "[" + Std.string(key) + "]";
					if(!utest_Assert.sameAs(map.get(key),vmap.get(key),status,approx)) {
						status.error = "expected " + utest_Assert.q(status.expectedValue) + " but it is " + utest_Assert.q(status.actualValue) + (status.path == "" ? "" : " for field " + status.path);
						return false;
					}
				}
			}
			return true;
		}
		if(utest_Assert.isIterator(expected,false)) {
			if(status.recursive || status.path == "") {
				var evalues = Lambda.array({ iterator : function() {
					return expected;
				}});
				var vvalues = Lambda.array({ iterator : function() {
					return value;
				}});
				if(evalues.length != vvalues.length) {
					status.error = "expected " + evalues.length + " values in Iterator but they are " + vvalues.length + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				var _g2 = evalues.length;
				while(_g1 < _g2) {
					var i = _g1++;
					status.path = path == "" ? "iterator[" + i + "]" : path + "[" + i + "]";
					if(!utest_Assert.sameAs(evalues[i],vvalues[i],status,approx)) {
						status.error = "expected " + utest_Assert.q(status.expectedValue) + " but it is " + utest_Assert.q(status.actualValue) + (status.path == "" ? "" : " for field " + status.path);
						return false;
					}
				}
			}
			return true;
		}
		if(utest_Assert.isIterable(expected,false)) {
			if(status.recursive || status.path == "") {
				var evalues = Lambda.array(expected);
				var vvalues = Lambda.array(value);
				if(evalues.length != vvalues.length) {
					status.error = "expected " + evalues.length + " values in Iterable but they are " + vvalues.length + (status.path == "" ? "" : " for field " + status.path);
					return false;
				}
				var path = status.path;
				var _g1 = 0;
				var _g2 = evalues.length;
				while(_g1 < _g2) {
					var i = _g1++;
					status.path = path == "" ? "iterable[" + i + "]" : path + "[" + i + "]";
					if(!utest_Assert.sameAs(evalues[i],vvalues[i],status,approx)) {
						return false;
					}
				}
			}
			return true;
		}
		if(status.recursive || status.path == "") {
			var fields = Type.getInstanceFields(js_Boot.getClass(expected));
			var path = status.path;
			var _g1 = 0;
			while(_g1 < fields.length) {
				var field = fields[_g1];
				++_g1;
				status.path = path == "" ? field : path + "." + field;
				var e = Reflect.field(expected,field);
				if(Reflect.isFunction(e)) {
					continue;
				}
				var v = Reflect.field(value,field);
				if(!utest_Assert.sameAs(e,v,status,approx)) {
					return false;
				}
			}
		}
		return true;
	case 7:
		var e = _g.e;
		var eexpected = e.__ename__;
		var e = Type.getEnum(value);
		var evalue = e.__ename__;
		if(eexpected != evalue) {
			status.error = "expected enumeration of " + utest_Assert.q(eexpected) + " but it is " + utest_Assert.q(evalue) + (status.path == "" ? "" : " for field " + status.path);
			return false;
		}
		if(status.recursive || status.path == "") {
			if(expected._hx_index != value._hx_index) {
				var e = expected;
				var tmp = "expected enum constructor " + utest_Assert.q($hxEnums[e.__enum__].__constructs__[e._hx_index]._hx_name) + " but it is ";
				var e = value;
				status.error = tmp + utest_Assert.q($hxEnums[e.__enum__].__constructs__[e._hx_index]._hx_name) + (status.path == "" ? "" : " for field " + status.path);
				return false;
			}
			var eparams = Type.enumParameters(expected);
			var vparams = Type.enumParameters(value);
			var path = status.path;
			var _g = 0;
			var _g1 = eparams.length;
			while(_g < _g1) {
				var i = _g++;
				status.path = path == "" ? "enum[" + i + "]" : path + "[" + i + "]";
				if(!utest_Assert.sameAs(eparams[i],vparams[i],status,approx)) {
					status.error = "expected enum param " + utest_Assert.q(expected) + " but it is " + utest_Assert.q(value) + (status.path == "" ? "" : " for field " + status.path) + " with " + status.error;
					return false;
				}
			}
		}
		return true;
	case 8:
		throw haxe_Exception.thrown("Unable to compare two unknown types");
	}
};
utest_Assert.q = function(v) {
	if(typeof(v) == "string") {
		return "\"" + StringTools.replace(v,"\"","\\\"") + "\"";
	} else {
		return Std.string(v);
	}
};
utest_Assert.same = function(expected,value,recursive,msg,approx,pos) {
	if(null == approx) {
		approx = 1e-5;
	}
	var status = { recursive : null == recursive ? true : recursive, path : "", error : null, expectedValue : expected, actualValue : value};
	if(utest_Assert.sameAs(expected,value,status,approx)) {
		return utest_Assert.pass(msg,pos);
	} else {
		return utest_Assert.fail(msg == null ? status.error : msg,pos);
	}
};
utest_Assert.raises = function(method,type,msgNotThrown,msgWrongType,pos) {
	var name = type != null ? type.__name__ : "Dynamic";
	try {
		method();
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
		var ex = haxe_Exception.caught(_g).unwrap();
		if(null == type) {
			return utest_Assert.pass(null,pos);
		} else {
			if(null == msgWrongType) {
				msgWrongType = "expected throw of type " + name + " but it is " + Std.string(ex);
			}
			return utest_Assert.isTrue(js_Boot.__instanceof(ex,type),msgWrongType,pos);
		}
	}
	if(null == msgNotThrown) {
		msgNotThrown = "exception of type " + name + " not raised";
	}
	return utest_Assert.fail(msgNotThrown,pos);
};
utest_Assert.allows = function(possibilities,value,msg,pos) {
	if(Lambda.has(possibilities,value)) {
		return utest_Assert.isTrue(true,msg,pos);
	} else {
		return utest_Assert.fail(msg == null ? "value " + utest_Assert.q(value) + " not found in the expected possibilities " + Std.string(possibilities) : msg,pos);
	}
};
utest_Assert.contains = function(match,values,msg,pos) {
	if(Lambda.has(values,match)) {
		return utest_Assert.isTrue(true,msg,pos);
	} else {
		return utest_Assert.fail(msg == null ? "values " + utest_Assert.q(values) + " do not contain " + Std.string(match) : msg,pos);
	}
};
utest_Assert.notContains = function(match,values,msg,pos) {
	if(!Lambda.has(values,match)) {
		return utest_Assert.isTrue(true,msg,pos);
	} else {
		return utest_Assert.fail(msg == null ? "values " + utest_Assert.q(values) + " do contain " + Std.string(match) : msg,pos);
	}
};
utest_Assert.stringContains = function(match,value,msg,pos) {
	if(value != null && value.indexOf(match) >= 0) {
		return utest_Assert.isTrue(true,msg,pos);
	} else {
		return utest_Assert.fail(msg == null ? "value " + utest_Assert.q(value) + " does not contain " + utest_Assert.q(match) : msg,pos);
	}
};
utest_Assert.stringSequence = function(sequence,value,msg,pos) {
	if(null == value) {
		return utest_Assert.fail(msg == null ? "null argument value" : msg,pos);
	}
	var p = 0;
	var _g = 0;
	while(_g < sequence.length) {
		var s = sequence[_g];
		++_g;
		var p2 = value.indexOf(s,p);
		if(p2 < 0) {
			if(msg == null) {
				msg = "expected '" + s + "' after ";
				if(p > 0) {
					var cut = HxOverrides.substr(value,0,p);
					if(cut.length > 30) {
						cut = "..." + HxOverrides.substr(cut,-27,null);
					}
					msg += " '" + cut + "'";
				} else {
					msg += " begin";
				}
			}
			return utest_Assert.fail(msg,pos);
		}
		p = p2 + s.length;
	}
	return utest_Assert.isTrue(true,msg,pos);
};
utest_Assert.pass = function(msg,pos) {
	if(msg == null) {
		msg = "pass expected";
	}
	return utest_Assert.isTrue(true,msg,pos);
};
utest_Assert.fail = function(msg,pos) {
	if(msg == null) {
		msg = "failure expected";
	}
	return utest_Assert.isTrue(false,msg,pos);
};
utest_Assert.warn = function(msg) {
	utest_Assert.results.add(utest_Assertation.Warning(msg));
};
utest_Assert.createAsync = function(f,timeout) {
	return function() {
	};
};
utest_Assert.createEvent = function(f,timeout) {
	return function(e) {
	};
};
utest_Assert.typeToString = function(t) {
	try {
		var _t = js_Boot.getClass(t);
		if(_t != null) {
			t = _t;
		}
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	try {
		return t.__name__;
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	try {
		var _t = Type.getEnum(t);
		if(_t != null) {
			t = _t;
		}
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	try {
		return t.__ename__;
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	try {
		return Std.string(Type.typeof(t));
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	try {
		return Std.string(t);
	} catch( _g ) {
		haxe_NativeStackTrace.lastError = _g;
	}
	return "<unable to retrieve type name>";
};
var utest_Assertation = $hxEnums["utest.Assertation"] = { __ename__:"utest.Assertation",__constructs__:null
	,Success: ($_=function(pos) { return {_hx_index:0,pos:pos,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="Success",$_.__params__ = ["pos"],$_)
	,Failure: ($_=function(msg,pos) { return {_hx_index:1,msg:msg,pos:pos,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="Failure",$_.__params__ = ["msg","pos"],$_)
	,Error: ($_=function(e,stack) { return {_hx_index:2,e:e,stack:stack,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="Error",$_.__params__ = ["e","stack"],$_)
	,SetupError: ($_=function(e,stack) { return {_hx_index:3,e:e,stack:stack,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="SetupError",$_.__params__ = ["e","stack"],$_)
	,TeardownError: ($_=function(e,stack) { return {_hx_index:4,e:e,stack:stack,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="TeardownError",$_.__params__ = ["e","stack"],$_)
	,TimeoutError: ($_=function(missedAsyncs,stack) { return {_hx_index:5,missedAsyncs:missedAsyncs,stack:stack,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="TimeoutError",$_.__params__ = ["missedAsyncs","stack"],$_)
	,AsyncError: ($_=function(e,stack) { return {_hx_index:6,e:e,stack:stack,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="AsyncError",$_.__params__ = ["e","stack"],$_)
	,Warning: ($_=function(msg) { return {_hx_index:7,msg:msg,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="Warning",$_.__params__ = ["msg"],$_)
	,Ignore: ($_=function(reason) { return {_hx_index:8,reason:reason,__enum__:"utest.Assertation",toString:$estr}; },$_._hx_name="Ignore",$_.__params__ = ["reason"],$_)
};
utest_Assertation.__constructs__ = [utest_Assertation.Success,utest_Assertation.Failure,utest_Assertation.Error,utest_Assertation.SetupError,utest_Assertation.TeardownError,utest_Assertation.TimeoutError,utest_Assertation.AsyncError,utest_Assertation.Warning,utest_Assertation.Ignore];
var utest_Async = function(timeoutMs) {
	if(timeoutMs == null) {
		timeoutMs = 250;
	}
	this.branches = [];
	this.callbacks = [];
	this.timedOut = false;
	this.resolved = false;
	this.timeoutMs = timeoutMs;
	this.startTime = HxOverrides.now() / 1000;
	this.timer = haxe_Timer.delay($bind(this,this.setTimedOutState),timeoutMs);
};
utest_Async.__name__ = "utest.Async";
utest_Async.getResolved = function() {
	if(utest_Async.resolvedInstance == null) {
		utest_Async.resolvedInstance = new utest_Async();
		utest_Async.resolvedInstance.done({ fileName : "utest/Async.hx", lineNumber : 30, className : "utest.Async", methodName : "getResolved"});
	}
	return utest_Async.resolvedInstance;
};
utest_Async.prototype = {
	resolved: null
	,timedOut: null
	,callbacks: null
	,timeoutMs: null
	,startTime: null
	,timer: null
	,branches: null
	,done: function(pos) {
		if(this.resolved) {
			if(this.timedOut) {
				throw haxe_Exception.thrown("Cannot done() at " + pos.fileName + ":" + pos.lineNumber + " because async is timed out.");
			} else {
				throw haxe_Exception.thrown("Cannot done() at " + pos.fileName + ":" + pos.lineNumber + " because async is done already.");
			}
		}
		this.resolved = true;
		this.timer.stop();
		var _g = 0;
		var _g1 = this.callbacks;
		while(_g < _g1.length) {
			var cb = _g1[_g];
			++_g;
			cb();
		}
	}
	,setTimeout: function(timeoutMs,pos) {
		if(this.resolved) {
			throw haxe_Exception.thrown("Cannot setTimeout(" + timeoutMs + ") at " + pos.fileName + ":" + pos.lineNumber + " because async is done.");
		}
		if(this.timedOut) {
			throw haxe_Exception.thrown("Cannot setTimeout(" + timeoutMs + ") at " + pos.fileName + ":" + pos.lineNumber + " because async is timed out.");
		}
		this.timer.stop();
		this.timeoutMs = timeoutMs;
		var delay = timeoutMs - Math.round(1000 * (HxOverrides.now() / 1000 - this.startTime));
		this.timer = haxe_Timer.delay($bind(this,this.setTimedOutState),delay);
	}
	,branch: function(fn,pos) {
		var branch = new utest_Async(this.timeoutMs);
		this.branches.push(branch);
		var _g = $bind(this,this.checkBranches);
		var pos1 = pos;
		branch.then(function() {
			_g(pos1);
		});
		if(fn != null) {
			fn(branch);
		}
		return branch;
	}
	,checkBranches: function(pos) {
		var _gthis = this;
		if(this.resolved) {
			return;
		}
		var _g = 0;
		var _g1 = this.branches;
		while(_g < _g1.length) {
			var branch = _g1[_g];
			++_g;
			if(!branch.resolved) {
				return;
			}
			if(branch.timedOut) {
				this.setTimedOutState();
				return;
			}
		}
		var branchCount = this.branches.length;
		haxe_Timer.delay(function() {
			if(branchCount == _gthis.branches.length) {
				_gthis.done(pos);
			}
		},5);
	}
	,then: function(cb) {
		if(this.resolved) {
			cb();
		} else {
			this.callbacks.push(cb);
		}
	}
	,setTimedOutState: function() {
		if(this.resolved) {
			return;
		}
		this.timedOut = true;
		this.done({ fileName : "utest/Async.hx", lineNumber : 115, className : "utest.Async", methodName : "setTimedOutState"});
	}
	,__class__: utest_Async
};
var utest__$Dispatcher_EventException = $hxEnums["utest._Dispatcher.EventException"] = { __ename__:"utest._Dispatcher.EventException",__constructs__:null
	,StopPropagation: {_hx_name:"StopPropagation",_hx_index:0,__enum__:"utest._Dispatcher.EventException",toString:$estr}
};
utest__$Dispatcher_EventException.__constructs__ = [utest__$Dispatcher_EventException.StopPropagation];
var utest_Dispatcher = function() {
	this.handlers = [];
};
utest_Dispatcher.__name__ = "utest.Dispatcher";
utest_Dispatcher.stop = function() {
	throw haxe_Exception.thrown(utest__$Dispatcher_EventException.StopPropagation);
};
utest_Dispatcher.prototype = {
	handlers: null
	,add: function(h) {
		this.handlers.push(h);
		return h;
	}
	,remove: function(h) {
		var _g = 0;
		var _g1 = this.handlers.length;
		while(_g < _g1) {
			var i = _g++;
			if(Reflect.compareMethods(this.handlers[i],h)) {
				return this.handlers.splice(i,1)[0];
			}
		}
		return null;
	}
	,clear: function() {
		this.handlers = [];
	}
	,dispatch: function(e) {
		try {
			var list = this.handlers.slice();
			var _g = 0;
			while(_g < list.length) {
				var l = list[_g];
				++_g;
				l(e);
			}
			return true;
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			if(js_Boot.__instanceof(haxe_Exception.caught(_g).unwrap(),utest__$Dispatcher_EventException)) {
				return false;
			} else {
				throw _g;
			}
		}
	}
	,has: function() {
		return this.handlers.length > 0;
	}
	,__class__: utest_Dispatcher
};
var utest_Notifier = function() {
	this.handlers = [];
};
utest_Notifier.__name__ = "utest.Notifier";
utest_Notifier.stop = function() {
	throw haxe_Exception.thrown(utest__$Dispatcher_EventException.StopPropagation);
};
utest_Notifier.prototype = {
	handlers: null
	,add: function(h) {
		this.handlers.push(h);
		return h;
	}
	,remove: function(h) {
		var _g = 0;
		var _g1 = this.handlers.length;
		while(_g < _g1) {
			var i = _g++;
			if(Reflect.compareMethods(this.handlers[i],h)) {
				return this.handlers.splice(i,1)[0];
			}
		}
		return null;
	}
	,clear: function() {
		this.handlers = [];
	}
	,dispatch: function() {
		try {
			var list = this.handlers.slice();
			var _g = 0;
			while(_g < list.length) {
				var l = list[_g];
				++_g;
				l();
			}
			return true;
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			if(js_Boot.__instanceof(haxe_Exception.caught(_g).unwrap(),utest__$Dispatcher_EventException)) {
				return false;
			} else {
				throw _g;
			}
		}
	}
	,has: function() {
		return this.handlers.length > 0;
	}
	,__class__: utest_Notifier
};
var utest_ITest = function() { };
utest_ITest.__name__ = "utest.ITest";
utest_ITest.__isInterface__ = true;
var utest_TestHandler = function(fixture) {
	this.wasBound = false;
	this.finished = false;
	if(fixture == null) {
		throw haxe_Exception.thrown("fixture argument is null");
	}
	this.fixture = fixture;
	this.results = new haxe_ds_List();
	this.asyncStack = new haxe_ds_List();
	this.onTested = new utest_Dispatcher();
	this.onTimeout = new utest_Dispatcher();
	this.onComplete = new utest_Dispatcher();
	this.onPrecheck = new utest_Dispatcher();
	if(fixture.ignoringInfo != null) {
		this.results.add(utest_Assertation.Ignore(fixture.ignoringInfo));
	}
};
utest_TestHandler.__name__ = "utest.TestHandler";
utest_TestHandler.exceptionStack = function(pops) {
	if(pops == null) {
		pops = 2;
	}
	var stack = haxe_CallStack.exceptionStack();
	while(pops-- > 0) stack.pop();
	return stack;
};
utest_TestHandler.prototype = {
	results: null
	,fixture: null
	,finished: null
	,asyncStack: null
	,onTested: null
	,onTimeout: null
	,onComplete: null
	,onPrecheck: null
	,precheck: null
	,wasBound: null
	,execute: function() {
		var _gthis = this;
		if(this.fixture.ignoringInfo != null) {
			this.executeFinally();
			return;
		}
		var isSync = true;
		var expectingAsync = true;
		var run = function() {
			if(isSync) {
				expectingAsync = false;
				return;
			}
			_gthis.executeFixtureMethod();
			_gthis.executeFinally();
		};
		try {
			this.executeMethod(this.fixture.setup);
			this.executeAsyncMethod(this.fixture.setupAsync,run);
			if(!expectingAsync) {
				this.executeFixtureMethod();
			}
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.SetupError(e,utest_TestHandler.exceptionStack()));
		}
		isSync = false;
		if(!expectingAsync) {
			this.executeFinally();
		}
	}
	,executeFixtureMethod: function() {
		try {
			this.executeMethod(this.fixture.method);
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.Error(e,utest_TestHandler.exceptionStack()));
		}
	}
	,executeFinally: function() {
		this.onPrecheck.dispatch(this);
		this.checkTested();
	}
	,checkTested: function() {
		if(this.expiration == null || this.asyncStack.length == 0) {
			this.tested();
		} else if(HxOverrides.now() / 1000 > this.expiration) {
			this.timeout();
		} else {
			haxe_Timer.delay($bind(this,this.checkTested),10);
		}
	}
	,expiration: null
	,setTimeout: function(timeout) {
		var newExpire = HxOverrides.now() / 1000 + timeout / 1000;
		this.expiration = this.expiration == null ? newExpire : newExpire > this.expiration ? newExpire : this.expiration;
	}
	,bindHandler: function() {
		if(this.wasBound) {
			return;
		}
		utest_Assert.results = this.results;
		utest_Assert.createAsync = $bind(this,this.addAsync);
		utest_Assert.createEvent = $bind(this,this.addEvent);
		this.wasBound = true;
	}
	,unbindHandler: function() {
		if(!this.wasBound) {
			return;
		}
		utest_Assert.results = null;
		utest_Assert.createAsync = function(f,t) {
			return function() {
			};
		};
		utest_Assert.createEvent = function(f,t) {
			return function(e) {
			};
		};
		this.wasBound = false;
	}
	,addAsync: function(f,timeout) {
		if(timeout == null) {
			timeout = 250;
		}
		if(null == f) {
			f = function() {
			};
		}
		this.asyncStack.add(f);
		var handler = this;
		this.setTimeout(timeout);
		return function() {
			if(!handler.asyncStack.remove(f)) {
				handler.results.add(utest_Assertation.AsyncError("async function already executed",[]));
				return;
			}
			try {
				handler.bindHandler();
				f();
			} catch( _g ) {
				haxe_NativeStackTrace.lastError = _g;
				var e = haxe_Exception.caught(_g).unwrap();
				handler.results.add(utest_Assertation.AsyncError(e,utest_TestHandler.exceptionStack(0)));
			}
		};
	}
	,addEvent: function(f,timeout) {
		if(timeout == null) {
			timeout = 250;
		}
		this.asyncStack.add(f);
		var handler = this;
		this.setTimeout(timeout);
		return function(e) {
			if(!handler.asyncStack.remove(f)) {
				handler.results.add(utest_Assertation.AsyncError("event already executed",[]));
				return;
			}
			try {
				handler.bindHandler();
				f(e);
			} catch( _g ) {
				haxe_NativeStackTrace.lastError = _g;
				var e = haxe_Exception.caught(_g).unwrap();
				handler.results.add(utest_Assertation.AsyncError(e,utest_TestHandler.exceptionStack(0)));
			}
		};
	}
	,executeMethod: function(name) {
		if(name == null) {
			return;
		}
		this.bindHandler();
		Reflect.field(this.fixture.target,name).apply(this.fixture.target,[]);
	}
	,executeAsyncMethod: function(name,done) {
		if(name == null) {
			done();
			return;
		}
		this.bindHandler();
		Reflect.field(this.fixture.target,name).apply(this.fixture.target,[done]);
	}
	,tested: function() {
		if(this.results.length == 0) {
			this.results.add(utest_Assertation.Warning("no assertions"));
		}
		this.onTested.dispatch(this);
		this.completed();
	}
	,timeout: function() {
		this.results.add(utest_Assertation.TimeoutError(this.asyncStack.length,[]));
		this.onTimeout.dispatch(this);
		this.completed();
	}
	,completed: function() {
		var _gthis = this;
		if(this.fixture.ignoringInfo != null) {
			this.completedFinally();
			return;
		}
		var isSync = true;
		var expectingAsync = true;
		var complete = function() {
			if(isSync) {
				expectingAsync = false;
				return;
			}
			_gthis.completedFinally();
		};
		try {
			this.executeMethod(this.fixture.teardown);
			this.executeAsyncMethod(this.fixture.teardownAsync,complete);
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.TeardownError(e,utest_TestHandler.exceptionStack(2)));
		}
		isSync = false;
		if(!expectingAsync) {
			this.completedFinally();
		}
	}
	,completedFinally: function() {
		this.finished = true;
		this.unbindHandler();
		this.onComplete.dispatch(this);
	}
	,__class__: utest_TestHandler
};
var utest_ITestHandler = function(fixture) {
	utest_TestHandler.call(this,fixture);
	if(!fixture.isITest) {
		throw haxe_Exception.thrown("Invalid fixture type for utest.ITestHandler");
	}
	this.testCase = js_Boot.__cast(fixture.target , utest_ITest);
	this.test = fixture.test;
	if(this.test == null) {
		throw haxe_Exception.thrown("Fixture is missing test data");
	}
};
utest_ITestHandler.__name__ = "utest.ITestHandler";
utest_ITestHandler.__super__ = utest_TestHandler;
utest_ITestHandler.prototype = $extend(utest_TestHandler.prototype,{
	testCase: null
	,test: null
	,setupAsync: null
	,testAsync: null
	,teardownAsync: null
	,execute: function() {
		if(this.fixture.ignoringInfo != null) {
			this.executeFinally();
			return;
		}
		this.bindHandler();
		this.runSetup();
	}
	,runSetup: function() {
		try {
			this.setupAsync = this.fixture.setupMethod();
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.SetupError(e,haxe_CallStack.exceptionStack()));
			this.completedFinally();
			return;
		}
		this.setupAsync.then($bind(this,this.checkSetup));
	}
	,checkSetup: function() {
		if(this.setupAsync.timedOut) {
			this.results.add(utest_Assertation.SetupError("Setup timeout",[]));
			this.completedFinally();
		} else {
			this.runTest();
		}
	}
	,runTest: function() {
		try {
			this.testAsync = this.test.execute();
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.Error(e,haxe_CallStack.exceptionStack()));
			this.runTeardown();
			return;
		}
		this.testAsync.then($bind(this,this.checkTest));
	}
	,checkTest: function() {
		this.onPrecheck.dispatch(this);
		if(this.testAsync.timedOut) {
			this.results.add(utest_Assertation.TimeoutError(1,[]));
			this.onTimeout.dispatch(this);
		} else if(this.testAsync.resolved) {
			if(this.results.length == 0) {
				this.results.add(utest_Assertation.Warning("no assertions"));
			}
			this.onTested.dispatch(this);
		} else {
			throw haxe_Exception.thrown("Unexpected test state");
		}
		this.runTeardown();
	}
	,runTeardown: function() {
		try {
			this.teardownAsync = this.fixture.teardownMethod();
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.results.add(utest_Assertation.TeardownError(e,haxe_CallStack.exceptionStack()));
			this.completedFinally();
			return;
		}
		this.teardownAsync.then($bind(this,this.checkTeardown));
	}
	,checkTeardown: function() {
		if(this.teardownAsync.timedOut) {
			this.results.add(utest_Assertation.TeardownError("Teardown timeout",[]));
		}
		this.completedFinally();
	}
	,bindHandler: function() {
		if(this.wasBound) {
			return;
		}
		utest_Assert.results = this.results;
		var msg = " is not allowed in tests extending utest.ITest. Add `async:utest.Async` argument to the test method instead.";
		utest_Assert.createAsync = function(f,t) {
			throw haxe_Exception.thrown("Assert.createAsync() " + msg);
		};
		utest_Assert.createEvent = function(f,t) {
			throw haxe_Exception.thrown("Assert.createEvent() " + msg);
		};
		this.wasBound = true;
	}
	,__class__: utest_ITestHandler
});
var utest_IgnoredFixture = {};
utest_IgnoredFixture.__properties__ = {get_ignoreReason:"get_ignoreReason",get_isIgnored:"get_isIgnored"};
utest_IgnoredFixture.NotIgnored = function() {
	var this1 = null;
	return this1;
};
utest_IgnoredFixture.Ignored = function(reason) {
	var this1 = reason != null ? reason : "";
	return this1;
};
utest_IgnoredFixture._new = function(reason) {
	var this1 = reason;
	return this1;
};
utest_IgnoredFixture.get_isIgnored = function(this1) {
	return this1 != null;
};
utest_IgnoredFixture.get_ignoreReason = function(this1) {
	return this1;
};
var utest_Runner = function() {
	this.executedFixtures = 0;
	this.pos = 0;
	this.complete = false;
	this.globalPattern = null;
	this.iTestFixtures = new haxe_ds_StringMap();
	this.fixtures = [];
	this.onProgress = new utest_Dispatcher();
	this.onStart = new utest_Dispatcher();
	this.onComplete = new utest_Dispatcher();
	this.onPrecheck = new utest_Dispatcher();
	this.onTestStart = new utest_Dispatcher();
	this.onTestComplete = new utest_Dispatcher();
	this.length = 0;
	var envPattern = null;
	if(envPattern != null) {
		this.globalPattern = new EReg(envPattern,"");
	}
};
utest_Runner.__name__ = "utest.Runner";
utest_Runner.prototype = {
	fixtures: null
	,iTestFixtures: null
	,onProgress: null
	,onStart: null
	,onComplete: null
	,onPrecheck: null
	,onTestStart: null
	,onTestComplete: null
	,length: null
	,globalPattern: null
	,complete: null
	,addCase: function(test,setup,teardown,prefix,pattern,setupAsync,teardownAsync) {
		if(teardownAsync == null) {
			teardownAsync = "teardownAsync";
		}
		if(setupAsync == null) {
			setupAsync = "setupAsync";
		}
		if(prefix == null) {
			prefix = "test";
		}
		if(teardown == null) {
			teardown = "teardown";
		}
		if(setup == null) {
			setup = "setup";
		}
		if(js_Boot.__implements(test,utest_ITest)) {
			this.addITest(test,pattern);
		} else {
			this.addCaseOld(test,setup,teardown,prefix,pattern,setupAsync,teardownAsync);
		}
	}
	,addITest: function(testCase,pattern) {
		var c = js_Boot.getClass(testCase);
		var className = c.__name__;
		if(Object.prototype.hasOwnProperty.call(this.iTestFixtures.h,className)) {
			throw haxe_Exception.thrown("Cannot add the same test twice.");
		}
		var fixtures = [];
		var init = testCase.__initializeUtest__();
		var _g = 0;
		var _g1 = init.tests;
		while(_g < _g1.length) {
			var test = _g1[_g];
			++_g;
			if(!this.isTestFixtureName(className,test.name,["test","spec"],pattern,this.globalPattern)) {
				continue;
			}
			var fixture = utest_TestFixture.ofData(testCase,test,init.accessories);
			this.addFixture(fixture);
			fixtures.push(fixture);
		}
		if(fixtures.length > 0) {
			var this1 = this.iTestFixtures;
			var value = { caseInstance : testCase, setupClass : utest_utils_AccessoriesUtils.getSetupClass(init.accessories), dependencies : init.dependencies, fixtures : fixtures, teardownClass : utest_utils_AccessoriesUtils.getTeardownClass(init.accessories)};
			this1.h[className] = value;
		}
	}
	,addCaseOld: function(test,setup,teardown,prefix,pattern,setupAsync,teardownAsync) {
		if(teardownAsync == null) {
			teardownAsync = "teardownAsync";
		}
		if(setupAsync == null) {
			setupAsync = "setupAsync";
		}
		if(prefix == null) {
			prefix = "test";
		}
		if(teardown == null) {
			teardown = "teardown";
		}
		if(setup == null) {
			setup = "setup";
		}
		if(!Reflect.isObject(test)) {
			throw haxe_Exception.thrown("can't add a null object as a test case");
		}
		if(!this.isMethod(test,setup)) {
			setup = null;
		}
		if(!this.isMethod(test,setupAsync)) {
			setupAsync = null;
		}
		if(!this.isMethod(test,teardown)) {
			teardown = null;
		}
		if(!this.isMethod(test,teardownAsync)) {
			teardownAsync = null;
		}
		var fields = Type.getInstanceFields(js_Boot.getClass(test));
		var c = js_Boot.getClass(test);
		var className = c.__name__;
		var _g = 0;
		while(_g < fields.length) {
			var field = fields[_g];
			++_g;
			if(!this.isMethod(test,field)) {
				continue;
			}
			if(!this.isTestFixtureName(className,field,[prefix],pattern,this.globalPattern)) {
				continue;
			}
			this.addFixture(new utest_TestFixture(test,field,setup,teardown,setupAsync,teardownAsync));
		}
	}
	,isTestFixtureName: function(caseName,testName,prefixes,pattern,globalPattern) {
		if(pattern == null && globalPattern == null) {
			var _g = 0;
			while(_g < prefixes.length) {
				var prefix = prefixes[_g];
				++_g;
				if(StringTools.startsWith(testName,prefix)) {
					return true;
				}
			}
			return false;
		}
		if(pattern == null) {
			pattern = globalPattern;
		}
		return pattern.match("" + caseName + "." + testName);
	}
	,addFixture: function(fixture) {
		this.fixtures.push(fixture);
		this.length++;
	}
	,getFixture: function(index) {
		return this.fixtures[index];
	}
	,isMethod: function(test,name) {
		try {
			return Reflect.isFunction(Reflect.field(test,name));
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			return false;
		}
	}
	,run: function() {
		this.onStart.dispatch(this);
		var iTestRunner = new utest__$Runner_ITestRunner(this);
		iTestRunner.run();
		this.waitForCompletion();
	}
	,waitForCompletion: function() {
		if(!this.complete) {
			haxe_Timer.delay($bind(this,this.waitForCompletion),100);
		}
	}
	,pos: null
	,executedFixtures: null
	,runNext: function(finishedHandler) {
		var currentCase = null;
		var _g = this.pos;
		var _g1 = this.fixtures.length;
		while(_g < _g1) {
			var i = _g++;
			var fixture = this.fixtures[this.pos++];
			if(fixture.isITest) {
				continue;
			}
			if(currentCase != fixture.target) {
				currentCase = fixture.target;
				var c = js_Boot.getClass(currentCase);
				utest_utils_Print.startCase(c.__name__);
			}
			var handler = this.runFixture(fixture);
			if(!handler.finished) {
				handler.onComplete.add($bind(this,this.runNext));
				return;
			}
		}
		this.complete = true;
		this.onComplete.dispatch(this);
	}
	,runFixture: function(fixture) {
		var handler = fixture.isITest ? new utest_ITestHandler(fixture) : new utest_TestHandler(fixture);
		handler.onComplete.add($bind(this,this.testComplete));
		handler.onPrecheck.add(($_=this.onPrecheck,$bind($_,$_.dispatch)));
		utest_utils_Print.startTest(fixture.method);
		this.onTestStart.dispatch(handler);
		handler.execute();
		return handler;
	}
	,testComplete: function(h) {
		++this.executedFixtures;
		this.onTestComplete.dispatch(h);
		this.onProgress.dispatch({ result : utest_TestResult.ofHandler(h), done : this.executedFixtures, totals : this.length});
	}
	,__class__: utest_Runner
};
var utest__$Runner_ITestRunner = function(runner) {
	this.failedCases = [];
	this.failedTestsInCurrentCase = [];
	var _gthis = this;
	this.runner = runner;
	runner.onTestComplete.add(function(handler) {
		var _g_head = handler.results.h;
		while(_g_head != null) {
			var val = _g_head.item;
			_g_head = _g_head.next;
			var result = val;
			if(result._hx_index == 0) {
				var _g = result.pos;
			} else {
				_gthis.failedTestsInCurrentCase.push(handler.fixture.method);
				var c = js_Boot.getClass(handler.fixture.target);
				_gthis.failedCases.push(c.__name__);
			}
		}
	});
};
utest__$Runner_ITestRunner.__name__ = "utest._Runner.ITestRunner";
utest__$Runner_ITestRunner.prototype = {
	runner: null
	,cases: null
	,currentCaseName: null
	,currentCase: null
	,currentCaseFixtures: null
	,teardownClass: null
	,setupAsync: null
	,teardownAsync: null
	,failedTestsInCurrentCase: null
	,failedCases: null
	,run: function() {
		this.cases = this.orderClassesByDependencies();
		this.runCases();
	}
	,orderClassesByDependencies: function() {
		var _gthis = this;
		var result = [];
		var error = function(testCase,msg) {
			_gthis.runner.onProgress.dispatch({ totals : _gthis.runner.length, result : utest_TestResult.ofFailedSetupClass(testCase,utest_Assertation.SetupError(msg,[])), done : _gthis.runner.executedFixtures});
		};
		var added_h = Object.create(null);
		var addClass = null;
		addClass = function(cls,stack) {
			if(Object.prototype.hasOwnProperty.call(added_h,cls)) {
				return;
			}
			var data = _gthis.runner.iTestFixtures.h[cls];
			if(stack.indexOf(cls) >= 0) {
				error(data.caseInstance,"Circular dependencies among test classes detected: " + stack.join(" -> "));
				return;
			}
			stack.push(cls);
			var dependencies = data.dependencies;
			var _g = 0;
			while(_g < dependencies.length) {
				var dependency = dependencies[_g];
				++_g;
				if(Object.prototype.hasOwnProperty.call(_gthis.runner.iTestFixtures.h,dependency)) {
					addClass(dependency,stack);
				} else {
					error(data.caseInstance,"This class depends on " + dependency + ", but it cannot be found. Was it added to test runner?");
					return;
				}
			}
			result.push(cls);
			added_h[cls] = true;
		};
		var h = this.runner.iTestFixtures.h;
		var cls_h = h;
		var cls_keys = Object.keys(h);
		var cls_length = cls_keys.length;
		var cls_current = 0;
		while(cls_current < cls_length) {
			var cls = cls_keys[cls_current++];
			addClass(cls,[]);
		}
		return new haxe_iterators_ArrayIterator(result);
	}
	,failedDependencies: function(data) {
		var _g = 0;
		var _g1 = data.dependencies;
		while(_g < _g1.length) {
			var dependency = _g1[_g];
			++_g;
			if(this.failedCases.indexOf(dependency) >= 0) {
				return true;
			}
		}
		return false;
	}
	,runCases: function() {
		while(this.cases.hasNext()) {
			this.currentCaseName = this.cases.next();
			var data = this.runner.iTestFixtures.h[this.currentCaseName];
			this.currentCase = data.caseInstance;
			this.failedTestsInCurrentCase = [];
			if(this.failedDependencies(data)) {
				this.failedCases.push(this.currentCaseName);
				continue;
			}
			utest_utils_Print.startCase(this.currentCaseName);
			this.currentCaseFixtures = data.fixtures;
			this.teardownClass = data.teardownClass;
			try {
				this.setupAsync = data.setupClass();
			} catch( _g ) {
				haxe_NativeStackTrace.lastError = _g;
				var e = haxe_Exception.caught(_g).unwrap();
				this.setupFailed(utest_Assertation.SetupError("setupClass failed: " + Std.string(e),haxe_CallStack.exceptionStack()));
				return;
			}
			if(this.setupAsync.resolved) {
				if(!this.runFixtures()) {
					return;
				}
			} else {
				this.setupAsync.then($bind(this,this.checkSetup));
				return;
			}
		}
		this.runner.runNext();
	}
	,checkSetup: function() {
		if(this.setupAsync.timedOut) {
			this.setupFailed(utest_Assertation.SetupError("setupClass timeout",[]));
		} else {
			this.runFixtures();
		}
	}
	,setupFailed: function(assertation) {
		this.runner.executedFixtures += this.currentCaseFixtures.length;
		this.runner.onProgress.dispatch({ totals : this.runner.length, result : utest_TestResult.ofFailedSetupClass(this.currentCase,assertation), done : this.runner.executedFixtures});
		this.runCases();
	}
	,runFixtures: function(finishedHandler) {
		while(this.currentCaseFixtures.length > 0) {
			var fixture = this.currentCaseFixtures.shift();
			var _g = 0;
			var _g1 = fixture.test.dependencies;
			while(_g < _g1.length) {
				var dep = _g1[_g];
				++_g;
				if(this.failedTestsInCurrentCase.indexOf(dep) >= 0) {
					fixture.ignoringInfo = utest_IgnoredFixture.Ignored("Failed dependencies");
					break;
				}
			}
			var handler = this.runner.runFixture(fixture);
			if(!handler.finished) {
				handler.onComplete.add($bind(this,this.runFixtures));
				return false;
			}
		}
		try {
			this.teardownAsync = this.teardownClass();
		} catch( _g ) {
			haxe_NativeStackTrace.lastError = _g;
			var e = haxe_Exception.caught(_g).unwrap();
			this.teardownFailed(utest_Assertation.TeardownError("teardownClass failed: " + Std.string(e),haxe_CallStack.exceptionStack()));
			return true;
		}
		if(this.teardownAsync.resolved && finishedHandler == null) {
			return true;
		}
		this.teardownAsync.then($bind(this,this.checkTeardown));
		return false;
	}
	,checkTeardown: function() {
		if(this.teardownAsync.timedOut) {
			this.teardownFailed(utest_Assertation.TeardownError("teardownClass timeout",[]));
		}
		this.runCases();
	}
	,teardownFailed: function(assertation) {
		this.runner.onProgress.dispatch({ totals : this.runner.length, result : utest_TestResult.ofFailedTeardownClass(this.currentCase,assertation), done : this.runner.executedFixtures});
	}
	,__class__: utest__$Runner_ITestRunner
};
var utest_AccessoryName = function() { };
utest_AccessoryName.__name__ = "utest.AccessoryName";
var utest_TestFixture = function(target,method,setup,teardown,setupAsync,teardownAsync) {
	this.isITest = false;
	this.target = target;
	this.method = method;
	this.setup = setup;
	this.setupAsync = setupAsync;
	this.teardown = teardown;
	this.teardownAsync = teardownAsync;
	this.ignoringInfo = this.getIgnored();
};
utest_TestFixture.__name__ = "utest.TestFixture";
utest_TestFixture.ofData = function(target,test,accessories) {
	var fixture = new utest_TestFixture(target,test.name);
	fixture.isITest = true;
	fixture.test = test;
	fixture.setupMethod = utest_utils_AccessoriesUtils.getSetup(accessories);
	fixture.teardownMethod = utest_utils_AccessoriesUtils.getTeardown(accessories);
	return fixture;
};
utest_TestFixture.prototype = {
	target: null
	,method: null
	,setup: null
	,setupAsync: null
	,teardown: null
	,teardownAsync: null
	,ignoringInfo: null
	,isITest: null
	,test: null
	,setupMethod: null
	,teardownMethod: null
	,checkMethod: function(name,arg) {
		var field = Reflect.field(this.target,name);
		if(field == null) {
			throw haxe_Exception.thrown(arg + " function " + name + " is not a field of target");
		}
		if(!Reflect.isFunction(field)) {
			throw haxe_Exception.thrown(arg + " function " + name + " is not a function");
		}
	}
	,getIgnored: function() {
		var metas = haxe_rtti_Meta.getFields(js_Boot.getClass(this.target));
		var metasForTestMetas = Reflect.getProperty(metas,this.method);
		if(metasForTestMetas == null || !Object.prototype.hasOwnProperty.call(metasForTestMetas,"Ignored")) {
			return utest_IgnoredFixture.NotIgnored();
		}
		var ignoredArgs = Reflect.getProperty(metasForTestMetas,"Ignored");
		if(ignoredArgs == null || ignoredArgs.length == 0 || ignoredArgs[0] == null) {
			return utest_IgnoredFixture.Ignored();
		}
		var ignoredReason = Std.string(ignoredArgs[0]);
		return utest_IgnoredFixture.Ignored(ignoredReason);
	}
	,__class__: utest_TestFixture
};
var utest_TestResult = function() {
};
utest_TestResult.__name__ = "utest.TestResult";
utest_TestResult.ofHandler = function(handler) {
	var r = new utest_TestResult();
	var c = js_Boot.getClass(handler.fixture.target);
	var path = c.__name__.split(".");
	r.cls = path.pop();
	r.pack = path.join(".");
	r.method = handler.fixture.method;
	r.setup = handler.fixture.setup;
	r.setupAsync = handler.fixture.setupAsync;
	r.teardown = handler.fixture.teardown;
	r.teardownAsync = handler.fixture.teardownAsync;
	r.assertations = handler.results;
	return r;
};
utest_TestResult.ofFailedSetupClass = function(testCase,assertation) {
	var r = new utest_TestResult();
	var c = js_Boot.getClass(testCase);
	var path = c.__name__.split(".");
	r.cls = path.pop();
	r.pack = path.join(".");
	r.method = "setup";
	r.assertations = new haxe_ds_List();
	r.assertations.add(assertation);
	return r;
};
utest_TestResult.ofFailedTeardownClass = function(testCase,assertation) {
	var r = new utest_TestResult();
	var c = js_Boot.getClass(testCase);
	var path = c.__name__.split(".");
	r.cls = path.pop();
	r.pack = path.join(".");
	r.method = "setup";
	r.assertations = new haxe_ds_List();
	r.assertations.add(assertation);
	return r;
};
utest_TestResult.prototype = {
	pack: null
	,cls: null
	,method: null
	,setup: null
	,setupAsync: null
	,teardown: null
	,teardownAsync: null
	,assertations: null
	,__class__: utest_TestResult
};
var utest_ui_Report = function() { };
utest_ui_Report.__name__ = "utest.ui.Report";
utest_ui_Report.create = function(runner,displaySuccessResults,headerDisplayMode) {
	var report;
	if(typeof window != 'undefined') {
		report = new utest_ui_text_HtmlReport(runner,null,true);
	} else {
		report = new utest_ui_text_PrintReport(runner);
	}
	if(null == displaySuccessResults) {
		report.displaySuccessResults = utest_ui_common_SuccessResultsDisplayMode.ShowSuccessResultsWithNoErrors;
	} else {
		report.displaySuccessResults = displaySuccessResults;
	}
	if(null == headerDisplayMode) {
		report.displayHeader = utest_ui_common_HeaderDisplayMode.ShowHeaderWithResults;
	} else {
		report.displayHeader = headerDisplayMode;
	}
	return report;
};
var utest_ui_common_ClassResult = function(className,setupName,teardownName) {
	this.fixtures = new haxe_ds_StringMap();
	this.className = className;
	this.setupName = setupName;
	this.hasSetup = setupName != null;
	this.teardownName = teardownName;
	this.hasTeardown = teardownName != null;
	this.methods = 0;
	this.stats = new utest_ui_common_ResultStats();
};
utest_ui_common_ClassResult.__name__ = "utest.ui.common.ClassResult";
utest_ui_common_ClassResult.prototype = {
	fixtures: null
	,className: null
	,setupName: null
	,teardownName: null
	,hasSetup: null
	,hasTeardown: null
	,methods: null
	,stats: null
	,add: function(result) {
		if(Object.prototype.hasOwnProperty.call(this.fixtures.h,result.methodName)) {
			throw haxe_Exception.thrown("invalid duplicated fixture: " + this.className + "." + result.methodName);
		}
		this.stats.wire(result.stats);
		this.methods++;
		this.fixtures.h[result.methodName] = result;
	}
	,get: function(method) {
		return this.fixtures.h[method];
	}
	,exists: function(method) {
		return Object.prototype.hasOwnProperty.call(this.fixtures.h,method);
	}
	,methodNames: function(errorsHavePriority) {
		if(errorsHavePriority == null) {
			errorsHavePriority = true;
		}
		var names = [];
		var h = this.fixtures.h;
		var name_h = h;
		var name_keys = Object.keys(h);
		var name_length = name_keys.length;
		var name_current = 0;
		while(name_current < name_length) {
			var name = name_keys[name_current++];
			names.push(name);
		}
		if(errorsHavePriority) {
			var me = this;
			names.sort(function(a,b) {
				var as = me.get(a).stats;
				var bs = me.get(b).stats;
				if(as.hasErrors) {
					if(!bs.hasErrors) {
						return -1;
					} else if(as.errors == bs.errors) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.errors,bs.errors);
					}
				} else if(bs.hasErrors) {
					return 1;
				} else if(as.hasFailures) {
					if(!bs.hasFailures) {
						return -1;
					} else if(as.failures == bs.failures) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.failures,bs.failures);
					}
				} else if(bs.hasFailures) {
					return 1;
				} else if(as.hasWarnings) {
					if(!bs.hasWarnings) {
						return -1;
					} else if(as.warnings == bs.warnings) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.warnings,bs.warnings);
					}
				} else if(bs.hasWarnings) {
					return 1;
				} else {
					return Reflect.compare(a,b);
				}
			});
		} else {
			names.sort(function(a,b) {
				return Reflect.compare(a,b);
			});
		}
		return names;
	}
	,__class__: utest_ui_common_ClassResult
};
var utest_ui_common_FixtureResult = function(methodName) {
	this.methodName = methodName;
	this.list = new haxe_ds_List();
	this.hasTestError = false;
	this.hasSetupError = false;
	this.hasTeardownError = false;
	this.hasTimeoutError = false;
	this.hasAsyncError = false;
	this.stats = new utest_ui_common_ResultStats();
};
utest_ui_common_FixtureResult.__name__ = "utest.ui.common.FixtureResult";
utest_ui_common_FixtureResult.prototype = {
	methodName: null
	,hasTestError: null
	,hasSetupError: null
	,hasTeardownError: null
	,hasTimeoutError: null
	,hasAsyncError: null
	,stats: null
	,list: null
	,iterator: function() {
		return new haxe_ds__$List_ListIterator(this.list.h);
	}
	,add: function(assertation) {
		this.list.add(assertation);
		switch(assertation._hx_index) {
		case 0:
			var _g = assertation.pos;
			this.stats.addSuccesses(1);
			break;
		case 1:
			var _g = assertation.msg;
			var _g = assertation.pos;
			this.stats.addFailures(1);
			break;
		case 2:
			var _g = assertation.e;
			var _g = assertation.stack;
			this.stats.addErrors(1);
			break;
		case 3:
			var _g = assertation.e;
			var _g = assertation.stack;
			this.stats.addErrors(1);
			this.hasSetupError = true;
			break;
		case 4:
			var _g = assertation.e;
			var _g = assertation.stack;
			this.stats.addErrors(1);
			this.hasTeardownError = true;
			break;
		case 5:
			var _g = assertation.missedAsyncs;
			var _g = assertation.stack;
			this.stats.addErrors(1);
			this.hasTimeoutError = true;
			break;
		case 6:
			var _g = assertation.e;
			var _g = assertation.stack;
			this.stats.addErrors(1);
			this.hasAsyncError = true;
			break;
		case 7:
			var _g = assertation.msg;
			this.stats.addWarnings(1);
			break;
		case 8:
			var _g = assertation.reason;
			this.stats.addIgnores(1);
			break;
		}
	}
	,__class__: utest_ui_common_FixtureResult
};
var utest_ui_common_HeaderDisplayMode = $hxEnums["utest.ui.common.HeaderDisplayMode"] = { __ename__:"utest.ui.common.HeaderDisplayMode",__constructs__:null
	,AlwaysShowHeader: {_hx_name:"AlwaysShowHeader",_hx_index:0,__enum__:"utest.ui.common.HeaderDisplayMode",toString:$estr}
	,NeverShowHeader: {_hx_name:"NeverShowHeader",_hx_index:1,__enum__:"utest.ui.common.HeaderDisplayMode",toString:$estr}
	,ShowHeaderWithResults: {_hx_name:"ShowHeaderWithResults",_hx_index:2,__enum__:"utest.ui.common.HeaderDisplayMode",toString:$estr}
};
utest_ui_common_HeaderDisplayMode.__constructs__ = [utest_ui_common_HeaderDisplayMode.AlwaysShowHeader,utest_ui_common_HeaderDisplayMode.NeverShowHeader,utest_ui_common_HeaderDisplayMode.ShowHeaderWithResults];
var utest_ui_common_SuccessResultsDisplayMode = $hxEnums["utest.ui.common.SuccessResultsDisplayMode"] = { __ename__:"utest.ui.common.SuccessResultsDisplayMode",__constructs__:null
	,AlwaysShowSuccessResults: {_hx_name:"AlwaysShowSuccessResults",_hx_index:0,__enum__:"utest.ui.common.SuccessResultsDisplayMode",toString:$estr}
	,NeverShowSuccessResults: {_hx_name:"NeverShowSuccessResults",_hx_index:1,__enum__:"utest.ui.common.SuccessResultsDisplayMode",toString:$estr}
	,ShowSuccessResultsWithNoErrors: {_hx_name:"ShowSuccessResultsWithNoErrors",_hx_index:2,__enum__:"utest.ui.common.SuccessResultsDisplayMode",toString:$estr}
};
utest_ui_common_SuccessResultsDisplayMode.__constructs__ = [utest_ui_common_SuccessResultsDisplayMode.AlwaysShowSuccessResults,utest_ui_common_SuccessResultsDisplayMode.NeverShowSuccessResults,utest_ui_common_SuccessResultsDisplayMode.ShowSuccessResultsWithNoErrors];
var utest_ui_common_IReport = function() { };
utest_ui_common_IReport.__name__ = "utest.ui.common.IReport";
utest_ui_common_IReport.__isInterface__ = true;
utest_ui_common_IReport.prototype = {
	displaySuccessResults: null
	,displayHeader: null
	,setHandler: null
	,__class__: utest_ui_common_IReport
};
var utest_ui_common_PackageResult = function(packageName) {
	this.isEmpty = true;
	this.packageName = packageName;
	this.classes = new haxe_ds_StringMap();
	this.packages = new haxe_ds_StringMap();
	this.stats = new utest_ui_common_ResultStats();
};
utest_ui_common_PackageResult.__name__ = "utest.ui.common.PackageResult";
utest_ui_common_PackageResult.prototype = {
	packageName: null
	,isEmpty: null
	,classes: null
	,packages: null
	,stats: null
	,addResult: function(result,flattenPackage) {
		this.isEmpty = false;
		var pack = this.getOrCreatePackage(result.pack,flattenPackage,this);
		var cls = this.getOrCreateClass(pack,result.cls,result.setup,result.teardown);
		var fix = this.createFixture(result.method,result.assertations);
		cls.add(fix);
	}
	,addClass: function(result) {
		this.isEmpty = false;
		this.classes.h[result.className] = result;
		this.stats.wire(result.stats);
	}
	,addPackage: function(result) {
		this.isEmpty = false;
		this.packages.h[result.packageName] = result;
		this.stats.wire(result.stats);
	}
	,existsPackage: function(name) {
		return Object.prototype.hasOwnProperty.call(this.packages.h,name);
	}
	,existsClass: function(name) {
		return Object.prototype.hasOwnProperty.call(this.classes.h,name);
	}
	,getPackage: function(name) {
		if(this.packageName == null && name == "") {
			return this;
		}
		return this.packages.h[name];
	}
	,getClass: function(name) {
		return this.classes.h[name];
	}
	,classNames: function(errorsHavePriority) {
		if(errorsHavePriority == null) {
			errorsHavePriority = true;
		}
		var names = [];
		var h = this.classes.h;
		var name_h = h;
		var name_keys = Object.keys(h);
		var name_length = name_keys.length;
		var name_current = 0;
		while(name_current < name_length) {
			var name = name_keys[name_current++];
			names.push(name);
		}
		if(errorsHavePriority) {
			var me = this;
			names.sort(function(a,b) {
				var as = me.getClass(a).stats;
				var bs = me.getClass(b).stats;
				if(as.hasErrors) {
					if(!bs.hasErrors) {
						return -1;
					} else if(as.errors == bs.errors) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.errors,bs.errors);
					}
				} else if(bs.hasErrors) {
					return 1;
				} else if(as.hasFailures) {
					if(!bs.hasFailures) {
						return -1;
					} else if(as.failures == bs.failures) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.failures,bs.failures);
					}
				} else if(bs.hasFailures) {
					return 1;
				} else if(as.hasWarnings) {
					if(!bs.hasWarnings) {
						return -1;
					} else if(as.warnings == bs.warnings) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.warnings,bs.warnings);
					}
				} else if(bs.hasWarnings) {
					return 1;
				} else {
					return Reflect.compare(a,b);
				}
			});
		} else {
			names.sort(function(a,b) {
				return Reflect.compare(a,b);
			});
		}
		return names;
	}
	,packageNames: function(errorsHavePriority) {
		if(errorsHavePriority == null) {
			errorsHavePriority = true;
		}
		var names = [];
		if(this.packageName == null) {
			names.push("");
		}
		var h = this.packages.h;
		var name_h = h;
		var name_keys = Object.keys(h);
		var name_length = name_keys.length;
		var name_current = 0;
		while(name_current < name_length) {
			var name = name_keys[name_current++];
			names.push(name);
		}
		if(errorsHavePriority) {
			var me = this;
			names.sort(function(a,b) {
				var as = me.getPackage(a).stats;
				var bs = me.getPackage(b).stats;
				if(as.hasErrors) {
					if(!bs.hasErrors) {
						return -1;
					} else if(as.errors == bs.errors) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.errors,bs.errors);
					}
				} else if(bs.hasErrors) {
					return 1;
				} else if(as.hasFailures) {
					if(!bs.hasFailures) {
						return -1;
					} else if(as.failures == bs.failures) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.failures,bs.failures);
					}
				} else if(bs.hasFailures) {
					return 1;
				} else if(as.hasWarnings) {
					if(!bs.hasWarnings) {
						return -1;
					} else if(as.warnings == bs.warnings) {
						return Reflect.compare(a,b);
					} else {
						return Reflect.compare(as.warnings,bs.warnings);
					}
				} else if(bs.hasWarnings) {
					return 1;
				} else {
					return Reflect.compare(a,b);
				}
			});
		} else {
			names.sort(function(a,b) {
				return Reflect.compare(a,b);
			});
		}
		return names;
	}
	,createFixture: function(method,assertations) {
		var f = new utest_ui_common_FixtureResult(method);
		var assertation = $getIterator(assertations);
		while(assertation.hasNext()) {
			var assertation1 = assertation.next();
			f.add(assertation1);
		}
		return f;
	}
	,getOrCreateClass: function(pack,cls,setup,teardown) {
		if(pack.existsClass(cls)) {
			return pack.getClass(cls);
		}
		var c = new utest_ui_common_ClassResult(cls,setup,teardown);
		pack.addClass(c);
		return c;
	}
	,getOrCreatePackage: function(pack,flat,ref) {
		if(pack == null || pack == "") {
			return ref;
		}
		if(flat) {
			if(ref.existsPackage(pack)) {
				return ref.getPackage(pack);
			}
			var p = new utest_ui_common_PackageResult(pack);
			ref.addPackage(p);
			return p;
		} else {
			var parts = pack.split(".");
			var _g = 0;
			while(_g < parts.length) {
				var part = parts[_g];
				++_g;
				ref = this.getOrCreatePackage(part,true,ref);
			}
			return ref;
		}
	}
	,__class__: utest_ui_common_PackageResult
};
var utest_ui_common_ReportTools = function() { };
utest_ui_common_ReportTools.__name__ = "utest.ui.common.ReportTools";
utest_ui_common_ReportTools.hasHeader = function(report,stats) {
	switch(report.displayHeader._hx_index) {
	case 0:
		return true;
	case 1:
		return false;
	case 2:
		if(!stats.isOk) {
			return true;
		}
		switch(report.displaySuccessResults._hx_index) {
		case 0:case 2:
			return true;
		case 1:
			return false;
		}
		break;
	}
};
utest_ui_common_ReportTools.skipResult = function(report,stats,isOk) {
	if(!stats.isOk) {
		return false;
	}
	switch(report.displaySuccessResults._hx_index) {
	case 0:
		return false;
	case 1:
		return true;
	case 2:
		return !isOk;
	}
};
utest_ui_common_ReportTools.hasOutput = function(report,stats) {
	if(!stats.isOk) {
		return true;
	}
	return utest_ui_common_ReportTools.hasHeader(report,stats);
};
var utest_ui_common_ResultAggregator = function(runner,flattenPackage) {
	if(flattenPackage == null) {
		flattenPackage = false;
	}
	if(runner == null) {
		throw haxe_Exception.thrown("runner argument is null");
	}
	this.flattenPackage = flattenPackage;
	this.runner = runner;
	runner.onStart.add($bind(this,this.start));
	runner.onProgress.add($bind(this,this.progress));
	runner.onComplete.add($bind(this,this.complete));
	this.onStart = new utest_Notifier();
	this.onComplete = new utest_Dispatcher();
	this.onProgress = new utest_Dispatcher();
};
utest_ui_common_ResultAggregator.__name__ = "utest.ui.common.ResultAggregator";
utest_ui_common_ResultAggregator.prototype = {
	runner: null
	,flattenPackage: null
	,root: null
	,onStart: null
	,onComplete: null
	,onProgress: null
	,start: function(runner) {
		this.checkNonITest();
		this.root = new utest_ui_common_PackageResult(null);
		this.onStart.dispatch();
	}
	,checkNonITest: function() {
		var first = null;
		var total = 0;
		var _g = 0;
		var _g1 = this.runner.length;
		while(_g < _g1) {
			var i = _g++;
			var fixture = this.runner.getFixture(i);
			if(!fixture.isITest) {
				++total;
				if(first == null) {
					var c = js_Boot.getClass(fixture.target);
					first = c.__name__;
				}
			}
		}
		if(total > 0) {
			var baseMsg = "implement utest.ITest. Non-ITest tests are deprecated. Implement utest.ITest or extend utest.Test.";
			var msg;
			switch(total) {
			case 1:
				msg = "" + first + " doesn't " + baseMsg;
				break;
			case 2:
				msg = "" + first + " and 1 other don't " + baseMsg;
				break;
			default:
				msg = "" + first + " and " + total + " others don't " + baseMsg;
			}
			haxe_Log.trace(msg,{ fileName : "utest/ui/common/ResultAggregator.hx", lineNumber : 54, className : "utest.ui.common.ResultAggregator", methodName : "checkNonITest"});
		}
	}
	,getOrCreatePackage: function(pack,flat,ref) {
		if(ref == null) {
			ref = this.root;
		}
		if(pack == null || pack == "") {
			return ref;
		}
		if(flat) {
			if(ref.existsPackage(pack)) {
				return ref.getPackage(pack);
			}
			var p = new utest_ui_common_PackageResult(pack);
			ref.addPackage(p);
			return p;
		} else {
			var parts = pack.split(".");
			var _g = 0;
			while(_g < parts.length) {
				var part = parts[_g];
				++_g;
				ref = this.getOrCreatePackage(part,true,ref);
			}
			return ref;
		}
	}
	,getOrCreateClass: function(pack,cls,setup,teardown) {
		if(pack.existsClass(cls)) {
			return pack.getClass(cls);
		}
		var c = new utest_ui_common_ClassResult(cls,setup,teardown);
		pack.addClass(c);
		return c;
	}
	,createFixture: function(result) {
		var f = new utest_ui_common_FixtureResult(result.method);
		var _g_head = result.assertations.h;
		while(_g_head != null) {
			var val = _g_head.item;
			_g_head = _g_head.next;
			var assertation = val;
			f.add(assertation);
		}
		return f;
	}
	,progress: function(e) {
		this.root.addResult(e.result,this.flattenPackage);
		this.onProgress.dispatch(e);
	}
	,complete: function(runner) {
		if(this.root.isEmpty) {
			this.root.addResult(this.createNoTestsResult(),false);
		}
		this.onComplete.dispatch(this.root);
	}
	,createNoTestsResult: function() {
		var result = new utest_TestResult();
		result.pack = "";
		result.cls = "";
		result.method = "";
		result.assertations = new haxe_ds_List();
		var pos = { fileName : "", lineNumber : 1, className : "utest.Runner", methodName : "run"};
		result.assertations.add(utest_Assertation.Failure("No tests executed.",pos));
		return result;
	}
	,__class__: utest_ui_common_ResultAggregator
};
var utest_ui_common_ResultStats = function() {
	this.assertations = 0;
	this.successes = 0;
	this.failures = 0;
	this.errors = 0;
	this.warnings = 0;
	this.ignores = 0;
	this.isOk = true;
	this.hasFailures = false;
	this.hasErrors = false;
	this.hasWarnings = false;
	this.hasIgnores = false;
	this.onAddSuccesses = new utest_Dispatcher();
	this.onAddFailures = new utest_Dispatcher();
	this.onAddErrors = new utest_Dispatcher();
	this.onAddWarnings = new utest_Dispatcher();
	this.onAddIgnores = new utest_Dispatcher();
};
utest_ui_common_ResultStats.__name__ = "utest.ui.common.ResultStats";
utest_ui_common_ResultStats.prototype = {
	assertations: null
	,successes: null
	,failures: null
	,errors: null
	,warnings: null
	,ignores: null
	,onAddSuccesses: null
	,onAddFailures: null
	,onAddErrors: null
	,onAddWarnings: null
	,onAddIgnores: null
	,isOk: null
	,hasFailures: null
	,hasErrors: null
	,hasWarnings: null
	,hasIgnores: null
	,addSuccesses: function(v) {
		if(v == 0) {
			return;
		}
		this.assertations += v;
		this.successes += v;
		this.onAddSuccesses.dispatch(v);
	}
	,addFailures: function(v) {
		if(v == 0) {
			return;
		}
		this.assertations += v;
		this.failures += v;
		this.hasFailures = this.failures > 0;
		this.isOk = !(this.hasFailures || this.hasErrors || this.hasWarnings);
		this.onAddFailures.dispatch(v);
	}
	,addErrors: function(v) {
		if(v == 0) {
			return;
		}
		this.assertations += v;
		this.errors += v;
		this.hasErrors = this.errors > 0;
		this.isOk = !(this.hasFailures || this.hasErrors || this.hasWarnings);
		this.onAddErrors.dispatch(v);
	}
	,addIgnores: function(v) {
		if(v == 0) {
			return;
		}
		this.assertations += v;
		this.ignores += v;
		this.hasIgnores = this.ignores > 0;
		this.onAddIgnores.dispatch(v);
	}
	,addWarnings: function(v) {
		if(v == 0) {
			return;
		}
		this.assertations += v;
		this.warnings += v;
		this.hasWarnings = this.warnings > 0;
		this.isOk = !(this.hasFailures || this.hasErrors || this.hasWarnings);
		this.onAddWarnings.dispatch(v);
	}
	,sum: function(other) {
		this.addSuccesses(other.successes);
		this.addFailures(other.failures);
		this.addErrors(other.errors);
		this.addWarnings(other.warnings);
		this.addIgnores(other.ignores);
	}
	,subtract: function(other) {
		this.addSuccesses(-other.successes);
		this.addFailures(-other.failures);
		this.addErrors(-other.errors);
		this.addWarnings(-other.warnings);
		this.addIgnores(-other.ignores);
	}
	,wire: function(dependant) {
		dependant.onAddSuccesses.add($bind(this,this.addSuccesses));
		dependant.onAddFailures.add($bind(this,this.addFailures));
		dependant.onAddErrors.add($bind(this,this.addErrors));
		dependant.onAddWarnings.add($bind(this,this.addWarnings));
		dependant.onAddIgnores.add($bind(this,this.addIgnores));
		this.sum(dependant);
	}
	,unwire: function(dependant) {
		dependant.onAddSuccesses.remove($bind(this,this.addSuccesses));
		dependant.onAddFailures.remove($bind(this,this.addFailures));
		dependant.onAddErrors.remove($bind(this,this.addErrors));
		dependant.onAddWarnings.remove($bind(this,this.addWarnings));
		dependant.onAddIgnores.remove($bind(this,this.addIgnores));
		this.subtract(dependant);
	}
	,__class__: utest_ui_common_ResultStats
};
var utest_ui_text_HtmlReport = function(runner,outputHandler,traceRedirected) {
	if(traceRedirected == null) {
		traceRedirected = true;
	}
	this.aggregator = new utest_ui_common_ResultAggregator(runner,true);
	runner.onStart.add($bind(this,this.start));
	this.aggregator.onComplete.add($bind(this,this.complete));
	if(null == outputHandler) {
		this.setHandler($bind(this,this._handler));
	} else {
		this.setHandler(outputHandler);
	}
	if(traceRedirected) {
		this.redirectTrace();
	}
	this.displaySuccessResults = utest_ui_common_SuccessResultsDisplayMode.AlwaysShowSuccessResults;
	this.displayHeader = utest_ui_common_HeaderDisplayMode.AlwaysShowHeader;
};
utest_ui_text_HtmlReport.__name__ = "utest.ui.text.HtmlReport";
utest_ui_text_HtmlReport.__interfaces__ = [utest_ui_common_IReport];
utest_ui_text_HtmlReport.prototype = {
	traceRedirected: null
	,displaySuccessResults: null
	,displayHeader: null
	,handler: null
	,aggregator: null
	,oldTrace: null
	,_traces: null
	,setHandler: function(handler) {
		this.handler = handler;
	}
	,redirectTrace: function() {
		if(this.traceRedirected) {
			return;
		}
		this._traces = [];
		this.oldTrace = haxe_Log.trace;
		haxe_Log.trace = $bind(this,this._trace);
	}
	,restoreTrace: function() {
		if(!this.traceRedirected) {
			return;
		}
		haxe_Log.trace = this.oldTrace;
	}
	,_traceTime: null
	,_trace: function(v,infos) {
		var time = HxOverrides.now() / 1000;
		var delta = this._traceTime == null ? 0 : time - this._traceTime;
		this._traces.push({ msg : StringTools.htmlEscape(Std.string(v)), infos : infos, time : time - this.startTime, delta : delta, stack : haxe_CallStack.callStack()});
		this._traceTime = HxOverrides.now() / 1000;
	}
	,startTime: null
	,start: function(e) {
		this.startTime = HxOverrides.now() / 1000;
	}
	,cls: function(stats) {
		if(stats.hasErrors) {
			return "error";
		} else if(stats.hasFailures) {
			return "failure";
		} else if(stats.hasWarnings) {
			return "warn";
		} else {
			return "ok";
		}
	}
	,resultNumbers: function(buf,stats) {
		var numbers = [];
		if(stats.assertations == 1) {
			numbers.push("<strong>1</strong> test");
		} else {
			numbers.push("<strong>" + stats.assertations + "</strong> tests");
		}
		if(stats.successes != stats.assertations) {
			if(stats.successes == 1) {
				numbers.push("<strong>1</strong> pass");
			} else if(stats.successes > 0) {
				numbers.push("<strong>" + stats.successes + "</strong> passes");
			}
		}
		if(stats.errors == 1) {
			numbers.push("<strong>1</strong> error");
		} else if(stats.errors > 0) {
			numbers.push("<strong>" + stats.errors + "</strong> errors");
		}
		if(stats.failures == 1) {
			numbers.push("<strong>1</strong> failure");
		} else if(stats.failures > 0) {
			numbers.push("<strong>" + stats.failures + "</strong> failures");
		}
		if(stats.warnings == 1) {
			numbers.push("<strong>1</strong> warning");
		} else if(stats.warnings > 0) {
			numbers.push("<strong>" + stats.warnings + "</strong> warnings");
		}
		var x = numbers.join(", ");
		buf.b += Std.string(x);
	}
	,blockNumbers: function(buf,stats) {
		var x = "<div class=\"" + this.cls(stats) + "bg statnumbers\">";
		buf.b += Std.string(x);
		this.resultNumbers(buf,stats);
		buf.b += "</div>";
	}
	,formatStack: function(stack,addNL) {
		if(addNL == null) {
			addNL = true;
		}
		var parts = [];
		var nl = addNL ? "\n" : "";
		var last = null;
		var count = 1;
		var _g = 0;
		var _g1 = haxe_CallStack.toString(stack).split("\n");
		while(_g < _g1.length) {
			var part = _g1[_g];
			++_g;
			if(StringTools.trim(part) == "") {
				continue;
			}
			if(-1 < part.indexOf("Called from utest.")) {
				continue;
			}
			if(part == last) {
				parts[parts.length - 1] = part + " (#" + ++count + ")";
			} else {
				count = 1;
				last = part;
				parts.push(last);
			}
		}
		var s = "<ul><li>" + parts.join("</li>" + nl + "<li>") + "</li></ul>" + nl;
		return "<div>" + s + "</div>" + nl;
	}
	,addFixture: function(buf,result,name,isOk) {
		if(utest_ui_common_ReportTools.skipResult(this,result.stats,isOk)) {
			return;
		}
		buf.b += "<li class=\"fixture\"><div class=\"li\">";
		var x = "<span class=\"" + this.cls(result.stats) + "bg fixtureresult\">";
		buf.b += Std.string(x);
		if(result.stats.isOk) {
			buf.b += "OK ";
		} else if(result.stats.hasErrors) {
			buf.b += "ERROR ";
		} else if(result.stats.hasFailures) {
			buf.b += "FAILURE ";
		} else if(result.stats.hasWarnings) {
			buf.b += "WARNING ";
		}
		buf.b += "</span>";
		buf.b += "<div class=\"fixturedetails\">";
		buf.b += Std.string("<strong>" + name + "</strong>");
		buf.b += ": ";
		this.resultNumbers(buf,result.stats);
		var messages = [];
		var _g = result.iterator();
		while(_g.head != null) {
			var val = _g.head.item;
			_g.head = _g.head.next;
			var assertation = val;
			switch(assertation._hx_index) {
			case 0:
				var _g1 = assertation.pos;
				break;
			case 1:
				var msg = assertation.msg;
				var pos = assertation.pos;
				messages.push("<strong>line " + pos.lineNumber + "</strong>: <em>" + StringTools.htmlEscape(msg) + "</em>");
				break;
			case 2:
				var e = assertation.e;
				var s = assertation.stack;
				messages.push("<strong>error</strong>: <em>" + this.getErrorDescription(e) + "</em>\n<br/><strong>stack</strong>:" + this.getErrorStack(s,e));
				break;
			case 3:
				var e1 = assertation.e;
				var s1 = assertation.stack;
				messages.push("<strong>setup error</strong>: " + this.getErrorDescription(e1) + "\n<br/><strong>stack</strong>:" + this.getErrorStack(s1,e1));
				break;
			case 4:
				var e2 = assertation.e;
				var s2 = assertation.stack;
				messages.push("<strong>tear-down error</strong>: " + this.getErrorDescription(e2) + "\n<br/><strong>stack</strong>:" + this.getErrorStack(s2,e2));
				break;
			case 5:
				var _g2 = assertation.stack;
				var missedAsyncs = assertation.missedAsyncs;
				messages.push("<strong>missed async call(s)</strong>: " + missedAsyncs);
				break;
			case 6:
				var e3 = assertation.e;
				var s3 = assertation.stack;
				messages.push("<strong>async error</strong>: " + this.getErrorDescription(e3) + "\n<br/><strong>stack</strong>:" + this.getErrorStack(s3,e3));
				break;
			case 7:
				var msg1 = assertation.msg;
				messages.push(StringTools.htmlEscape(msg1));
				break;
			case 8:
				var reason = assertation.reason;
				messages.push(StringTools.htmlEscape(reason));
				break;
			}
		}
		if(messages.length > 0) {
			buf.b += "<div class=\"testoutput\">";
			var x = messages.join("<br/>");
			buf.b += Std.string(x);
			buf.b += "</div>\n";
		}
		buf.b += "</div>\n";
		buf.b += "</div></li>\n";
	}
	,getErrorDescription: function(e) {
		return Std.string(e);
	}
	,getErrorStack: function(s,e) {
		return this.formatStack(s);
	}
	,addClass: function(buf,result,name,isOk) {
		if(utest_ui_common_ReportTools.skipResult(this,result.stats,isOk)) {
			return;
		}
		buf.b += "<li>";
		buf.b += Std.string("<h2 class=\"classname\">" + name + "</h2>");
		this.blockNumbers(buf,result.stats);
		buf.b += "<ul>\n";
		var _g = 0;
		var _g1 = result.methodNames();
		while(_g < _g1.length) {
			var mname = _g1[_g];
			++_g;
			this.addFixture(buf,result.get(mname),mname,isOk);
		}
		buf.b += "</ul>\n";
		buf.b += "</li>\n";
	}
	,addPackages: function(buf,result,isOk) {
		if(utest_ui_common_ReportTools.skipResult(this,result.stats,isOk)) {
			return;
		}
		buf.b += "<ul id=\"utest-results-packages\">\n";
		var _g = 0;
		var _g1 = result.packageNames(false);
		while(_g < _g1.length) {
			var name = _g1[_g];
			++_g;
			this.addPackage(buf,result.getPackage(name),name,isOk);
		}
		buf.b += "</ul>\n";
	}
	,addPackage: function(buf,result,name,isOk) {
		if(utest_ui_common_ReportTools.skipResult(this,result.stats,isOk)) {
			return;
		}
		if(name == "" && result.classNames().length == 0) {
			return;
		}
		buf.b += "<li>";
		buf.b += Std.string("<h2>" + name + "</h2>");
		this.blockNumbers(buf,result.stats);
		buf.b += "<ul>\n";
		var _g = 0;
		var _g1 = result.classNames();
		while(_g < _g1.length) {
			var cname = _g1[_g];
			++_g;
			this.addClass(buf,result.getClass(cname),cname,isOk);
		}
		buf.b += "</ul>\n";
		buf.b += "</li>\n";
	}
	,getTextResults: function() {
		var newline = "\n";
		var indents = function(count) {
			var _g = [];
			var _g1 = 0;
			var _g2 = count;
			while(_g1 < _g2) {
				var i = _g1++;
				_g.push("  ");
			}
			return _g.join("");
		};
		var dumpStack = function(stack) {
			if(stack.length == 0) {
				return "";
			}
			var parts = haxe_CallStack.toString(stack).split("\n");
			var r = [];
			var _g = 0;
			while(_g < parts.length) {
				var part = parts[_g];
				++_g;
				if(part.indexOf(" utest.") >= 0) {
					continue;
				}
				r.push(part);
			}
			return r.join(newline);
		};
		var buf_b = "";
		var _g = 0;
		var _g1 = this.result.packageNames();
		while(_g < _g1.length) {
			var pname = _g1[_g];
			++_g;
			var pack = this.result.getPackage(pname);
			if(utest_ui_common_ReportTools.skipResult(this,pack.stats,this.result.stats.isOk)) {
				continue;
			}
			var _g2 = 0;
			var _g3 = pack.classNames();
			while(_g2 < _g3.length) {
				var cname = _g3[_g2];
				++_g2;
				var cls = pack.getClass(cname);
				if(utest_ui_common_ReportTools.skipResult(this,cls.stats,this.result.stats.isOk)) {
					continue;
				}
				buf_b += Std.string((pname == "" ? "" : pname + ".") + cname + newline);
				var _g4 = 0;
				var _g5 = cls.methodNames();
				while(_g4 < _g5.length) {
					var mname = _g5[_g4];
					++_g4;
					var fix = cls.get(mname);
					if(utest_ui_common_ReportTools.skipResult(this,fix.stats,this.result.stats.isOk)) {
						continue;
					}
					buf_b += Std.string(indents(1) + mname + ": ");
					if(fix.stats.isOk) {
						buf_b += "OK ";
					} else if(fix.stats.hasErrors) {
						buf_b += "ERROR ";
					} else if(fix.stats.hasFailures) {
						buf_b += "FAILURE ";
					} else if(fix.stats.hasWarnings) {
						buf_b += "WARNING ";
					}
					var messages = "";
					var _g6 = fix.iterator();
					while(_g6.head != null) {
						var val = _g6.head.item;
						_g6.head = _g6.head.next;
						var assertation = val;
						switch(assertation._hx_index) {
						case 0:
							var _g7 = assertation.pos;
							buf_b += ".";
							break;
						case 1:
							var msg = assertation.msg;
							var pos = assertation.pos;
							buf_b += "F";
							messages += indents(2) + "line: " + pos.lineNumber + ", " + msg + newline;
							break;
						case 2:
							var e = assertation.e;
							var s = assertation.stack;
							buf_b += "E";
							messages += indents(2) + Std.string(e) + dumpStack(s) + newline;
							break;
						case 3:
							var e1 = assertation.e;
							var s1 = assertation.stack;
							buf_b += "S";
							messages += indents(2) + Std.string(e1) + dumpStack(s1) + newline;
							break;
						case 4:
							var e2 = assertation.e;
							var s2 = assertation.stack;
							buf_b += "T";
							messages += indents(2) + Std.string(e2) + dumpStack(s2) + newline;
							break;
						case 5:
							var missedAsyncs = assertation.missedAsyncs;
							var s3 = assertation.stack;
							buf_b += "O";
							messages += indents(2) + "missed async calls: " + missedAsyncs + dumpStack(s3) + newline;
							break;
						case 6:
							var e3 = assertation.e;
							var s4 = assertation.stack;
							buf_b += "A";
							messages += indents(2) + Std.string(e3) + dumpStack(s4) + newline;
							break;
						case 7:
							var msg1 = assertation.msg;
							buf_b += "W";
							messages += indents(2) + msg1 + newline;
							break;
						case 8:
							var reason = assertation.reason;
							buf_b += "I";
							if(reason != null && reason != "") {
								messages += indents(2) + ("With reason: " + reason) + newline;
							}
							break;
						}
					}
					buf_b += newline == null ? "null" : "" + newline;
					buf_b += messages == null ? "null" : "" + messages;
				}
			}
		}
		return buf_b;
	}
	,getHeader: function() {
		var buf = new StringBuf();
		if(!utest_ui_common_ReportTools.hasHeader(this,this.result.stats)) {
			return "";
		}
		var end = HxOverrides.now() / 1000;
		var time = ((end - this.startTime) * 1000 | 0) / 1000;
		var msg = "TEST OK";
		if(this.result.stats.hasErrors) {
			msg = "TEST ERRORS";
		} else if(this.result.stats.hasFailures) {
			msg = "TEST FAILED";
		} else if(this.result.stats.hasWarnings) {
			msg = "WARNING REPORTED";
		}
		var x = "<h1 class=\"" + this.cls(this.result.stats) + "bg header\">" + msg + "</h1>\n";
		buf.b += Std.string(x);
		buf.b += "<div class=\"headerinfo\">";
		this.resultNumbers(buf,this.result.stats);
		buf.b += Std.string(" performed on <strong>" + utest_ui_text_HtmlReport.platform + "</strong>, executed in <strong> " + time + " sec. </strong></div >\n ");
		return buf.b;
	}
	,getTrace: function() {
		var buf_b = "";
		if(this._traces == null || this._traces.length == 0) {
			return "";
		}
		buf_b += "<div class=\"trace\"><h2>traces</h2><ol>";
		var _g = 0;
		var _g1 = this._traces;
		while(_g < _g1.length) {
			var t = _g1[_g];
			++_g;
			buf_b += "<li><div class=\"li\">";
			var stack = StringTools.replace(this.formatStack(t.stack,false),"'","\\'");
			var method = "<span class=\"tracepackage\">" + t.infos.className + "</span><br/>" + t.infos.methodName + "(" + t.infos.lineNumber + ")";
			buf_b += Std.string("<span class=\"tracepos\" onmouseover=\"utestTooltip(this.parentNode, '" + stack + "')\" onmouseout=\"utestRemoveTooltip()\">");
			buf_b += method == null ? "null" : "" + method;
			buf_b += "</span><span class=\"tracetime\">";
			buf_b += Std.string("@ " + this.formatTime(t.time));
			if(Math.round(t.delta * 1000) > 0) {
				buf_b += Std.string(", ~" + this.formatTime(t.delta));
			}
			buf_b += "</span><span class=\"tracemsg\">";
			buf_b += Std.string(StringTools.replace(StringTools.trim(t.msg),"\n","<br/>\n"));
			buf_b += "</span><div class=\"clr\"></div></div></li>";
		}
		buf_b += "</ol></div>";
		return buf_b;
	}
	,getResults: function() {
		var buf = new StringBuf();
		this.addPackages(buf,this.result,this.result.stats.isOk);
		return buf.b;
	}
	,getAll: function() {
		if(!utest_ui_common_ReportTools.hasOutput(this,this.result.stats)) {
			return "";
		} else {
			return this.getHeader() + this.getTrace() + this.getResults();
		}
	}
	,getHtml: function(title) {
		if(null == title) {
			title = "utest: " + utest_ui_text_HtmlReport.platform;
		}
		var s = this.getAll();
		if("" == s) {
			return "";
		} else {
			return this.wrapHtml(title,s);
		}
	}
	,result: null
	,complete: function(result) {
		this.result = result;
		this.handler(this);
		this.restoreTrace();
		var exposedResult = { isOk : result.stats.isOk, message : this.getTextResults()};
		if('undefined' != typeof window) {
			window.utest_result = exposedResult;
		}
	}
	,formatTime: function(t) {
		return Math.round(t * 1000) + " ms";
	}
	,cssStyle: function() {
		return "body, dd, dt {\n  font-family: Verdana, Arial, Sans-serif;\n  font-size: 12px;\n}\ndl {\n  width: 180px;\n}\ndd, dt {\n  margin : 0;\n  padding : 2px 5px;\n  border-top: 1px solid #f0f0f0;\n  border-left: 1px solid #f0f0f0;\n  border-right: 1px solid #CCCCCC;\n  border-bottom: 1px solid #CCCCCC;\n}\ndd.value {\n  text-align: center;\n  background-color: #eeeeee;\n}\ndt {\n  text-align: left;\n  background-color: #e6e6e6;\n  float: left;\n  width: 100px;\n}\n\nh1, h2, h3, h4, h5, h6 {\n  margin: 0;\n  padding: 0;\n}\n\nh1 {\n  text-align: center;\n  font-weight: bold;\n  padding: 5px 0 4px 0;\n  font-family: Arial, Sans-serif;\n  font-size: 18px;\n  border-top: 1px solid #f0f0f0;\n  border-left: 1px solid #f0f0f0;\n  border-right: 1px solid #CCCCCC;\n  border-bottom: 1px solid #CCCCCC;\n  margin: 0 2px 0px 2px;\n}\n\nh2 {\n  font-weight: bold;\n  padding: 2px 0 2px 8px;\n  font-family: Arial, Sans-serif;\n  font-size: 13px;\n  border-top: 1px solid #f0f0f0;\n  border-left: 1px solid #f0f0f0;\n  border-right: 1px solid #CCCCCC;\n  border-bottom: 1px solid #CCCCCC;\n  margin: 0 0 0px 0;\n  background-color: #FFFFFF;\n  color: #777777;\n}\n\nh2.classname {\n  color: #000000;\n}\n\n.okbg {\n  background-color: #66FF55;\n}\n.errorbg {\n  background-color: #CC1100;\n}\n.failurebg {\n  background-color: #EE3322;\n}\n.warnbg {\n  background-color: #FFCC99;\n}\n.headerinfo {\n  text-align: right;\n  font-size: 11px;\n  font - color: 0xCCCCCC;\n  margin: 0 2px 5px 2px;\n  border-left: 1px solid #f0f0f0;\n  border-right: 1px solid #CCCCCC;\n  border-bottom: 1px solid #CCCCCC;\n  padding: 2px;\n}\n\nli {\n  padding: 4px;\n  margin: 2px;\n  border-top: 1px solid #f0f0f0;\n  border-left: 1px solid #f0f0f0;\n  border-right: 1px solid #CCCCCC;\n  border-bottom: 1px solid #CCCCCC;\n  background-color: #e6e6e6;\n}\n\nli.fixture {\n  background-color: #f6f6f6;\n  padding-bottom: 6px;\n}\n\ndiv.fixturedetails {\n  padding-left: 108px;\n}\n\nul {\n  padding: 0;\n  margin: 6px 0 0 0;\n  list-style-type: none;\n}\n\nol {\n  padding: 0 0 0 28px;\n  margin: 0px 0 0 0;\n}\n\n.statnumbers {\n  padding: 2px 8px;\n}\n\n.fixtureresult {\n  width: 100px;\n  text-align: center;\n  display: block;\n  float: left;\n  font-weight: bold;\n  padding: 1px;\n  margin: 0 0 0 0;\n}\n\n.testoutput {\n  border: 1px dashed #CCCCCC;\n  margin: 4px 0 0 0;\n  padding: 4px 8px;\n  background-color: #eeeeee;\n}\n\nspan.tracepos, span.traceposempty {\n  display: block;\n  float: left;\n  font-weight: bold;\n  font-size: 9px;\n  width: 170px;\n  margin: 2px 0 0 2px;\n}\n\nspan.tracepos:hover {\n  cursor : pointer;\n  background-color: #ffff99;\n}\n\nspan.tracemsg {\n  display: block;\n  margin-left: 180px;\n  background-color: #eeeeee;\n  padding: 7px;\n}\n\nspan.tracetime {\n  display: block;\n  float: right;\n  margin: 2px;\n  font-size: 9px;\n  color: #777777;\n}\n\n\ndiv.trace ol {\n  padding: 0 0 0 40px;\n  color: #777777;\n}\n\ndiv.trace li {\n  padding: 0;\n}\n\ndiv.trace li div.li {\n  color: #000000;\n}\n\ndiv.trace h2 {\n  margin: 0 2px 0px 2px;\n  padding-left: 4px;\n}\n\n.tracepackage {\n  color: #777777;\n  font-weight: normal;\n}\n\n.clr {\n  clear: both;\n}\n\n#utesttip {\n  margin-top: -3px;\n  margin-left: 170px;\n  font-size: 9px;\n}\n\n#utesttip li {\n  margin: 0;\n  background-color: #ffff99;\n  padding: 2px 4px;\n  border: 0;\n  border-bottom: 1px dashed #ffff33;\n}";
	}
	,jsScript: function() {
		return "function utestTooltip(ref, text) {\n  var el = document.getElementById(\"utesttip\");\n  if(!el) {\n    var el = document.createElement(\"div\")\n    el.id = \"utesttip\";\n    el.style.position = \"absolute\";\n    document.body.appendChild(el)\n  }\n  var p = utestFindPos(ref);\n  el.style.left = (4 + p[0]) + \"px\";\n  el.style.top = (p[1] - 1) + \"px\";\n  el.innerHTML =  text;\n}\n\nfunction utestFindPos(el) {\n  var left = 0;\n  var top = 0;\n  do {\n    left += el.offsetLeft;\n    top += el.offsetTop;\n  } while(el = el.offsetParent)\n  return [left, top];\n}\n\nfunction utestRemoveTooltip() {\n  var el = document.getElementById(\"utesttip\")\n  if(el)\n    document.body.removeChild(el)\n}";
	}
	,wrapHtml: function(title,s) {
		return "<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" />\n<title>" + title + "</title>\n      <style type=\"text/css\">" + this.cssStyle() + "</style>\n      <script type=\"text/javascript\">\n" + this.jsScript() + "\n</" + "script>\n</head>\n      <body>\n" + s + "\n</body>\n</html>";
	}
	,_handler: function(report) {
		var _gthis = this;
		if(window.document.readyState == "loading") {
			var onReadyStateChange = null;
			onReadyStateChange = function() {
				if(window.document.readyState != "loading") {
					window.document.removeEventListener("readystatechange",onReadyStateChange);
					_gthis._handler(report);
				}
			};
			window.document.addEventListener("readystatechange",onReadyStateChange);
			return;
		}
		var isDef = function(v) {
			return typeof v != 'undefined';
		};
		var hasProcess = typeof process != 'undefined';
		if(hasProcess) {
			process.stdout.write(report.getHtml());
			return;
		}
		var head = window.document.getElementsByTagName("head")[0];
		var script = window.document.createElement("script");
		script.type = "text/javascript";
		var sjs = report.jsScript();
		if(isDef(script.text)) {
			script.text = sjs;
		} else {
			script.innerHTML = sjs;
		}
		head.appendChild(script);
		var style = window.document.createElement("style");
		style.type = "text/css";
		var scss = report.cssStyle();
		if(isDef(style.styleSheet)) {
			style.styleSheet.cssText = scss;
		} else if(isDef(style.cssText)) {
			style.cssText = scss;
		} else if(isDef(style.innerText)) {
			style.innerText = scss;
		} else {
			style.innerHTML = scss;
		}
		head.appendChild(style);
		var el = window.document.getElementById("utest-results");
		if(null == el) {
			el = window.document.createElement("div");
			el.id = "utest-results";
			window.document.body.appendChild(el);
		}
		el.innerHTML = report.getAll();
	}
	,__class__: utest_ui_text_HtmlReport
};
var utest_ui_text_PlainTextReport = function(runner,outputHandler) {
	this.aggregator = new utest_ui_common_ResultAggregator(runner,true);
	runner.onStart.add($bind(this,this.start));
	this.aggregator.onComplete.add($bind(this,this.complete));
	if(null != outputHandler) {
		this.setHandler(outputHandler);
	}
	this.displaySuccessResults = utest_ui_common_SuccessResultsDisplayMode.AlwaysShowSuccessResults;
	this.displayHeader = utest_ui_common_HeaderDisplayMode.AlwaysShowHeader;
};
utest_ui_text_PlainTextReport.__name__ = "utest.ui.text.PlainTextReport";
utest_ui_text_PlainTextReport.__interfaces__ = [utest_ui_common_IReport];
utest_ui_text_PlainTextReport.prototype = {
	displaySuccessResults: null
	,displayHeader: null
	,handler: null
	,aggregator: null
	,newline: null
	,indent: null
	,setHandler: function(handler) {
		this.handler = handler;
	}
	,startTime: null
	,start: function(e) {
		this.startTime = this.getTime();
	}
	,getTime: function() {
		return HxOverrides.now() / 1000;
	}
	,indents: function(c) {
		var s = "";
		while(--c >= 0) s += this.indent;
		return s;
	}
	,dumpStack: function(stack) {
		if(stack.length == 0) {
			return "";
		}
		var parts = haxe_CallStack.toString(stack).split("\n");
		var r = [];
		var _g = 0;
		while(_g < parts.length) {
			var part = parts[_g];
			++_g;
			if(part.indexOf(" utest.") >= 0) {
				continue;
			}
			r.push(part);
		}
		return r.join(this.newline);
	}
	,addHeader: function(buf,result) {
		if(!utest_ui_common_ReportTools.hasHeader(this,result.stats)) {
			return;
		}
		var end = this.getTime();
		var time = ((end - this.startTime) * 1000 | 0) / 1000;
		buf.b += Std.string("\nassertations: " + result.stats.assertations + this.newline);
		buf.b += Std.string("successes: " + result.stats.successes + this.newline);
		buf.b += Std.string("errors: " + result.stats.errors + this.newline);
		buf.b += Std.string("failures: " + result.stats.failures + this.newline);
		buf.b += Std.string("warnings: " + result.stats.warnings + this.newline);
		buf.b += Std.string("execution time: " + time + this.newline);
		buf.b += Std.string(this.newline);
		buf.b += Std.string("results: " + (result.stats.isOk ? "ALL TESTS OK (success: true)" : "SOME TESTS FAILURES (success: false)"));
		buf.b += Std.string(this.newline);
	}
	,result: null
	,getResults: function() {
		var buf = new StringBuf();
		this.addHeader(buf,this.result);
		var _g = 0;
		var _g1 = this.result.packageNames();
		while(_g < _g1.length) {
			var pname = _g1[_g];
			++_g;
			var pack = this.result.getPackage(pname);
			if(utest_ui_common_ReportTools.skipResult(this,pack.stats,this.result.stats.isOk)) {
				continue;
			}
			var _g2 = 0;
			var _g3 = pack.classNames();
			while(_g2 < _g3.length) {
				var cname = _g3[_g2];
				++_g2;
				var cls = pack.getClass(cname);
				if(utest_ui_common_ReportTools.skipResult(this,cls.stats,this.result.stats.isOk)) {
					continue;
				}
				buf.b += Std.string((pname == "" ? "" : pname + ".") + cname + this.newline);
				var _g4 = 0;
				var _g5 = cls.methodNames();
				while(_g4 < _g5.length) {
					var mname = _g5[_g4];
					++_g4;
					var fix = cls.get(mname);
					if(utest_ui_common_ReportTools.skipResult(this,fix.stats,this.result.stats.isOk)) {
						continue;
					}
					var x = this.indents(1) + mname + ": ";
					buf.b += Std.string(x);
					if(fix.stats.isOk) {
						buf.b += "OK ";
					} else if(fix.stats.hasErrors) {
						buf.b += "ERROR ";
					} else if(fix.stats.hasFailures) {
						buf.b += "FAILURE ";
					} else if(fix.stats.hasWarnings) {
						buf.b += "WARNING ";
					}
					var messages = "";
					var _g6 = fix.iterator();
					while(_g6.head != null) {
						var val = _g6.head.item;
						_g6.head = _g6.head.next;
						var assertation = val;
						switch(assertation._hx_index) {
						case 0:
							var _g7 = assertation.pos;
							buf.b += ".";
							break;
						case 1:
							var msg = assertation.msg;
							var pos = assertation.pos;
							buf.b += "F";
							messages += this.indents(2) + "line: " + pos.lineNumber + ", " + msg + this.newline;
							break;
						case 2:
							var e = assertation.e;
							var s = assertation.stack;
							buf.b += "E";
							messages += this.indents(2) + Std.string(e) + this.dumpStack(s) + this.newline;
							break;
						case 3:
							var e1 = assertation.e;
							var s1 = assertation.stack;
							buf.b += "S";
							messages += this.indents(2) + Std.string(e1) + this.dumpStack(s1) + this.newline;
							break;
						case 4:
							var e2 = assertation.e;
							var s2 = assertation.stack;
							buf.b += "T";
							messages += this.indents(2) + Std.string(e2) + this.dumpStack(s2) + this.newline;
							break;
						case 5:
							var missedAsyncs = assertation.missedAsyncs;
							var s3 = assertation.stack;
							buf.b += "O";
							messages += this.indents(2) + "missed async calls: " + missedAsyncs + this.dumpStack(s3) + this.newline;
							break;
						case 6:
							var e3 = assertation.e;
							var s4 = assertation.stack;
							buf.b += "A";
							messages += this.indents(2) + Std.string(e3) + this.dumpStack(s4) + this.newline;
							break;
						case 7:
							var msg1 = assertation.msg;
							buf.b += "W";
							messages += this.indents(2) + msg1 + this.newline;
							break;
						case 8:
							var reason = assertation.reason;
							buf.b += "I";
							if(reason != null && reason != "") {
								messages += this.indents(2) + ("With reason: " + reason) + this.newline;
							}
							break;
						}
					}
					buf.b += Std.string(this.newline);
					buf.b += messages == null ? "null" : "" + messages;
				}
			}
		}
		return buf.b;
	}
	,complete: function(result) {
		this.result = result;
		if(this.handler != null) {
			this.handler(this);
		}
		if(typeof phantom != "undefined") {
			var tmp = result.stats.isOk ? 0 : 1;
			phantom.exit(tmp);
		}
		if(typeof process != "undefined") {
			var tmp = result.stats.isOk ? 0 : 1;
			process.exit(tmp);
		}
	}
	,__class__: utest_ui_text_PlainTextReport
};
var utest_ui_text_PrintReport = function(runner) {
	utest_ui_text_PlainTextReport.call(this,runner,$bind(this,this._handler));
	this.newline = "\n";
	this.indent = "  ";
};
utest_ui_text_PrintReport.__name__ = "utest.ui.text.PrintReport";
utest_ui_text_PrintReport.__super__ = utest_ui_text_PlainTextReport;
utest_ui_text_PrintReport.prototype = $extend(utest_ui_text_PlainTextReport.prototype,{
	_handler: function(report) {
		this._trace(report.getResults());
	}
	,_trace: function(s) {
		s = StringTools.replace(s,"  ",this.indent);
		s = StringTools.replace(s,"\n",this.newline);
		haxe_Log.trace(s,{ fileName : "utest/ui/text/PrintReport.hx", lineNumber : 52, className : "utest.ui.text.PrintReport", methodName : "_trace"});
	}
	,__class__: utest_ui_text_PrintReport
});
var utest_utils_AccessoriesUtils = function() { };
utest_utils_AccessoriesUtils.__name__ = "utest.utils.AccessoriesUtils";
utest_utils_AccessoriesUtils.getSetupClass = function(accessories) {
	if(accessories.setupClass == null) {
		return utest_Async.getResolved;
	} else {
		return accessories.setupClass;
	}
};
utest_utils_AccessoriesUtils.getSetup = function(accessories) {
	if(accessories.setup == null) {
		return utest_Async.getResolved;
	} else {
		return accessories.setup;
	}
};
utest_utils_AccessoriesUtils.getTeardown = function(accessories) {
	if(accessories.teardown == null) {
		return utest_Async.getResolved;
	} else {
		return accessories.teardown;
	}
};
utest_utils_AccessoriesUtils.getTeardownClass = function(accessories) {
	if(accessories.teardownClass == null) {
		return utest_Async.getResolved;
	} else {
		return accessories.teardownClass;
	}
};
var utest_utils_AsyncUtils = function() { };
utest_utils_AsyncUtils.__name__ = "utest.utils.AsyncUtils";
utest_utils_AsyncUtils.orResolved = function(_async) {
	if(_async == null) {
		return utest_Async.getResolved();
	} else {
		return _async;
	}
};
var utest_utils_Misc = function() { };
utest_utils_Misc.__name__ = "utest.utils.Misc";
utest_utils_Misc.isOfType = function(v,t) {
	return js_Boot.__instanceof(v,t);
};
var utest_utils_Print = function() { };
utest_utils_Print.__name__ = "utest.utils.Print";
utest_utils_Print.immediately = function(msg) {
	console.log(msg);
};
utest_utils_Print.startCase = function(caseName) {
};
utest_utils_Print.startTest = function(name) {
};
function $getIterator(o) { if( o instanceof Array ) return new haxe_iterators_ArrayIterator(o); else return o.iterator(); }
function $bind(o,m) { if( m == null ) return null; if( m.__id__ == null ) m.__id__ = $global.$haxeUID++; var f; if( o.hx__closures__ == null ) o.hx__closures__ = {}; else f = o.hx__closures__[m.__id__]; if( f == null ) { f = m.bind(o); o.hx__closures__[m.__id__] = f; } return f; }
$global.$haxeUID |= 0;
if(typeof(performance) != "undefined" ? typeof(performance.now) == "function" : false) {
	HxOverrides.now = performance.now.bind(performance);
}
if( String.fromCodePoint == null ) String.fromCodePoint = function(c) { return c < 0x10000 ? String.fromCharCode(c) : String.fromCharCode((c>>10)+0xD7C0)+String.fromCharCode((c&0x3FF)+0xDC00); }
String.prototype.__class__ = String;
String.__name__ = "String";
Array.__name__ = "Array";
Date.prototype.__class__ = Date;
Date.__name__ = "Date";
var Int = { };
var Dynamic = { };
var Float = Number;
var Bool = Boolean;
var Class = { };
var Enum = { };
js_Boot.__toStr = ({ }).toString;
Xml.Element = 0;
Xml.CData = 2;
Xml.Document = 6;
com_plantuml_mindmap_Tetris.MAX_VALUE = 999999999.0;
haxe_crypto_Base64.CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
haxe_crypto_Base64.BYTES = haxe_io_Bytes.ofString(haxe_crypto_Base64.CHARS);
hx_strings_Char.CHAR_CASE_MAPPER = new hx_strings__$Char_CharCaseMapper();
hx_strings_Char.BACKSPACE = 8;
hx_strings_Char.TAB = 9;
hx_strings_Char.LF = 10;
hx_strings_Char.CR = 13;
hx_strings_Char.ESC = 27;
hx_strings_Char.SPACE = 32;
hx_strings_Char.EXCLAMATION_MARK = 33;
hx_strings_Char.DOUBLE_QUOTE = 34;
hx_strings_Char.HASH = 35;
hx_strings_Char.DOLLAR = 36;
hx_strings_Char.AMPERSAND = 38;
hx_strings_Char.SINGLE_QUOTE = 39;
hx_strings_Char.BRACKET_ROUND_LEFT = 40;
hx_strings_Char.BRACKET_ROUND_RIGHT = 41;
hx_strings_Char.ASTERISK = 42;
hx_strings_Char.PLUS = 43;
hx_strings_Char.COMMA = 44;
hx_strings_Char.MINUS = 45;
hx_strings_Char.DOT = 46;
hx_strings_Char.SLASH = 47;
hx_strings_Char.ZERO = 48;
hx_strings_Char.ONE = 49;
hx_strings_Char.TWO = 50;
hx_strings_Char.TRHEE = 51;
hx_strings_Char.FOUR = 52;
hx_strings_Char.FIVE = 53;
hx_strings_Char.SIX = 54;
hx_strings_Char.SEVEN = 55;
hx_strings_Char.EIGHT = 56;
hx_strings_Char.NINE = 57;
hx_strings_Char.COLON = 58;
hx_strings_Char.SEMICOLON = 59;
hx_strings_Char.LOWER_THAN = 60;
hx_strings_Char.EQUALS = 61;
hx_strings_Char.GREATER_THAN = 62;
hx_strings_Char.QUESTION_MARK = 63;
hx_strings_Char.BRACKET_SQUARE_LEFT = 91;
hx_strings_Char.BACKSLASH = 92;
hx_strings_Char.BRACKET_SQUARE_RIGHT = 93;
hx_strings_Char.CARET = 94;
hx_strings_Char.UNDERSCORE = 95;
hx_strings_Char.BRACKET_CURLY_LEFT = 123;
hx_strings_Char.PIPE = 124;
hx_strings_Char.BRACKET_CURLY_RIGHT = 125;
hx_strings__$CharIterator_NullCharIterator.INSTANCE = new hx_strings__$CharIterator_NullCharIterator();
hx_strings_Pattern.__meta__ = { obj : { immutable : null, threadSafe : null}};
hx_strings_Matcher.__meta__ = { obj : { notThreadSafe : null}};
hx_strings_StringBuilder.__meta__ = { obj : { notThreadSafe : null}};
hx_strings_internal_OS.isNodeJS = (typeof process !== 'undefined') && (typeof process.release !== 'undefined') && (process.release.name === 'node');
hx_strings_internal_OS.isWindows = (function($this) {
	var $r;
	var os = hx_strings_internal_OS.isNodeJS ? process.platform : $global.navigator.platform;
	$r = new EReg("win","i").match(os);
	return $r;
}(this));
hx_strings_Strings.REGEX_ANSI_ESC = (function($this) {
	var $r;
	var this1 = hx_strings_internal__$Either3__$Either3.b("g");
	$r = hx_strings_Pattern.compile(String.fromCodePoint(27) + "\\[[;\\d]*m",this1);
	return $r;
}(this));
hx_strings_Strings.REGEX_HTML_UNESCAPE = (function($this) {
	var $r;
	var this1 = hx_strings_internal__$Either3__$Either3.b("g");
	$r = hx_strings_Pattern.compile("&(#\\d+|amp|nbsp|apos|lt|gt|quot);",this1);
	return $r;
}(this));
hx_strings_Strings.REGEX_SPLIT_LINES = (function($this) {
	var $r;
	var this1 = hx_strings_internal__$Either3__$Either3.b("g");
	$r = hx_strings_Pattern.compile("\\r?\\n",this1);
	return $r;
}(this));
hx_strings_Strings.REGEX_REMOVE_XML_TAGS = (function($this) {
	var $r;
	var this1 = hx_strings_internal__$Either3__$Either3.b("g");
	$r = hx_strings_Pattern.compile("<[!a-zA-Z\\/][^>]*>",this1);
	return $r;
}(this));
hx_strings_Strings.POS_NOT_FOUND = -1;
hx_strings_Strings.NEW_LINE_NIX = "\n";
hx_strings_Strings.NEW_LINE_WIN = "\r\n";
hx_strings_Strings.NEW_LINE = hx_strings_internal_OS.isWindows ? "\r\n" : "\n";
utest_TestHandler.POLLING_TIME = 10;
utest_AccessoryName.SETUP_NAME = "setup";
utest_AccessoryName.SETUP_CLASS_NAME = "setupClass";
utest_AccessoryName.TEARDOWN_NAME = "teardown";
utest_AccessoryName.TEARDOWN_CLASS_NAME = "teardownClass";
utest_ui_text_HtmlReport.platform = "javascript";
MainJs.main();
})(typeof exports != "undefined" ? exports : typeof window != "undefined" ? window : typeof self != "undefined" ? self : this, typeof window != "undefined" ? window : typeof global != "undefined" ? global : typeof self != "undefined" ? self : this);
