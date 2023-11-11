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
        <div id="maize" class="cursor" @click="changeType('maize')">
          <img src="../assets/picture/yumiICON.png" alt="Icon" />
          <h5>Maize</h5>
        </div>
      </div>

      <div class="product-list-item">
        <div id="rice" class="cursor" @click="changeType('rice')">
          <img
            src="../assets/picture/southeast-removebg-preview.png"
            alt="Icon"
          />
          <h5>Rice</h5>
        </div>
      </div>
      <div class="product-list-item">
        <div id="cotton" class="cursor" @click="changeType('cotton')">
          <img src="../assets/picture/mianhuaICON.png" alt="Icon" />
          <h5>Cotton</h5>
        </div>
      </div>
      <div class="product-list-item">
        <div id="wheat" class="cursor" @click="changeType('wheat')">
          <img src="../assets/picture/xiaomaiICON.png" alt="Icon" />
          <h5>Wheat</h5>
        </div>
      </div>
    </div>
    <!-- <div v-show="type == ''">
      <h1>Please select a species</h1>
    </div> -->
    <div v-loading="Loading">
      <div v-if="type == 'maize'">
        <div>
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
                <el-tab-pane label="Ear(Li et al. 2019)">
                  <Table :tdata="ppi_dou_ear"></Table>
                  <!-- <Chart chartName="chart1"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="Ear(Sun et al. 2020)">
                  <Table :tdata="ppi_dou_pie"></Table>
                  <!-- <Chart chartName="chart2"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="Tassel(Sun et al. 2020)">
                  <Table :tdata="ppi_dou_pit"></Table>
                  <!-- <Chart chartName="chart3"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="Shoot(Peng et al. 2019)">
                  <Table :tdata="ppi_dou_py"></Table>
                </el-tab-pane>
                <el-tab-pane label="Shoot(Li et al. 2019)">
                  <Table :tdata="ppi_dou_shoot"></Table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-card>
          <el-card class="resTabs">
            <div slot="header">
              <span class="tableTitle">PPI SEQ TABLE</span>
            </div>
            <div>
              <el-tabs tab-position="top" stretch class="resTabs" @tab-click="changeMaizeHot">
                <el-tab-pane label="PPI-gene1" :lazy="true">
                  <Chart
                    chartName="gradient1"
                    chartHotname="HotMap1"
                    v-if="ppi_seq1.gradient"
                    :visData="ppi_seq1.gradient"
                    :chartHotData="ppi_seq1.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PPI-gene2" :lazy="true">
                  <Chart
                    chartName="gradient2"
                    chartHotname="HotMap2"
                    v-if="ppi_seq2.gradient"
                    :visData="ppi_seq2.gradient"
                    :chartHotData="ppi_seq2.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PPI-gene3" :lazy="true">
                  <Chart
                    chartName="gradient3"
                    chartHotname="HotMap3"
                    v-if="ppi_seq3.gradient"
                    :visData="ppi_seq3.gradient"
                    :chartHotData="ppi_seq3.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PPI-gene4" :lazy="true">
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
                <el-tab-pane label="Ear(Li et al. 2019)">
                  <Table :tdata="pdi_dou_ear"></Table>
                </el-tab-pane>
                <el-tab-pane label="Shoot(Peng et al. 2019)">
                  <Table :tdata="pdi_dou_py"></Table>
                </el-tab-pane>
                <el-tab-pane label="Shoot(Li et al. 2019)">
                  <Table :tdata="pdi_dou_shoot"></Table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-card>
          <el-card class="resTabs">
            <div slot="header">
              <span class="tableTitle">PDI SEQ TABLE</span>
            </div>
            <div>
              <el-tabs tab-position="top" stretch class="resTabs"  @tab-click="changeMaizeHot">
                <el-tab-pane label="PDI-gene1" :lazy="true">
                  <Chart
                    chartName="gradient5"
                    chartHotname="HotMap5"
                    v-if="pdi_seq1.gradient"
                    :visData="pdi_seq1.gradient"
                    :chartHotData="pdi_seq1.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PDI-gene2" :lazy="true">
                  <Chart
                    chartName="gradient6"
                    chartHotname="HotMap6"
                    v-if="pdi_seq2.gradient"
                    :visData="pdi_seq2.gradient"
                    :chartHotData="pdi_seq2.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PDI-gene3" :lazy="true">
                  <Chart
                    chartName="gradient7"
                    chartHotname="HotMap7"
                    v-if="pdi_seq3.gradient"
                    :visData="pdi_seq3.gradient"
                    :chartHotData="pdi_seq3.heat"
                  ></Chart>
                </el-tab-pane>
                <el-tab-pane label="PDI-gene4" :lazy="true">
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
      </div>
      <div v-if="type == 'rice'">
        <div>
          <el-card class="resTabs">
            <div slot="header">
              <span class="tableTitle">RICE EXPRESSION TABLE</span>
            </div>
            <div>
              <el-tabs tab-position="top" stretch>
                <el-tab-pane label="H3K4me3" :lazy="true">
                  <Table :tdata="table1"></Table>
                </el-tab-pane>
                <el-tab-pane label="H3K9me2" :lazy="true">
                  <Table :tdata="table2"></Table>
                </el-tab-pane>
                <el-tab-pane label="RNAP2" :lazy="true">
                  <Table :tdata="table3"></Table>
                </el-tab-pane>
                <el-tab-pane label="H3K4">
                  <Table :tdata="table4"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_H3K4me3">
                  <Table :tdata="table5"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_H3K9me2">
                  <Table :tdata="table6"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_RNAP2">
                  <Table :tdata="table7"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_H3K4">
                  <Table :tdata="table8"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_H3K9">
                  <Table :tdata="table9"></Table>
                </el-tab-pane>
                <el-tab-pane label="Pred_ZS_RNAP2">
                  <Table :tdata="table10"></Table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-card>
        </div>
      </div>
      <div v-if="type == 'cotton'">
        <div>
          <el-card class="resTabs">
            <div slot="header">
              <span class="tableTitle">COTTON EXPRESSION TABLE</span>
            </div>
            <div>
              <el-tabs tab-position="top" stretch>
                <el-tab-pane label="A2">
                  <Table :tdata="table1"></Table>
                  <!-- <Chart chartName="chart1"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="B1">
                  <Table :tdata="table2"></Table>
                  <!-- <Chart chartName="chart2"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="C1">
                  <Table :tdata="table3"></Table>
                  <!-- <Chart chartName="chart3"></Chart> -->
                </el-tab-pane>
                <el-tab-pane label="D5">
                  <Table :tdata="table4"></Table>
                </el-tab-pane>
                <el-tab-pane label="OutA1">
                  <Table :tdata="table5"></Table>
                </el-tab-pane>
                <el-tab-pane label="OutB1">
                  <Table :tdata="table6"></Table>
                </el-tab-pane>
                <el-tab-pane label="OutC1">
                  <Table :tdata="table7"></Table>
                </el-tab-pane>
                <el-tab-pane label="OutD5">
                  <Table :tdata="table8"></Table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-card>
        </div>
      </div>
      <div v-if="type == 'wheat'">
        <div>
          <el-card class="resTabs">
            <div slot="header">
              <span class="tableTitle">WHEAT EXPRESSION TABLE</span>
            </div>
            <div>
              <el-tabs tab-position="top" stretch>
                <el-tab-pane label="Pred_wheat-interaction">
                  <Table :tdata="table1"></Table>
                </el-tab-pane>
                <el-tab-pane label="Wheat-interaction">
                  <Table :tdata="table2"></Table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-card>
        </div>
      </div>
    </div>

    <Back></Back>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Loading } from "element-ui";
