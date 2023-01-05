<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="result">
    <!-- <div style="margin: 15px; margin: 0 auto; width: 80%; text-align: center">
      <h1>This is an result page</h1>
    </div> -->
    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 30px">Promoter proximal region interaction</h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PPI EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch>
          <el-tab-pane label="ear">
            <Table :tableId="1"></Table>
          </el-tab-pane>
          <el-tab-pane label="pie">
            <Table :tableId="2"></Table>
          </el-tab-pane>
          <el-tab-pane label="pit">
            <Table :tableId="3"></Table>
          </el-tab-pane>
          <el-tab-pane label="py">
            <Table :tableId="4"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot">
            <Table :tableId="5"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>
    <el-card  class="resTabs">
      <div slot="header">
        <span class="tableTitle">PPI SEQ TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch class="resTabs">
          <el-tab-pane label="gene1">
            <Table :tableId="1"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene2">
            <Table :tableId="2"></Table>
          </el-tab-pane>
          <el-tab-pane label="gen3">
            <Table :tableId="3"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene4">
            <Table :tableId="4"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>

    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 30px">Promoter-distal element interaction</h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PDI  EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch class="resTabs">
          <el-tab-pane label="ear">
            <Table :tableId="6"></Table>
          </el-tab-pane>
          <el-tab-pane label="py">
            <Table :tableId="7"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot">
            <Table :tableId="8"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>
    <el-card  class="resTabs">
      <div slot="header">
        <span class="tableTitle">PDI SEQ TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch class="resTabs">
          <el-tab-pane label="gene1">
            <Table :tableId="1"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene2">
            <Table :tableId="2"></Table>
          </el-tab-pane>
          <el-tab-pane label="gen3">
            <Table :tableId="3"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene4">
            <Table :tableId="4"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Result",
  components: {},
  data() {
    return {
      data2: [],
      data3: [],
      header: [],
      header1: [],
    };
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
.result {
  /* height: 80%; */
  /* text-align: center; */
  width: 80%;
  margin: 0 auto;
}
.top {
  width: 90%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  margin: 15px;
  margin: 0 auto;
  height: 50px;
  margin-top: 50px;
  background-color: #f0f8ff;
}
::v-deep .el-tabs__nav-scroll {
  width: 80%;
  margin: 0 auto;
}
::v-deep .el-tabs__item {
  font-size: 20px;
}

.resTabs {
  margin-top: 30px;
  margin-bottom: 20px;
  /* width: 80%;
  margin: 0 auto; */
}
.tableTitle {
  margin-left: 20px;
  /* margin: auto; */
  font-size: 20px;
  font-weight: bold;
  color:#FB636F ;
}
</style>
