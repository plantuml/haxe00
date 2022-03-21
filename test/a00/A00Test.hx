package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A00Test extends AbstractTest {
	function testExecute() {
		final diag2 = "
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
		final p = new Plantuml();
		p.addLines(diag2);
		final svg = p.getSvg();
		Assert.isTrue(svg.length > 0);
		Assert.equals("047b2793566ee7772ed3c6462dd7dd5cc80bb027", svg.orderMe().sha1());
	}
}
