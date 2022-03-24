package tcom;

import utest.Assert;

using hx.strings.Strings;

class CharSizeTest extends utest.Test {
	function testSimple() {
		final s = "A".code;
		final ascii = "A".charCodeAt(0);
		Assert.equals(65, s);
		Assert.equals(65, ascii);
	}

	function testUnicode() {
		final ascii = getLetterAccent().charCodeAt(0);
		Assert.equals(12480, ascii);
	}

    function getLetterAccent() {
		final s = "&#12480;".htmlDecode();
		#if !js
		Assert.equals("ダ", s);
		#end
		Assert.equals("&#12480;", s.htmlEncode());
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		return s;
	}

}
