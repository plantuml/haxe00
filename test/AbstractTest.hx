import com.plantuml.api.v1.Plantuml;

using hx.strings.Strings;
using com.plantuml.utils.StartUtils;

import utest.Test;
import utest.utils.Print;
import utest.Assert;

class AbstractTest extends Test {
	public function new() {
		super();
	}

	function getPath():String {
		final name = Std.string(this);
		final path = "test/" + name.replaceAll(".", "/") + ".hx";
		return path;
	}

	function getTarget():String {
		#if js
		return "js";
		#elseif java
		return "java";
		#elseif python
		return "py";
		#elseif hashlink
		return "hashlink";
		#elseif hl
		return "hl";
		#elseif necko
		return "necko";
		#elseif interp
		return "interp";
		#end
		return "other";
	}

	function exportSvgAndCheck(diag2:String, sha1:String) {
		final p = new Plantuml();
		p.addLines(diag2);
		final svg = p.getSvg();
		Assert.isTrue(svg.length > 0);
		Assert.equals(sha1, svg.orderMe().sha1());

		final target = getTarget();
		final path = getPath().replaceFirst(".hx", '-$target.svg');
		trace(path);
		trace('Je suis la target $target');
		#if !js
		sys.io.File.saveContent(path, svg);
		#end
	}
} // http://www.unexpected-vortices.com/haxe/brief-tutorial.html
// http://thx-lib.org/api/thx/Set.html
