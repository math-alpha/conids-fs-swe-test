<script setup lang="ts">
import { ref } from 'vue';
import { useProductPurchaseStore } from "@/stores/product";

const productStore = useProductPurchaseStore();
const products = productStore.products;
const representative = productStore.representative;
const priorities = productStore.priorities;
const vendors = productStore.vendors;
const selectedProductId = ref(null);
</script>

<template>
  <div class=" row">
    <div class="col-md-12">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title" v-model="title" />
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="searchTitle">
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-8">
      <h4>Purchases List</h4>
      <ul class="list-group">
        <li
          class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(purchase, index) in purchases"
          :key="index"
          @click="setActivePurchase(purchase, index); selectedProductId = index"
        >
          {{ purchase.order_reference }}
        </li>
      </ul>

      <button class="my-3 btn btn-sm btn-danger col-2" @click="removeAllPurchases">Remove All</button>
    </div>
    <div class="col-md-4">
      <div v-if="currentPurchase.id">
        <h4>Purchase</h4>
        <div>
          <label><strong>Order Ref:</strong></label>
          {{ currentPurchase.order_reference }}
        </div>
        <div>
          <label><strong>Purchase Representative:</strong></label>
          {{ representative[currentPurchase.purchase_representative] }}
        </div>
        <div>
          <label><strong>Priority:</strong></label>
          {{ priorities[currentPurchase.priority] }}
        </div>
        <div>
          <label><strong>Product Reference:</strong></label>
          {{ products[currentPurchase.product_reference] }}
        </div>
        <div>
          <label><strong>Product Deadline:</strong></label>
          {{ currentPurchase.order_deadline || date }}
        </div>
        <div>
          <label><strong>Vendor:</strong></label>
          {{ vendors[currentPurchase.vendor] }}
        </div>
        <div>
          <label><strong>Total:</strong></label>
          {{ currentPurchase.total }}
        </div>
        <div>
          <label><strong>Status:</strong></label>
          {{ currentPurchase.status }}
        </div>

        <button @click="editPurchase" class="btn btn-primary col-8 mx-auto"
          >Edit
        </button>
      </div>
      <div v-else>
        <br />
        <p>Please click on a Purchase...</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import PurchaseDataService from '@/services/PurchaseDataService'

import Purchase from '@/types/Purchase'
import ResponseData from '@/types/ResponseData'
import { useProductPurchaseStore } from "@/stores/product";

export default defineComponent({
  name: 'purchases-list',
  setup(){
    const productStore = useProductPurchaseStore();
    return {productStore}
  },
  data() {
    return {
      purchases: [] as Purchase[],
      currentPurchase: {} as Purchase,
      currentIndex: -1,
      title: ''
    }
  },
  methods: {
    editPurchase(){
      this.$router.push(`/purchase/${this.currentPurchase.id}`)
    },
    retrievePurchases() {
      PurchaseDataService.getAll()
        .then((response: ResponseData) => {
          this.purchases = response.data
          console.log(response.data)
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    refreshList() {
      this.retrievePurchases()
      this.currentPurchase = {} as Purchase
      this.currentIndex = -1
    },

    setActivePurchase(purchase: Purchase, index = -1) {
      this.currentPurchase = purchase
      this.currentIndex = index
    },

    removeAllPurchases() {
      PurchaseDataService.deleteAll()
        .then((response: ResponseData) => {
          console.log(response.data)
          this.refreshList()
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    searchTitle() {
      PurchaseDataService.findByTitle(this.title)
        .then((response: ResponseData) => {
          this.purchases = response.data
          this.setActivePurchase({} as Purchase)
          console.log(response.data)
        })
        .catch((e: Error) => {
          console.log(e)
        })
    }
  },
  mounted() {
    this.retrievePurchases()
  }
})
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
