<template>
  <div>
    <div class="all">
      <div class="Title">QTG-LGBM</div>
      <div class="filter">
        <div class="select">
          <el-card class="inputdiv" shadow="never">
            <div slot="header">
              <p class="leftTitle">Please select the species</p>
            </div>
            <el-select v-model="species">
              <el-option
                v-for="value in specieslist"
                :key="value"
                :value="value"
              >
                {{ value }}
              </el-option>
            </el-select>
          </el-card>

          <!-- <el-select placeholder="选择待预测性状" v-model="trait">
            <el-option v-for="value in traitlist" :key="value" :value="value">
              {{ value }}
            </el-option>
          </el-select> -->

          <el-card class="inputdiv" shadow="never">
            <div slot="header">
              <p class="leftTitle">Please enter the trait name</p>
            </div>
            <el-input v-model="trait" placeholder="example: PH (Plant Height)"></el-input>
          </el-card>
        </div>
        <div class="geneqtl">
          <el-card class="inputdiv" shadow="never">
            <div slot="header">
              <p class="inputTitle">Please enter the positive gene list</p>
            </div>
            <el-input
              class="lgbmInput"
              type="textarea"
              :autosize="{ minRows: 14, maxRows: 14 }"
              v-model="gene"
              :placeholder="geneEX"
            ></el-input>
          </el-card>
        </div>
        <div class="geneqtl">
          <el-card class="inputdiv" shadow="never">
            <div slot="header">
              <p class="inputTitle">Please enter the QTL gene list</p>
            </div>
            <el-input
              class="lgbmInput"
              type="textarea"
              :autosize="{ minRows: 14, maxRows: 14 }"
              v-model="qtl"
              :placeholder="qtlEX"
            ></el-input>
          </el-card>
        </div>
      </div>
      <div class="email">
        <!-- <p
          style="font-size: 20px; color: #18bc9c; margin: 0; line-height: 40px"
        >
          Email: &ensp;&ensp;
        </p>
        <el-input v-model="email"></el-input> -->
        <!-- <el-alert title="消息提示的文案" type="info"  style="margin-top: -40px;margin-bottom: 10px;"> </el-alert> -->

        <el-form :model="updataForm" ref="updataForm" label-position="right">
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
            <el-input
              v-model="updataForm.email"
              placeholder="Please enter your email to receive the results"
            ></el-input>
          </el-form-item>
          <el-form-item
            prop="verify"
            label-width="200px"
            :rules="[
              {
                required: true,
                message: 'Please enter the Verify code',
                trigger: 'blur',
              },
            ]"
          >
            <span slot="label" style="font-size: 20px">
              Enter the number:
            </span>
            <div style="display: flex">
              <el-input v-model="inputCaptcha"></el-input>
              <img
                :src="captchaImg"
                alt=""
                @click="reflshCaptch"
                style="cursor: pointer; margin-left: 20px"
              />
            </div>
          </el-form-item>
        </el-form>
      </div>
      <div class="submit">
        <el-button @click="submit" icon="el-icon-s-promotion" type="primary"
          >Submit</el-button
        >
        <el-button
          type="danger"
          icon="el-icon-refresh-right"
          @click="resetInfo"
          style="background-color: #ec971f; border-color: #ec971f"
          >Reset</el-button
        >
        <el-button icon="el-icon-s-data" @click="updataEx">Example</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LightGBM",
  data() {
    return {
      species: "Maize",
      trait: "",

      specieslist: ["Maize", "Arabidopsis", "Rice", "Setaria", "Sorghum"],
      //   traitlist: [],

      gene: "",
      qtl: "",

      taskBoby: {
        datasets: [],
        qtl: [],
        trait: "",
        species: "",
        email: "",
        uuid: "",
        captcha: "",
      },
      uuid: undefined,
      captchaImg: "",
      inputCaptcha: undefined,

      updataForm: {
        email: "",
        verify: "",
      },

      tishi: {
        Maize: [
          "The format of the Maize positive gene list:\nZm00001d003162\nZm00001d003477\nZm00001d003804\nZm00001d006198\nZm00001d006212\n...",
          "The format of the Maize QTL gene list:\nZm00001d028038\nZm00001d027924\nZm00001d028515\nZm00001d028458\nZm00001d027880\n...",
        ],
        Arabidopsis: [
          "The format of the Arabidopsis positive gene list:\nAT1G01010\nAT1G01020\nAT1G01030\nAT1G01040\nAT1G01050\n...",
          "The format of the Arabidopsis QTL gene list:\nAT1G02391\nAT1G02400\nAT1G02405\nAT1G02410\nAT1G02420\n...",
        ],
        Rice: [
          "The format of the Rice positive gene list:\nLOC_Os01g01010\nLOC_Os01g01019\nLOC_Os01g01030\nLOC_Os01g01040\nLOC_Os01g01050\n...",
          "The format of the Rice QTL gene list:\nLOC_Os03g12810\nLOC_Os03g12815\nLOC_Os03g12820\nLOC_Os03g12840\nLOC_Os03g12860\n...",
        ],
        Setaria: [
          "The format of the Setaria positive gene list:\nSevir.1G000100\nSevir.1G000200\nSevir.1G000300\nSevir.1G000400\nSevir.1G000501\n...",
          "The format of the Setaria QTL gene list:\nSevir.1G014600\nSevir.1G014700\nSevir.1G014800\nSevir.1G014900\nSevir.1G015000\n...",
        ],
        Sorghum: [
          "The format of the Sorghum positive gene list:\nSobic.001G000100\nSobic.001G000200\nSobic.001G000400\nSobic.001G000501\nSobic.001G000700\n...",
          "The format of the Sorghum QTL gene list:\nSobic.002G225800\nSobic.002G225900\nSobic.002G226000\nSobic.002G226100\nSobic.002G226200\n...",
        ],
      },
    };
  },
  watch: {
    inputCaptcha(newName, oldName) {
      this.updataForm.verify = newName;
    },
    species() {
      this.gene = "";
      this.qtl = "";
    },
  },

  computed: {
    geneEX() {
      return this.tishi[this.species][0];
    },
    qtlEX() {
      return this.tishi[this.species][1];
    },
  },
  methods: {
    async reflshCaptch() {
      this.inputCaptcha = undefined;
      let result = await this.$API.reqCaptchaImg();
      if (result.code == 200) {
        this.captchaImg = "data:image/png;base64," + result.img;
        this.uuid = result.uuid;
      }
    },
    submit() {
      this.$refs.updataForm.validate(async (valid) => {
        if (valid) {
          this.taskBoby.captcha = this.inputCaptcha;
          this.taskBoby.email = this.updataForm.email;
          this.taskBoby.trait = this.trait;
          this.taskBoby.species = this.species;
          this.taskBoby.uuid = this.uuid;

          var datasets_list = this.gene.split("\n");
          var qtl_list = this.qtl.split("\n");

          this.taskBoby.qtl = qtl_list;
          this.taskBoby.datasets = datasets_list;

          let result = await this.$API.reqLGBMtask(this.taskBoby);

          if (result.code == 200) {
            this.$msgbox({
              title: "Upload succeeded!",
              message:
                "We will send the results to your email about 12-24 hours later.\n ",
              type: "success",
              confirmButtonText: "confrim",

              callback: (action) => {
                // this.$router.go(0);
                this.reflshCaptch();
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
          this.$msgbox({
            message: "please enter correct Email and Verify code",
            type: "error",
            confirmButtonText: "confrim",
          });
          return false;
        }
      });
    },

    resetInfo() {
      this.species = "Maize";
      this.trait = "";
      this.gene = "";
      this.qtl = "";

      this.updataForm.email = "";
      this.inputCaptcha = undefined;
    },
    updataEx() {
      this.species = "Maize";
      this.trait = "DTA";
      this.$nextTick(() => {
        this.gene =
          "Zm00001d003162\nZm00001d003477\nZm00001d003804\nZm00001d006198\nZm00001d006212\nZm00001d006835\nZm00001d006918\nZm00001d007382\nZm00001d007949\nZm00001d007951\nZm00001d008826\nZm00001d010646\nZm00001d010752\nZm00001d010755\nZm00001d010987\nZm00001d011876\nZm00001d013259\nZm00001d013331\nZm00001d013402\nZm00001d014673\nZm00001d014963\nZm00001d016915\nZm00001d017176\nZm00001d017241\nZm00001d018403\nZm00001d021291\nZm00001d022590\nZm00001d022613\nZm00001d023420\nZm00001d024430\nZm00001d024909\nZm00001d028169\nZm00001d028173\nZm00001d028905\nZm00001d031662\nZm00001d032922\nZm00001d033325\nZm00001d033799\nZm00001d034038\nZm00001d034045\nZm00001d034313\nZm00001d035447\nZm00001d037565\nZm00001d039165\nZm00001d039589\nZm00001d042315\nZm00001d042319\nZm00001d043682\nZm00001d045735\nZm00001d047632\nZm00001d047761\nZm00001d048474\nZm00001d049543\nZm00001d050649\nZm00001d051684\nZm00001d052781";
        this.qtl =
          "Zm00001d038728\nZm00001d038769\nZm00001d038772\nZm00001d038773\nZm00001d038775\nZm00001d038776\nZm00001d038777\nZm00001d038649\nZm00001d038650\nZm00001d038640\nZm00001d038665\nZm00001d038525\nZm00001d038796\nZm00001d038608\nZm00001d038606\nZm00001d038824\nZm00001d038826\nZm00001d038620\nZm00001d038622\nZm00001d038473\nZm00001d038751\nZm00001d038750\nZm00001d038779\nZm00001d039145\nZm00001d038732\nZm00001d038815\nZm00001d038518\nZm00001d038517\nZm00001d038604\nZm00001d038465\nZm00001d038741\nZm00001d038570\nZm00001d038762\nZm00001d038763\nZm00001d038794\nZm00001d038536\nZm00001d038537\nZm00001d038466\nZm00001d038765\nZm00001d038660\nZm00001d038661\nZm00001d038803\nZm00001d038804\nZm00001d038807\nZm00001d038658\nZm00001d038645\nZm00001d038646\nZm00001d038783\nZm00001d038784\nZm00001d038676\nZm00001d038595\nZm00001d038618\nZm00001d038642\nZm00001d038667\nZm00001d038605\nZm00001d038506\nZm00001d038534\nZm00001d038577\nZm00001d038578\nZm00001d038579\nZm00001d038494\nZm00001d038599\nZm00001d038600\nZm00001d038842\nZm00001d038841\nZm00001d038562\nZm00001d038625\nZm00001d038812\nZm00001d038658\nZm00001d038467\nZm00001d038752\nZm00001d038756\nZm00001d038757\nZm00001d038758\nZm00001d038702\nZm00001d038671\nZm00001d038747\nZm00001d038704\nZm00001d038840\nZm00001d038547\nZm00001d038548\nZm00001d038538\nZm00001d038539\nZm00001d038540\nZm00001d038541\nZm00001d038542\nZm00001d038544\nZm00001d038546\nZm00001d038684\nZm00001d038685\nZm00001d038702\nZm00001d038471\nZm00001d038820\nZm00001d038714\nZm00001d038481\nZm00001d038520\nZm00001d038521\nZm00001d038526\nZm00001d038791\nZm00001d038728\nZm00001d038692\nZm00001d038549\nZm00001d038551\nZm00001d038554\nZm00001d038555\nZm00001d038581\nZm00001d038699\nZm00001d038700\nZm00001d038724\nZm00001d038725\nZm00001d038726\nZm00001d038668\nZm00001d038682\nZm00001d038514\nZm00001d038513\nZm00001d038528\nZm00001d038530\nZm00001d038532\nZm00001d038829\nZm00001d038830\nZm00001d038831\nZm00001d035265\nZm00001d038722\nZm00001d038833\nZm00001d038572\nZm00001d038502\nZm00001d038526\nZm00001d038589\nZm00001d038630\nZm00001d038510\nZm00001d038509\nZm00001d038593\nZm00001d038511\nZm00001d038799\nZm00001d038718\nZm00001d038723\nZm00001d038651\nZm00001d038494\nZm00001d038504\nZm00001d038623\nZm00001d038686\nZm00001d037911\nZm00001d038689\nZm00001d038690\nZm00001d038846\nZm00001d038648\nZm00001d038576\nZm00001d035360\nZm00001d038823\nZm00001d038825\nZm00001d038614\nZm00001d038612\nZm00001d038610\nZm00001d038609\nZm00001d038479\nZm00001d038814\nZm00001d038806\nZm00001d038476\nZm00001d038657\nZm00001d038655\nZm00001d038644\nZm00001d038672\nZm00001d038643\nZm00001d038583\nZm00001d038717\nZm00001d038678\nZm00001d038563\nZm00001d038624\nZm00001d038761\nZm00001d038475\nZm00001d038838\nZm00001d038597\nZm00001d038598\nZm00001d038707\nZm00001d038707\nZm00001d038706\nZm00001d038739\nZm00001d038712\nZm00001d038695\nZm00001d038522\nZm00001d038483\nZm00001d038792\nZm00001d038691\nZm00001d038693\nZm00001d038548\nZm00001d038550\nZm00001d038553\nZm00001d038698\nZm00001d038515\nZm00001d038531\nZm00001d035507\nZm00001d036307\nZm00001d038809\nZm00001d038812\nZm00001d038687\nZm00001d038766\nZm00001d036448\nZm00001d038835\nZm00001d035725\nZm00001d038580\nZm00001d038808\nZm00001d038485\nZm00001d038486\nZm00001d038489\nZm00001d038491\nZm00001d038527\nZm00001d038616\nZm00001d038752\nZm00001d038797\nZm00001d038795\nZm00001d038843";
      });
    },
  },
  mounted() {
    this.reflshCaptch();
  },
};
</script>

<style scoped>
.all {
  width: 80%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.Title {
  text-align: center;
  font-size: 35px;
  color: #109278;
  font-weight: bolder;
  margin-top: 15px;
}

.filter {
  display: flex;

  justify-content: space-between;

  margin-bottom: 20px;

  height: 420px;
}

.select {
  display: flex;
  justify-content: space-between;

  flex-direction: column;

  width: 20%;
  height: 100%;
}

.geneqtl {
  display: flex;
  justify-content: center;
  /* align-self: center; */
  flex-direction: column;
  width: 35%;
}

.email {
  width: 40%;
  margin: 0 auto;
  display: flex;
  align-self: center;

  flex-direction: column;
}

.submit {
  width: 30%;
  margin: 0 auto;
  margin-bottom: 20px;

  display: flex;
  justify-content: center;
}

.lgbmInput {
}

.inputTitle {
  /* text-align: center; */
  font-size: 20px;
  color: #fff;
  font-weight: bolder;
  margin: 0;
}

.leftTitle {
  /* text-align: center; */
  font-size: 18px;
  color: #fff;
  font-weight: bolder;
  margin: 0;

  min-width: 420px;
}

.inputdiv {
  height: 100%;
  border: #18bc9c;
}

::v-deep .el-card__header {
  background-color: #18bc9c;
  border: 1px solid;
  border-color: #18bc9c;
}

::v-deep .el-card__body {
  border: 1px solid;
  border-color: #18bc9c;
}

::v-deep .el-input__inner {
  border-color: #2c3e50;
}
::v-deep .el-textarea__inner {
  border-color: #2c3e50;
}
</style>