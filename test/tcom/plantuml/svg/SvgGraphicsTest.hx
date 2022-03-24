package tcom.plantuml.svg;

import com.plantuml.svg.SvgGraphics;
import utest.*;

using com.plantuml.utils.StartUtils;

class SvgGraphicsTest extends utest.Test {
	function testBasicThing0() {
		var s = "azertyzz".orderMe();
		Assert.equals("a(1)e(1)r(1)t(1)y(1)z(3)", s);
		Assert.equals("13ce5723ce8efb4bdd4930c4b4e3ec4ae912034b", s.sha1());
	}

	function testBasicThing1() {
		final svg = new SvgGraphics();
		final result = svg.toSvg();
		Assert.equals("adf7f36581e997bf6f126b2900a5555608cde5bd", result.orderMe().sha1());
	}

	function testBasicThing2() {
		final svg = new SvgGraphics();
		svg.text("Hello World", 10, 10, "", 14, "", "plain", "", 100.0, [], "white");
		final result = svg.toSvg();
		Assert.equals("9ce927ac1a41410139fe3789e3226ead4bd7ff1c", result.orderMe().sha1());
	}
}
