package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A00Test extends AbstractTest {
	function testExecute() {
		final diag = "
			@startmindmap
			* Debian
			** Ubuntu
			*** Linux Mint
			*** Kubuntu
			*** Lubuntu
			*** KDE Neon
			** LMDE
			** SolydXK
			** SteamOS
			** Raspbian with a very long name
			@endmindmap
		";
		final sha1 = exportSvgAndCheck(diag);
		Assert.equals("202371649d0d064a3054fc2fc453c3ed96724192", sha1);
	}
}
