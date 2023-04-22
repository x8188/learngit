import requests from "./Ajax";

// 获取result页面表格
export const reqResultInfo = () =>
  requests({ url: `/model/show`, method: "get" });

// 提交序列作业接口
export const reqSubmitSeq = (taskBody) =>
  requests({ url: `model/expression/submit`, method: "post", data: taskBody });

// 提交文件作业接口
export const reqSubmitFlie = (taskBody) =>
  requests({
    url: `model/expression/file`,
    method: "post",
    data: taskBody,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

export const reqTasksInfo = () =>
  requests({ url: `/model/status`, method: "get" });

export const reqTaskResultInfo = (taskID) =>
  requests({ url: `/model/result`, method: "get", params: { taskID: taskID } });


export const reqCaptchaImg = () =>
  requests({ url: `/model/captcha`, method: "get" });

export const reqVisImg = (taskID,seqID) =>
  requests({ url: `/model/gradient`, method: "get",params: { taskID,seqID } });
