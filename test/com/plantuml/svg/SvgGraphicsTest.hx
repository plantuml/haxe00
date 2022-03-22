package com.plantuml.svg;

import com.plantuml.svg.SvgGraphics;
import utest.*;

using com.plantuml.utils.StartUtils;

class SvgGraphicsTest extends utest.Test {
	function testBasicThing0() {
		var s = "azertyzz".orderMe();
		Assert.equals("sb.toString()", s);
		Assert.equals("b343e2f4826e91f119c58eca2b2fc976f286c6e1", s.sha1());
	}

	function testBasicThing1() {
		final svg = new SvgGraphics();
		final result = svg.toSvg();
		Assert.equals("b343e2f4826e91f119c58eca2b2fc976f286c6e1", result.orderMe().sha1());
	}

	function testBasicThing2() {
		final svg = new SvgGraphics();
		svg.text("Hello World", 10, 10, "", 14, "", "plain", "", 100.0, [], "white");
		final result = svg.toSvg();
		Assert.equals("b343e2f4826e91f119c58eca2b2fc976f286c6e1", result.orderMe().sha1());
	}
}
