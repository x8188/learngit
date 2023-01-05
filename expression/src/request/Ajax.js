import axios from "axios";

import nprogress from "nprogress";
import "nprogress/nprogress.css";
//start进度条开始，done进度条结束

import store from "@/store";

// 利用axios对象的方法create，创建一个axios的实例
// request就是axios，只不过稍微配置一下
const requests = axios.create({
  // 配置对象
  // 基础路径，发请求的时候路径会出现api
  baseURL: "http://124.220.197.196:8080",
  timeout: 5000,
});

//请求拦截器 ，发请求之前可以检测到，在发出去之前做一些事情
requests.interceptors.request.use((config) => {

  nprogress.start();
  return config;
});

// 响应拦截器
requests.interceptors.response.use(
  (res) => {
    // 成功的回调函数：服务器相应数据回来以后，响应拦截器可以检测到，并做一些事情
    nprogress.done();
    
    return res.data;
  },
  (error) => {
    //响应失败的回调函数
    return Promise.reject(new Error("faile"));
  }
);

export default requests;
