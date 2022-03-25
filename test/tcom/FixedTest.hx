package tcom;

using com.plantuml.math.Constant;

import haxe.exceptions.NotImplementedException;
import com.plantuml.utils.AbstractEnumTools;
import utest.*;

using hx.strings.Strings;

abstract Fixed(Int) {
	private function new(value:Int) {
		this = value;
	}

	@:from
	static public function fromInt(i:Int) {
		return new Fixed(i * 1000);
	}

	@:from
	static public function fromArray(array:Array<Int>) {
		if (array.length != 2)
			throw new NotImplementedException();
		final dec = array[1];
		if (dec >= 1000 || dec < 0)
			throw new NotImplementedException();
		if (dec < 10)
			return new Fixed(array[0] * 1000 + 100 * dec);
		if (dec < 100)
			return new Fixed(array[0] * 1000 + 10 * dec);
		return new Fixed(array[0] * 1000 + dec);
	}

	private /*inline*/ function toIntValue():Int {
		return this;
	}

	@:op(A + B) private static /*inline*/ function add(a:Fixed, b:Fixed):Fixed {
		return new Fixed(a.toIntValue() + b.toIntValue());
	}

	@:op(A - B) private static /*inline*/ function sub(a:Fixed, b:Fixed):Fixed {
		return new Fixed(a.toIntValue() - b.toIntValue());
	}

	@:op(A * B) private static /*inline*/ function mul(a:Fixed, b:Fixed):Fixed {
		return new Fixed(divBy1000(a.toIntValue() * b.toIntValue()));
	}

	public static /*inline*/ function divBy1000(v:Int):Int {
		return Std.int(v / 1000);
	}

	public static /*inline*/ function divBy10(v:Int):Int {
		return Std.int(v / 10);
	}

	public function toString() {
		final s:String = Std.string(this);
		return s.substring(0, s.length - 3) + "." + s.substring(s.length - 3);
	}
}

class FixedTest extends utest.Test {
	function testMinMax() {
		trace("Ints.MIN = " + Ints.MIN);
		trace("Ints.MAX = " + Ints.MAX);

		Assert.isTrue(Ints.MAX > Ints.MIN);

		Assert.equals(57, Fixed.divBy1000(57000));
		Assert.equals(57, Fixed.divBy1000(57900));
		Assert.equals(57, Fixed.divBy1000(57999));
		Assert.equals(58, Fixed.divBy1000(58000));
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
