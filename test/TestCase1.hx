import utest.*;
import utest.Runner;
import utest.ui.Report;
import com.plantuml.command.regex.*;
import com.plantuml.api.v1.*;

class TestCase1 extends utest.Test {
	function testAz() {
		final az = new RegexLeaf(1, "([a-z]+)", "name");
		Assert.isTrue(az.match("lapin"));
		Assert.isFalse(az.match("123"));
	}

	function testNumber() {
		final az = new RegexLeaf(1, "([0-9]+)", "name");
		Assert.isFalse(az.match("lapin"));
		Assert.isTrue(az.match("123"));
	}

	function test123lapin() {
		var r = new RegexLeaf(2, "^cmd ([0-9]+) ([a-z]+)$");
		trace(r.match("cmd123lapin"));
		trace(r.match("cmd 123 lapin"));
		final array = r.matchArray("cmd 123 lapin");
		Assert.notNull(array);
		Assert.equals(2, array.length);
		Assert.equals("123", array[0]);
		Assert.equals("lapin", array[1]);

		final array = r.matchArray("cmd123lapin");
		Assert.isNull(array);
	}

	function testCmd1() {
		var start = new RegexLeaf(0, "^");
		var cmd = new RegexLeaf(1, "(cmd)", "COMMAND");
		var spaces = new RegexLeaf(0, "\\s*");
		var number = new RegexLeaf(1, "([0-9]+)", "NUMBER");
		var az = new RegexLeaf(1, "([a-z]+)", "AZ");
		var end = new RegexLeaf(0, "$");
		var r = new RegexConcat([start, cmd, spaces, number, spaces, az, end]);
		Assert.isTrue(r.match("cmd 123 lapin"));
	}

	function testCmd2() {
		var start = new RegexLeaf(0, "^");
		var cmd = new RegexLeaf(1, "(cmd)", "COMMAND");
		var spaces = new RegexLeaf(0, "\\s*");
		var number = new RegexLeaf(1, "([0-9]+)", "NUMBER");
		var az = new RegexLeaf(1, "([a-z]+)", "AZ");
		var end = new RegexLeaf(0, "$");
		var r = new RegexConcat([start, cmd, spaces, number, spaces, az, end]);
		trace(r.match("cmd 123 lapin"));
		var res = r.matcher("cmd 123 lapin");
		Assert.equals("123", res.get("NUMBER"));
		Assert.equals("cmd", res.get("COMMAND"));
		Assert.equals("lapin", res.get("AZ"));
	}

	function testCmd3() {
		var start = new RegexLeaf(0, "^");
		var cmd = new RegexOptional(new RegexLeaf(1, "(cmd)", "COMMAND"));
		var spaces = new RegexLeaf(0, "\\s*");
		var number = new RegexLeaf(1, "([0-9]+)", "NUMBER");
		var az = new RegexLeaf(1, "([a-z]+)", "AZ");
		var end = new RegexLeaf(0, "$");
		var r = new RegexConcat([start, cmd, spaces, number, spaces, az, end]);
		trace(r.match("cmd 123 lapin"));
		var res = r.matcher("cmd 123 lapin");
		Assert.equals("123", res.get("NUMBER"));
		Assert.equals("cmd", res.get("COMMAND"));
		Assert.equals("lapin", res.get("AZ"));
		var res = r.matcher("123 lapin");
		Assert.equals("123", res.get("NUMBER"));
		Assert.isNull(res.get("COMMAND"));
		Assert.equals("lapin", res.get("AZ"));
	}
}
