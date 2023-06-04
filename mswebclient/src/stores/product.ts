import { defineStore } from "pinia";
import { ref, Ref, UnwrapRef } from "vue";

import ProductTag from "@/types/ProductTag";

export const useProductPurchaseStore = defineStore('product', () => {
  const products: Ref<UnwrapRef<ProductTag>> = ref({})
  const priorities: Ref<UnwrapRef<ProductTag>> = ref({})
  const categories: Ref<UnwrapRef<ProductTag>> = ref({})
  const representative: Ref<UnwrapRef<ProductTag>> = ref({})
  const vendors: Ref<UnwrapRef<ProductTag>> = ref({})

  return {products, priorities, categories, representative, vendors}
})
