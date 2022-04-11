package com.plantuml.skin;

class ArrowConfiguration {
	private final body:ArrowBody;

	private final dressing1:ArrowDressing;
	private final dressing2:ArrowDressing;

	private final decoration1:ArrowDecoration;
	private final decoration2:ArrowDecoration;

	private final color:HColor;

	private final isSelf:Bool;
	private final thickness:Float;
	private final reverseDefine:Bool;

	private function new(body, dressing1, dressing2, decoration1, decoration2, color, isSelf, thickness, reverseDefine) {
		Objects.requireNonNull(body);
		Objects.requireNonNull(dressing1);
		Objects.requireNonNull(dressing2);
		this.reverseDefine = reverseDefine;
		this.thickness = thickness;
		this.body = body;
		this.dressing1 = dressing1;
		this.dressing2 = dressing2;
		this.decoration1 = decoration1;
		this.decoration2 = decoration2;
		this.color = color;
		this.isSelf = isSelf;
	}

	public static function withDirectionNormal() {
		return new ArrowConfiguration(ArrowBody.NORMAL, ArrowDressing.create(), ArrowDressing.create().withHead(ArrowHead.NORMAL), ArrowDecoration.NONE,
			ArrowDecoration.NONE, null, false, 1, false);
	}

	public static function withDirectionBoth() {
		return new ArrowConfiguration(ArrowBody.NORMAL, ArrowDressing.create().withHead(ArrowHead.NORMAL), ArrowDressing.create().withHead(ArrowHead.NORMAL),
			ArrowDecoration.NONE, ArrowDecoration.NONE, null, false, 1, false);
	}

	public function withBody(type:ArrowBody) {
		return new ArrowConfiguration(type, dressing1, dressing2, decoration1, decoration2, color, isSelf, thickness, reverseDefine);
	}

	public function withHead(head:ArrowHead) {
		final newDressing1 = addHead(dressing1, head);
		final newDressing2 = addHead(dressing2, head);
		return new ArrowConfiguration(body, newDressing1, newDressing2, decoration1, decoration2, color, isSelf, thickness, reverseDefine);
	}

	private static function addHead(dressing, head) {
		if (dressing.getHead() == ArrowHead.NONE)
			return dressing;

		return dressing.withHead(head);
	}
}
