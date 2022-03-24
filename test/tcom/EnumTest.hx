package tcom;

import com.plantuml.utils.AbstractEnumTools;
import utest.*;

using hx.strings.Strings;

@:enum
abstract HttpStatus1(Int) {
	var NotFound1 = 404;
	var MethodNotAllowed1 = 405;

	public function doit() {
		trace('je suis doit $this');
	}
}

@:enum
abstract HttpStatus2(String) {
	var NotFound2 = "string404";
	var MethodNotAllowed2 = "string405";

	public function doit() {
		trace('I am in $this');
	}
}

class Toto {
	public static macro function trace_build_age_with_reification() {
		var buildTime = Math.floor(Date.now().getTime() / 1000);

		var e = macro {
			var runTime = Math.floor(Date.now().getTime() / 1000);
			var age = runTime - $v{buildTime};
			trace("Right now it's " + runTime + ", and this build is " + age + " seconds old");
		};

		return e;
	}
}

class EnumTest extends utest.Test {
	function testBasicThing1() {
		final v = NotFound1;
		Assert.equals(NotFound1, v);
		trace('v=$v');
		v.doit();

		var values = AbstractEnumTools.getValues(HttpStatus1);
		trace(values);
		Toto.trace_build_age_with_reification();
	}

	function testBasicThing2() {
		final v2 = NotFound2;
		Assert.equals(NotFound2, v2);
		trace('v=$v2');
		v2.doit();

		var values = AbstractEnumTools.getValues(HttpStatus2);
		trace(values);
		Toto.trace_build_age_with_reification();
	}
}
