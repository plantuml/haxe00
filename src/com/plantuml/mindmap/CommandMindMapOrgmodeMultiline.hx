package com.plantuml.mindmap;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

import com.plantuml.command.*;
import com.plantuml.command.CommandControl;
import com.plantuml.command.CommandExecutionResult;
import com.plantuml.command.CommandMultilines2;
import com.plantuml.command.regex.*;
import com.plantuml.command.regex.RegexConcat;
import com.plantuml.core.Diagram;

class CommandMindMapOrgmodeMultiline extends CommandMultilines2 {
	public function new() {
		final start = new RegexConcat([
			RegexLeaf.start(), //
			new RegexLeaf(1, "([*]+)", "TYPE"), //
			new RegexOptional(new RegexLeaf(1, "\\[(#\\w+)\\]", "BACKCOLOR")), //
			new RegexLeaf(1, "(_)?", "SHAPE"), //
			new RegexLeaf(0, ":"), //
			new RegexLeaf(1, "(.*)", "DATA"), //
			RegexLeaf.end()
		]);

		final end = new RegexConcat([
			RegexLeaf.start(), //
			new RegexLeaf(1, "(.*)", "DATA"), //
			new RegexLeaf(0, ";"), //
			new RegexOptional(new RegexLeaf(1, "[%s]*\\<\\<(.+)\\>\\>", "STEREO")), //
			RegexLeaf.end()
		]);

		super(start, end);
	}

	public function execute(diagram_:Diagram, lines:BlocLines):CommandExecutionResult {
		final diagram:MindMapDiagram = cast(diagram_, MindMapDiagram);
		final line0 = getStartingPattern().matcher(lines.getFirst().getTrimmed().getString());
		trace('lines=$lines');
		trace('line0=$line0');
		//
		//		final List<String> lineLast = StringUtils.getSplit(MyPattern.cmpile(getPatternEnd()),
		//				lines.getLast().getString());
		//		lines = lines.removeStartingAndEnding(line0.get("DATA", 0), 1);
		//
		//		final String stereotype = lineLast.get(1);
		//		if (stereotype != null) {
		//			lines = lines.overrideLastLine(lineLast.get(0));
		//		}
		//
		//		final String type = line0.get("TYPE", 0);
		//		final String stringColor = line0.get("BACKCOLOR", 0);
		//		HColor backColor = null;
		//		if (stringColor != null) {
		//			backColor = diagram.getSkinParam().getIHtmlColorSet().getColor(diagram.getSkinParam().getThemeStyle(),
		//					stringColor);
		//		}
		//
		//		if (stereotype == null) {
		//			return diagram.addIdea(backColor, type.length() - 1, lines.toDisplay(),
		//					IdeaShape.fromDesc(line0.get("SHAPE", 0)));
		//		}
		//		return diagram.addIdea(stereotype, backColor, type.length() - 1, lines.toDisplay(),
		//				IdeaShape.fromDesc(line0.get("SHAPE", 0)));
		throw new haxe.exceptions.NotImplementedException();
	}
}
