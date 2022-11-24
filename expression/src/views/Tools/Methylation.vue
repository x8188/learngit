<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="tool">
    <Steps></Steps>
    <div class="tool-up">
      <div class="top-text">
        <h1 style="font-size: 35px">
          Maize DNA methylation level prediction and analysis
        </h1>
        <h3>
          Introductions ntroductions ntroductions ntroductions
          ntroductionsntroductions ntroductions ntroductions ntroductions
          ntroductionsntroductions ntroductions ntroductions ntroductions
          ntroductions
        </h3>
      </div>

      <div style="margin-top: 50px; height: 330px; text-align: center">
        <a-row>
          <a-col :span="12">
            <div>
              <h2>Choose your methylation type 👇</h2>
              <div>
                <a-select style="width: 120px" v-model="methltype">
                  <a-select-option v-for="value in typelist" :key="value" :value="value">
                    {{ value }}
                  </a-select-option>
                </a-select>
                <a-button style="margin-top: 6px" type="primary" @click="confirmtype">
                  Confirm
                </a-button>
              </div>
              <a-spin style="margin-top: 50px" size="large" :spinning="loading" />
              <a-result v-show="!loading" status="success" title="Successfully Load Model!!" />
            </div>
          </a-col>
          <a-col :span="12">
            <div>
              <h2>Paste one sequence(3001bp) here 👇</h2>
              <a-textarea v-model="InputSeqs" placeholder="Input your Seqs" :auto-size="{ minRows: 10, maxRows: 10 }" />
              <a-row style="text-align: center">
                <a-col :span="10">
                  <h2 style="margin-top: 6px; font-weight: bold">
                    Or load it from disk:
                  </h2>
                </a-col>
                <a-col :span="6">
                  <a-upload :file-list="fileList" :disabled="isDisabled" :before-upload="handleChange"
                    @change="changestatue">
                    <a-button>
                      <a-icon :disabled="isDisabled" type="upload" />Click to
                      Upload
                    </a-button>
                  </a-upload>
                </a-col>
              </a-row>
              <a-row>
                <a-col :span="6">
                  <h1 style="float: left; margin-left: 40%">E-mail:</h1>
                </a-col>
                <a-col :span="12">
                  <a-input v-model="email" type="email" />
                </a-col>
              </a-row>
              <a-button style="margin-top: 6px" type="primary" block @click="submitseqs">
                {{ uploading ? "Uploading" : "Start Upload" }}
              </a-button>
            </div>
          </a-col>
        </a-row>
      </div>
    </div>
    <div style="width: 80%; margin-left: 12%">
      <h1>Heatmap:</h1>
    </div>
    <div id="imgId" @click="openimg" class="showimg">
      <img style="width: 100%; height: 280px" src="../../img/CHG_TN.png" />
      <img style="width: 100%; height: 110px" src="../../img/seqs.png" />
    </div>
  </div>
</template>

<script>
import { getResult, uploadfile, uploadseq } from "../../request/api.js";

export default {
  name: "Methylation",
  components: {},

  data() {
    return {
      list1: [],
      typelist: [
        "NCNR_CG",
        "NCNR_CHG",
        "TE_CG",
        "TE_CHG",
        "CODE_CG",
        "CODE_CHG",
      ],
      InputSeqs: ">",
      loading: true,
      uploading: false,
      methltype: "NCNR_CG",
      isShowImg: false,
      preresult: "",
      fileList: [],
      isDisabled: false,
      email: "",
    };
  },
  methods: {
    confirmtype() {
      this.loading = false;
    },
    handleChange(file) {
      file;
      // console.log(file);
      return false;
    },
    changestatue(info) {
      let fileList = [...info.fileList];

      // 1. Limit the number of uploaded files
      //    Only to show two recent uploaded files, and old ones will be replaced by the new
      fileList = fileList.slice(-1);
      this.fileList = fileList;
      console.log(this.fileList);
    },
    submitseqs() {
      let strArr = [];
      let str = "";
      for (var i = 1; i < this.InputSeqs.length; i++) {
        //遍历字符串，枚举每个字符
        if (this.InputSeqs[i] != ">") {
          if (this.InputSeqs[i] != "\n") str += this.InputSeqs[i];
        } else {
          strArr.push(str);
          str = "";
        }
      }
      strArr.push(str);
      // console.log(strArr);
      let dataForm = new FormData();
      dataForm.append("file", this.fileList[0]);
      dataForm.append("seq", strArr);
      dataForm.append("email", this.email);
      dataForm.append("modelName", "NCNR_CG_DP");

      let seqdata = {
        email: "344501734@qq.com",
        modelName: "NCNR_CG_DP",
        seq: strArr,
      };

      console.log(seqdata);
      uploadseq(seqdata).then((res) => {
        console.log(res);
      });
      // uploadfile(dataForm).then((res) => {
      //   console.log(res);
      // });
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
  created() { },
};
</script>
<style scoped>
.tool {
  height: 1500px;
}

.tool-up {
  width: 80%;
  margin: 0 auto;
}

.top-text {
  text-align: center;
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

.upload-list-inline :deep(.ant-upload-list-item) {
  float: left;
  width: 200px;
  margin-right: 8px;
}

.upload-list-inline [class*="-upload-list-rtl"] :deep(.ant-upload-list-item) {
  float: right;
}
</style>