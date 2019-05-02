export function change_from_hgvs(x, include_transcript = false) {
	if (!x || !x.includes(":")) return x;

	if (include_transcript) {
		const parts = x.split(":");
		return {transcript: parts[0], change: parts[1]};
	}

	return x.split(":")[1];
}

export function var_to_position(variant, with_change = false) {
	const r = /.*:g\.([0-9]+)(.*)$/;

	if (!variant.hgvs_g || !variant.chromosome || !variant.hgvs_g.match(r))
		return null;

	if (with_change) {
		return `chr${variant.chromosome}:${variant.hgvs_g.replace(r, "$1$2")}`;
	}

	return `chr${variant.chromosome}:${variant.hgvs_g.replace(r, "$1")}`;
}

export function normalizeItemList(items) {
	if (!items) return items;

	return items
		.split(",")
		.map(x => x.trim())
		.join(", ");
}

export function titleCase(str, lowerCaseAll=false, glue = ["of", "for", "and"]) {
	if (!str) { return str; }
	return str.replace(/(\w)(\w*)/g, function (_, i, r) {
		const frag = (r != null ? r : "");
		const j = i.toUpperCase() + (lowerCaseAll ? frag.toLocaleLowerCase() : frag);
		return glue.indexOf(j.toLowerCase()) < 0 ? j : j.toLowerCase();
	});
}

export function desnakify(x, lowerCaseAll=false) {
	if (!x) { return x; }
	return titleCase(x.split("_").join(" "), lowerCaseAll);
}