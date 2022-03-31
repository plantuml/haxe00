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
			new RegexOr([
				new RegexConcat([
					new RegexLeaf(1, "(-+)", "ARROW_BODYA1"), //
					new RegexLeaf(1, getColorOrStylePattern(), "ARROW_STYLE1"), //
					new RegexLeaf(1, "(-*)", "ARROW_BODYB1")
				]), //
				new RegexConcat([
					new RegexLeaf(1, "(-*)", "ARROW_BODYA2"), //
					new RegexLeaf(1, getColorOrStylePattern(), "ARROW_STYLE2"), //
					new RegexLeaf(1, "(-+)", "ARROW_BODYB2")
				])
			]),
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
			new RegexLeaf(UrlBuilder.getRegexpSize() + 1, "(" + UrlBuilder.getRegexp() + ")?", "URL"), //
			RegexLeaf.spaceZeroOrMore(), //
			new RegexLeaf(1, "(?::[%s]*(.*))?", "MESSAGE"), //
			// RegexLeaf.end()).protectSize(2000);
			RegexLeaf.end()
		]);
	}

	private function getOrCreateParticipant(system:SequenceDiagram, arg2:Map<String, String>, n:String):Participant {
		var code;
		var display;
		if (arg2.get(n + "CODE") != null) {
			code = arg2.get(n + "CODE");
			display = Display.getWithNewlines(code);
			//		} else if (arg2.get(n + "LONG", 0) != null) {
			//			code = arg2.get(n + "LONG", 0);
			//			display = Display.getWithNewlines(code);
			//		} else if (arg2.get(n + "LONGCODE", 0) != null) {
			//			display = Display.getWithNewlines(arg2.get(n + "LONGCODE", 0));
			//			code = arg2.get(n + "LONGCODE", 1);
			//		} else if (arg2.get(n + "CODELONG", 0) != null) {
			//			code = arg2.get(n + "CODELONG", 0);
			//			display = Display.getWithNewlines(arg2.get(n + "CODELONG", 1));
			//			return system.getOrCreateParticipant(code, display);
		} else {
			throw new haxe.exceptions.NotImplementedException();
		}
		return system.getOrCreateParticipant(code, display);
	}

	private function contains(string:String, totest:Array<String>):Bool {
		for (t in totest)
			if (string.contains(t))
				return true;

		return false;
	}

	private function getDressing(arg:Map<String, String>, key):String {
		var value = arg[key];
		if (value == null)
			return "";
		return value.replaceAll("_", "").toLowerCase();
	}

	public function executeArg(diagram:SequenceDiagram, lines:BlocLines, arg:Map<String, String>):CommandExecutionResult {
		trace('map=$arg');
		trace('map=' + arg.removeNullValue());

		var p1;
		var p2;

		final dressing1 = getDressing(arg, "ARROW_DRESSING1");
		final dressing2 = getDressing(arg, "ARROW_DRESSING2");

		var circleAtStart;
		var circleAtEnd;

		final hasDressing2 = contains(dressing2, [">", "\\", "/", "x"]);
		final hasDressing1 = contains(dressing1, ["x", "<", "\\", "/"]);
		var reverseDefine;
		if (hasDressing2) {
			p1 = getOrCreateParticipant(diagram, arg, "PART1");
			p2 = getOrCreateParticipant(diagram, arg, "PART2");
			circleAtStart = dressing1.contains("o");
			circleAtEnd = dressing2.contains("o");
			reverseDefine = false;
			throw new haxe.exceptions.NotImplementedException();
		} else if (hasDressing1) {
			//			p2 = getOrCreateParticipant(diagram, arg, "PART1");
			//			p1 = getOrCreateParticipant(diagram, arg, "PART2");
			//			circleAtStart = dressing2.contains("o");
			//			circleAtEnd = dressing1.contains("o");
			//			reverseDefine = true;
			throw new haxe.exceptions.NotImplementedException();
		} else {
			return CommandExecutionResult.ERROR("Illegal sequence arrow");
		}
		//
		//		final boolean sync = contains(dressing1, "<<", "\\\\", "//") || contains(dressing2, ">>", "\\\\", "//");
		//
		//		final boolean dotted = getLength(arg) > 1;
		//
		//		final Display labels;
		//		if (arg.get("MESSAGE", 0) == null) {
		//			labels = Display.create("");
		//		} else {
		//			// final String message = UrlBuilder.multilineTooltip(arg.get("MESSAGE", 0));
		//			final String message = arg.get("MESSAGE", 0);
		//			labels = Display.getWithNewlines(message);
		//		}
		//
		//		ArrowConfiguration config = hasDressing1 && hasDressing2 ? ArrowConfiguration.withDirectionBoth()
		//				: ArrowConfiguration.withDirectionNormal();
		//		if (dotted)
		//			config = config.withBody(ArrowBody.DOTTED);
		//
		//		if (sync)
		//			config = config.withHead(ArrowHead.ASYNC);
		//
		//		if (dressing2.contains("\\") || dressing1.contains("/"))
		//			config = config.withPart(ArrowPart.TOP_PART);
		//
		//		if (dressing2.contains("/") || dressing1.contains("\\"))
		//			config = config.withPart(ArrowPart.BOTTOM_PART);
		//
		//		if (circleAtEnd)
		//			config = config.withDecoration2(ArrowDecoration.CIRCLE);
		//
		//		if (circleAtStart)
		//			config = config.withDecoration1(ArrowDecoration.CIRCLE);
		//
		//		if (reverseDefine) {
		//			if (dressing1.contains("x"))
		//				config = config.withHead2(ArrowHead.CROSSX);
		//
		//			if (dressing2.contains("x"))
		//				config = config.withHead1(ArrowHead.CROSSX);
		//
		//		} else {
		//			if (dressing1.contains("x"))
		//				config = config.withHead1(ArrowHead.CROSSX);
		//
		//			if (dressing2.contains("x"))
		//				config = config.withHead2(ArrowHead.CROSSX);
		//
		//		}
		//		if (reverseDefine)
		//			config = config.reverseDefine();
		//
		//		config = applyStyle(diagram.getSkinParam().getThemeStyle(), arg.getLazzy("ARROW_STYLE", 0), config);
		//
		//		final String activationSpec = arg.get("ACTIVATION", 0);
		//
		//		if (activationSpec != null && activationSpec.charAt(0) == '*')
		//			diagram.activate(p2, LifeEventType.CREATE, null);
		//
		//		final String messageNumber = diagram.getNextMessageNumber();
		//		final Message msg = new Message(diagram.getSkinParam().getCurrentStyleBuilder(), p1, p2,
		//				diagram.manageVariable(labels), config, messageNumber);
		//		msg.setMulticast(getMulticasts(diagram, arg));
		//		final String url = arg.get("URL", 0);
		//		if (url != null) {
		//			final UrlBuilder urlBuilder = new UrlBuilder(diagram.getSkinParam().getValue("topurl"), UrlMode.STRICT);
		//			final Url urlLink = urlBuilder.getUrl(url);
		//			msg.setUrl(urlLink);
		//		}
		//
		//		if (arg.get("STEREOTYPE", 0) != null) {
		//			final Stereotype stereotype = Stereotype.build(arg.get("STEREOTYPE", 0));
		//			msg.getStereotype(stereotype);
		//		}
		//
		//		final boolean parallel = arg.get("PARALLEL", 0) != null;
		//		if (parallel)
		//			msg.goParallel();
		//
		//		msg.setAnchor(arg.get("ANCHOR", 1));
		//		msg.setPart1Anchor(arg.get("PART1ANCHOR", 1));
		//		msg.setPart2Anchor(arg.get("PART2ANCHOR", 1));
		//
		//		final String error = diagram.addMessage(msg);
		//		if (error != null)
		//			return CommandExecutionResult.error(error);
		//
		//		final String s = arg.get("LIFECOLOR", 0);
		//
		//		final HColor activationColor = s == null ? null
		//				: diagram.getSkinParam().getIHtmlColorSet().getColor(diagram.getSkinParam().getThemeStyle(), s);
		//
		//		if (activationSpec != null)
		//			return manageActivations(activationSpec, diagram, p1, p2, activationColor);
		//
		//		if (diagram.isAutoactivate() && (config.getHead() == ArrowHead.NORMAL || config.getHead() == ArrowHead.ASYNC))
		//			if (config.isDotted())
		//				diagram.activate(p1, LifeEventType.DEACTIVATE, null);
		//			else
		//				diagram.activate(p2, LifeEventType.ACTIVATE, activationColor);
		//
		//		return CommandExecutionResult.ok();

		throw new haxe.exceptions.NotImplementedException();
	}
}
