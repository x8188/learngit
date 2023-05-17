<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="result">
    <!-- <div style="margin: 15px; margin: 0 auto; width: 80%; text-align: center">
      <h1>This is an result page</h1>
    </div> -->
    <div class="product-list-box" style="width: 70%; margin: 0 auto">
      <div class="product-list-item">
        <div class="cursor" @click="changeType('Corn')">
          <img src="../assets/picture/yumiICON.png" alt="Icon" />
          <h5>Corn</h5>
        </div>
      </div>

      <div class="product-list-item">
        <div class="cursor"  @click="changeType('Rice')">
          <img
            src="../assets/picture/southeast-removebg-preview.png"
            alt="Icon"
          />
          <h5>Rice</h5>
        </div>
      </div>
      <div class="product-list-item">
        <div class="cursor"  @click="changeType('Cotton')">
          <img src="../assets/picture/mianhuaICON.png" alt="Icon" />
          <h5>Cotton</h5>
        </div>
      </div>
      <div class="product-list-item">
        <div class="cursor"  @click="changeType('Rice')">
          <img
            src="../assets/picture/southeast-removebg-preview.png"
            alt="Icon"
          />
          <h5>Rice</h5>
        </div>
      </div>
    </div>
    <div v-show="type==''">
      <h1>Please select a species</h1>
    </div>
    <div v-show="type=='Corn'">
      <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 40px; font-weight: bold">
        Promoter proximal region interaction
      </h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PPI EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" stretch>
          <el-tab-pane label="ear(Li et al. 2019)">
            <Table :tableId="0" :tdata="ppi_dou_ear"></Table>
            <!-- <Chart chartName="chart1"></Chart> -->
          </el-tab-pane>
          <el-tab-pane  label="ear(Sun et al. 2020)">
            <Table :tableId="0" :tdata="ppi_dou_pie"></Table>
            <!-- <Chart chartName="chart2"></Chart> -->
          </el-tab-pane>
          <el-tab-pane label="tassel(Sun et al. 2020)">
            <Table :tableId="0" :tdata="ppi_dou_pit"></Table>
            <!-- <Chart chartName="chart3"></Chart> -->
          </el-tab-pane>
          <el-tab-pane label="shoot(Peng et al. 2019)">
            <Table :tableId="0" :tdata="ppi_dou_py"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot(Li et al. 2019)">
            <Table :tableId="0" :tdata="ppi_dou_shoot"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PPI SEQ TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" stretch class="resTabs">
          <el-tab-pane label="gene1" :lazy="true">
            <Chart
              chartName="gradient1"
              chartHotname="HotMap1"
              v-if="ppi_seq1.gradient"
              :visData="ppi_seq1.gradient"
              :chartHotData="ppi_seq1.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gene2" :lazy="true">
            <Chart
              chartName="gradient2"
              chartHotname="HotMap2"
              v-if="ppi_seq2.gradient"
              :visData="ppi_seq2.gradient"
              :chartHotData="ppi_seq2.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gen3" :lazy="true">
            <Chart
              chartName="gradient3"
              chartHotname="HotMap3"
              v-if="ppi_seq3.gradient"
              :visData="ppi_seq3.gradient"
              :chartHotData="ppi_seq3.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gene4" :lazy="true">
            <Chart
              chartName="gradient4"
              chartHotname="HotMap4"
              v-if="ppi_seq4.gradient"
              :visData="ppi_seq4.gradient"
              :chartHotData="ppi_seq4.heat"
            ></Chart>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>

    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 40px; font-weight: bold">
        Promoter-distal element interaction
      </h1>
      <!-- </div> -->
    </div>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PDI EXPRESSION TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" stretch class="resTabs">
          <el-tab-pane label="ear(Li et al. 2019)">
            <Table :tableId="0" :tdata="pdi_dou_ear"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot(Peng et al. 2019)">
            <Table :tableId="0" :tdata="pdi_dou_py"></Table>
          </el-tab-pane>
          <el-tab-pane label="shoot(Li et al. 2019)">
            <Table :tableId="0" :tdata="pdi_dou_shoot"></Table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>
    <el-card class="resTabs">
      <div slot="header">
        <span class="tableTitle">PDI SEQ TABLE</span>
      </div>
      <div>
        <el-tabs tab-position="top" stretch class="resTabs">
          <el-tab-pane label="gene1" :lazy="true">
            <Chart
              chartName="gradient5"
              chartHotname="HotMap5"
              v-if="pdi_seq1.gradient"
              :visData="pdi_seq1.gradient"
              :chartHotData="pdi_seq1.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gene2" :lazy="true">
            <Chart
              chartName="gradient6"
              chartHotname="HotMap6"
              v-if="pdi_seq2.gradient"
              :visData="pdi_seq2.gradient"
              :chartHotData="pdi_seq2.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gen3" :lazy="true">
            <Chart
              chartName="gradient7"
              chartHotname="HotMap7"
              v-if="pdi_seq3.gradient"
              :visData="pdi_seq3.gradient"
              :chartHotData="pdi_seq3.heat"
            ></Chart>
          </el-tab-pane>
          <el-tab-pane label="gene4" :lazy="true">
            <Chart
              chartName="gradient8"
              chartHotname="HotMap8"
              v-if="pdi_seq3.gradient"
              :visData="pdi_seq3.gradient"
              :chartHotData="pdi_seq3.heat"
            ></Chart>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-card>


    </div>
    <div v-show="type=='Rice'">
      <h1>Rice</h1>
    </div>
    <div v-show="type=='Cotton'">
      <h1>Cotton</h1>
    </div>
    <div v-show="type=='Rice'">
      <h1>Rice</h1>
    </div>
    <Back></Back>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Chart from "../components/Chart.vue";
