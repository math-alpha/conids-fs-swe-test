<script setup lang="ts">
import { customRef, ref } from 'vue'
import { useProductPurchaseStore } from '@/stores/product'

const productStore = useProductPurchaseStore()
const products = productStore.products
const representative = productStore.representative
const priorities = productStore.priorities
const vendors = productStore.vendors
const selectedProductId = ref(null)
</script>

<template>
  <div v-if="currentPurchase.id" class="container col-md-8">
    <h4>Purchase</h4>
    <form>
      <div class="flex-row row">
        <div class="col-6">
          <div class="form-group">
            <label for="title"><strong>Order Reference</strong></label>
            <input
              type="text"
              class="form-control"
              id="title"
              v-model="currentPurchase.order_reference"
            />
          </div>

          <div class="form-group">
            <label for="description"><strong>Purchase Representative</strong></label>
            <select :v-model="currentPurchase.purchase_representative" class="form-select d-block">
              <option v-for="(name, id) in representative" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Product Reference</strong></label>
            <select :v-model="currentPurchase.product_reference" class="form-select d-block">
              <option v-for="(name, id) in products" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Priority</strong></label>
            <select :v-model="currentPurchase.priority" class="form-select d-block">
              <option v-for="(name, id) in priorities" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Vendor</strong></label>
            <select :v-model="currentPurchase.vendor" class="form-select d-block">
              <option v-for="(name, id) in vendors" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label><strong>Product Deadline</strong></label>
            <input
              v-model="currentPurchase.order_deadline"
              class="form-select"
              type="datetime-local"
            />
          </div>

          <div class="form-group">
            <label for="title"><strong>Total</strong></label>
            <input type="number" class="form-control" id="number" v-model="currentPurchase.total" />
          </div>

          <div class="form-group">
            <label for="status"><strong>Status</strong></label>
            <input type="text" class="form-control" id="status" v-model="currentPurchase.status" />
          </div>

          <div class="form-group">
            <label for="status"><strong>Activities</strong></label>
            <input
              type="text"
              class="form-control"
              id="status"
              v-model="currentPurchase.activities"
            />
          </div>
        </div>
      </div>
    </form>

    <div class="d-flex gap-2 col-12 mx-auto my-4">
      <input type="button" value="Delete" class="btn btn-danger btn-lg col-6" @click="deletePurchase" />

      <input type="button" value="Update" class="btn btn-primary btn-lg col-6" @click="updatePurchase" />
    </div>

    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Purchase...</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PurchaseDataService from '@/services/PurchaseDataService'
import Purchase from '@/types/Purchase'
import ResponseData from '@/types/ResponseData'

export default defineComponent({
  name: 'Purchase',
  data() {
    return {
      currentPurchase: {} as Purchase,
      message: ''
    }
  },
  methods: {
    getPurchase(id: any) {
      PurchaseDataService.get(id)
        .then((response: ResponseData) => {
          this.currentPurchase = response.data
          console.log(response.data)
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    updatePurchase() {
      PurchaseDataService.update(this.currentPurchase.id, this.currentPurchase)
        .then((response: ResponseData) => {
          console.log(response.data)
          this.message = 'The purchase was updated successfully!'
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    deletePurchase() {
      PurchaseDataService.delete(this.currentPurchase.id)
        .then((response: ResponseData) => {
          console.log(response.data)
          this.$router.push({ name: 'purchases' })
        })
        .catch((e: Error) => {
          console.log(e)
        })
    }
  },
  mounted() {
    this.message = ''
    this.getPurchase(this.$route.params.id)
  }
})
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}

.form-group {
  margin-top: 8px;
}
</style>
