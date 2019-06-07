<template>
	<!--
  /************************ LICENCE ***************************
  *     This file is part of <ViKM Vital-IT Knowledge Management web application>
  *     Copyright (C) <2016> SIB Swiss Institute of Bioinformatics
  *
  *     This program is free software: you can redistribute it and/or modify
  *     it under the terms of the GNU Affero General Public License as
  *     published by the Free Software Foundation, either version 3 of the
  *     License, or (at your option) any later version.
  *
  *     This program is distributed in the hope that it will be useful,
  *     but WITHOUT ANY WARRANTY; without even the implied warranty of
  *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  *     GNU Affero General Public License for more details.
  *
  *     You should have received a copy of the GNU Affero General Public License
  *    along with this program.  If not, see <http://www.gnu.org/licenses/>
  *
  *****************************************************************/
  -->

	<div class="card mt-3">
		<div class="card-header">
			<div class="card-title">Publicly Available Information</div>
		</div>

		<div class="card-body top-level">
			<b-table :fields="fields" :items="items" :sort-by.sync="sortBy" :sort-desc="false">
				<template slot="source" slot-scope="row">
					<div style="display: flex; align-items: center;">
						<SourceIcon :name="row.item.source.name" :size="20" :margin-right="8" :no-tip="true" />
						<a :href="row.item.variant_url" target="_blank">{{ row.item.source.display_name }}</a>
					</div>
				</template>

				<template slot="diseases" slot-scope="data">
					<component v-if="rowHasPart(data, 'diseases')" :is="data.item.colum_parts.diseases" :row="data" />
					<span v-else>
					{{ Object.keys(data.item.diseases).length }} disease{{ Object.keys(data.item.diseases).length !== 1 ? "s" : "" }}
					</span>
				</template>

				<template slot="association_count" slot-scope="data">
						<component v-if="rowHasPart(data, 'publication_count')" :is="data.item.colum_parts.publication_count" :row="data" />
						<span v-else>
						{{ data.value.toLocaleString() }} evidence{{ data.value !== 1 ? "s" : "" }}
						</span>
				</template>

				<template slot="clinical" slot-scope="data">
					<component v-if="rowHasPart(data, 'clinical')" :is="data.item.colum_parts.clinical" :row="data" />
					<evidenceTypesBarPlot v-else :data="data.item.evidence_types" />
				</template>

				<template slot="scores" slot-scope="data">
						<component v-if="rowHasPart(data, 'scores')" :is="data.item.colum_parts.scores" :row="data" />
						<score-plot v-else :scores="data.item.scores" :source-name="data.item.source.name"></score-plot>
				</template>

				<template slot="actions" slot-scope="row">
					<div class="details-tray" style="text-align: right;">
						<!-- We use @click.stop here to prevent a 'row-clicked' event from also happening -->
						<b-button size="sm" @click.stop="row.toggleDetails">
							{{ row.detailsShowing ? "Hide" : "Show" }} Details
						</b-button>
					</div>
				</template>

				<template slot="row-details" slot-scope="row">
					<div class="row-details">
						<component v-if="row.item.details_part" :is="row.item.details_part" :row="row" :variant="variant" />
						<div v-else>No row details control provided!</div>
					</div>
				</template>
			</b-table>

			<div v-if="sourcesNotFound.length > 0" class="var-not-found">
			No data available for this variant in {{ sourcesNotFound.map(x => x.display_name).join(", ") }}
			</div>
		</div>
	</div>
</template>

<script>
import store from '@/store';
import scorePlot from "@/components/plots/scorePlot";
// import significanceBarPlot from "@/components/plots/significanceBarPlot";
import evidenceTypesBarPlot from '@/components/plots/evidenceTypesBarPlot';
import {normalizeItemList} from "../../../utils";
import CosmicRowDetails from "./sources/cosmic/CosmicRowDetails";
import CosmicPubCountCol from "@/components/genes/variants/sources/cosmic/CosmicPubCountCol";
import UnavailableCol from "@/components/genes/variants/sources/shared/UnavailableCol";
import OncoKBRowDetails from "./sources/oncokb/OncoKBRowDetails";
import SourceIcon from "@/components/widgets/SourceIcon";
import CivicRowDetails from "@/components/genes/variants/sources/civic/CivicRowDetails";

const overrides = {
	civic: {
		details_part: CivicRowDetails
	},
	cosmic: {
		colum_parts: {
			clinical: UnavailableCol,
			publication_count: CosmicPubCountCol,
			scores: UnavailableCol
		},
		details_part: CosmicRowDetails
	},
	oncokb: {
		details_part: OncoKBRowDetails
	}
};

export default {
	name: "VariantPublicDatabases",
	components: {SourceIcon, scorePlot, evidenceTypesBarPlot},
	props: {variant: {type: Object, required: true}},
	data() {
		return {
			sortBy: "source",
			fields: [
				{
					key: "source",
					label: "Source",
					sortable: true
				},
				{
					key: "diseases",
					label: "Diseases",
					sortable: true
				},
				{
					key: "association_count",
					label: "Database Evidences",
					sortable: true
				},
				{
					key: "clinical",
					label: "Clinical Significance / Interpretation",
					sortable: false
				},
				{
					key: "scores",
					label: "Evidence Levels",
					sortable: false
				},
				{
					key: "actions",
					label: "",
					sortable: false
				}
			]
		};
	},
	computed: {
		items() {
			return this.variant.variantinsource_set.map(vis => {
				return {
					...vis,
					_showDetails: false,
					filter: "",
					colum_parts: overrides.hasOwnProperty(vis.source.name) ? overrides[vis.source.name].colum_parts : null,
					details_part: overrides.hasOwnProperty(vis.source.name) ? overrides[vis.source.name].details_part : null
				}
			});
		},
		sourcesNotFound() {
			// we're sure sources exists because we populated it from the store
			return store.state.genes.sources
				.filter(x => x.num_variants > 0 && !this.variant.variantinsource_set.find(y => x.name === y.source.name));
		}
	},
	methods: {
		rowHasPart(row, part) {
			return row.item.colum_parts && row.item.colum_parts[part];
		},
		normalizeItemList
	},
	created() {
		store.dispatch('getSources');
	}
};
</script>

<style scoped>
.var-not-found {
	background: #f5f5f5;
	-webkit-border-radius: 5px;-moz-border-radius: 5px;border-radius: 5px;
	padding: 10px;
	padding-left: 15px;
	font-style: italic;
	color: #999;
}

.details-tray button {
	width: 100px;
}
</style>