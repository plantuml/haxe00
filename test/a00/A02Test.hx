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
		Assert.equals("58afa8a6a954f6481e018e94d51071299a2055ea", sha1);
	}
}
