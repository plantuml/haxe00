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
		final v = "&#12394;&#12480;&#12452;&#12450;&#12464;&#12521;&#12512;".htmlDecode();
		final diag2 = '
			@startmindmap
			* Debian$v
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
		';
		#if !js
		Assert.equals(diag, diag2);
		#end
		final sha1 = exportSvgAndCheck(diag2);
		Assert.equals("e5dfb2837b5ae6512fe64e7861e2bbf31fe7d2db", sha1);
	}
}
