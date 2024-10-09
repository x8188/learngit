import requests from "./Ajax";

// 获取result页面表格
export const reqResultInfo = (Type) =>
  requests({ url: `/model/show/${Type}`, method: "get" });

// export const reqRiceResultInfo = () =>
//   requests({ url: `/model/show/rice`, method: "get" });

// export const reqCornResultInfo = () =>
//   requests({ url: `/model/show/maize`, method: "get" });

// export const reqCottonResultInfo = () =>
//   requests({ url: `/model/show/cotton`, method: "get" });

// export const reqWheatResultInfo = () =>
//   requests({ url: `/model/show/wheat`, method: "get" });

// 提交序列作业接口
export const reqSubmitSeq = (taskBody) =>
  requests({ url: `model/submit/custom`, method: "post", data: taskBody });

// 提交文件作业接口
export const reqSubmitFlie = (taskBody) =>
  requests({
    url: `/model/submit/file`,
    method: "post",
    data: taskBody,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

export const reqTasksInfo = () =>
  requests({ url: `/model/status`, method: "get" });

export const reqTaskResultInfo = (params) =>
  requests({ url: `/model/result/predict`, method: "get", params: params });


export const reqCaptchaImg = () =>
  requests({ url: `/model/captcha`, method: "get" });

export const reqVisImg = (taskID,seqID) =>
  requests({ url: `/model/result/saliency`, method: "get",params: { taskID,seqID } });

export const reqMaizeHot = (id) =>
  requests({ url: `/model/maize/heat/${id}`, method: "get"});

export const reqLGBMtask = (taskBody) =>
  requests({ url: `/model/submit/qtg_lgbm`, method: "post", data: taskBody });
