import utest.*;

#if js
import js.lib.RegExp;
#end
using hx.strings.Strings;

class UnicodeRegexTest extends utest.Test {
	function testBasicThing1() {
		var r = new EReg("\\w", "i");
		final s = "a";
		Assert.isTrue(r.match(s));
	}
	
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
