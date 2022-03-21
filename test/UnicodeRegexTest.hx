
import utest.*;

using hx.strings.Strings;

class UnicodeRegexTest extends utest.Test {
	function testBasicThing1() {
		var r = new EReg("\\w", "i");
		final s = "a";
		Assert.isTrue(r.match(s));
	}
	
	function testBasicThing1Accent() {
		var r = new EReg("\\w", "i");
		final s = "&#233;".htmlDecode();
		#if !js
		Assert.equals("é", s); 
		#end
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);

		Assert.isTrue(r.match(s), "Not a letter");
	}
	

}
