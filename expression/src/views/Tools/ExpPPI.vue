<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="tool">
    <Steps :steps1="steps1"></Steps>
    <div class="tool-up">
      <div class="top-text">
        <h1 style="font-size: 35px">Maize Expression prediction base on DNA</h1>
      </div>
      <div style="margin-top: 50px">
        <div style="width: 100%">
          <!-- 输入数据模式 -->
          <el-row type="flex" justify="center">
            <el-col :span="12">
              <h1 style="margin-top: 6px; font-weight: bold">PPI Prediction</h1>
              <div style="width: 80%">
                <h3>
                  In these models, the strength of plant core promoter(labels of
                  samples) is defined as the ability to drive expression of a
                  barcoded reporter gene in maize protoplasts with or without
                  enhancer in dark.
                </h3>
                <h3>
                  Promoter proximal region interaction (PPI)
                </h3>

                <h3 style="color:#FB6672; font-weight: bold;">Please select PPI models here👇</h3>
                <el-select
                  style="width: 240px"
                  placeholder="-----Select Model-----"
                  @change="PPIchangeTools"
                  v-model="PPImodel"
                >
                  <el-option
                    v-for="value in PPImodellist"
                    :key="value"
                    :value="value"
                  >
                    {{ value }}
                  </el-option>
                </el-select>
              </div>
            </el-col>
            <el-col :span="6">
              <el-card>
                <div slot="header">
                  <span class="cardTitle">Note</span>
                </div>
                <div>
                  <p style="font-size: 15px">
                    To run the PPI-based model, you need to prepare the data in
                    fasta format, where the length of each chromatin sequence is
                    3000bp. You can upload the required forecast data and
                    forecast tasks in two formats, online or locally. Each task
                    will take different time depending on the amount of data you
                    provide. When you submit your homework, please keep it in
                    mind ID, so that you can check the results later.
                  </p>
                </div>
              </el-card>
            </el-col>

            <!-- <el-col :span="12">
              <h1 style="margin-top: 6px; font-weight: bold">PDI Prediction</h1>
              <div style="width: 80%">
                <h3>
                  In these models, the strength of plant core promoter(labels of
                  samples) is defined as the ability to drive expression of a
                  barcoded reporter gene in maize protoplasts with or without
                  enhancer in dark.
                </h3>
                <el-select
                  style="width: 240px"
                  placeholder="-----Select Model-----"
                  @change="PDIchangeTools"
                  v-model="PDImodel"
                >
                  <el-option
                    v-for="value in PDImodellist"
                    :key="value"
                    :value="value"
                  >
                    {{ value }}
                  </el-option>
                </el-select>
              </div>
            </el-col> -->
          </el-row>
          <el-tabs
            tab-position="top"
            type="border-card"
            stretch
            @tab-click="methodsChange"
            value="input"
            style="margin-top: 20px; margin-bottom: 20px"
          >
            <!-- 选择模型输入序列 -->
            <el-tab-pane label="Manual input" name="input">
              <div style="text-align: center">
                <el-alert
                  title="BE CAREFUL-------After switching the method, the entered sequence will be cleared"
                  style="width: 50%; margin: 0 auto"
                  center
                  type="info"
                  close-text="got it"
                >
                </el-alert>
                <el-input
                  type="textarea"
                  style="width: 47%; margin: 10px"
                  v-model="Seq1"
                  :disabled="!seqflag"
                  rows="4"
                  placeholder="Please select the model from above first"
                />
                <el-input
                  type="textarea"
                  style="width: 47%; margin: 10px"
                  v-model="Seq2"
                  :disabled="!seqflag"
                  rows="4"
                  placeholder="Please select the model from above first"
                />
                <el-button type="primary" @click="Checkinput"
                  >Check the sequence input</el-button
                >
                <i
                  class="el-icon-circle-check"
                  style="font-size: 25px; color: #67c23a"
                  v-show="inputFlag"
                ></i>
              </div>
            </el-tab-pane>
            <!-- 或者直接上传文件 -->
            <el-tab-pane label="Upload files" name="file">
              <el-row style="text-align: center">
                <el-col :span="4">
                  <h2 style="margin-top: 6px; font-weight: bold">
                    Or load it from disk:
                  </h2>
                </el-col>
                <el-col :span="5" style="margin-top: 10px">
                  <el-upload
                    class="upload-demo"
                    ref="upload"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :on-remove="handleRemove"
                    :on-success="handlerSuccess"
                    :on-change="fileChange"
                    :file-list="fileList"
                    :auto-upload="false"
                    accept=".fasta,.jpg"
                  >
                    <el-button
                      slot="trigger"
                      size="medium"
                      type="primary"
                      :disabled="!seqflag"
                      >选取文件</el-button
                    >
                    <el-button
                      style="margin-left: 10px"
                      size="medium"
                      icon="el-icon-upload2"
                      @click="submitUpload"
                      :disabled="!seqflag"
                      >上传到服务器</el-button
                    >
                  </el-upload>
                </el-col>
                <!-- <el-col :span="3" style="margin-top: 5px">
              <h1 style="float: left; margin-left: 40%">E-mail:</h1>
            </el-col> -->
              </el-row>
            </el-tab-pane>
          </el-tabs>

          <!-- 输入邮箱 -->
          <el-row type="flex" justify="center">
            <el-col :span="12" style="margin-top: 10px">
              <el-form :model="updataForm" ref="updataForm">
                <el-form-item
                  prop="email"
                  label="E-mail:"
                  label-width="100px"
                  :rules="[
                    {
                      required: true,
                      message: 'Please enter the email address',
                      trigger: 'blur',
                    },
                    {
                      type: 'email',
                      message: 'Please enter the correct email address',
                      trigger: ['blur', 'change'],
                    },
                  ]"
                >
                  <el-input v-model="updataForm.email"></el-input>
                </el-form-item>
              </el-form>
            </el-col>
          </el-row>
          <!-- 提交 -->
          <el-row type="flex" justify="center">
            <el-col :span="12" id="ToolButton">
              <el-button
                style="margin-top: 6px"
                type="primary"
                @click="submitInputSeq"
              >
                {{ uploading ? "Uploading" : "Start Upload" }}
              </el-button>
              <el-button
                type="danger"
                icon="el-icon-refresh-right"
                @click="resetInfo"
                >RESET</el-button
              >
              <el-button icon="el-icon-s-data">Example</el-button>
            </el-col>
          </el-row>
          <!-- <input type="file" @change="fileChange"></input> -->
        </div>
      </div>
    </div>
    <!-- <div style="width: 80%; margin-left: 10%"> -->
    <!-- <h1 style="font-weight: bold">Output:</h1> -->

    <!-- <div class="contain" style="text-align: center; font-size: 30px">
        <el-table :columns="columns" :data-source="data" bordered>
          <template slot="name" slot-scope="text">
            <a>{{ text }}</a>
          </template>
        </el-table>
      </div> -->
    <!-- <el-button
        style="margin-top: 6px; width: 20%"
        type="primary"
        @click="submitseqs"
      >
        Dowload Results
      </el-button> -->
    <!-- <hr /> -->
    <!-- </div> -->
    <!-- <div style="width: 80%; margin-left: 10%">
      <h3>
        We use Saliency to show contribution scores. The family assignment rules
        (see details) and thresholds determined by established methods (see
        details) are used to identify transcrption factors from the input
        sequences. When you input nucleic acid sequences
      </h3>
    </div>
    <div id="imgId" @click="openimg" class="showimg">
      <img style="width: 100%; height: 280px" src="../../img/CHG_TN.png" />
      <img style="width: 100%; height: 110px" src="../../img/seqs.png" />
    </div> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Message } from "element-ui";
