package com.plantuml.math;

import haxe.exceptions.NotImplementedException;

using com.plantuml.math.Constant;
using hx.strings.Strings;

abstract Fixed(Int) {
	private function new(value:Int) {
		this = value;
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

	public function toString() {
		final s:String = Std.string(this);
		return s.substring(0, s.length - 3) + "." + s.substring(s.length - 3);
	}
}
