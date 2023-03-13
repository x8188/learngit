<!-- 
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
    <div class="tool">
      <h1 id="modelSelect">Please Select MH63/ZS97 Model</h1>
      <el-row type="flex" style="margin-bottom:30px">
        <el-col :span="12" class="cardFa">
          <el-card class="card">
            <div slot="header">
              <span class="cardTitle">MH63</span>
            </div>
            <div style="text-align: center">
              <p class="modelP">

              </p>
              <p class="modelP">

              </p>
              <el-button
                class="rouButton"
                @click="$router.push('/Expression/mh63')"
                >Go MH63</el-button
              >
            </div>
          </el-card>
        </el-col>
        <el-col :span="12" class="cardFa">
          <el-card class="card">
            <div slot="header">
              <span class="cardTitle">ZS97</span>
            </div>
            <div style="text-align: center">
              <p class="modelP">

              </p>
              <p class="modelP">

              </p>
              <el-button
                class="rouButton"
                @click="$router.push('/Expression/zs97')"
                >Go ZS97</el-button
              >
            </div>
          </el-card>
        </el-col>
      </el-row>
      <Back></Back>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  // import HelloWorld from '@/components/HelloWorld.vue'
  
  export default {
    name: "indexShui",
    components: {},
    data() {
      return {};
    },
    methods: {},
    created() {},
  };
  </script>
  <style scoped>
  .tool {
    width: 80%;
    margin: 0 auto;
    height: 800px;
  }
  
  .cardTitle {
    margin-left: 20px;
    /* margin: auto; */
    font-size: 30px;
    font-weight: bold;
    color: #22cab3;
  }
  .card {
    width: 80%;
    height: 100%;
  }
  .cardFa{
    display:flex;
  justify-content:center;
  }
  .modelP {
    text-align: justify;
    font-size: 18px;
  }
  
  #modelSelect {
    text-align: center;
    font-weight: bold;
    color: #003164;
    margin: 50px;
  }
  
  .rouButton {
    margin-top: 20px;
    font-size: 20px;
    width: 150px;
    height: 60px;
    color: #fff;
    background-color: #4db6ac;
    border-color: #4db6ac;
    border-radius: 0px;
  }
  .rouButton:hover {
    background: #71d8ce !important;
    border-color: #71d8ce !important;
    color: #fff !important;
  }
  </style>
  