package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A02Test extends AbstractTest {
	function testExecute() {
		final diag = "
			@startmindmap
			ERROR
			@endmindmap
		";
		final sha1 = exportSvgAndGetSha1(diag);
		final ok = Assert.equals("6c48f6d5dbe28d16ee8dbc2a0674dcf793adbccc", sha1);
		if (!ok)
			errorInSha1(sha1);
	}
}
