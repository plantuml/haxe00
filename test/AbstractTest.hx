import com.plantuml.command.BlocLines;
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
		final name = Type.getClassName(Type.getClass(this));
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

	function exportSvgAndCheck(diag2:String):String {
		var bl = new BlocLines();
		bl.addLines(diag2);
		bl = bl.findStartSomething();

		final p = new Plantuml();
		p.addLinesArray(bl.getLines());

		final svg = p.getSvg();
		Assert.isTrue(svg.length > 0);

		final target = getTarget();
		final path = getPath().replaceFirst(".hx", '-$target.svg');

		#if !js
		sys.io.File.saveContent(path, svg);
		#end
		return svg.orderMe().sha1();
	}
} // http://www.unexpected-vortices.com/haxe/brief-tutorial.html
// http://thx-lib.org/api/thx/Set.html
