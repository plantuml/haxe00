package com.plantuml.regex;

import utest.Assert;

class MyPatternTest extends utest.Test {
	function testBasicThing1() {
		final s = "^([a-z]*)(\\d*)$";
		final p = MyPattern.cmpile(s);

		final m = p.matcher("abc123");
		Assert.equals("abc", m.group(1));
		Assert.equals("123", m.group(2));
	}
}
