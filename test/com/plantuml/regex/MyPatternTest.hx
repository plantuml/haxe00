package com.plantuml.regex;

import utest.Assert;

class MyPatternTest extends utest.Test {
	function testBasicThing1() {
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
