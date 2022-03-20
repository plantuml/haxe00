using hx.strings.Strings;

import utest.Test;
import utest.utils.Print;
import sys.io.File;
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
