import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/Home";
import ViewGene from "@/components/genes/ViewGene";
import ViewVariant from "@/components/genes/ViewVariant";
import Login from "@/components/user/Login";
import UserInfo from "@/components/user/UserInfo";

// import {ServerTable, ClientTable, Event} from 'vue-tables-2';

Vue.use(Router);
// Vue.use(ClientTable);

import store from '@/store';
import {TokenErrors} from "../store/modules/users";

const router = new Router({
	mode: "history",
	routes: [
		{
			path: "/gene/:gene_id",
			name: "gene",
			component: ViewGene
		},
		{
			path: "/gene/:gene_id/variant/:variant_id",
			name: "variant",
			component: ViewVariant
		},

		{
			path: "/login",
			name: "login",
			component: Login,
			props: true
		},
		{
			path: "/user-info",
			name: "user-info",
			component: UserInfo
		},

		{
			path: "*",
			name: "home",
			component: Home
		}
	]
});

router.beforeEach((to, from, next) => {
	// FIXME: only check credentials if the route includes authorized content; if not, we'll get rejected if we have invalid creds even for public routes
	// (we'd probably do that by adding a 'requiresAuth' and/or 'groups' fields to the route definitions)
	store.dispatch("checkCredentials").then((result) => {
		if (!result.valid && (result.reason === TokenErrors.EXPIRED || result.reason === TokenErrors.REFRESH_EXPIRED) && to.name !== "login") {
			// if our token's expired, go get a new one from the login page,
			// remembering where we eventually want to go to as well
			next({ name: 'login', params: { default_error_msg: "Token expired, please log in again", nextRoute: to.path } });
		}
		else {
			next();
		}
	});
});

export default router;
