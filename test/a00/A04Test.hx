package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A04Test extends AbstractTest {
	function testExecute() {
		final diag = "
		@startmindmap
		* Debian
		**: This is ubuntu
		on several
		lines
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
		Assert.equals("d519ff5a30fec9b7da4ac48612df603a9a9902e8", sha1);
	}
}
