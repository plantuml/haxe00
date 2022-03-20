package com.plantuml.utils;

using hx.strings.Strings;

class StartUtils {
	static public function beforeStartUml(s:String):String {
		final x = s.indexOf("@start");
		if (x == -1)
			return null;
		return s.substr(0, x);
	}

	static public function removeHeader(s:String, header:String):String {
		if (header != null && s.startsWith(header))
			return s.substring(header.length);
		return s;
	}
}
