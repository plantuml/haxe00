package tcom;

import hx.strings.StringBuilder;
import hx.strings.Char;
import utest.Assert;

using hx.strings.Strings;

class CharSizeTest extends utest.Test {
	function testSimple() {
		final s = "A".code;
		final ascii = "A".charCodeAt(0);
		Assert.equals(65, s);
		Assert.equals(65, ascii);
	}

	function testSimple2() {
		final c:Char = 65.toChar();
		Assert.equals("A", "" + c);
	}

	function testUnicode() {
		final ascii = getLetterAccent().charCodeAt(0);
		Assert.equals(12480, ascii);
	}

	function testGetLongString() {
		Assert.equals("BBB", getLongString(66, 3));
	}

	function getLetterAccent() {
		final s = "&#12480;".htmlDecode();
		#if !js
		Assert.equals("ダ", s);
		#end
		Assert.equals("&#12480;", s.htmlEncode());
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		Assert.equals(s, "" + 12480.toChar());
		return s;
	}

	function getLongString(codepoint:Int, size:Int) {
		final sb = new StringBuilder();
		for (i in 0...size)
			sb.add("" + codepoint.toChar());
		return sb.toString();
	}
}
