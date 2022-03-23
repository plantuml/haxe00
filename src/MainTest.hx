import a00.*;
import com.plantuml.command.regex.*;
import com.plantuml.mindmap.*;
import com.plantuml.regex.*;
import com.plantuml.svg.*;
import utest.Runner;
import utest.ui.Report;

class MainTest {
	static function main() {
		trace("hello");
		// the long way
		var runner = new Runner();
		runner.addCases('a00');
		runner.addCase(new MinMapDiagramTest());
		runner.addCase(new SvgGraphicsTest());
		runner.addCase(new RegexLeafTest());
		runner.addCase(new CommandMindMapDirectionTest());
		runner.addCase(new CommandMindMapOrgmodeTest());
		runner.addCase(new StripeFrontierTest());
		runner.addCase(new StripeTest());
		runner.addCase(new UnicodeTest());
		runner.addCase(new UnicodeRegexTest());
		runner.addCase(new MyPatternTest());

		Report.create(runner);
		runner.run();
	}
}
