package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A05Test extends AbstractTest {
	function testExecute() {
		final diag = "
		@startmindmap
		+ level0
		++ level1a
		++ level1b
		@endmindmap
		";
		final sha1 = exportSvgAndGetSha1(diag);
		final ok = Assert.equals("x", sha1);
		if (!ok)
			errorInSha1(sha1);
	}
}
