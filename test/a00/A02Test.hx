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
		final sha1 = exportSvgAndCheck(diag);
		Assert.equals("35dda6e4b6f7e6821df4ff5f8a894ae492e3148b", sha1);
	}
}
