<template>
  <div id="show">
    <Steps :steps1="3" :steps2="steps2"></Steps>
    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">EXPRESSION TABLE</span>
          <el-button class="dowload" icon="el-icon-download">Dowload</el-button>
        </div>
        <div>
          <!-- <el-button class="dowload" icon="el-icon-download">Dowload</el-button> -->
          <el-table :data="expData" stripe style="width: 100%" height="400">
            <el-table-column prop="Annotation1" label="Annotation1">
            </el-table-column>
            <el-table-column prop="Annotation2" label="Annotation2">
            </el-table-column>
            <el-table-column prop="exp" label="exp"> </el-table-column>
            <el-table-column prop="pre" label="pre"> </el-table-column>
          </el-table>
        </div>
      </el-card>

      <!-- <img style="width: 100%; height: 280px" src="../../dist/img/back.png" /> -->
    </div>

    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">SEQ TABLE</span>
          <el-button class="dowload" icon="el-icon-download">Dowload</el-button>
        </div>
        <div>
          <!-- <el-button class="dowload" icon="el-icon-download">Dowload</el-button> -->
          <el-table :data="data2" stripe style="width: 100%">
            <el-table-column
              v-for="(item, index) in header"
              :key="index"
              :label="item"
              align="center"
              width="110"
            >
              <template slot-scope="scope">
                <span>{{ scope.row[item] }}</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-card>
    </div>
    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">Visualization image</span>
          <el-button class="dowload" icon="el-icon-download">Dowload</el-button>
        </div>
        <div>
          <!-- <el-button class="dowload" icon="el-icon-download">Dowload</el-button> -->
          <div id="imgId" @click="openimg" class="showimg">
            <img style="width: 100%; height: 280px" :src="imgurl.chg" />
            <img style="width: 100%; height: 110px" :src="imgurl.seq" />
          </div>
        </div>
      </el-card>
    </div>
    <el-upload
      ref="uploadFile"
      :auto-upload="false"
      :limit="1"
      :multiple="false"
      :on-change="readCsv"
      :show-file-list="false"
      accept=".csv"
      action="Fake Action"
      class="upload-demo"
      style="margin-right: 10px"
    >
      <el-button type="primary">临时1</el-button>
    </el-upload>
    <el-upload
      ref="uploadFile"
      :auto-upload="false"
      :limit="1"
      :multiple="false"
      :on-change="readCsv2"
      :show-file-list="false"
      accept=".csv"
      action="Fake Action"
      class="upload-demo"
      style="margin-right: 10px"
    >
      <el-button type="primary">临时2</el-button>
    </el-upload>
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
      header: [],
      imgurl: {
        chg: require("../img/CHG_TN.png"),
        seq: require("../img/seqs.png"),
      },
      steps2: 1,
    };
  },
  methods: {
    //读取数据
    readCsv(file, fileList) {
      let reader = new FileReader();
      reader.readAsText(file.raw, "UTF-8");
      let data = [];
      reader.onload = (evt) => {
        // 读取文件内容 csv格式
        let fileString = evt.target.result;
        //转化为array对象
        // console.log(fileString);

        var delimiter = ",";
        const headers = fileString
          .slice(0, fileString.indexOf("\n"))
          .split(delimiter);
        const rows = fileString.slice(fileString.indexOf("\n") + 1).split("\n");

        headers[headers.length - 1] = headers
          .slice(-1)[0]
          .replace(/[\r\n]/g, "");

        // rows.forEach((element,index) => {
        //     rows[index]=element.replace(/[\r\n]/g, "")
        // });

        data = rows.map((row) => {
          const values = row.split(delimiter);
          return headers.reduce((object, header, index) => {
            object[header] = values[index];
            return object;
          }, {});
        });

        this.expData = data;
      };
      //最后清楚选择文件信息，可以再进行选择文件继续操作
      //   this.$refs.uploadFile.clearFiles();
    },
    readCsv2(file, fileList) {
      // console.log(file)
      let reader = new FileReader();
      reader.readAsText(file.raw, "UTF-8");
      let data = [];
      reader.onload = (evt) => {
        // 读取文件内容 csv格式
        let fileString = evt.target.result;
        //转化为array对象
        // console.log(fileString);

        var delimiter = ",";
        const headers = fileString
          .slice(0, fileString.indexOf("\n"))
          .split(delimiter);
        const rows = fileString.slice(fileString.indexOf("\n") + 1).split("\n");

        headers[headers.length - 1] = headers
          .slice(-1)[0]
          .replace(/[\r\n]/g, "");

        // rows.forEach((element,index) => {
        //     rows[index]=element.replace(/[\r\n]/g, "")
        // });
        let getLocation = rows.indexOf("");
        rows.splice(getLocation, 1);

        data = rows.map((row) => {
          const values = row.split(delimiter);
          return headers.reduce((object, header, index) => {
            object[header] = values[index];
            return object;
          }, {});
        });
        this.header = Object.keys(data[0]);
        // console.log(Object.keys(data[0]))
        this.data2 = data;
        // console.log(this.data2)
      };
      //最后清楚选择文件信息，可以再进行选择文件继续操作
      //   this.$refs.uploadFile.clearFiles();
    },
    openimg() {
      this.isShowImg = !this.isShowImg;
      if (this.isShowImg) {
        let temp = document.getElementById("imgId");
        // console.log(temp.childNodes);
        temp.childNodes[0].style.width = "160%";
        temp.childNodes[0].style.height = "340px";
        temp.childNodes[1].style.width = "160%";
        temp.childNodes[1].style.height = "160px";
        temp.setAttribute("class", "isopenimg");
      } else {
        let temp = document.getElementById("imgId");
        // console.log(temp.childNodes);
        temp.childNodes[0].style.width = "100%";
        temp.childNodes[0].style.height = "280px";
        temp.childNodes[1].style.width = "100%";
        temp.childNodes[1].style.height = "110px";
        temp.setAttribute("class", "showimg");
      }
    },
  },
  async created() {
    // const url = "../assets/ppi/dou_pit.csv";

    // const response= await fetch(url)
    // console.log('bodyUsed:', response.bodyUsed)
    
    // const body = await response.blob()
 
    // console.log(body)
 
    // console.log('bodyUsed:', response.bodyUsed)
 
    // const bodyAgain = await response.blob()
    
    // console.log(bodyAgain)
  },
};
</script>

<style>
#show {
  width: 80%;
  margin: 0 auto;
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
  background: #df6666 !important;
  border-color: #df6666 !important;
  color: #fff !important;
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
  cursor: zoom-in;
  /* width: 80%; */
}
.isopenimg {
  width: 90%;
  margin: 0 auto;
  overflow-x: scroll;
  cursor: zoom-out;
}
</style>
