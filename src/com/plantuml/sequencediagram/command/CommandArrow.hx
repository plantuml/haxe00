package com.plantuml.sequencediagram.command;

import com.plantuml.descdiagram.command.CommandLinkElement;
import utest.Assert;

class CommandArrow extends SingleLineCommand<SequenceDiagram> {
	static final ANCHOR = "(\\{([%W]+)\\}[%s]+)?";

	public static function getColorOrStylePattern() {
		return "(?:\\[(" + CommandLinkElement.LINE_STYLE + ")\\])?";
	}

	public function new() {
		_init([
			RegexLeaf.start(), //
			new RegexLeaf(1, "(&[%s]*)?", "PARALLEL"), //
			new RegexLeaf(2, ANCHOR, "ANCHOR"), //
			new RegexOr("PART1", [
				new RegexLeaf(1, "([%W.@]+)", "PART1CODE"), //
				new RegexLeaf(1, "[%g]([^%g]+)[%g]", "PART1LONG"),
				new RegexLeaf(2, "[%g]([^%g]+)[%g][%s]*as[%s]+([%W.@]+)", "PART1LONGCODE"), //
				new RegexLeaf(2, "([%W.@]+)[%s]+as[%s]*[%g]([^%g]+)[%g]", "PART1CODELONG")
			]),
			new RegexLeaf(2, ANCHOR, "PART1ANCHOR"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "([%s][ox]|(?:[%s][ox])?<<?_?|(?:[%s][ox])?//?|(?:[%s][ox])?\\\\\\\\?)?", "ARROW_DRESSING1"), //
			// new RegexOr(
			new RegexConcat([
				new RegexLeaf(1, "(-+)", "ARROW_BODYA1"), //
				new RegexLeaf(1, getColorOrStylePattern(), "ARROW_STYLE1"), //
				new RegexLeaf(1, "(-*)", "ARROW_BODYB1")
			]), //
			//         new RegexConcat( //
			//                 new RegexLeaf("ARROW_BODYA2", "(-*)"), //
			//                 new RegexLeaf("ARROW_STYLE2", getColorOrStylePattern()), //
			//                 new RegexLeaf("ARROW_BODYB2", "(-+)"))), //
			new RegexLeaf(1, "(_?>>?(?:[ox][%s])?|//?(?:[ox][%s])?|\\\\\\\\?(?:[ox][%s])?|[ox][%s])?", "ARROW_DRESSING2"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexOr("PART2", [
				new RegexLeaf(1, "([%W.@]+)", "PART2CODE"), //
				new RegexLeaf(1, "[%g]([^%g]+)[%g]", "PART2LONG"), //
				new RegexLeaf(2, "[%g]([^%g]+)[%g][%s]*as[%s]+([%W.@]+)", "PART2LONGCODE"), //
				new RegexLeaf(2, "([%W.@]+)[%s]+as[%s]*[%g]([^%g]+)[%g]", "PART2CODELONG")
			]),
			new RegexLeaf(1, "((?:\\s&\\s[%W.@]+)*)", "MULTICAST"), //
			new RegexLeaf(2, ANCHOR, "PART2ANCHOR"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(?:(\\+\\+|\\*\\*|!!|--|--\\+\\+|\\+\\+--)?)", "ACTIVATION"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(?:(#\\w+)?)", "LIFECOLOR"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(\\<\\<.*\\>\\>)?", "STEREOTYPE"), //
			RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("URL", "(" + UrlBuilder.getRegexp() + ")?"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(?::[%s]*(.*))?", "MESSAGE"), //
			// RegexLeaf.end()).protectSize(2000);
			RegexLeaf.end()
		]);
	}

	public function executeArg(diagram:SequenceDiagram, lines:BlocLines, map:Map<String, String>):CommandExecutionResult {
		trace('map=$map');
		trace('map=' + map.removeNullValue());
		Assert.equals("{ARROW_BODYA1=-, ARROW_DRESSING2=>, MESSAGE=hello, PART1=Alice, PART1CODE=Alice, PART2=Bob, PART2CODE=Bob}",
			map.removeNullValue().toString());
		throw new haxe.exceptions.NotImplementedException();
	}
}
