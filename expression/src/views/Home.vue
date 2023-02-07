<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <!-- <el-carousel :interval="4000" height="400px">
        <el-carousel-item v-for="item in 6" :key="item">
          <h3 class="medium">{{ item }}</h3>
        </el-carousel-item>
    </el-carousel> -->
  <div id="components-layout-demo-basic">
    <div class="teacher-overview-welcome" style="width: 70%; margin: 0 auto">
      <div class="welcome">
        <p class="welcome-title">WELCOME</p>
        <p class="welcome-organization">This is DeepCBA</p>
        <p class="welcome-email">
          xx xx xxx xx xx x <span class="bindEmail">xx xx xxx xx xx x </span>
        </p>
        <p class="welcome-time">xx xx xxx xx xx x</p>
        <p></p>
        <div class="welcome-bd">
          <div class="weather"></div>
          <div class="temp">
            x xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx
          </div>
        </div>
      </div>
    </div>

    <div class="top-text" style="margin-top: 20px; width: 100%">
      <a-row type="flex" justify="center">
        <a-col :span="14">
          <el-card class="homecard" style="border-radius: 20px">
            <div>
              <p>
                &nbsp; &nbsp;&nbsp;&nbsp; MaizeDeepCBA is a web server that
                integrates maize chromatin interaction and deep learning models
                for maize Gene expression prediction. Based on the interaction
                between the proximal and distal ends of the maize promoter, it
                predicts gene expression in relevant target tissues. At the same
                time, MaizeDeepCBA can achieve Gene expression prediction across
                tissues and genotypes. Based on related computer vision methods,
                MaizeDeepCBA can mine important segments, sites or motifs that
                affect Gene expression in the proximal and distal interactions
                of promoters. Maize DeepCBA is freely accessible for all users.
              </p>
            </div>
            <div
              class="image-content"
              style="margin-top: 10px; width: 100%; text-align: center"
            >
              <img src="../img/home_1.jpg" style="width: 60%" />
            </div>

            <el-button
              class="rouButton"
              @click="$router.push('/result')"
              style="position: relative; right: 10%"
              >RESULT</el-button
            >
            <el-button
              class="rouButton"
              @click="$router.push('/tutorial')"
              style="position: relative; left: 10%"
              >TUORIAL</el-button
            >
          </el-card>
        </a-col>
      </a-row>
    </div>
    <div>
      <div class="teacher3-serve">
        <div
          style="
            width: 80%;
            margin: 0 auto;
            margin-top: 200px;
            margin-bottom: 150px;
          "
        >
          <el-row :gutter="40" type="flex">
            <el-col :span="12">
              <el-card
                class="homecard"
                style="background-color: #296d7f; color: #ffffff;border-radius: 15px"
              >
                <p style="font-weight: bold; font-size: 30px">Introduction</p>
                <p>
                  The core structure of the deep neural network used in Deep CBA
                  can be divided into three modules: convolution neural network
                  module, bidirectional long-term and short-term memory network
                  module and self-attention mechanism module, as shown in the
                  following figure. 
                </p>
                <div
                  class="image-content"
                  style="margin-top: 10px; width: 100%"
                >
                  <img src="../img/home_2.jpg" style="width: 80%" />
                </div>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card
                class="homecard"
                style="
                  background: -webkit-linear-gradient(left, #fff1eb, #ace0f9);
                  border-radius: 15px
                "
              >
                <p>
                  The overall process of DeepCBA is as
                  follows: First, encode the sequence with length of 3000 bp and
                  1500 bp into 4*3000/4*1500 one-pot encoding matrix;
                  Secondly, take the encoded one-pot encoding matrix as the
                  input of the CNN Layer, use the ReLU activation function to
                  propagate the forward output and eliminate the reverse output,
                  and then use the maximum pooling operation to reduce the
                  dimension, and achieve the extraction of higher-level
                  features; Next, combine the information output by CNN and
                  input it into the bidirectional long-term and short-term
                  memory network to extract more important information from the
                  merged CNN information; Finally, use Self-Attention to
                  redistribute the weights of the network model, and then
                  realize the final prediction.
                </p>
                <div
                  class="image-content"
                  style="margin-top: 10px; width: 100%"
                >
                  <img src="../img/home_3.jpg" style="width: 80%" />
                </div>
                <el-button
                  class="rouButton"
                  @click="$router.push('/Expression/index')"
                  >Go Tools</el-button
                >
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
    <div
      style="
        width: 80%;
        margin: 0 auto;
        margin-top: -150px;
        margin-bottom: 100px;
      "
    >
      <el-row type="flex" justify="center">
        <el-col :span="20">
          <el-card
            style="
              text-align: center;
              /* background: linear-gradient(220.55deg, #0C3A2D 0%, #6D9773 100%);             */
              color: #ffffff;
              border-radius: 30px;
              /* background: linear-gradient(220.55deg, #EAEAEA 0%, #8B8B8B 100%); */
            "
          >
            <div style="margin-bottom: 50px; text-align: justify">
              <p style="font-size: 20px">
                &nbsp; &nbsp;&nbsp;&nbsp;The DeepCBA framework includes a CNN
                module for extracting sequence features and feature
                dimensionality reduction, a Bidirectional Long Short-term Memory
                Network (BiLSTM) for capturing sequence timing features, and an
                attention for weight reassignment. The force mechanism has three
                parts. DeepCBA first performs one-hot encoding on the input
                chromatin sequence of length 3002; its encoding format is as
                follows: A(1,0,0,0)T, C(0,1,0,0)T, G( 0,0,1,0)T, T(0,0,0,1)T;
                Input the encoded sequence into the convolutional neural network
                to achieve feature dimensionality reduction and feature
                extraction; in order to capture the time-series features in the
                sequence, such as sequence Before and after the influence of the
                middle bases, etc., use the bidirectional long short-term memory
                network to capture the timing features hidden in the DNA
                sequence, and obtain two vector matrices of 3*64; vertically
                splicing the two vector matrices to obtain a matrix of 6*64, and
                then use the attention The force mechanism enhances the
                contribution of key features to the model, and uses dropout to
                prevent overfitting, etc. In the output layer, the
                sigmoid/linear function is used to complete the corresponding
                promoter proximal interaction and the prediction of maize gene
                expression fused with PPI data, etc.
              </p>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
    <div class="themeBg"></div>
    <!-- <div class="image-content" style="margin-top: 10px; width: 90%; text-align: center">
        <img src="../img/expression_fig1.jpg" style="width: 80%" />
      </div> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Home",
  components: {},
  data() {
    return {
      list1: [],
    };
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
#components-layout-demo-basic .ant-layout-content {
  background: rgb(255, 255, 255);
  color: black;
}
#components-layout-demo-basic {
  width: 100%;
  margin: 0 auto;
  /* justify-content:center; */
  /* display: flex; */
}

