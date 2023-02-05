<template>
  <div id="show">
    <Steps :steps1="3" :steps2="steps2"></Steps>

    <h1 style="font-size: 30px;font-weight: bolder;color:#22CAB3;margin-top: 20px;">TASK ID : {{ id }} RESULT</h1>

    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">EXPRESSION TABLE</span>
          <el-button class="dowload" icon="el-icon-download" @click="dowload(1,$event)"
            >Dowload</el-button
          >
        </div>
        <div>
          <Table :tableId="0" :tdata="expData"></Table>
        </div>
      </el-card>

      <!-- <img style="width: 100%; height: 280px" src="../../dist/img/back.png" /> -->
    </div>

    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">SEQ TABLE</span>
          <el-button class="dowload" icon="el-icon-download" @click="dowload(2,$event)"
            >Dowload</el-button
          >
        </div>
        <div>
          <Table :tableId="1" :tdata="data2"></Table>
        </div>
      </el-card>
    </div>
    <div class="childShow">
      <el-card>
        <div slot="header">
          <span class="tableTitle">Visualization image</span>
          <el-button class="dowload" icon="el-icon-download" @click="dowload(3,$event)"
            >Dowload</el-button
          >
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
      
      fileurl:[]
    };
  },
  methods: {
    //读取数据
    // readCsv(file, fileList) {
    //   let reader = new FileReader();
    //   reader.readAsText(file.raw, "UTF-8");
    //   let data = [];
    //   reader.onload = (evt) => {
    //     // 读取文件内容 csv格式
    //     let fileString = evt.target.result;
    //     //转化为array对象
    //     // console.log(fileString);

    //     var delimiter = ",";
    //     const headers = fileString
    //       .slice(0, fileString.indexOf("\n"))
    //       .split(delimiter);
    //     const rows = fileString.slice(fileString.indexOf("\n") + 1).split("\n");

    //     headers[headers.length - 1] = headers
    //       .slice(-1)[0]
    //       .replace(/[\r\n]/g, "");

    //     // rows.forEach((element,index) => {
    //     //     rows[index]=element.replace(/[\r\n]/g, "")
    //     // });

    //     data = rows.map((row) => {
    //       const values = row.split(delimiter);
    //       return headers.reduce((object, header, index) => {
    //         object[header] = values[index];
    //         return object;
    //       }, {});
    //     });

    //     this.expData = data;
    //   };
    //   //最后清楚选择文件信息，可以再进行选择文件继续操作
    //   //   this.$refs.uploadFile.clearFiles();
    // },
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
    async getTaskInfo() {
      let result = await this.$API.reqTaskResultInfo(this.id);
      if (result.code == 200) {
        this.expData = result["1_1_2.csv"];
        this.data2 = result["1_1_1.csv"];
        this.fileurl=result.fileurl
        this.imgurl.chg="http://124.220.197.196/"+result.fileurl[1]
        this.imgurl.seq="http://124.220.197.196/"+result.fileurl[1]
      }
    },
    dowload(flag,event) {
      let dowload_url="http://124.220.197.196/"
      if(flag==1){
        dowload_url=dowload_url+this.fileurl[2]
      }else if(flag==2){
        dowload_url=dowload_url+this.fileurl[0]
      }else{
        dowload_url=dowload_url+this.fileurl[1]
      }
      // console.log(dowload_url)
      window.open(dowload_url)
      
      let target = event.target;
      if (target.nodeName === "BUTTON" || target.nodeName === "SPAN"){
          target.parentNode.blur();
      }
      target.blur();

    },
  },
  created() {
    this.getTaskInfo();
  },
};
</script>

<style>
#show {
  width: 80%;
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
  background: #df6666 ;
  border-color: #df6666 ;
  color: #fff ;
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
