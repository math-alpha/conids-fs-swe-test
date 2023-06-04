import apiClient from "@/http-common";

import { useProductPurchaseStore } from '@/stores/product'
import type ProductTag from "@/types/ProductTag";
import type ResponseData from "@/types/ResponseData";

class PurchaseDataService {
  getAll(): Promise<any> {

    const productStore = useProductPurchaseStore();

    apiClient.get('/product/').then((res: ResponseData) => {
      res.data.map((p: ProductTag ) => {
        productStore.products[p.id] = p.name;
      });
    });
    apiClient.get('/priority/').then((res: ResponseData) => {
      res.data.map((p: ProductTag ) => {
        productStore.priorities[p.id] = p.name;
      });
    });
    apiClient.get('/responsible/').then((res: ResponseData) => {
      res.data.map((p: ProductTag ) => {
        productStore.representative[p.id] = p.name;
      });
    });
    apiClient.get('/vendors/').then((res: ResponseData) => {
      res.data.map((p: ProductTag ) => {
        productStore.vendors[p.id] = p.name;
      });
    });

    return apiClient.get("/purchases/");
  }

  get(id: any): Promise<any> {
    return apiClient.get(`/purchases/${id}/`);
  }

  create(data: any): Promise<any> {
    return apiClient.post("/purchases/", data);
  }

  update(id: any, data: any): Promise<any> {
    return apiClient.put(`/purchases/${id}/`, data);
  }

  delete(id: any): Promise<any> {
    return apiClient.delete(`/purchases/${id}/`);
  }

  deleteAll(): Promise<any> {
    return apiClient.delete(`/purchases`);
  }

  findByTitle(title: string): Promise<any> {
    return apiClient.get(`/purchases?title=${title}`);
  }
}

export default new PurchaseDataService();
