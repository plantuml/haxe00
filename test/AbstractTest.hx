import hx.strings.StringBuilder;
import com.plantuml.command.BlocLines;
import com.plantuml.api.v1.Plantuml;

using hx.strings.Strings;
using com.plantuml.utils.StartUtils;

import utest.Test;
import utest.utils.Print;
import utest.Assert;

class AbstractTest extends Test {
	private static var allPaths = [];

	public function new() {
		super();
	}

	function getPath():String {
		final name = Type.getClassName(Type.getClass(this));
		final path = "test/" + name.replaceAll(".", "/") + ".hx";
		return path;
	}

	static function getTarget():String {
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
		final targetHtml = 'all-$target.html';

		#if !js
		sys.io.File.saveContent(path, svg);
		allPaths.push(path);
		trace(allPaths);
		#end
		return svg.orderMe().sha1();
	}

	public static function saveContentStrings() {
		trace("saveContentStrings");
		#if !js
		final target = getTarget();
		final targetHtml = 'all-$target.html';
		trace('targetHtml=$targetHtml');

		final content = [];
		content.push("<html>");
		content.push("<style>");
		content.push("body {");
		content.push("background-color: #f8f8f8;");
		content.push("}");
		content.push("</style>");
		content.push("<body>");
		for (p in allPaths) {
			content.push(p);
			content.push("<p>");
			content.push("<img src=\"" + p + "\">");
			content.push("<hr>");
		}
		content.push("</body>");
		content.push("</html>");

		final sb:StringBuilder = new StringBuilder();
		for (s in content) {
			sb.add(s);
			sb.add("\n");
		}
		sys.io.File.saveContent(targetHtml, sb.toString());
		#end
	}
} // http://www.unexpected-vortices.com/haxe/brief-tutorial.html
// http://thx-lib.org/api/thx/Set.html
