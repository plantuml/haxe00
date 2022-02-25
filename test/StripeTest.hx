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

class StripeTest extends utest.Test {
	function testBasicThing1() {
		var stripe1 = new Stripe(1, 2, 3);
		Assert.equals(1, stripe1.getStart());
		Assert.equals(2, stripe1.getEnd());
		Assert.equals(3, stripe1.getValue());

		var stripe10 = new Stripe(10, 11, 12);
		Assert.equals(10, stripe10.getStart());

		var tree:BalancedTreeStripe = new BalancedTreeStripe();
		tree.add(stripe10);
		Assert.equals("{10->11 (12)=true}", tree.toString());

		tree.add(stripe1);
		Assert.equals("{1->2 (3)=true, 10->11 (12)=true}", tree.toString());

		tree.add(new Stripe(5, 6, 120));
		Assert.equals("{1->2 (3)=true, 5->6 (120)=true, 10->11 (12)=true}", tree.toString());

		for (k in tree.keys())
			trace(k);
	}
}
