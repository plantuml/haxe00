package com.plantuml;

class UrlBuilder {
	private static final S_QUOTED = {size: 3,
		reg: "\\[\\[[%s]*"
		+ "[%g]([^%g]+)[%g]" // Quoted part
		+ "(?:[%s]*\\{([^{}]*)\\})?" // Optional tooltip
		+ "(?:[%s]([^%s\\{\\}\\[\\]][^\\[\\]]*))?" // Optional label
		+ "[%s]*\\]\\]"};

	private static final S_ONLY_TOOLTIP = {
		size: 1,
		reg: "\\[\\[[%s]*" + //
		"\\{(.*)\\}" + // Tooltip
		"[%s]*\\]\\]"
	};

	private static final S_ONLY_TOOLTIP_AND_LABEL = {
		size: 2,
		reg: "\\[\\[[%s]*" + //
		"\\{([^{}]*)\\}" + // Tooltip
		"[%s]*" + //
		"([^\\[%s\\{\\}\\[\\]][^\\[\\]]*)" // Label
		+ "[%s]*\\]\\]"
	};

	private static final S_LINK_TOOLTIP_NOLABEL = {
		size: 2,
		reg: "\\[\\[[%s]*" + //
		"([^\\s%g{}\\[\\]]+?)" + // Link
		"[%s]*\\{(.+)\\}" + // Tooltip
		"[%s]*\\]\\]"
	};

	private static final S_LINK_WITH_OPTIONAL_TOOLTIP_WITH_OPTIONAL_LABEL = {size: 3,
		reg: "\\[\\[[%s]*"
		+ "([^%s%g\\[\\]]+?)" // Link
		+ "(?:[%s]*\\{([^{}]*)\\})?" // Optional tooltip
		+ "(?:[%s]([^%s\\{\\}\\[\\]][^\\[\\]]*))?" // Optional label
		+ "[%s]*\\]\\]"};

	public static function getRegexp() {
		return S_QUOTED.reg //
			+ "|"
			+ S_ONLY_TOOLTIP.reg
			+ "|"
			+ S_ONLY_TOOLTIP_AND_LABEL.reg
			+ "|"
			+ S_LINK_TOOLTIP_NOLABEL.reg
			+ "|"
			+ S_LINK_WITH_OPTIONAL_TOOLTIP_WITH_OPTIONAL_LABEL.reg;
	}

	public static function getRegexpSize() {
		return S_QUOTED.size //
			+ S_ONLY_TOOLTIP.size
			+ S_ONLY_TOOLTIP_AND_LABEL.size
			+ S_LINK_TOOLTIP_NOLABEL.size
			+ S_LINK_WITH_OPTIONAL_TOOLTIP_WITH_OPTIONAL_LABEL.size;
	}
}
