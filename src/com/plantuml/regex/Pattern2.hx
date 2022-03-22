package com.plantuml.regex;

class Pattern2 {
	final p:String;

	public function new(p:String) {
		this.p = p;
	}

	public function matcher(input:String):Matcher2 {
		// final r = new EReg(p, "i");
		return new Matcher2(p, input);
	}
}
