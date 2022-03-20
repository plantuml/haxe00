package a00;

using hx.strings.Strings;

import utest.Test;
import utest.utils.Print;
import sys.io.File;
import utest.Assert;

/*
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
 */
class A00Test extends AbstractTest {
	function testExecute() {

		final path = getPath();
		Sys.println('p1=$path');
		Assert.equals("test/a00/A00Test.hx", path);
		var data = File.getContent(path);
		Sys.println(data);
		Assert.isTrue(false);
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