import Chart from "../components/Chart.vue";

function convertToElTableFormat(data) {
  const formattedData = [];

  // 获取所有列名
  const columns = Object.keys(data);

  // 假设以第一个列数据的长度为基准，保证所有列数据的长度一致
  const numRows = data[columns[0]].length;

  for (let i = 0; i < numRows; i++) {
    const row = {};
    for (const column of columns) {
      row[column] = data[column][i];
    }
    formattedData.push(row);
  }

  return formattedData;
}

function convertToCustomFormat(array) {
  const result = [];

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array[i].length; j++) {
      result.push([j, i, array[i][j]]);
    }
  }

  return result;
}

function verticalSum(arr) {
  const n = arr[0].length;
  const result = new Array(n).fill(0);

  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < n; j++) {
      result[j] += arr[i][j];
    }
  }

  return result;
}
// 因为列是自动生成的，所以在这里调整pre的顺序
function lastpre(data) {

  const preValue = data.Prediction;
  delete data.Prediction;
  data.Prediction=preValue
  return data;
}
export default {
  name: "Result",
  components: { Chart },
  data() {
    return {
      type: "maize",

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

      table1: [],
      table2: [],
      table3: [],
      table4: [],
      table5: [],
      table6: [],
      table7: [],
      table8: [],
      table9: [],
      table10: [],


      Loading:false,
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

        // this.ppi_seq1 = result["ppi/tp%Zm00001d015179%Zm00001d013461.csv"];
        // this.ppi_seq2 = result["ppi/tp%Zm00001d015196%Zm00001d015201.csv"];
        // this.ppi_seq3 = result["ppi/tp%Zm00001d015200%Zm00001d015195.csv"];
        // this.ppi_seq4 = result["ppi/tp%Zm00001d015437%Zm00001d015442.csv"];

        // this.pdi_seq1 =
        //   result["pdi/tp%Dm7-172648446-172650936%Zm00001d022198.csv"];
        // this.pdi_seq2 =
        //   result["pdi/tp%Dm7-173145242-173149220%Zm00001d022226.csv"];
        // this.pdi_seq3 =
        //   result["pdi/tp%Dm7-179246147-179251064%Zm00001d022425.csv"];
        // this.pdi_seq4 = result["pdi/tp%Dm8-5125573-5135954%Zm00001d008316.csv"];
      }
    },
    async changeType(ty) {
      this.Loading=true

      var rediv = document.getElementById(this.type);
      rediv.classList.remove("active");

      this.type = ty;
      var div = document.getElementById(ty);
      div.classList.add("active");

      await this.getdata(ty);

      this.Loading=false

    },
    async getdata(ty) {


      let result = await this.$API.reqResultInfo(ty);
      // console.log(result);
      console.log(ty);
      if (ty == "maize") {
        // console.log(result["ppi/dou_ear.csv"])
        // console.log(lastpre(result["ppi/dou_ear.csv"]))
        this.ppi_dou_ear = convertToElTableFormat(lastpre(result["ppi/dou_ear.csv"]));
        this.ppi_dou_pie = convertToElTableFormat (lastpre(result["ppi/dou_pie.csv"]));
        this.ppi_dou_pit = convertToElTableFormat (lastpre(result["ppi/dou_pit.csv"]));
        this.ppi_dou_py = convertToElTableFormat (lastpre(result["ppi/dou_py.csv"]));
        this.ppi_dou_shoot = convertToElTableFormat (lastpre( result["ppi/dou_shoot.csv"]));
        this.pdi_dou_ear = convertToElTableFormat (lastpre(result["pdi/dou_ear.csv"]));
        this.pdi_dou_py = convertToElTableFormat (lastpre(result["pdi/dou_py.csv"]));
        this.pdi_dou_shoot = convertToElTableFormat (lastpre(result["pdi/dou_shoot.csv"]));

        // let id=1
        // let result1=await this.$API.reqMaizeHot(id)
        // if(id==1){
        //   this.ppi_seq1.heat = convertToCustomFormat(result1['data'])
        //   this.ppi_seq1.gradient = verticalSum(result1['data'])
        // }

        // await this.getMaizeHot(0);
        // await this.getMaizeHot(1);
        // await this.getMaizeHot(2);
        // await this.getMaizeHot(3);
        // await this.getMaizeHot(4);
        // await this.getMaizeHot(5);
        // await this.getMaizeHot(6);
        // await this.getMaizeHot(7);

        // this.ppi_seq1.heat = convertToCustomFormat(result["ppi/tn%Zm00001d001808%Zm00001d001799.csv"]);
        // this.ppi_seq1.gradient= verticalSum(result["ppi/tn%Zm00001d001808%Zm00001d001799.csv"]);
        // this.ppi_seq2.heat = convertToCustomFormat(result["ppi/tn%Zm00001d001831%Zm00001d001837.csv"]);
        // this.ppi_seq2.gradient = verticalSum(result["ppi/tn%Zm00001d001831%Zm00001d001837.csv"]);
        // this.ppi_seq3.heat = convertToCustomFormat(result["ppi/tn%Zm00001d001839%Zm00001d001841.csv"]);
        // this.ppi_seq3.gradient = verticalSum(result["ppi/tn%Zm00001d001839%Zm00001d001841.csv"]);
        // this.ppi_seq4.heat = convertToCustomFormat(result["ppi/tn%Zm00001d001933%Zm00001d001936.csv"]);
        // this.ppi_seq4.gradient = verticalSum(result["ppi/tn%Zm00001d001933%Zm00001d001936.csv"]);
        // // this.ppi_seq3 = result[""];
        // // this.ppi_seq4 = result[""];

        // this.pdi_seq1.heat =convertToCustomFormat(result["pdi/tp%Dm3-21615911-21620132%Zm00001d039976.csv"]);
        // this.pdi_seq1.gradient =verticalSum(result["pdi/tp%Dm3-21615911-21620132%Zm00001d039976.csv"]);
        // this.pdi_seq2.heat =convertToCustomFormat (result["pdi/tp%Dm3-172766947-172771212%Zm00001d042589.csv"]);
        // this.pdi_seq2.gradient =verticalSum (result["pdi/tp%Dm3-172766947-172771212%Zm00001d042589.csv"]);
        // this.pdi_seq3.heat =convertToCustomFormat (result["pdi/tp%Dm3-196060252-196064377%Zm00001d043312.csv"]);
        // this.pdi_seq3.gradient =verticalSum (result["pdi/tp%Dm3-196060252-196064377%Zm00001d043312.csv"]);
        // this.pdi_seq2.heat =convertToCustomFormat (result["pdi/tp%Dm3-203900476-203903784%Zm00001d043562.csv"]);
        // this.pdi_seq2.gradient =verticalSum (result["pdi/tp%Dm3-203900476-203903784%Zm00001d043562.csv"]);
        // this.pdi_seq3 =
        //   result["pdi/tp%Dm7-179246147-179251064%Zm00001d022425.csv"];
        // this.pdi_seq4 = result["pdi/tp%Dm8-5125573-5135954%Zm00001d008316.csv"];
      } else if (ty == "rice") {
        this.table1 =  convertToElTableFormat(result["rice/MH63.H3K4me3.csv"]);
        this.table2 =  convertToElTableFormat(result["rice/MH63.H3K9me2.csv"]);
        this.table3 =  convertToElTableFormat(result["rice/MH63.RNAP2.csv"]);
        this.table4 =  convertToElTableFormat(result["rice/ZS_H3K4.csv"]);
        this.table5 =  convertToElTableFormat (lastpre(result["rice/pred_MH_MH63.H3K4me3.csv"]));
        this.table6 =  convertToElTableFormat (lastpre(result["rice/pred_MH_MH63.H3K9me2.csv"]));
        this.table7 = convertToElTableFormat (lastpre(result["rice/pred_MH_MH63.RNAP2.csv"]));
        this.table8 =  convertToElTableFormat (lastpre(result["rice/pred_ZS_ZS_H3K4.csv"]));
        this.table9 =  convertToElTableFormat (lastpre(result["rice/pred_ZS_ZS_H3K9.csv"]));
        this.table10 =  convertToElTableFormat (lastpre(result["rice/pred_ZS_ZS_RNAP2.csv"]));
      }else if(ty=='cotton'){
        this.table1 = convertToElTableFormat(result["cotton/A2-enhancer-gene.csv"]);
        this.table2 = convertToElTableFormat(result["cotton/B1-enhancer-genedu.csv"]);
        this.table3 = convertToElTableFormat(result["cotton/C1-gene-genedu.csv"]);
        this.table4 = convertToElTableFormat(result["cotton/D5-enhancer-genedu.csv"]);
        this.table5 = convertToElTableFormat(result["cotton/output_A2_enhancer-gene.csv"]);
        this.table6 = convertToElTableFormat(result["cotton/output_B1_gene-enhancer.csv"]);
        this.table7 = convertToElTableFormat(result["cotton/output_C1_gene-gene.csv"]);
        this.table8 = convertToElTableFormat(result["cotton/output_D5_enhancer-gene.csv"]);

      }else{
        this.table1 = convertToElTableFormat (lastpre(result["wheat/pred_wheat-interaction-experssion(TPM).csv"]));
        this.table2 = convertToElTableFormat(result["wheat/wheat-interaction-experssion(TPM).csv"]);
      }

    },
    async changeMaizeHot(tab, event){
      console.log(tab, event);
      if(tab.label=='PPIgene1') {await this.getMaizeHot(0)}
      else if(tab.label=='PPIgene2') {await this.getMaizeHot(1);}
    },

    async getMaizeHot(id){
      let result=await this.$API.reqMaizeHot(id)
      if(id==0){
        this.ppi_seq1.heat = convertToCustomFormat(result['data'])
        this.ppi_seq1.gradient = verticalSum(result['data'])
      }else if(id==1){
        this.ppi_seq2.heat = convertToCustomFormat(result['data'])
        this.ppi_seq2.gradient = verticalSum(result['data'])
      }else if(id==2){
        this.ppi_seq3.heat = convertToCustomFormat(result['data'])
        this.ppi_seq3.gradient = verticalSum(result['data'])
      }else if(id==3){
        this.ppi_seq4.heat = convertToCustomFormat(result['data'])
        this.ppi_seq4.gradient = verticalSum(result['data'])
      }else if(id==4){
        this.pdi_seq1.heat = convertToCustomFormat(result['data'])
        this.pdi_seq1.gradient = verticalSum(result['data'])
      }else if(id==5){
        this.pdi_seq2.heat = convertToCustomFormat(result['data'])
        this.pdi_seq2.gradient = verticalSum(result['data'])
      }else if(id==6){
        this.pdi_seq3.heat = convertToCustomFormat(result['data'])
        this.pdi_seq3.gradient = verticalSum(result['data'])
      }else if(id==7){
        this.pdi_seq4.heat = convertToCustomFormat(result['data'])
        this.pdi_seq4.gradient = verticalSum(result['data'])
      }

    },
  },
  // async created(){
  //   await this.getMaizeHot(0);
  //   console.log(this.ppi_seq1.gradient!=undefined)
  // },
  async mounted() {
    // this.getTable();

    await this.getMaizeHot(0);
    await this.getMaizeHot(1);
    await this.getMaizeHot(2);
    await this.getMaizeHot(3);
    await this.getMaizeHot(4);
    await this.getMaizeHot(5);
    await this.getMaizeHot(6);
    await this.getMaizeHot(7);

    this.changeType(this.type);
    
    // console.log(this.ppi_seq1.gradient!=undefined)

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
/* ::v-deep .el-tabs__item {
  font-size: 20px;
} */

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

.active {
  /* background: #f7c35f !important; */
  background: #42b983 !important;
}
.active h5 {
  color: #04000b;
}
.product-list-box {
  max-width: 900px;
}

</style>
