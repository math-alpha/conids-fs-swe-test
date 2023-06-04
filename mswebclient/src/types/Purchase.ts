export default interface Purchase {
  id?:                      number;
  order_reference:         string;
  order_deadline:          Date;
  activities:              string;
  source_document:         string;
  total:                   number;
  status:                  string;
  priority:                number;
  product_reference:       number;
  vendor:                  number;
  purchase_representative: number;
}
