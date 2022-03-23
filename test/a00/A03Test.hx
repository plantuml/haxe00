package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A03Test extends AbstractTest {
	function testExecute() {
		final diag = "
		@startmindmap
		* Debian
		**: This is ubuntu
		on several
		lines;
		*** Linux Mint
		*** Kubuntu
		*** Lubuntu
		*** KDE Neon
		** LMDE
		** SolydXK
		** SteamOS
		** Raspbian with a very long name
		@endmindmap		";
		final sha1 = exportSvgAndCheck(diag);
		Assert.equals("37cfe2e351ce2cd2cbe680bfb48f4f457f75332a", sha1);
	}
}
