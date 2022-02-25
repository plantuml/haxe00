package com.plantuml.command.regex;

class MyPattern {
	static public function transform(p:String):String {
		p = StringTools.replace(p, "%s", "\\s\u00A0");
		return p;
	}
}
