<template>
  <div id="show">
    <Steps :steps1="3" :steps2="steps2"></Steps>

    <h1
      style="
        font-size: 30px;
        font-weight: bolder;
        color: #22cab3;
        margin-top: 20px;
      "
    >
      TASK ID : {{ id }} RESULT
    </h1>

    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">EXPRESSION TABLE</span>
          <el-button
            class="dowload"
            icon="el-icon-download"
            @click="dowload(1, $event)"
            >Dowload</el-button
          >
        </div>
        <div>
          <!-- <Table :tableId="0" :tdata="expData"></Table> -->
          <el-table :data="expData" stripe style="width: 100%" height="400">
            <el-table-column prop="Ann1_name" label="Annotation1">
            </el-table-column>
            <el-table-column prop="Ann2_name" label="Annotation2">
            </el-table-column>
            <!-- <el-table-column prop="exp" label="exp"> </el-table-column> -->
            <el-table-column prop="predict_val" label="pre"> </el-table-column>
          </el-table>
        </div>
      </el-card>

      <!-- <img style="width: 100%; height: 280px" src="../../dist/img/back.png" /> -->
    </div>

    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">SEQ TABLE</span>
          <!-- <el-button
            class="dowload"
            icon="el-icon-download"
            @click="dowload(2, $event)"
            >Dowload</el-button
          > -->
          <el-select
            style="width: 240px; float: right"
            @change="seqChange"
            v-model="visSeq"
          >
            <el-option
              v-for="value in visSeqOp"
              :key="value.index"
              :value="value.index"
            >
              {{ value.value }}
            </el-option>
          </el-select>
        </div>
        <div>
          <!-- <Table :tableId="1" :tdata="data2"></Table> -->
          <Chart
            :chartName="id + '-gradient'"
            :chartHotname="id + '-HotMap'"
            v-if="visData"
            :visData="visData"
            :chartHotData="chartHotData"
          ></Chart>
        </div>
      </el-card>
    </div>
    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">Visualization image</span>
          <el-button
            class="dowload"
            icon="el-icon-download"
            @click="dowload(3, $event)"
            >Dowload</el-button
          >
        </div>
        <div>
          <!-- <el-button class="dowload" icon="el-icon-download">Dowload</el-button> -->
          <div>
            <el-image
              class="showimg"
              :src="imgurl.chg"
              :preview-src-list="[imgurl.chg, imgurl.seq]"
            >
            </el-image>
            <el-image
              class="showimg"
              :src="imgurl.seq"
              :preview-src-list="[imgurl.chg, imgurl.seq]"
            >
            </el-image>
            <!-- <img style="width: 100%; height: 280px" :src="imgurl.chg" />
            <img style="width: 100%; height: 300px" :src="imgurl.seq" /> -->
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Show",
  components: {},
  data() {
    return {
      id: this.$route.params.id,
      expData: [],
      data2: [],

      imgurl: {
        chg: "",
        seq: "",
      },
      steps2: 1,

      fileurl: [],
      dowloadTable: "",
      dowloadTable2: "",

      visSeq: 0,
      visSeqOp: [],

      visData: undefined,
      chartHotData: undefined,
    };
  },
  methods: {
    async getTaskInfo() {
      let result = await this.$API.reqTaskResultInfo(this.id);
      if (result.code == 200) {
        // console.log(result);

        this.expData = result[this.id + "_predict.csv"];
        this.data2 = result[this.id + "_saliency.csv"];
        this.fileurl = result.fileurl;
        for (var i = 0; i < this.fileurl.length; i++) {
          if (this.fileurl[i].search("tmpcvre.png") != -1)
            this.imgurl.chg = "http://124.220.197.196/" + this.fileurl[i];
          if (this.fileurl[i].search("tmp.png") != -1)
            this.imgurl.seq = "http://124.220.197.196/" + this.fileurl[i];
          if (this.fileurl[i].search("predict.csv") != -1)
            this.dowloadTable = "http://124.220.197.196/" + this.fileurl[i];
          if (this.fileurl[i].search("saliency.csv") != -1)
            this.dowloadTable2 = "http://124.220.197.196/" + this.fileurl[i];
        }
        this.visSeqOp = this.expData.map((x, index) => {
          return {
            index: index,
            value: index + " : " + x.Ann1_name + x.Ann2_name,
          };
        });
      }
    },
    dowload(flag, event) {
      let dowload_url = "http://124.220.197.196/";
      if (flag == 1) {
        dowload_url = this.dowloadTable;
        window.open(dowload_url);
      } else if (flag == 2) {
        dowload_url = this.dowloadTable2;
        window.open(dowload_url);
      } else {
        dowload_url = this.imgurl.chg;
        window.open(dowload_url);
        // this.downloadImage(dowload_url);
        dowload_url = this.imgurl.seq;
        window.open(dowload_url);
        // this.downloadImage(dowload_url);
      }
      // console.log(dowload_url)

      let target = event.target;
      if (target.nodeName === "BUTTON" || target.nodeName === "SPAN") {
        target.parentNode.blur();
      }
      target.blur();
    },

    async seqChange() {
      let result = await this.$API.reqVisImg(this.id, this.visSeq);
      // console.log(result)
      if (result.code == 200) {
        this.$nextTick(() => {
          this.visData = result.gradient;
          this.chartHotData = result.heat;
        });
      }
    },
  },
  created() {
    this.getTaskInfo();
    this.seqChange();
  },
};
</script>

<style>
#show {
  width: 75%;
  margin: 0 auto;

  text-align: center;
}

.dowload {
  font-size: 20px;
  float: right;
  height: 50px;
  color: #fff;
  background-color: #d32f2f;
  border-color: #d32f2f;
}
.dowload:hover {
  background: #df6666;
  border-color: #df6666;
  color: #fff;
}
.childShow {
  margin-top: 20px;
  margin-bottom: 20px;
}
.tableTitle {
  margin-left: 20px;
  /* margin: auto; */
  font-size: 30px;
  font-weight: bold;
}
.showimg {
  /* cursor: zoom-in; */
  width: 80%;
  height: 80%;
  /* width: 80%; */
}
</style>
