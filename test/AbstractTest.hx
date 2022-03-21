using hx.strings.Strings;
using com.plantuml.utils.StartUtils;

import utest.Test;
import utest.utils.Print;
import utest.Assert;

class AbstractTest extends Test {
	public function new() {
		super();
	}

	function getPath():String {
		final name = Std.string(this);
		final path = "test/" + name.replaceAll(".", "/") + ".hx";
		return path;
	}
}
// http://www.unexpected-vortices.com/haxe/brief-tutorial.html
// http://thx-lib.org/api/thx/Set.html
