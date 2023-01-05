<template>
  <div>
    <h1>{{ tableId }}</h1>
    <el-table :data="expData" stripe style="width: 100%" height="400">
      <el-table-column prop="Annotation1" label="Annotation1">
      </el-table-column>
      <el-table-column prop="Annotation2" label="Annotation2">
      </el-table-column>
      <el-table-column prop="exp" label="exp"> </el-table-column>
      <el-table-column prop="pre" label="pre"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {

  name: "Table",
  props: ["tableId"],
  data(){
    return{
      expData: [],
    }
  },
  methods:{
  }
};
</script>

<style></style>
