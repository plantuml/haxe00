package com.plantuml.regex;

using hx.strings.Strings;

import utest.Assert;

class MyPatternTest extends utest.Test {
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
		final s = "&#12480;".htmlDecode();
		#if !js
		Assert.equals("ダ", s);
		#end
		Assert.equals("&#12480;", s.htmlEncode());
		Assert.equals(1, s.length8());
		Assert.equals(1, s.length);
		return s;
	}

	function testL() {
		final s = "^(%%L*)(\\d*)$";
		final p = MyPattern.cmpile(s);

		final m = p.matcher(getLetterAccent() + "abc123");
		Assert.isTrue(m.matches());
		Assert.equals(getLetterAccent() + "abc", m.group(1));
		Assert.equals("123", m.group(2));

		final m2 = p.matcher(";abc123");
		Assert.isFalse(m2.matches());
		Assert.isNull(m2.group(1));
		Assert.isNull(m2.group(2));
	}

	function testBasicThing2() {
		final s = "^([a-z]*)(\\d*)$";
		final p = MyPattern.cmpile(s);

		final m = p.matcher("abc123");
		Assert.isTrue(m.matches());
		Assert.equals("abc", m.group(1));
		Assert.equals("123", m.group(2));

		final m2 = p.matcher(";abc123");
		Assert.isFalse(m2.matches());
		Assert.isNull(m2.group(1));
		Assert.isNull(m2.group(2));
	}
}
