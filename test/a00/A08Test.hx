package a00;

import com.plantuml.api.v2.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A08Test extends AbstractTest {
	function testExecute() {
		final diag = "
		@startuml
		Alice -> Bob : hello
		@enduml
		";

		final sha1 = exportSvgAndGetSha1(diag);
		// final ok = Assert.equals("x", sha1);
		// if (!ok)
		errorInSha1(sha1);
	}
}
