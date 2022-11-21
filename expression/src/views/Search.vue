<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="result">
    <div class="top wrap1">
      <div class="box box1">
        <h1 style="font-size: 30px">Statistics of Data Used in PlantDeepSEA</h1>
      </div>
    </div>
    <div class="contain" style="text-align: center">
      <a-row :gutter="24" style="font-size: 20px; font-weight: bold">
        <a-col :span="5">ID</a-col>
        <a-col :span="4">Methyl_Type</a-col>
        <a-col :span="4">Methyl_Level</a-col>
        <a-col :span="4">SuppReads_Methyl</a-col>
        <a-col :span="6">SuppReads_ALL</a-col>
      </a-row>
      <a-row
        :gutter="24"
        style="font-size: 15px"
        v-for="item in DataList"
        :key="item.id"
      >
        <a-col :span="5">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="6">{{ item.description }}</a-col>
      </a-row>
    </div>
    <div class="top">
      <h1 style="font-size: 30px">Statistics of Result</h1>
    </div>
    <div class="contain">
      <h3 style="margin-top: 20px; margin-left: 10px">
        We counted the experimental data
      </h3>
      <div style="text-align: center">
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
      </div>
    </div>
    <div class="top">
      <h1 style="font-size: 30px">Evaluations of Models</h1>
    </div>
    <div class="contain">
      <h3 style="margin-top: 20px; margin-left: 10px">We get ROC curve</h3>
      <div style="text-align: center">
        <img src="../img/roc.png" style="width: 65%" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

const data = [
  {
    key: 1,
    name: "John Brown",
    age: 32,
    address: "New York No. 1 Lake Park",
    description: "My name is John Brown, I am 32 years old,",
  },
  {
    key: 2,
    name: "Jim Green",
    age: 42,
    address: "London No. 1 Lake Park",
    description: "My name is Jim Green, I am 42 years old, ",
  },
  {
    key: 3,
    name: "Joe Black",
    age: 32,
    address: "Sidney No. 1 Lake Park",
    description: "My name is Joe Black, I am 32 years old, ",
  },
  {
    key: 3,
    name: "Joe Black",
    age: 32,
    address: "Sidney No. 1 Lake Park",
    description: "My name is Joe Black, I am 32 years old, ",
  },
  {
    key: 3,
    name: "Joe Black",
    age: 32,
    address: "Sidney No. 1 Lake Park",
    description: "My name is Joe Black, I am 32 years old, ",
  },
];

export default {
  name: "Result",
  components: {},
  data() {
    return {
      DataList: data,
    };
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
.result {
  height: 2000px;
  width: 80%;
  margin: 0 auto;
}
.top {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 15px;
  margin: 0 auto;
  height: 75px;
  margin-top: 50px;
  background-color: #f0f8ff;
}
.contain {
  border-style: solid;
  border-color: #f5f5f5;
}
</style>