/* p::first-letter {
  font-size: 40px;
} */

.top-text {
  display: flex;
  width: fit-content;
}
.rouButton {
  margin-top: 20px;
  font-size: 20px;
  width: 150px;
  height: 60px;
  color: #fff;
  background-color: #4db6ac;
  border-color: #4db6ac;
  border-radius: 0px;
}
.rouButton:hover {
  background: #71d8ce !important;
  border-color: #71d8ce !important;
  color: #fff !important;
}
.homecard {
  text-align: center;
  height: 100%;
  /* background-color: #296D7F; */
}
.homecard p {
  font-size: 20px;
  text-align: justify;
}
.el-carousel__item {
  position: absolute;
  width: 100%;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #c0c0c0;
}

.themeBg {
  content: "";
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  --color-filter: hue-rotate(25.4219deg);
  background-size: cover;
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.2),
      rgba(255, 255, 255, 0.2)
    ),
    url("../img/homeback.png");
  /* background-image: linear-gradient(transparent, rgb(250, 250, 250) 85%),
    url("../img/homeback.png"); */

  z-index: -2;
}
.welcome {
  /* text-shadow: 0 2px 4px rgba(11,90,88,.5); */
  text-shadow: 0 2px 4px rgb(11 90 88 / 50%);
}

.welcome-title {
  /* padding-bottom: 30px; */
  margin-bottom: 30px;
  margin-top: 20px;
  font-size: 48px;
  font-family: PingFangSC-Medium, PingFang SC, sans-serif;
  font-weight: 500;
  line-height: 60px;
  color: #fff;
  letter-spacing: 4px;
}

.welcome-organization {
  font-size: 28px;
  color: #fff;
  /* padding-bottom: 20px; */
}

.welcome-email {
  font-size: 24px;
  color: #fff;
  /* padding-bottom: 30px; */
  display: flex;
  align-items: center;
}

.welcome-time {
  color: #fff;
  padding-bottom: 30px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.39);
  width: 400px;
}

.welcome-bd {
  display: flex;
  padding-top: 30px;
  padding-right: 65px;
  align-items: center;
}

.temp {
  font-size: 24px;
  font-family: PingFangSC-Regular, PingFang SC, sans-serif;
  font-weight: 400;
  color: #fff;
}

.teacher3-serve {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 960px;
  min-height: calc(100vh - 60px);
  background: -webkit-linear-gradient(rgba(250, 250, 250, 0.8), #fafafa 50%);
  padding-left: 0;
  padding-top: 193px !important;
  margin-top: -300px;
  padding-bottom: 110px;
  z-index: -1;
}
</style>