export default {
  name: "Result",
  components: { Chart },
  data() {
    return {
      type:"",

      ppi_dou_ear: [],
      ppi_dou_shoot: [],
      ppi_dou_py: [],
      ppi_dou_pit: [],
      ppi_dou_pie: [],
      pdi_dou_ear: [],
      pdi_dou_py: [],
      pdi_dou_shoot: [],
      ppi_seq1: {},
      ppi_seq2: {},
      ppi_seq3: {},
      ppi_seq4: {},
      pdi_seq1: {},
      pdi_seq2: {},
      pdi_seq3: {},
      pdi_seq4: {},
    };
  },
  methods: {
    async getTable() {
      let result = await this.$API.reqResultInfo();
      if (result.code == 200) {
        this.ppi_dou_ear = result["ppi/dou_ear.csv"];
        this.ppi_dou_pie = result["ppi/dou_pie.csv"];
        this.ppi_dou_pit = result["ppi/dou_pit.csv"];
        this.ppi_dou_py = result["ppi/dou_py.csv"];
        this.ppi_dou_shoot = result["ppi/dou_shoot.csv"];
        this.pdi_dou_ear = result["pdi/dou_ear.csv"];
        this.pdi_dou_py = result["pdi/dou_py.csv"];
        this.pdi_dou_shoot = result["pdi/dou_shoot.csv"];

        this.ppi_seq1 = result["ppi/tp%Zm00001d015179%Zm00001d013461.csv"];
        this.ppi_seq2 = result["ppi/tp%Zm00001d015196%Zm00001d015201.csv"];
        this.ppi_seq3 = result["ppi/tp%Zm00001d015200%Zm00001d015195.csv"];
        this.ppi_seq4 = result["ppi/tp%Zm00001d015437%Zm00001d015442.csv"];

        this.pdi_seq1 =
          result["pdi/tp%Dm7-172648446-172650936%Zm00001d022198.csv"];
        this.pdi_seq2 =
          result["pdi/tp%Dm7-173145242-173149220%Zm00001d022226.csv"];
        this.pdi_seq3 =
          result["pdi/tp%Dm7-179246147-179251064%Zm00001d022425.csv"];
        this.pdi_seq4 = result["pdi/tp%Dm8-5125573-5135954%Zm00001d008316.csv"];
      }
    },
    changeType(ty){
      this.type=ty
    }
  },
  created() {
    this.getTable();
  },
};
</script>

<style scoped src='../assets/css/style.css'></style>

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
  /* background:-webkit-linear-gradient(top,#A3EFE6,#C3EAEF) ; */
  border-radius: 8px;
}
::v-deep .el-tabs__nav-scroll {
  width: 100%;
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
