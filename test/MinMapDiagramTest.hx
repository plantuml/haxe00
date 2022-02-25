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

class MinMapDiagramTest extends utest.Test {
	function testBasicThing1() {
		var lines = new BlocLines([
			"* WORLD", "** America", "*** Canada", "*** USA", "** Europe", "*** UK ", "*** France", "*** Germany", "*** Italy", "** Africa"
		]);

		var factory = new MindMapDiagramFactory();

		var diagram = factory.createSystem(lines);
		Assert.notNull(diagram);

		var svg:UGraphicSvg = UGraphicSvg.create();
		diagram.exportDiagramNow(svg);
		var s = svg.getSvg();

		#if js
		#else
		sys.io.File.saveContent('MinMapDiagramTest.svg', s);
		#end
	}
}
