package tcom;

import com.plantuml.math.Fixed;

using com.plantuml.math.Constant;

import haxe.exceptions.NotImplementedException;
import com.plantuml.utils.AbstractEnumTools;
import utest.*;

using hx.strings.Strings;

class FixedTest extends utest.Test {
	function testMinMax() {
		trace("Ints.MIN = " + Ints.MIN);
		trace("Ints.MAX = " + Ints.MAX);

		Assert.isTrue(Ints.MAX > Ints.MIN);
	}

	function testBasicThing1() {
		var f41:Fixed = 41;
		Assert.equals("41.000", "" + f41);
		var f42:Fixed = 42;
		Assert.equals("42.000", "" + f42);
		var f83 = f41 + f42;
		Assert.equals("83.000", "" + f83);
		var diff = f41 - f42;
		Assert.equals("-1.000", "" + diff);
	}

	function testDecimal() {
		var a:Fixed = [3, 4];
		Assert.equals("3.400", "" + a);
		var a:Fixed = [3, 41];
		Assert.equals("3.410", "" + a);
		var a:Fixed = [3, 413];
		Assert.equals("3.413", "" + a);
	}

	function testMult() {
		var a:Fixed = [3, 4];
		Assert.equals("3.400", "" + a);
		var b:Fixed = [7, 41];
		Assert.equals("7.410", "" + b);

		var c = a * b;
		Assert.equals("25.194", "" + c);
	}

	function testMultBig() {
		var a:Fixed = [1003, 4];
		var b:Fixed = [2037, 41];
		var c = a * b;
		Assert.equals("2044337.194", "" + c);
	}

	function testMultBig2() {
		var a:Fixed = [21003, 425];
		var b:Fixed = [42037, 941];
		var c = a * b;
		Assert.equals("882940740.947", "" + c);
	}
}
