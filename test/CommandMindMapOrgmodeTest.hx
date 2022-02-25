import com.plantuml.command.CommandControl;
import com.plantuml.command.BlocLines;
import com.plantuml.mindmap.*;
import utest.*;
import utest.Runner;
import utest.ui.Report;
import com.plantuml.command.regex.RegexLeaf;
import com.plantuml.api.v1.*;

class CommandMindMapOrgmodeTest extends utest.Test {
	function testPattern() {
		var cmd = new CommandMindMapOrgmode();
		var p = cmd.getPattern();
		Assert.equals("^([ \t]*[*]+)(?:\\[(#\\w+)\\])?(_)?[\\s\u00A0]+([^\\s\u00A0].*)$", p);
	}

	function testBasicThing1() {
		var cmd = new CommandMindMapOrgmode();
		var lines = new BlocLines(["* toto1"]);
		Assert.equals(CommandControl.OK, cmd.isValid(lines));
	}
}
