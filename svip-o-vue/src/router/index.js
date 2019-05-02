import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/Home";
import Genes from "@/components/genes/Genes";
import ViewGene from "@/components/genes/ViewGene";
import ViewVariant from "@/components/genes/ViewVariant";
import Login from "@/components/user/Login";
import UserInfo from "@/components/user/UserInfo";

// import {ServerTable, ClientTable, Event} from 'vue-tables-2';

Vue.use(Router);
// Vue.use(ClientTable);

const router = new Router({
	mode: "history",
	routes: [
		{
			path: "/genes",
			name: "genes",
			component: Genes
		},
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
			component: Login
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

// function requireAuth (to, from, next) {
//   store.dispatch('getCredentials').then(test => {
//     if (!test) {
//       next({
//         path: '/',
//         query: { redirect: to.fullPath }
//       })
//     } else {
//       if (to.matched.some(record => record.meta.permissions.length > 0)) {
//         store.dispatch('checkPermissions', { permissions: to.meta.permissions, condition: to.meta.condition }).then(res => {
//           if (res) {
//             next()
//           } else {
//             next({
//               path: '/permissionDenied'
//             })
//           }
//         })
//       } else {
//         next()
//       }
//     }
//   })
// }
export default router;