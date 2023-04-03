<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div>
    <!-- <div class="choose-us-style-one-area overflow-hidden default-padding">
      <div class="container">
        <div class="row align-center">
          <div class="col-lg-6 choose-us-style-one">
            <div class="thumb">
              <img src="../../assets/picture/1.jpg" alt="Image Not Found" />
              <div class="shape">
                <img
                  class="wow fadeInDown"
                  src="../../assets/picture/22.png"
                  alt="Image not found"
                />
              </div>
              <div class="product-produce">
                <div class="icon">
                  <i class="flaticon-farmer"></i>
                </div>
                <div class="fun-fact">
                  <div class="counter">
                    <div class="timer" data-to="258" data-speed="2000">258</div>
                    <div class="operator">K</div>
                  </div>
                  <span class="medium">Agriculture, Organic Products</span>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6 choose-us-style-one">
            <h5 class="sub-title">Get to know us</h5>
            <h2 class="title">
              Agriculture matters to <br />
              the future of development
            </h2>
            <div class="accordion accordion-regular mt-35" id="faqAccordion">
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                  <button
                    class="accordion-button"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseOne"
                    aria-expanded="true"
                    aria-controls="collapseOne"
                  >
                    What do you add to the soil before you plant a crop?
                  </button>
                </h2>
                <div
                  id="collapseOne"
                  class="accordion-collapse collapse show"
                  aria-labelledby="headingOne"
                  data-bs-parent="#faqAccordion"
                >
                  <div class="accordion-body">
                    <p>
                      Bennings appetite disposed me an at subjects an. To no
                      indulgence diminution so discovered mr apartments. Are off
                      under folly death wrote cause her way spite. Plan upon yet
                      way get cold spot its week.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingTwo">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseTwo"
                    aria-expanded="false"
                    aria-controls="collapseTwo"
                  >
                    Do you use herbicides?
                  </button>
                </h2>
                <div
                  id="collapseTwo"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingTwo"
                  data-bs-parent="#faqAccordion"
                >
                  <div class="accordion-body">
                    <p>
                      Cennings appetite disposed me an at subjects an. To no
                      indulgence diminution so discovered mr apartments. Are off
                      under folly death wrote cause her way spite. Plan upon yet
                      way get cold spot its week.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingThree">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseThree"
                    aria-expanded="false"
                    aria-controls="collapseThree"
                  >
                    Where does the water come from that you use on your crops?
                  </button>
                </h2>
                <div
                  id="collapseThree"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingThree"
                  data-bs-parent="#faqAccordion"
                >
                  <div class="accordion-body">
                    <p>
                      Tennings appetite disposed me an at subjects an. To no
                      indulgence diminution so discovered mr apartments. Are off
                      under folly death wrote cause her way spite. Plan upon yet
                      way get cold spot its week.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
    <div class="tool">
      <Steps :steps1="steps1"></Steps>
      <div class="tool-up">
        <div class="top-text">
          <h1 style="font-size: 35px; font-weight: bolder">
            Maize Expression prediction base on DNA
          </h1>
        </div>

        <div style="margin-top: 20px">
          <div style="width: 100%">
            <!-- 输入数据模式 -->
            <el-row type="flex" justify="center">
              <el-col :span="12">
                <el-card class="cardModel">
                  <div slot="header">
                    <span class="mdoelT">MH63 Prediction</span>
                  </div>
                  <div>
                    <h3>
                      In these models, the strength of plant core
                      promoter(labels of samples) is defined as the ability to
                      drive expression of a barcoded reporter gene in maize
                      protoplasts with or without enhancer in dark.
                    </h3>
                    <h3>Promoter proximal region interaction (MH63)</h3>

                    <h3 style="color: #fb6672; font-weight: bold">
                      Please select MH63 models here👇
                    </h3>
                    <el-select
                      style="width: 240px"
                      placeholder="-----Select Model-----"
                      @change="MH63changeTools"
                      v-model="MH63model"
                    >
                      <el-option
                        v-for="value in MH63modellist"
                        :key="value"
                        :value="value"
                      >
                        {{ value }}
                      </el-option>
                    </el-select>
                  </div>
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card>
                  <div slot="header">
                    <span class="cardTitle">Note</span>
                  </div>
                  <div>
                    <p style="font-size: 15px">
                      To run the MH63-based model, you need to prepare the data
                      in fasta format, where the length of each chromatin
                      sequence is 3000bp. You can upload the required forecast
                      data and forecast tasks in two formats, online or locally.
                      Each task will take different time depending on the amount
                      of data you provide. When you submit your homework, please
                      keep it in mind ID, so that you can check the results
                      later.
                    </p>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <el-tabs
              tab-position="top"
              stretch
              @tab-click="methodsChange"
              value="input"
              style="margin-top: 40px; margin-bottom: 20px"
            >
              <!-- 选择模型输入序列 -->
              <el-tab-pane name="input">
                <span slot="label" class="tabLable"
                  ><i class="el-icon-edit"></i> Manual input</span
                >
                <div>
                  <el-alert
                    title="BE CAREFUL-------After switching the method, the entered sequence will be cleared"
                    style="width: 50%; margin: 0 auto; margin-bottom: 10px"
                    center
                    type="info"
                    close-text="got it"
                  >
                  </el-alert>
                  <div class="tipsButton">
                    <el-popover
                      placement="top"
                      width="500"
                      trigger="hover"
                      :open-delay="100"
                    >
                      <h2 style="text-align: center; margin: 0 auto">
                        Right example
                      </h2>
                      <el-input
                        type="textarea"
                        style="width: 95%; margin: 10px"
                        :value="exampleSeq"
                        rows="10"
                        :readonly="true"
                      />
                      <el-button
                        slot="reference"
                        class="el-icon-info"
                        ref="dataBu"
                      >
                        First : Correct data format</el-button
                      >
                    </el-popover>
                    <el-popover
                      placement="top"
                      width="400"
                      trigger="hover"
                      :open-delay="100"
                    >
                      <h2 style="text-align: center; margin: 0 auto">
                        Wrong example
                      </h2>
                      <el-input
                        type="textarea"
                        style="width: 43%; margin: 10px"
                        :value="NumSeq1"
                        rows="5"
                        :readonly="true"
                      />
                      <el-input
                        type="textarea"
                        style="width: 43%; margin: 10px"
                        :value="NumSeq2"
                        rows="5"
                        :readonly="true"
                      />
                      <el-button
                        slot="reference"
                        class="el-icon-info"
                        ref="numBu"
                      >
                        Second : Same number of genes</el-button
                      >
                    </el-popover>
                    <el-popover
                      placement="top"
                      width="400"
                      trigger="hover"
                      :open-delay="100"
                    >
                      <h2 style="text-align: center; margin: 0 auto">
                        Wrong example
                      </h2>
                      <el-input
                        type="textarea"
                        style="width: 43%; margin: 10px"
                        :value="NameSeq1"
                        rows="5"
                        :readonly="true"
                      />
                      <el-input
                        type="textarea"
                        style="width: 43%; margin: 10px"
                        :value="NameSeq2"
                        rows="5"
                        :readonly="true"
                      />
                      <el-button
                        slot="reference"
                        class="el-icon-info"
                        ref="nameBu"
                      >
                        Third : Different gene names</el-button
                      >
                    </el-popover>
                  </div>
                  <div>
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
                  <div class="ToolButton" style="display: flex">
                    <el-button
                      icon="el-icon-s-data"
                      @click="updataEx"
                      style="margin: 0 auto"
                      :disabled="!seqflag"
                      >Example</el-button
                    >
                  </div>
                </div>
              </el-tab-pane>
              <!-- 或者直接上传文件 -->
              <el-tab-pane name="file">
                <span slot="label" class="tabLable"
                  ><i class="el-icon-folder-add"></i> Upload files</span
                >
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
                        <!-- <i class="el-icon-upload" style="color:#d32f2f"></i> -->
                        <span
                          class="iconfont icon-jinyong"
                          style="font-size: 70px; color: #d32f2f"
                        ></span>

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
                    <span slot="label" style="font-size: 20px"> E-mail: </span>
                    <el-input v-model="updataForm.email"></el-input>
                  </el-form-item>
                </el-form>
              </el-col>
            </el-row>
            <!-- 提交 -->
            <el-row type="flex" justify="center">
              <div class="ToolButton">
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
              </div>
            </el-row>
            <!-- <input type="file" @change="fileChange"></input> -->
            <!-- <img :src="captchaImg" />
          <el-input v-model="inputCaptcha"></el-input> -->
          </div>
        </div>
        <!-- <div>
        <input type="text" ref="myInput"/>
        <button @click="handleClick">Click me</button>
      </div> -->
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Message } from "element-ui";
export default {
  name: "ExpMH63",
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
      MH63modellist: ["MH_MH63_H3K4", "MH_MH63_H3K9", "MH_MH64_RNAP2"],
      // PDImodellist: ["SHOOT1", "EAR", "SHOOT2"],
      options: [{ value: "1" }, { value: "2" }],
      updataForm: {
        email: "",
      },
      MH63model: undefined,
      // PDImodel: undefined,

      // 当前进行到第几步
      steps1: 0,
      // 表示使用的是哪种方法。0为手动，1为上传
      method: 0,
      // 检查两种数据是否校验成功
      inputFlag: false,
      fileFlag: false,

      taskBoby_seq: {
        modelName: "",
        seq: [],
        email: "",
        uuid: undefined,
        captcha: undefined,
      },
      taskBoby_file: {
        modelName: "",
        email: "",
        uuid: undefined,
        captcha: undefined,
      },
      uuid: undefined,
      captchaImg: "",
      inputCaptcha: undefined,

      exampleSeq:
        ">Zm00001d027230_1_+_43289-44789_49337-50837\n" +
        "GGAAGAGAGAGGCTGCTCCCTCTGTACATGGGGGAGTTCTAATCTCCCCTATTTCGGTAATCTATGTTTTA\n" +
        ">Zm00001d027235_1_+_121120-122620_122114-123614\n" +
        "AATGGCCTCCTCTAACATCTGTCCTTCCCTTCCATAAAAACCCCCTGCGAATCTTATCAATAGCTCTAA\n" +
        "\nwhich means:\n>your Gene Name\nyour Gene Seq",

      NumSeq1: ">GeneName1\nATCGATCGATCG\n>GeneName2\nATCGATCGATCG\n",
      NumSeq2: ">GeneName3\nATCGATCGATCG",
      NameSeq1: ">GeneName1\nATCGATCGATCG\n>GeneName2\nATCGATCGATCG\n",
      NameSeq2: ">GeneName1\nATCGATCGATCG\n>GeneName2\nATCGATCGATCG\n",

      EXseq1:
        ">Zm00001d027230_1_+_43289-44789_49337-50837\n" +
        "GGAAGAGAGAGGCTGCTCCCTCTGTACATGGGGGAGTTCTAATCTCCCCTATTTCGGTAATCTATGTTTTA",
      EXseq2:
        ">Zm00001d027235_1_+_121120-122620_122114-123614\n" +
        "AATGGCCTCCTCTAACATCTGTCCTTCCCTTCCATAAAAACCCCCTGCGAATCTTATCAATAGCTCTAA",
    };
  },
  computed: {
    // 输入的序列长度
    seqlenth() {
      // if (this.MH63model) return 3000;
      // else if (this.PDImodel) return 1500;
      // else return "undetermined";
      return 3000;
    },
    // seqflag 用来表明序列是否可以输入
    seqflag() {
      if (this.MH63model) return true;
      else return false;
    },
  },
  methods: {
    // handleClick() {
    //   console.log("id:",document.getElementById("myInput")); // 输出input元素
    //   console.log("ref:",this.$refs.myInput); // 输出undefined
    //   // 使用this.$nextTick在DOM更新后获取DOM节点
    //   // this.$nextTick(() => {
    //   //   console.log(3,this.$refs.myInput); // 输出input元素
    //   // });
    // },
    confirmtype() {
      this.loading = !this.loading;
      console.log(this.methltype);
    },

    async getcaptch() {
      let flag = undefined;
      this.inputCaptcha = undefined;
      let result = await this.$API.reqCaptchaImg();

      if (result.code == 200) {
        this.captchaImg = "data:image/png;base64," + result.img;
        this.uuid = result.uuid;

        const h = this.$createElement;
        const inputElem = h(
          "input",
          {
            attrs: {
              value: this.inputCaptcha,
              id: "input1",
            },
            style: {
              width: "60%",
            },
            on: {
              input: function (event) {
                this.inputCaptcha = event.target.value;
              }.bind(this),
            },
          },
          ""
        );
        const imgElem = this.$createElement("img", {
          ref: "captchaImg",

          attrs: {
            src: this.captchaImg,
            // id: "captcha-img",
          },
          style: {
            "margin-top": "20px",
          },
          // 在这里。需要加上key才能保证el.msgbox每次都能渲染组件。
          // 详情见el官方文档。
          key: Date.now(),
        });

        // 将 input 和 img 元素放到 Vue 组件之外的 div 中
        const divElem = h("div", [inputElem, imgElem]);
        await this.$msgbox({
          title: "Please enter the verification code",
          message: divElem,
          type: "warning",
          center: true,
          showCancelButton: true,
          confirmButtonText: "Confirm",
          cancelButtonText: "Refresh",
          distinguishCancelAndClose: true,
          beforeClose: async (action, instance, done) => {
            // console.log(action);
            if (action === "confirm") {
              flag = true;
              done();
            } else if (action === "cancel") {
              let result = await this.$API.reqCaptchaImg();
              this.captchaImg = "data:image/png;base64," + result.img;
              this.uuid = result.uuid;

              this.$nextTick(() => {
                // 更新captchaImg元素的src属性

                // 在这里有两种解决方法，一种是使用ref，一种是使用id
                // 使用ref的话需要同时为元素绑定key属性
                this.$refs.captchaImg.src = this.captchaImg;
                // document.getElementById("captcha-img").src = this.captchaImg;
              });
            } else {
              flag = false;
              done();
            }
          },
        })
          .then((action) => {})
          .catch((action) => {});
      }
      // 返回的值代表用户是否提交了验证码
      if (this.inputCaptcha == undefined) flag = false;
      // 每次关闭后清空输入的验证码
      document.getElementById("input1").value = "";
      // console.log(flag);
      return flag;
    },

    // 新输入提交提交
    submitInputSeq() {
      // 先进行表单验证邮箱
      this.$refs.updataForm.validate(async (valid) => {
        if (valid) {
          // 如果是文件输入
          if (this.method == 1) {
            // 在这里进行数据整理并提交个服务器
            // 暂时直接显示成功
            // 判断步骤2是否成功
            if (this.fileFlag) {
              let t = await this.getcaptch();

              if (t != true) return;

              this.taskBoby_file.file = this.fileList[0].raw;
              this.taskBoby_file.email = this.updataForm.email;
              this.taskBoby_file.modelName = this.MH63model;
              this.taskBoby_file.uuid = this.uuid;
              this.taskBoby_file.captcha = this.inputCaptcha;

              let result = await this.$API.reqSubmitFlie(this.taskBoby_file);

              if (result.code == 200) {
                this.steps1 = 3;
                this.$msgbox({
                  title: "Upload sequence succeeded!",
                  message:
                    "Your email will receive an email with a TASK NAME.\n \
                  Please query the progress of this task according to this TASK NAME",
                  type: "success",
                  confirmButtonText: "confrim",
                  callback: (action) => {
                    this.$router.go(0);
                  },
                });
              } else if (result.code == 500) {
                this.$msgbox({
                  title: "error!\n ",
                  message: "File processing error",
                  type: "error",
                  confirmButtonText: "confrim",
                });
              } else if (result.code == 400) {
                this.$msgbox({
                  title: "error!\n ",
                  message: "Verification code error",
                  type: "error",
                  confirmButtonText: "confrim",
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
              let t = await this.getcaptch();
              if (t != true) return;

              this.taskBoby_seq.seq = [];
              this.taskBoby_seq.seq.push(this.Seq1);
              this.taskBoby_seq.seq.push(this.Seq2);
              this.taskBoby_seq.email = this.updataForm.email;
              this.taskBoby_seq.modelName = this.MH63model;
              this.taskBoby_seq.uuid = this.uuid;
              this.taskBoby_seq.captcha = this.inputCaptcha;

              let result = await this.$API.reqSubmitSeq(this.taskBoby_seq);
              if (result.code == 200) {
                this.steps1 = 3;
                this.$msgbox({
                  title: "Upload sequence succeeded!\n ",
                  message:
                    "Your email will receive an email with a TASK NAME.\n \
                  Please query the progress of this task according to this TASK NAME",
                  type: "success",
                  confirmButtonText: "confrim",
                  callback: (action) => {
                    this.$router.go(0);
                  },
                });
              } else if (result.code == 500) {
                this.$msgbox({
                  title: "error!\n ",
                  message: "File processing error",
                  type: "error",
                  confirmButtonText: "confrim",
                });
              } else if (result.code == 400) {
                this.$msgbox({
                  title: "error!\n ",
                  message: "Verification code error",
                  type: "error",
                  confirmButtonText: "confrim",
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
            confirmButtonText: "confrim",
          });
          return false;
        }
      });
    },

    MH63changeTools(value) {
      this.steps1 = 1;
      // if (this.PDImodel) this.PDImodel = undefined;
      // this.$router.push(`/Tools/MH63_${value}`);
      // console.log(value);
    },

    handlerSuccess(response, file, fileList) {},

    // 文件改变时监视，限制文件大小
    fileChange(file, fileList) {
      const isSize = file.size / 1024 / 1024;
      let lim = 10;
      if (isSize > lim) {
        this.$msgbox({
          message: "The file size exceeds the limit. MH63:10mb PDI:10mb",
          type: "error",
          confirmButtonText: "confrim",
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

    checkSeq(seq1, seq2) {
      var seq1_list = seq1.split("\n");
      var seq2_list = seq2.split("\n");

      // 1:表示基因格式错误
      if (seq1_list.length % 2 != 0 || seq2_list.length % 2 != 0) return 1;
      // 2:表示两侧基因个数不一致
      if (seq1_list.length != seq2_list.length) return 2;

      // console.log(seq_list)
      for (var i = 0; i < seq1_list.length; i++) {
        if (i % 2 == 0) {
          if (seq1_list[i][0] != ">" || seq2_list[i][0] != ">") return 1;
          // 3表示交互的基因名重复了
          if (seq1_list[i] == seq2_list[i]) return 3;
        }
        if (
          i % 2 == 1 &&
          (!/^[ATCG]+$/.test(seq1_list[i]) || !/^[ATCG]+$/.test(seq2_list[i]))
        ) {
          return 1;
        }
      }
      // if(seq_list)
      return 0;
    },
    // 检查输入序列格式
    checkinput() {
      if (this.Seq2 != "" && this.Seq1 != "") {
        this.Seq1 = this.Seq1.trim();
        this.Seq2 = this.Seq2.trim();
        // 判断是否基因数过多
        var len1 = this.Seq1.split("\n").length;
        var len2 = this.Seq1.split("\n").length;
        if (len1 > 20 || len2 > 20) {
          this.$alert(
            "Maximum number of genes:20.If you want to upload more genes, please select File Upload ",
            "Too many genes!",
            {
              confirmButtonText: "confrim",
              type: "error",
            }
          );
          this.steps1 = 1;
          this.inputFlag = false;
          return;
        }

        var tem = this.checkSeq(this.Seq1, this.Seq2);
        var wrongBu = "";
        if (tem == 0) {
          this.steps1 = 2;
          this.inputFlag = true;
        } else if (tem == 1) {
          // this.$refs.dataBu[0].setAttribute("class", " wrongBu");
          Message({
            message:
              "Wrong data format !!! Please view the correct data format from above",
            type: "error",
            offset: 400,
          });
          this.steps1 = 1;
          this.inputFlag = false;

          wrongBu = "dataBu";
        } else if (tem == 2) {
          Message({
            message:
              "The number of genes in the two input boxes should be the same",
            type: "error",
            offset: 400,
          });
          this.steps1 = 1;
          this.inputFlag = false;

          wrongBu = "numBu";
        } else if (tem == 3) {
          Message({
            message:
              "The gene name of the interaction (that is, the gene name of the same line) cannot be the same",
            type: "error",
            offset: 400,
          });
          this.steps1 = 1;
          this.inputFlag = false;

          wrongBu = "nameBu";
        }
        if (wrongBu != "") {
          this.$refs[wrongBu].$el.classList.add("wrongBu");
          setTimeout(() => {
            this.$refs[wrongBu].$el.classList.remove("wrongBu");
          }, 3000);
        }
      }
    },
    // 清空已经填入的数据
    resetInfo() {
      this.MH63model = "";
      // 手动输入
      if (this.method == 0) {
        this.inputFlag = false;
        this.Seq1 = "";
        this.Seq2 = "";
      }
      // 上传文件
      else {
        this.fileFlag = false;
        this.fileList = [];
      }

      this.updataForm.email = "";
      this.steps1 = 0;
    },

    updataEx() {
      this.Seq1 = this.EXseq1;
      this.Seq2 = this.EXseq2;

      this.steps1 = 2;
      this.inputFlag = true;
    },
  },
  created() {},
};
// import "../../assets/js/bootstrap.bundle.min.js"
</script>
<style scoped>
/* @import "../../assets/css/bootstrap.css";
@import "../../assets/css/style.css"; */

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
  width: 70%;
  margin: 0 auto;
}

.top-text {
  text-align: center;
  margin: 0 auto;
  height: 70px;
  margin-top: 30px;

  /* background:-webkit-linear-gradient(left,#93a5cf,#e4efe9) ; */
  /* background: -webkit-linear-gradient(left, #fff1eb, #ace0f9); */
  border-radius: 8px;
}

th.column-money,
td.column-money {
  text-align: right !important;
}

.ToolButton button {
  font-size: 20px;
}

.ToolButton button:nth-child(2) {
  background-color: #d32f2f;
  border-color: #d32f2f;
}
.ToolButton button:nth-child(2):hover {
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
.cardModel {
  width: 80%;
}

.cardModel ::v-deep .el-card__header {
  background-color: #18bc9c;
  /* border: #A5ECE4; */
}

.mdoelT {
  margin-left: 10px;
  /* margin: auto; */
  font-size: 25px;
  font-weight: bold;
}

.tipsButton {
  display: flex;
  /* margin: 0 auto; */
  justify-content: space-evenly;
}

.wrongBu {
  color: #fff;
  background-color: #d32f2f;
  border-color: #d32f2f;
}

.tabLable {
  font-size: 25px;
  font-weight: bolder;
}
</style>
