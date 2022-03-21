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
		Assert.equals("047b2793566ee7772ed3c6462dd7dd5cc80bb027", sha1);
		
	}
}
