import com.plantuml.command.CommandControl;
import com.plantuml.command.BlocLines;
import com.plantuml.mindmap.CommandMindMapDirection;
import utest.*;
import utest.Runner;
import utest.ui.Report;
import com.plantuml.command.regex.RegexLeaf;
import com.plantuml.api.v1.*;

class CommandMindMapDirectionTest extends utest.Test {
	function testBasicThing1() {
		var cmd = new CommandMindMapDirection();
		var lines = new BlocLines(["toto1", "toto2"]);
		Assert.equals(CommandControl.NOT_OK, cmd.isValid(lines));
	}
}
