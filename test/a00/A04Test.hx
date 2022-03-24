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
		Assert.equals("f1791f494f48f1cbde72b79f1018a41536c6cff5", sha1);
	}
}
