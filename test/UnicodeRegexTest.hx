import utest.*;
#if js
import js.lib.RegExp;
#end
#if python
import python.lib.Re;
#end
#if java
import java.util.regex.Pattern;
#end

using hx.strings.Strings;

class UnicodeRegexTest extends utest.Test {
	function testBasicThing1() {
		var r = new EReg("\\w", "i");
		Assert.isTrue(r.match(getLetter()));
	}

	#if python
	function testBasicThing1AccentPython() {
		// https://api.haxe.org/python/lib/Regex.html

		final onlyLetter = Re.compile("[^\\W\\d_]", Re.UNICODE);
		final onlyDigit = Re.compile("[\\d]", Re.UNICODE);

		Assert.notNull(Re.match(onlyLetter, getLetterAccent()));
		Assert.isNull(Re.match(onlyDigit, getLetterAccent()));

		Assert.isNull(Re.match(onlyLetter, getNumber()));
		Assert.notNull(Re.match(onlyDigit, getNumber()));
	}
	#end

	#if java
	function testBasicThing1AccentJava() {
		// https://api.haxe.org/java/util/regex/Pattern.html
		var onlyDigit = Pattern.compile("\\d");
		Assert.notNull(onlyDigit);
	}
	#end

	#if js
	function testBasicThing1AccentJs() {
		// https://api.haxe.org/js/lib/RegExp.html
		var onlyLetter = new RegExp("\\p{Letter}", "u");
		var onlyDigit = new RegExp("\\d", "u");

		Assert.isTrue(onlyLetter.test(getLetterAccent()));
		Assert.isFalse(onlyDigit.test(getLetterAccent()));

		Assert.isFalse(onlyLetter.test(getNumber()));
		Assert.isTrue(onlyDigit.test(getNumber()));
	}
	#else
	function testBasicThing1Accent() {
		var r1 = new EReg("\\w", "i");
		#if java
		var r2 = new EReg("\\p{L}", "u");
		#end

		Assert.isTrue(r1.match(getLetterAccent()), "Not a letter");
		#if java
		Assert.isTrue(r2.match(getLetterAccent()), "Not a letter");
		#end
	}
	#end

	function getLetter() {
		final s = "a";
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		return s;
	}

	function getNumber() {
		final s = "2";
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		return s;
	}

	function getLetterAccent() {
		final s = "&#233;".htmlDecode();
		#if !js
		Assert.equals("é", s);
		#end
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		return s;
	}
}
