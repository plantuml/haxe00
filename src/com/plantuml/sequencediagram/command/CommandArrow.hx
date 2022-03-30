package com.plantuml.sequencediagram.command;

import utest.Assert;

class CommandArrow extends SingleLineCommand<SequenceDiagram> {
	static final ANCHOR = "(\\{([%%W]+)\\}[%s]+)?";

	public function new() {
		_init([
			RegexLeaf.start(), //
			new RegexLeaf(1, "(&[%s]*)?", "PARALLEL"), //
			new RegexLeaf(2, ANCHOR, "ANCHOR"), //
			// new RegexOr("PART1", //
			new RegexOr("PART1", [
				new RegexLeaf(1, "([%W.@]+)", "PART1CODE") //
					//         new RegexLeaf("PART1LONG", "[%g]([^%g]+)[%g]"), //
					//         new RegexLeaf("PART1LONGCODE", "[%g]([^%g]+)[%g][%s]*as[%s]+([%pLN_.@]+)"), //
					//         new RegexLeaf("PART1CODELONG", "([%pLN_.@]+)[%s]+as[%s]*[%g]([^%g]+)[%g]")), //
			]), //
			// new RegexLeaf("PART1ANCHOR", ANCHOR), //
			RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("ARROW_DRESSING1",
			//         "([%s][ox]|(?:[%s][ox])?<<?_?|(?:[%s][ox])?//?|(?:[%s][ox])?\\\\\\\\?)?"), //
			// new RegexOr(new RegexConcat( //
			new RegexLeaf(1, "(-+)", "ARROW_BODYA1"), //
			//         new RegexLeaf("ARROW_STYLE1", getColorOrStylePattern()), //
			//         new RegexLeaf("ARROW_BODYB1", "(-*)")), //
			//         new RegexConcat( //
			//                 new RegexLeaf("ARROW_BODYA2", "(-*)"), //
			//                 new RegexLeaf("ARROW_STYLE2", getColorOrStylePattern()), //
			//                 new RegexLeaf("ARROW_BODYB2", "(-+)"))), //
			new RegexLeaf(1, "(_?>>?(?:[ox][%s])?|//?(?:[ox][%s])?|\\\\\\\\?(?:[ox][%s])?|[ox][%s])?", "ARROW_DRESSING2"), //
			RegexLeaf.spaceZeroOrMore(), //
			// new RegexOr("PART2", //
			new RegexLeaf(1, "([%W.@]+)", "PART2CODE"), //
			//         new RegexLeaf("PART2LONG", "[%g]([^%g]+)[%g]"), //
			//         new RegexLeaf("PART2LONGCODE", "[%g]([^%g]+)[%g][%s]*as[%s]+([%pLN_.@]+)"), //
			//         new RegexLeaf("PART2CODELONG", "([%pLN_.@]+)[%s]+as[%s]*[%g]([^%g]+)[%g]")), //
			// new RegexLeaf("MULTICAST", "((?:\\s&\\s[%pLN_.@]+)*)"), //
			// new RegexLeaf("PART2ANCHOR", ANCHOR), //
			// RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("ACTIVATION", "(?:(\\+\\+|\\*\\*|!!|--|--\\+\\+|\\+\\+--)?)"), //
			// RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("LIFECOLOR", "(?:(#\\w+)?)"), //
			// RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("STEREOTYPE", "(\\<\\<.*\\>\\>)?"), //
			// RegexLeaf.spaceZeroOrMore(), //
			// new RegexLeaf("URL", "(" + UrlBuilder.getRegexp() + ")?"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(?::[%s]*(.*))?", "MESSAGE"), //
			// RegexLeaf.end()).protectSize(2000);
			RegexLeaf.end()
		]);
	}

	public function executeArg(diagram:SequenceDiagram, lines:BlocLines, map:Map<String, String>):CommandExecutionResult {
		trace('map=' + map.removeNullValue());
		Assert.equals("{ARROW_BODYA1=-, ARROW_DRESSING2=>, MESSAGE=hello, PART1CODE=Alice, PART2CODE=Bob}", map.removeNullValue().toString());
		throw new haxe.exceptions.NotImplementedException();
	}
}
