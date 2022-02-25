import com.plantuml.mindmap.StripeFrontier;
import haxe.ds.BalancedTree;
import com.plantuml.mindmap.Stripe;
import com.plantuml.ugraphic.UGraphicSvg;
import com.plantuml.mindmap.MindMapDiagramFactory;
import com.plantuml.command.CommandControl;
import com.plantuml.command.BlocLines;
import com.plantuml.mindmap.CommandMindMapDirection;
import utest.*;
import utest.Runner;
import utest.ui.Report;
import com.plantuml.command.regex.RegexLeaf;
import com.plantuml.api.v1.*;

class StripeFrontierTest extends utest.Test {
	function testBasicThing1() {
		var cut = new StripeFrontier();
		Assert.isTrue(cut.isEmpty());
	}
}
