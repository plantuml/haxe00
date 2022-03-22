package com.plantuml.regex;

#if js
import js.lib.RegExp;
#end
#if python
import python.lib.Re;
#end
#if java
import java.util.regex.Pattern;
import java.util.regex.Matcher;
#end

class Matcher2 {
	final pString:String;
	final input:String;

	#if java
	final p:Pattern;
	final m:Matcher;

	public function new(pString, input, p:Pattern) {
		this.pString = pString;
		this.input = input;
		this.p = p;
		this.m = p.matcher(input);
	}
	#else
	public function new(pString, input) {
		this.pString = pString;
		this.input = input;
	}
	#end

	public function matches():Bool {
		#if java
		return m.matches();
		#else
		final r = new EReg(pString, "i");
		return r.match(input);
		#end
	}

	public function group(n:Int):String {
		#if java
		if (m.matches() == false)
			return null;
		return m.group(n);
		#else
		trace('n=$n');
		final r = new EReg(pString, "i");
		var m = r.match(input);
		trace('m=$m');
		if (m == false)
			return null;
		return r.matched(n);
		#end
	}
}
