import utest.*;

#if js
import js.lib.RegExp;
#end
#if python
import python.lib.Re;
#end
using hx.strings.Strings;

class UnicodeRegexTest extends utest.Test {
	function testBasicThing1() {
		var r = new EReg("\\w", "i");
		final s = "a";
		Assert.isTrue(r.match(s));
	}
	
	#if python
	function testBasicThing1AccentPython() {
		// https://api.haxe.org/java/util/regex/Pattern.html
		// https://api.haxe.org/python/lib/Regex.html
		final s = "&#233;".htmlDecode();
		Assert.equals("é", s); 
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);

		var re = Re.compile("\\w");
		Assert.isNull(Re.match(re, ";"));
		var toto = Re.match(re, s);
		trace(toto);
		trace(toto.group());

		Assert.notNull(Re.match(Re.compile("[^\\W\\d_]", Re.UNICODE), s));

	}
	#end
	#if js
	function testBasicThing1AccentJs() {
		// https://api.haxe.org/js/lib/RegExp.html
		var r = new RegExp("\\p{Letter}", "u");
		final s = "&#233;".htmlDecode();
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);

		Assert.isTrue(r.test(s), "Not a letter");

	}
	#else
	function testBasicThing1Accent() {
		var r1 = new EReg("\\w", "i");
		#if java
		var r2 = new EReg("\\p{L}", "u");
		#end
		final s = "&#233;".htmlDecode();
		Assert.equals("é", s); 
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);

		Assert.isTrue(r1.match(s), "Not a letter");
		#if java
		Assert.isTrue(r2.match(s), "Not a letter");
		#end
	}
	#end
	

}
