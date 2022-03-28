package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A06Test extends AbstractTest {
	function testExecute() {
		final diag = "
		@startmindmap
		left side
		* count with a very long name
		** 100
		*** 101
		*** 102
		** 200
		@endmindmap
		";

		final sha1 = exportSvgAndGetSha1(diag);
		final ok = Assert.equals("x", sha1);
		if (!ok)
			errorInSha1(sha1);
	}
}
