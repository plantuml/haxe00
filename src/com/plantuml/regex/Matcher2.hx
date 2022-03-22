package com.plantuml.regex;

class Matcher2 {
	final p:String;
	final input:String;

	public function new(p, input) {
		this.p = p;
		this.input = input;
	}

	public function matches():Bool {
		final r = new EReg(p, "i");
		return r.match(input);
	}

	public function group(?n:Int):String {
		trace('n=$n');
		final r = new EReg(p, "i");
		var m = r.match(input);
		trace('m=$m');
		if (m == false)
			return null;
		return r.matched(n);
	}
}
