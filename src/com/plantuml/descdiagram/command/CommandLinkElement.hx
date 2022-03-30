package com.plantuml.descdiagram.command;

class CommandLinkElement {
	private static final KEY1 = "dotted|dashed|plain|bold|hidden|norank|single|thickness=\\d+";
	private static final KEY2 = ",dotted|,dashed|,plain|,bold|,hidden|,norank|,single|,thickness=\\d+";
	public static final LINE_STYLE = "(?:#\\w+|" + CommandLinkElement.KEY1 + ")(?:,#\\w+|" + CommandLinkElement.KEY2 + ")*";
	private static final LINE_STYLE_MUTILPLES = LINE_STYLE + "(?:(?:;" + LINE_STYLE + ")*)";
	public static final STYLE_COLORS_MULTIPLES = "-\\[(" + LINE_STYLE_MUTILPLES + "*)\\]->";
}
