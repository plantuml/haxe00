package a00;

import com.plantuml.api.v1.Plantuml;
import utest.Assert;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class A00Test extends AbstractTest {
	function testExecute() {
		// final path = getPath();
		// trace('p1=$path');
		// Assert.equals("test/a00/A00Test.hx", path);
		// final diag1 = foo();
		// trace(diag1);
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
		trace(p.getInternalText());
		final svg = p.getSvg();
		trace(svg);
		// var data = File.getContent(path);
		// Sys.println(data);
		// Assert.isTrue(false);
	}
	/*
			@Test
		public void testExecute() throws IOException, InterruptedException {
			final List<GeneratedImage> r = javaFileReader().getGeneratedImages();
			AssertJUnit.assertEquals(1, r.size());
			AssertJUnit.assertTrue("no file", r.get(0).getPngFile().exists());
			assertImage(r.get(0));
	}*/
}
