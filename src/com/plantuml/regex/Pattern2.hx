package com.plantuml.regex;

#if js
import js.lib.RegExp;
#end
#if python
import python.lib.Re;
#end
#if java
import java.util.regex.Pattern;
#end

class Pattern2 {
	final pString:String;
	#if java
	final p:Pattern;
	#elseif python
	final p:Pattern;
	#end

	public function new(p:String) {
		this.pString = p;
		#if java
		this.p = Pattern.compile(p);
		#elseif python
		this.p = Re.compile(p, Re.UNICODE);
		#end
	}

	public function matcher(input:String):Matcher2 {
		#if java
		return new Matcher2(pString, input, p);
		#elseif python
		return new Matcher2(pString, input, p);
		#else
		return new Matcher2(pString, input);
		#end
	}
}
