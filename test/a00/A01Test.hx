package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A01Test extends AbstractTest {
	function testExecute() {
		final diag = "
			@startmindmap
			* Debianなダイアグラム
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
		Assert.equals("b343e2f4826e91f119c58eca2b2fc976f286c6e1", sha1);
		
	}
}