using hx.strings.Strings;
using com.plantuml.utils.StartUtils;

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

	function foo() {
		var data = File.getContent(getPath());
		var headerToRemove = null;
		for (s in data.splitLines()) {
			final tmp = s.beforeStartUml();
			if (tmp != null)
				headerToRemove = tmp;
			s = s.removeHeader(headerToRemove);
			Sys.println(s);
		}
	}
}
// http://www.unexpected-vortices.com/haxe/brief-tutorial.html
// http://thx-lib.org/api/thx/Set.html