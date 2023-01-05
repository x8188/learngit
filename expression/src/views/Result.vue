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
      <h1 style="font-size: 40px;  font-weight: bold;">Promoter proximal region interaction</h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PPI EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch>
          <el-tab-pane label="ear">
            <Table :tableId="0" :tdata="ppi_dou_ear"></Table>
          </el-tab-pane>
          <el-tab-pane label="pie">
            <Table :tableId="0" :tdata="ppi_dou_pie"></Table>
          </el-tab-pane>
          <el-tab-pane label="pit">
            <Table :tableId="0" :tdata="ppi_dou_pit"></Table>
          </el-tab-pane>
          <el-tab-pane label="py">
            <Table :tableId="0" :tdata="ppi_dou_py"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot">
            <Table :tableId="0" :tdata="ppi_dou_shoot"></Table>
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
            <Table :tableId="1" :tdata="ppi_seq1"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene2">
            <Table :tableId="1" :tdata="ppi_seq2"></Table>
          </el-tab-pane>
          <el-tab-pane label="gen3">
            <Table :tableId="1" :tdata="ppi_seq3"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene4">
            <Table :tableId="1" :tdata="ppi_seq4"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>

    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 40px;  font-weight: bold;">Promoter-distal element interaction</h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PDI  EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" type="card" stretch class="resTabs">
          <el-tab-pane label="ear">
            <Table :tableId="0" :tdata="pdi_dou_ear"></Table>
          </el-tab-pane>
          <el-tab-pane label="py">
            <Table :tableId="0" :tdata="pdi_dou_py"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot">
            <Table :tableId="0" :tdata="pdi_dou_shoot"></Table>
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
            <Table :tableId="1" :tdata="pdi_seq1"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene2">
            <Table :tableId="1" :tdata="pdi_seq2"></Table>
          </el-tab-pane>
          <el-tab-pane label="gen3">
            <Table :tableId="1" :tdata="pdi_seq3"></Table>
          </el-tab-pane>
          <el-tab-pane label="gene4">
            <Table :tableId="1" :tdata="pdi_seq4"></Table>
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
      ppi_dou_ear: [],
      ppi_dou_shoot: [],
      ppi_dou_py: [],
      ppi_dou_pit: [],
      ppi_dou_pie: [],
      pdi_dou_ear: [],
      pdi_dou_py: [],
      pdi_dou_shoot: [],
      ppi_seq1: [],
      ppi_seq2: [],
      ppi_seq3: [],
      ppi_seq4: [],
      pdi_seq1: [],
      pdi_seq2: [],
      pdi_seq3: [],
      pdi_seq4: [],

    };
  },
  methods: {
    async getTable(){
      let result = await this.$API.reqResultInfo()
      if(result.code==200){
        this.ppi_dou_ear=result['ppi/dou_ear.csv']
        this.ppi_dou_pie=result['ppi/dou_pie.csv']
        this.ppi_dou_pit=result['ppi/dou_pit.csv']
        this.ppi_dou_py=result['ppi/dou_py.csv']
        this.ppi_dou_shoot=result['ppi/dou_shoot.csv']
        this.pdi_dou_ear=result['pdi/dou_ear.csv']
        this.pdi_dou_py=result['pdi/dou_py.csv']
        this.pdi_dou_shoot=result['pdi/dou_shoot.csv']

        this.ppi_seq1=result['ppi/tp%Zm00001d015179%Zm00001d013461.csv']
        this.ppi_seq2=result['ppi/tp%Zm00001d015196%Zm00001d015201.csv']
        this.ppi_seq3=result['ppi/tp%Zm00001d015200%Zm00001d015195.csv']
        this.ppi_seq4=result['ppi/tp%Zm00001d015437%Zm00001d015442.csv']

        this.pdi_seq1=result['pdi/tp%Dm7-172648446-172650936%Zm00001d022198.csv']
        this.pdi_seq2=result['pdi/tp%Dm7-173145242-173149220%Zm00001d022226.csv']
        this.pdi_seq3=result['pdi/tp%Dm7-179246147-179251064%Zm00001d022425.csv']
        this.pdi_seq4=result['pdi/tp%Dm8-5125573-5135954%Zm00001d008316.csv']
      }
    }
  },
  created() {
    this.getTable()
  },
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
  margin: 0 auto;
  display: flex;
  justify-content: center;
  margin: 15px;
  margin: 0 auto;
  height: 70px;
  margin-top: 50px;
  background:-webkit-linear-gradient(top,#A3EFE6,#C3EAEF) ;
  border-radius:8px
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
  /* color:#FB636F ; */
}
</style>
