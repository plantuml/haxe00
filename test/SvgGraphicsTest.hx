import com.plantuml.svg.SvgGraphics;

using com.plantuml.utils.StartUtils;

import haxe.ds.BalancedTree;
import hx.strings.StringBuilder;
import utest.*;

class SvgGraphicsTest extends utest.Test {
	function testBasicThing0() {
		var s = "azertyzz".orderMe();
		Assert.equals("aertyzzz", s);
		Assert.equals("f1241e2bfe0a0ee338e9d566d2368cd7d71f6146", s.sha1());
	}

	function testBasicThing1() {
		final svg = new SvgGraphics();
		final result = svg.toSvg();
		Assert.equals("d5f0f1a1135055305a43103b2e6f534d2e1751be", result.orderMe().sha1());
	}

	function testBasicThing2() {
		final svg = new SvgGraphics();
		svg.text("Hello World", 10, 10, "", 14, "", "plain", "", 100.0, [], "white");
		final result = svg.toSvg();
		Assert.equals("3b541638c4a78068387ac21d74365a195cd21848", result.orderMe().sha1());
	}
}
