<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control"
          placeholder="Search by title"
          v-model="title"
        />
        <div class="input-group-append">
          <button
            class="btn btn-outline-secondary"
            type="button"
            @click="searchTitle"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Purchases List</h4>
      <ul class="list-group">
        <li
          class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(purchase, index) in purchases"
          :key="index"
          @click="setActivePurchase(purchase, index)"
        >
          {{ purchase.order_reference }}
        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllPurchases">
        Remove All
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentPurchase.id">
        <h4>Purchase</h4>
        <div>
          <label><strong>Title:</strong></label> {{ currentPurchase.order_reference }}
        </div>
        <div>
          <label><strong>Description:</strong></label>
          {{ currentPurchase.purchase_representative }}
        </div>
        <div>
          <label><strong>Status:</strong></label>
          {{ currentPurchase.priority }}
        </div>

        <router-link
          :to="'/purchases/' + currentPurchase.id"
          class="badge badge-warning"
        >Edit</router-link
        >
      </div>
      <div v-else>
        <br />
        <p>Please click on a Purchase...</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PurchaseDataService from "@/services/PurchaseDataService";
import Purchase from "@/types/Purchase";
import ResponseData from "@/types/ResponseData";

export default defineComponent({
  name: "purchases-list",
  data() {
    return {
      purchases: [] as Purchase[],
      currentPurchase: {} as Purchase,
      currentIndex: -1,
      title: "",
    };
  },
  methods: {
    retrievePurchases() {
      PurchaseDataService.getAll()
        .then((response: ResponseData) => {
          this.purchases = response.data;
          console.log(response.data);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrievePurchases();
      this.currentPurchase = {} as Purchase;
      this.currentIndex = -1;
    },

    setActivePurchase(purchase: Purchase, index = -1) {
      this.currentPurchase = purchase;
      this.currentIndex = index;
    },

    removeAllPurchases() {
      PurchaseDataService.deleteAll()
        .then((response: ResponseData) => {
          console.log(response.data);
          this.refreshList();
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    searchTitle() {
      PurchaseDataService.findByTitle(this.title)
        .then((response: ResponseData) => {
          this.purchases = response.data;
          this.setActivePurchase({} as Purchase);
          console.log(response.data);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },
  },
  mounted() {
    this.retrievePurchases();
  },
});
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
