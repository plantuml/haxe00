import a00.*;
import utest.*;
import utest.Runner;
import utest.ui.Report;
import com.plantuml.command.regex.*;
import com.plantuml.api.v1.*;

class MainTest {
	static function main() {
		trace("hello");
		// the long way
		var runner = new Runner();
/* 		runner.addCase(new A00Test());
		runner.addCase(new A01Test());
		runner.addCase(new MinMapDiagramTest());
		runner.addCase(new SvgGraphicsTest());
		runner.addCase(new TestCase1());
		runner.addCase(new CommandMindMapDirectionTest());
		runner.addCase(new CommandMindMapOrgmodeTest());
		runner.addCase(new StripeFrontierTest());
		runner.addCase(new StripeTest());
 */		runner.addCase(new UnicodeTest());
 		runner.addCase(new UnicodeRegexTest());
 

		Report.create(runner);
		runner.run();
	}
}