export default {
  name: "ExpPPI",
  components: {},
  data() {
    return {
      list1: [],
      InputSeqs: "",
      loading: true,
      isShowImg: false,
      fileList: [],

      Seq1: "",
      Seq2: "",
      uploading: false,
      PPImodellist: ["SHOOT1", "EAR1", "SHOOT2", "EAR2", "TASSEL"],
      // PDImodellist: ["SHOOT1", "EAR", "SHOOT2"],
      options: [{ value: "1" }, { value: "2" }],
      columns: [
        {
          title: "Chromosome",
          dataIndex: "chromosome",
        },
        {
          title: "Expression",
          dataIndex: "expression",
        },
      ],
      data: [
        {
          key: "1",
          chromosome: "John Brown",
          expression: "300,000.00",
        },
        {
          key: "2",
          chromosome: "John Brown",
          expression: "￥00,000.00",
        },
      ],
      updataForm: {
        email: "",
      },
      PPImodel: undefined,
      // PDImodel: undefined,

      // 当前进行到第几步
      steps1: 0,
      // 表示使用的是哪种方法。0为手动，1为上传
      method: 0,
      // 检查两种数据是否校验成功
      inputFlag: false,
      fileFlag: false,
    };
  },
  computed: {
    // 输入的序列长度
    seqlenth() {
      // if (this.PPImodel) return 3000;
      // else if (this.PDImodel) return 1500;
      // else return "undetermined";
      return 3000;
    },
    // seqflag 用来表明序列是否可以输入
    seqflag() {
      if (this.PPImodel) return true;
      else return false;
    },
  },
  methods: {
    // handleChange(file) {
    //   return false;
    // },
    confirmtype() {
      this.loading = !this.loading;
      console.log(this.methltype);
    },
    // 原提交
    // submitseqs() {
    //   let dataForm = new FormData();
    //   dataForm.append("file", this.fileList[0]);
    //   dataForm.append("seq", strArr);
    //   dataForm.append("email", this.updataForm.email);
    //   dataForm.append("modelName", "NCNR_CG_DP");

    //   let seqdata = {
    //     email: "344501734@qq.com",
    //     modelName: "NCNR_CG",
    //     seq: strArr,
    //   };

    //   console.log(seqdata);
    //   uploadseq(seqdata).then((res) => {
    //     console.log(res);
    //   });
    // },

    // 新输入提交提交
    submitInputSeq() {
      // 先进行表单验证邮箱
      this.$refs.updataForm.validate((valid) => {
        if (valid) {
          // 如果是文件输入
          if (this.method == 1) {
            // 在这里进行数据整理并提交个服务器
            // 暂时直接显示成功

            // 判断步骤2是否成功
            if (this.fileFlag) {
              this.steps1 = 3;
              this.$msgbox({
                message:
                  "Upload sequence succeeded! \
                  Your email will receive an email with a TASK NAME. \
                  Please query the progress of this task according to this TASK NAME",
                type: "success",
              });
            } else {
              this.$alert(
                "Please upload the correct fasta file",
                "Step 2 is not complete",
                {
                  confirmButtonText: "confrim",
                  type: "error",
                }
              );
              return;
            }
          }
          // 如果是手动输入
          else {
            // 判断步骤2是否成功
            if (this.inputFlag) {
              this.steps1 = 3;
              this.$msgbox({
                message:
                  "Upload sequence succeeded! \
                  Your email will receive an email with a TASK NAME. \
                  Please query the progress of this task according to this TASK NAME",
                type: "success",
              });
            } else {
              this.$alert(
                "Please enter the correct sequence and verify",
                "Step 2 is not complete",
                {
                  confirmButtonText: "confrim",
                  type: "error",
                }
              );
              return;
            }
          }
        } else {
          this.$msgbox({
            message: "please enter correct email",
            type: "error",
          });
          return false;
        }
      });
    },
    // changestatue(info) {
    //   let fileList = [...info.fileList];

    //   // 1. Limit the number of uploaded files
    //   //    Only to show two recent uploaded files, and old ones will be replaced by the new
    //   fileList = fileList.slice(-1);
    //   // this.fileList = fileList;
    //   // console.log(this.fileList);
    //   fileList = fileList.map(file => {
    //     if (file.response) {
    //       // Component will show file.url as link
    //       file.url = file.response.url;
    //     }
    //     return file;
    //   });

    //   this.fileList = fileList;
    // },
    // handleChange(value) {
    //   console.log(`selected ${value}`);
    // },
    PPIchangeTools(value) {
      this.steps1 = 1;
      // if (this.PDImodel) this.PDImodel = undefined;
      // this.$router.push(`/Tools/PPI_${value}`);
      // console.log(value);
    },
    // PDIchangeTools(value) {
    //   this.steps1 = 1;
    //   if (this.PPImodel) this.PPImodel = undefined;
    //   // this.$router.push(`/Tools/PDI_${value}`);
    //   // console.log(value);
    // },
    openimg() {
      this.isShowImg = !this.isShowImg;
      if (this.isShowImg) {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "160%";
        temp.childNodes[0].style.height = "340px";
        temp.childNodes[1].style.width = "160%";
        temp.childNodes[1].style.height = "160px";
        temp.setAttribute("class", "isopenimg");
      } else {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "100%";
        temp.childNodes[0].style.height = "280px";
        temp.childNodes[1].style.width = "100%";
        temp.childNodes[1].style.height = "110px";
        temp.setAttribute("class", "showimg");
      }
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlerSuccess(response, file, fileList) {
      this.fileList = fileList;
      this.steps1 = 2;
      this.fileFlag = true;
    },
    submitUpload() {
      this.$refs.upload.submit();
    },
    // 文件改变时监视，限制文件大小
    fileChange(file, fileList) {
      this.fileList = fileList;
      const isSize = file.size / 1024 / 1024;
      let lim = 50;
      if (isSize > lim) {
        this.$msgbox({
          message: "The file size exceeds the limit. PPI:50mb PDI:80mb",
          type: "error",
        });
        const currIdx = this.fileList.indexOf(file);
        this.fileList.splice(currIdx, 1);
        return;
      }
    },
    // 输入数据方法切换,清空另一个的内容
    methodsChange(tab, event) {
      if (tab.name === "input") {
        this.fileFlag = false;
        this.method = 0;
      } else if (tab.name === "file") {
        this.method = 1;
        this.inputFlag = false;
        this.Seq1 = "";
        this.Seq2 = "";
      }
    },
    // 检查输入序列格式
    Checkinput() {
      if (
        this.Seq1.length != this.seqlenth ||
        this.Seq2.length != this.seqlenth
      ) {
        this.$alert("PPI:3000bp  PDI:1500bp ", "seq lenth error!", {
          confirmButtonText: "confrim",
          type: "error",
        });
        return;
      }
      this.steps1 = 2;
      this.inputFlag = true;
    },
    // 清空已经填入的数据
    resetInfo() {
      // 手动输入
      if (this.method == 0) {
        this.inputFlag = false;
        this.Seq1 = "";
        this.Seq2 = "";
      }
      // 上传文件
      else {
      }
    },
  },
  created() {},
};
</script>
<style scoped>
.tool {
  /* height: 1500px; */
  margin-bottom: 250px;
}
::v-deep .el-tabs__nav-scroll {
  width: 50%;
  margin: 0 auto;
}
::v-deep .el-tabs__item {
  font-size: 20px;
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

th.column-money,
td.column-money {
  text-align: right !important;
}

#ToolButton button {
  font-size: 20px;
}

#ToolButton button:nth-child(2) {
  background-color: #d32f2f;
  border-color: #d32f2f;
}
#ToolButton button:nth-child(2):hover {
  background: #df6666 !important;
  border-color: #df6666 !important;
  color: #fff !important;
}

.cardTitle {
  margin-left: 10px;
  /* margin: auto; */
  font-size: 20px;
  /* color: #FA5F6F; */
}
.el-card ::v-deep .el-card__header {
  background-color: #a5ece4;
  /* border: #A5ECE4; */
}
/* .el-card ::v-deep .el-card__body {
  background-color: #C3EAEF;
  border: #A5ECE4;
} */
</style>
