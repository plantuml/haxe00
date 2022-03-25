package tcom;

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

	private /*inline*/ function toIntValue():Int {
		return this;
	}

	@:op(A + B) private static /*inline*/ function add(a:Fixed, b:Fixed):Fixed {
		return new Fixed(a.toIntValue() + b.toIntValue());
	}

	@:op(A - B) private static /*inline*/ function sub(a:Fixed, b:Fixed):Fixed {
		return new Fixed(a.toIntValue() - b.toIntValue());
	}

	public function toString() {
		final s:String = Std.string(this);
		return s.substring(0, s.length - 3) + "." + s.substring(s.length - 3);
	}
}

class FixedTest extends utest.Test {
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
}
