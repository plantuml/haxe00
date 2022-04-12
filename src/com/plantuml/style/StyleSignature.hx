package com.plantuml.style;

interface StyleSignature {
	public function getMergedStyle(styleBuilder:StyleBuilder):Style;
	// public StyleSignature withTOBECHANGED(Stereotype stereotype);
	// public StyleSignature with(Stereostyles stereostyles);
}
