import requests from "./Ajax";

// 获取result页面表格
export const reqResultInfo = () =>
  requests({ url: `/model/show`, method: "get" });