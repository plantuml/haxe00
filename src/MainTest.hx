import tcom.plantuml.regex.MyPatternTest;
import tcom.plantuml.command.regex.*;
import tcom.plantuml.mindmap.*;
import a00.*;
import com.plantuml.command.regex.*;
import com.plantuml.mindmap.*;
import com.plantuml.regex.*;
import com.plantuml.svg.*;
import utest.Runner;
import utest.ui.Report;

class MainTest {
	static function main() {
		var runner = new Runner();
		runner.addCases("a00");
		runner.addCases("tcom");
		// runner.addCase(new A04Test());

		Report.create(runner);
		runner.run();
	}
}
