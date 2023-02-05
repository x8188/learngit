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
              <h1 style="margin-top: 6px; font-weight: bold">PDI Prediction</h1>
              <div style="width: 80%">
                <h3>
                  In these models, the strength of plant core promoter(labels of
                  samples) is defined as the ability to drive expression of a
                  barcoded reporter gene in maize protoplasts with or without
                  enhancer in dark.
                </h3>
                <h3>Promoter-distal element interactions (PDI)</h3>
                <h3 style="color: #fb6672; font-weight: bold">
                  Please select PDI models here👇
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
            </el-col>
            <el-col :span="6">
              <el-card>
                <div slot="header">
                  <span class="cardTitle">Note</span>
                </div>
                <div>
                  <p>
                    To run a PDI-based model, you need to prepare the data in
                    fasta format, where each chromatin sequence is 1500bp in
                    length. You can upload the required forecast data and
                    forecast tasks in two formats, online or locally. Each task
                    will take different time depending on the amount of data you
                    provide. When you submit your homework, please keep it in
                    mind ID, so that you can check the results later.
                  </p>
                </div>
              </el-card>
            </el-col>
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
                  @blur="checkinput(1)"
                />
                <el-input
                  type="textarea"
                  style="width: 47%; margin: 10px"
                  v-model="Seq2"
                  :disabled="!seqflag"
                  rows="4"
                  placeholder="Please select the model from above first"
                  @blur="checkinput(2)"
                />
              </div>
            </el-tab-pane>
            <!-- 或者直接上传文件 -->
            <el-tab-pane label="Upload files" name="file">
              <el-row style="text-align: center">
                <el-alert
                  title="BE CAREFUL-------After switching the method, the uploaded file will be cleared"
                  style="width: 50%; margin: 0 auto"
                  center
                  type="info"
                  close-text="got it"
                >
                </el-alert>
                <el-col :span="24" style="margin-top: 10px">
                  <div>
                    <h1
                      v-if="!seqflag"
                      style="color: #fb6672; font-weight: bold"
                    >
                      👆👆👆 Please select the model from above first
                    </h1>
                    <h1
                      v-if="fileFlag"
                      style="color: #47b347; font-weight: bold"
                    >
                      Successfully uploaded the file
                    </h1>
                  </div>
                  <el-upload
                    class="upload-demo"
                    drag
                    action=""
                    multiple
                    :on-change="fileChange"
                    :file-list="fileList"
                    :auto-upload="false"
                    accept=".fasta"
                    :disabled="!seqflag"
                    :limit="1"
                  >
                    <div v-if="seqflag">
                      <i class="el-icon-upload"></i>
                      <div class="el-upload__text">
                        Drop files here, Or <em>Click Upload</em>
                      </div>
                    </div>
                    <div v-else>
                      <i class="el-icon-upload" style="color: #d32f2f"></i>
                      <div class="el-upload__text">
                        You haven't selected the model from above
                      </div>
                    </div>
                    <div class="el-upload__tip" slot="tip">
                      Only .fasta files can be uploaded
                    </div>
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
                      trigger: ['blur'],
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
            <div id="ToolButton">
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
            </div>
          </el-row>
          <!-- <input type="file" @change="fileChange"></input> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Message } from "element-ui";
