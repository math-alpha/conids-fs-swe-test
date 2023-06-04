import apiClient from "@/http-common";

class PurchaseDataService {
  getAll(): Promise<any> {
    console.log("Getting all purchases")
    return apiClient.get("/purchases/");
  }

  get(id: any): Promise<any> {
    return apiClient.get(`/purchases/${id}`);
  }

  create(data: any): Promise<any> {
    return apiClient.post("/purchases", data);
  }

  update(id: any, data: any): Promise<any> {
    return apiClient.put(`/purchases/${id}`, data);
  }

  delete(id: any): Promise<any> {
    return apiClient.delete(`/purchases/${id}`);
  }

  deleteAll(): Promise<any> {
    return apiClient.delete(`/purchases`);
  }

  findByTitle(title: string): Promise<any> {
    return apiClient.get(`/purchases?title=${title}`);
  }
}

export default new PurchaseDataService();
