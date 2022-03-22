package com.plantuml.regex;

using hx.strings.Strings;

class MyPattern {
	public static function cmpile(p:String):Pattern2 {
		trace('before=$p');
		p = transform(p);
		trace('after =$p');
		return new Pattern2(p);
	}

	static function transform(s:String):String {
		#if java
		s = s.replaceAll("%%L", "[\\p{L}]");
		#elseif python
		s = s.replaceAll("%%L", "[^\\W\\d_]");
		#else
		s = s.replaceAll("%%L", "[\\p{L}]");
		#end
		return s;
	}

	// private static String transform(String p) {
	// 	// Replace ReadLineReader.java
	// 	p = p.replace("%pLN", "\\p{L}0-9"); // Unicode Letter, digit
	// 	p = p.replace("%s", "\\s\u00A0"); // space
	// 	p = p.replace("%q", "'\u2018\u2019"); // quote
	// 	p = p.replace("%g", "\"\u201c\u201d\u00ab\u00bb"); // double quote
	// 	return p;
	// }
}
