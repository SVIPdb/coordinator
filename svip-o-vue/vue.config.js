/* globals process, module, require */
const pkg_json = require('./package.json');
process.env.VUE_APP_VERSION = pkg_json.version;
process.env.VUE_APP_RELEASE_NAME = pkg_json.release_name;

module.exports = {
	runtimeCompiler: true,
	transpileDependencies: [
		/\bvue-awesome\b/
	]
}