export default {
  name: "ExpPDI",
  components: {},
  data() {
    return {
      fileList: [],

      Seq1: "",
      Seq2: "",
      uploading: false,
      PDImodellist: ["SHOOT1", "EAR", "SHOOT2"],
      updataForm: {
        email: "",
      },
      PDImodel: undefined,

      // 当前进行到第几步
      steps1: 0,
      // 表示使用的是哪种方法。0为手动，1为上传
      method: 0,
      // 检查两种数据是否校验成功
      inputFlag: false,
      fileFlag: false,

      taskBoby_seq: {
        modelName: "testseq",
        seq: [],
        email: "",
      },

      taskBoby_file: {
        modelName: "testfile",
        email: "",
      },
    };
  },
  computed: {
    // 输入的序列长度
    seqlenth() {
      return 1500;
    },
    // seqflag 用来表明序列是否可以输入
    seqflag() {
      if (this.PDImodel) return true;
      else return false;
    },
  },
  methods: {
    // handleChange(file) {
    //   return false;
    // },

    // 新输入提交提交
    submitInputSeq() {
      // 先进行表单验证邮箱
      this.$refs.updataForm.validate(async (valid) => {
        if (valid) {
          // 如果是文件输入
          if (this.method == 1) {
            // 在这里进行数据整理并提交个服务器

            // 判断步骤2是否成功
            if (this.fileFlag) {
              this.taskBoby_file.file = this.fileList[0].raw;
              this.taskBoby_file.email = this.updataForm.email;

              let result = await this.$API.reqSubmitFlie(this.taskBoby_file);

              if (result.code == 200) {
                this.steps1 = 3;
                this.$msgbox({
                  message:
                    "Upload sequence succeeded! \
                  Your email will receive an email with a TASK NAME. \
                  Please query the progress of this task according to this TASK NAME",
                  type: "success",
                });
              }
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
              this.taskBoby_seq.seq.push(this.Seq1);
              this.taskBoby_seq.seq.push(this.Seq2);
              this.taskBoby_seq.email = this.updataForm.email;

              let result = await this.$API.reqSubmitSeq(this.taskBoby_seq);

              if (result.code == 200) {
                this.steps1 = 3;
                this.$msgbox({
                  message:
                    "Upload sequence succeeded! \
                  Your email will receive an email with a TASK NAME. \
                  Please query the progress of this task according to this TASK NAME",
                  type: "success",
                });
              }
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
    PDIchangeTools(value) {
      this.steps1 = 1;
    },

    // 文件改变时监视，限制文件大小
    fileChange(file, fileList) {
      // this.fileList = fileList;
      const isSize = file.size / 1024 / 1024;
      let lim = 80;
      if (isSize > lim) {
        this.$msgbox({
          message: "The file size exceeds the limit. PPI:50mb PDI:80mb",
          type: "error",
        });
        // const currIdx = this.fileList.indexOf(file);
        // this.fileList.splice(currIdx, 1);
        return;
      }
      this.fileList = fileList;
      this.steps1 = 2;
      this.fileFlag = true;
    },
    // 输入数据方法切换,清空另一个的内容
    methodsChange(tab, event) {
      if (tab.name === "input") {
        this.fileFlag = false;
        this.method = 0;
        this.fileList = [];
      } else if (tab.name === "file") {
        this.method = 1;
        this.inputFlag = false;
        this.Seq1 = "";
        this.Seq2 = "";
      }
    },
    // 检查输入序列格式
    checkinput(seq) {
      if ((seq == 1 && this.Seq2 != "") || (seq == 2 && this.Seq1 != "")) {
        if (
          this.Seq1.length > this.seqlenth ||
          this.Seq2.length > this.seqlenth
        ) {
          this.$alert("PPI:3000bp  PDI:1500bp ", "seq lenth error!", {
            confirmButtonText: "confrim",
            type: "error",
          });
          return;
        }
        this.steps1 = 2;
        this.inputFlag = true;
      }
    },
    // 清空已经填入的数据
    resetInfo() {
      this.PDImodel="";
      // 手动输入
      if (this.method == 0) {
        this.inputFlag = false;
        this.Seq1 = "";
        this.Seq2 = "";
      }
      // 上传文件
      else {
        this.fileFlag=false
        this.fileList=[];
      }

      this.updataForm.email="" 
      this.steps1 = 0;
    },
  },
  created() {},
};
</script>
<style scoped>
.tool {
  /* height: 1500px; */
  margin-bottom: 50px;
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
  margin: 0 auto;
  height: 70px;
  margin-top: 30px;

  /* background:-webkit-linear-gradient(left,#93a5cf,#e4efe9) ; */
  background: -webkit-linear-gradient(left, #fff1eb, #ace0f9);
  border-radius: 8px;
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
  /* color: #f1b0a4; */
}

.el-card ::v-deep .el-card__header {
  background-color: #a5ece4;
  /* border: #A5ECE4; */
}
</style>
