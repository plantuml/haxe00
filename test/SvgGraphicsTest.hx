import hx.strings.StringBuilder;
import com.plantuml.api.v1.*;
import com.plantuml.command.BlocLines;
import com.plantuml.command.CommandControl;
import com.plantuml.command.regex.RegexLeaf;
import com.plantuml.mindmap.CommandMindMapDirection;
import com.plantuml.mindmap.MindMapDiagramFactory;
import com.plantuml.mindmap.Stripe;
import com.plantuml.svg.SvgGraphics;
import com.plantuml.ugraphic.UGraphicSvg;
import haxe.ds.BalancedTree;
import utest.*;
import utest.Runner;
import utest.ui.Report;

class SvgGraphicsTest extends utest.Test {
	function orderMe(s:String):String {
		final tree:BalancedTree<String, Int> = new BalancedTree();
		for (i in 0...s.length) {
			var c = s.charAt(i);
			if (c == " ")
				continue;
			var cpt = tree.get(c);
			if (cpt == null)
				tree.set(c, 1);
			else
				tree.set(c, cpt + 1);
		}
		var sb:StringBuilder = new StringBuilder();
		for (ent in tree.keyValueIterator())
			for (i in 0...ent.value)
				sb.add(ent.key);

		return sb.toString();
	}

	function testBasicThing0() {
		var s = orderMe("azertyzz");
		Assert.equals("aertyzzz", s);
	}

	function xtestBasicThing1() {
		final svg = new SvgGraphics();
		final result = svg.toSvg();
		trace(result);
		var exp = '<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" version="1.1"><defs/><g/></svg>';
		// Assert.equals(orderMe(exp), orderMe(result));
	}

	function xtestBasicThing2() {
		final svg = new SvgGraphics();
		svg.text("Hello World", 10, 10, "", 14, "", "plain", "", 100.0, [], "white");
		final result = svg.toSvg();
		trace(result);
		var exp = '<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" version="1.1"><defs/><g><text y="10" x="10" font-size="14"><![CDATA[Hello World]]></text></g></svg>';
		// Assert.equals(orderMe(exp), orderMe(result));
	}
}
