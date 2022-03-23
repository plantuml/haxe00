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
		Assert.equals("cb91212d4b835bef48f308bbbea1af30ec123f7f", sha1);
	}
}
