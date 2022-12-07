<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="home">
    <div id="components-layout-demo-basic">
      <div class="top-text" style="margin-top: 20px">
        <a-row type="flex" justify="center">
          <a-col :span="20">
            <el-card class="homecard">
              <div>
                <p >
                  &nbsp; &nbsp;&nbsp;&nbsp; MaizeDeepCBA is a web server that
                  integrates maize chromatin interaction and deep learning
                  models for maize Gene expression prediction. Based on the
                  interaction between the proximal and distal ends of the maize
                  promoter, it predicts gene expression in relevant target
                  tissues. At the same time, MaizeDeepCBA can achieve Gene
                  expression prediction across tissues and genotypes. Based on
                  related computer vision methods, MaizeDeepCBA can mine
                  important segments, sites or motifs that affect Gene
                  expression in the proximal and distal interactions of
                  promoters. Maize DeepCBA is freely accessible for all users.
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

      <div style="margin-top: 20px">
        <el-row :gutter="40" type="flex">
          <el-col :span="12">
            <el-card class="homecard" style="background-color: #296D7F;color:#FFFFFF">
              <p style="font-weight: bold;font-size: 30px;">Introduction</p>
              <p>
                xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                xxxxx
                xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                xxxxxxxxxxx
                xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                xxxxxxxxxxxxxxxxxxx
              </p>
              <div class="image-content" style="margin-top: 10px; width: 100%">
                <img src="../img/home_2.jpg" style="width: 80%" />
              </div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card class="homecard">
              <p>
                &nbsp; &nbsp;&nbsp;&nbsp; xxxxxxxxxxxxxxxxxxx
                xxxxxxxxxxxxxxxxxxx
              </p>
              <div class="image-content" style="margin-top: 10px; width: 100%">
                <img src="../img/home_3.jpg" style="width: 80%" />
              </div>
              <el-button class="rouButton" @click="$router.push('/Expression')"
                >Go Tools</el-button
              >
            </el-card>
          </el-col>
        </el-row>
      </div>

      <div style="margin: 20px">
        <el-row type="flex" justify="center">
          <el-col :span="20">
            <el-card style="text-align: center">
              <div style="margin-bottom: 50px; text-align: justify">
                <p style="font-size: 20px">
                  &nbsp; &nbsp;&nbsp;&nbsp;The DeepCBA framework includes a CNN
                  module for extracting sequence features and feature
                  dimensionality reduction, a Bidirectional Long Short-term
                  Memory Network (BiLSTM) for capturing sequence timing
                  features, and an attention for weight reassignment. The force
                  mechanism has three parts. DeepCBA first performs one-hot
                  encoding on the input chromatin sequence of length 3002; its
                  encoding format is as follows: A(1,0,0,0)T, C(0,1,0,0)T, G(
                  0,0,1,0)T, T(0,0,0,1)T; Input the encoded sequence into the
                  convolutional neural network to achieve feature dimensionality
                  reduction and feature extraction; in order to capture the
                  time-series features in the sequence, such as sequence Before
                  and after the influence of the middle bases, etc., use the
                  bidirectional long short-term memory network to capture the
                  timing features hidden in the DNA sequence, and obtain two
                  vector matrices of 3*64; vertically splicing the two vector
                  matrices to obtain a matrix of 6*64, and then use the
                  attention The force mechanism enhances the contribution of key
                  features to the model, and uses dropout to prevent
                  overfitting, etc. In the output layer, the sigmoid/linear
                  function is used to complete the corresponding promoter
                  proximal interaction and the prediction of maize gene
                  expression fused with PPI data, etc.
                </p>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>

      <!-- <div class="image-content" style="margin-top: 10px; width: 90%; text-align: center">
        <img src="../img/expression_fig1.jpg" style="width: 80%" />
      </div> -->
    </div>
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

.home {
  /* text-align: center; */
  /* height: 1000px; */
  /* background-color: rgb(0, 135, 172); */
  width: 80%;
  margin: 0 auto;
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
.homecard{
  text-align: center;
  height: 100%;
  /* background-color: #296D7F; */
}
.homecard p{
  font-size: 20px; 
  text-align: justify
}
</style>
