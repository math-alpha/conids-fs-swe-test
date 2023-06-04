<script setup lang="ts">
import { useProductPurchaseStore } from '@/stores/product'

const productStore = useProductPurchaseStore()

const products = productStore.products
const representative = productStore.representative
const priorities = productStore.priorities
const vendors = productStore.vendors
</script>

<template>
  <div class="container col-8">
    <h4 class="mb-5">Create Purchase</h4>
    <form v-if="!submitted">
      <div class="flex-row row">
        <div class="col-6">
          <div class="form-group">
            <label for="title"><strong>Order Reference</strong></label>
            <input type="text" class="form-control" id="title" v-model="purchase.order_reference" />
          </div>

          <div class="form-group">
            <label for="description"><strong>Purchase Representative</strong></label>
            <select v-model="purchase.purchase_representative" class="form-select d-block">
              <option v-for="(name, id) in representative" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Product Reference</strong></label>
            <select v-model="purchase.product_reference" class="form-select d-block">
              <option v-for="(name, id) in products" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Priority</strong></label>
            <select v-model="purchase.priority" class="form-select d-block">
              <option v-for="(name, id) in priorities" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label><strong>Vendor</strong></label>
            <select v-model="purchase.vendor" class="form-select d-block">
              <option v-for="(name, id) in vendors" :key="id" :value="id">
                {{ name }}
              </option>
            </select>
          </div>
        </div>
        <div class="col-6">
          <div class="form-group">
            <label><strong>Product Deadline</strong></label>
            <input v-model="purchase.order_deadline" class="form-select" type="datetime-local" />
          </div>

          <div class="form-group">
            <label for="title"><strong>Total</strong></label>
            <input type="number" class="form-control" id="number" v-model="purchase.total" />
          </div>

          <div class="form-group">
            <label for="status"><strong>Status</strong></label>
            <input type="text" class="form-control" id="status" v-model="purchase.status" />
          </div>

          <div class="form-group">
            <label for="status"><strong>Source Document</strong></label>
            <input type="text" class="form-control" id="status" v-model="purchase.source_document" />
          </div>

          <div class="form-group">
            <label for="status"><strong>Activities</strong></label>
            <input type="text" class="form-control" id="status" v-model="purchase.activities" />
          </div>
        </div>
      </div>

      <div class="d-flex gap-2 col-12 mx-auto my-5">
        <button type="reset" class="btn btn-outline-danger btn-lg col-6">Reset</button>
        <input
          type="button"
          value="Save"
          class="btn btn-primary btn-lg col-6"
          @click="savePurchase"
        />
      </div>
    </form>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newPurchase">Add Another</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PurchaseDataService from '@/services/PurchaseDataService'
import Purchase from '@/types/Purchase'
import ResponseData from '@/types/ResponseData'

export default defineComponent({
  name: 'add-purchase',
  data() {
    return {
      purchase: {} as Purchase,
      submitted: false
    }
  },
  methods: {
    savePurchase() {
      let data = this.purchase

      console.log(`local data ${data}`)
      console.log(data)

      PurchaseDataService.create(data)
        .then((response: ResponseData) => {
          this.purchase.id = response.data.id
          console.log(response.data)
          this.submitted = true
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    retrievePurchases() {
      console.log('Retrieving Purchases data')
      PurchaseDataService.getAll()
        .then((response: ResponseData) => {
          console.log(response.data)
        })
        .catch((e: Error) => {
          console.log(e)
        })
    },

    newPurchase() {
      this.submitted = false
      this.purchase = {} as Purchase
    }
  },
  mounted() {
    this.retrievePurchases()
  }
})
</script>
