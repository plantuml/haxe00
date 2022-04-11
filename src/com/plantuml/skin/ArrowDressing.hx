package com.plantuml.skin;

class ArrowDressing {
	private final head:ArrowHead;
	private final part:ArrowPart;

	private function new(head:ArrowHead, part:ArrowPart) {
		Objects.requireNonNull(head);
		Objects.requireNonNull(part);
		this.head = head;
		this.part = part;
	}

	public static function create() {
		return new ArrowDressing(ArrowHead.NONE, ArrowPart.FULL);
	}

	public function withHead(head) {
		return new ArrowDressing(head, part);
	}

	public function withPart(part) {
		return new ArrowDressing(head, part);
	}

	public function getHead() {
		return head;
	}

	public function getPart() {
		return part;
	}
}
