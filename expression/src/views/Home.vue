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
      <!-- <tem></tem> -->
      <div class="welcome">
        <p class="welcome-title">WELCOME</p>
        <p class="welcome-organization">This is website of DeepCBA</p>
        <p class="welcome-email">
          where you can simply understand DeepCBA and use online tools
          conveniently
        </p>
        <!-- <p class="welcome-time"></p> -->
        <p></p>
        <!-- <div class="welcome-bd">
          <div class="weather"></div>
          <div class="temp">DeepCBA: Precise prediction of maize gene expression based on chromatin interactions using DeepCBA</div>
        </div> -->
      </div>
    </div>

    <div class="top-text" style="margin-top: 20px; width: 100%">
      <a-row type="flex" justify="center">
        <a-col :span="14">
          <el-card class="homecard" style="border-radius: 20px">
            <div>
              <p style="font-weight: bold; font-size: 30px">Introduction</p>
              <p>
                &nbsp; &nbsp;&nbsp;&nbsp;DeepCBA realizes the prediction of
                target gene expression based on the proximal and distal
                interactions of chromatin in different tissues of higher plants.
                What's more important is that DeepCBA can mine important motifs
                that affect gene expression levels, and conduct detailed
                analysis of remote regulatory elements to achieve auxiliary
                design of target gene expression. DeepCBA can realize the
                prediction of gene expression across tissues and genotypes, and
                provides a new idea for the precise correlation of gene
                expression.
              </p>
            </div>
            <div
              class="image-content"
              style="margin-top: 10px; width: 100%; text-align: center"
            >
              <!-- <img src="../img/home_1.jpg" style="width: 60%" /> -->
            </div>

            <el-button
              class="rouButton"
              @click="$router.push('/Expression/index')"
              style="position: relative; right: 10%"
              >TOOLS</el-button
            >
            <el-button
              class="rouButton"
              @click="$router.push('/tutorial')"
              style="position: relative; left: 10%"
              >TUORIAL</el-button
            >
            <div class="shape-bottom-right" style="left: 0; opacity: 0.2">
              <img
                src="../assets/picture/11.png"
                alt="Image Not Found"
                style="width: 1100px"
              />
            </div>
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
          <!-- <el-row class="gallery-grids" type="flex" justify="space-around">
            <el-col class="baner-top" :span="8">
              <figure class="effect-bubba">
                <div
                  class="cursor"
                  onclick=" window.open('http://www.baidu.com','_blank'); "
                >
                  <img src="../img/yumi.jpg" alt="" class="img-responsive" />
                  <figcaption>
                    <h4>玉米</h4>
                    <p>
                      Happen active county. Winding morning ambition shyness
                      evident to poor. Because elderly new to the point to main
                      success.
                    </p>
                  </figcaption>
                </div>
              </figure>
            </el-col>
            <el-col class="baner-top" :span="8">
              <figure class="effect-bubba">
                <div
                  class="cursor"
                  onclick=" window.open('http://www.baidu.com','_blank'); "
                >
                  <img src="../img/shuidao.jpg" alt="" class="img-responsive" />
                  <figcaption>
                    <h4>水稻</h4>
                    <p>
                      Happen active county. Winding morning ambition shyness
                      evident to poor. Because elderly new to the point to main
                      success.
                    </p>
                  </figcaption>
                </div>
              </figure>
            </el-col>
          </el-row> -->
          <el-row :gutter="40" type="flex">
            <el-col :span="12">
              <el-card
                class="homecard"
                style="
                  background-color: #296d7f;
                  color: #ffffff;
                  border-radius: 15px;
                "
              >
                <p>
                  &ensp;&ensp;&ensp;DeepCBA integrates a total of 3kb chromatin
                  sequences upstream and downstream of the transcription
                  start site and transcription termination site of higher
                  plants (Maize, Rice, Cotton and Wheat) to predict gene
                  expression.
                  <!-- convolution neural network module, bidirectional long-term and
                  short-term memory network module and self-attention mechanism
                  module, as shown in the following figure. <br />
                  &ensp;&ensp;&ensp;The overall process of DeepCBA is as
                  follows:<br />
                  &ensp;&ensp;&ensp;First, encode the sequence with length of
                  3000 bp and 1500 bp into 4*3000/4*1500 one-pot encoding
                  matrix; -->
                  <br />
                  <br />
                </p>
                <div
                  class="image-content"
                  style="margin-top: 10px; width: 100%"
                >
                  <img src="../img/homeimg.png" style="width: 95%;;" />
                </div>
              </el-card>
            </el-col>

            <el-col :span="12">
              <el-card
                class="homecard"
                style="
                  background-color: #296d7f;
                  color: #ffffff;
                  border-radius: 15px;
                  background: #1f4e3d;
                  /* min-width: 800px; */
                  /* background: -webkit-linear-gradient(left, #fff1eb, #ace0f9); */
                "
              >
                <p>
                  &ensp;&ensp;&ensp;DeepCBA integrates data from different
                  tissues of higher plants to predict gene expression. It can
                  also realize important motif mining, cross-tissue and genotype
                  expression prediction, and refined research on remote
                  regulatory elements.
                </p>
                <div
                  class="image-content"
                  style="margin-top: 10px; width: 100%;"
                >
                  <img src="../img/home3.png" style="width: 82%" />
                </div>
                <!-- <el-button
                  class="rouButton"
                  @click="$router.push('/Expression/index')"
                  >Go Tools</el-button
                > -->

                <div
                  class="product-list-box"
                  style="width: 100%; margin: 0 auto"
                >
                  <div class="product-list-item">
                    <div
                      class="cursor"
                      @click="$router.push('/Expression/maize')"
                    >
                      <img src="../assets/picture/yumiICON.png" alt="Icon" />
                      <h5>Maize</h5>
                    </div>
                  </div>

                  <div class="product-list-item">
                    <div
                      class="cursor"
                      @click="$router.push('/Expression/rice')"
                    >
                      <img
                        src="../assets/picture/southeast-removebg-preview.png"
                        alt="Icon"
                      />
                      <h5>Rice</h5>
                    </div>
                  </div>
                  <div class="product-list-item">
                    <div
                      class="cursor"
                      @click="$router.push('/Expression/cotton')"
                    >
                      <img src="../assets/picture/mianhuaICON.png" alt="Icon" />
                      <h5>Cotton</h5>
                    </div>
                  </div>
                  <div class="product-list-item">
                    <div
                      class="cursor"
                      @click="$router.push('/Expression/wheat')"
                    >
                      <img src="../assets/picture/xiaomaiICON.png" alt="Icon" />
                      <h5>Wheat</h5>
                    </div>
                  </div>
                </div>
                <div class="shape-bottom-right">
                  <img src="../assets/picture/21.png" alt="Image Not Found" />
                </div>
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
        <el-col :span="24">
          <el-card class="bottom-card">
            <div style="margin-bottom: 50px; text-align: justify">
              <h2 style="font-weight: bold; font-size: 30px;position: relative;display: inline-block;" class="section-header">Related Publications</h2>
              <p style="font-size: 20px; width: 100%">
                Peng Y, Xiong D, Zhao L, et al. <strong>Chromatin interaction maps
                reveal genetic regulation for quantitative traits in maize.</strong> 
                Nature Communications 10: 2632(2019).<br />
                Li E, Liu H, Huang L, et al. <strong>Long-range interactions between
                proximal and distal regulatory regions in maize.</strong>  Nature
                Communications 10: 2633(2019).<br />
                Sun Y, Dong L, Zhang Y, et al. <strong>3D genome architecture
                coordinates trans and cis regulation of differentially expressed
                ear and tassel genes in maize.</strong>  Genome Biology 21(1):
                1-25(2020).<br />
                Washburn J D, Mejia-Guerra M K, Ramstein G, et al. <strong>
                  Evolutionarily informed deep learning methods for predicting
                relative transcript abundance from DNA sequence.</strong>
                 Proceedings of the National Academy of Sciences of the United States of America
                116(12): 5542-5549(2019).<br />
                Tu, X., Mejía-Guerra, M.K., Valdes Franco, J.A. et al. <strong>
                  Reconstructing the maize leaf regulatory network using ChIP-seq
                data of 104 transcription factors.
                </strong>
                 Nature Communications 11, 5089 (2020).
                <br />
                Tian, T., Wang, S., Yang, S. et al. <strong>
                  Genome assembly and
                genetic dissection of a prominent drought-resistant maize
                germplasm.
                </strong>  Nature Genetics 55, 496–506 (2023).
              </p>
            </div>
            <div class="shape-bottom-right">
              <img
                src="../assets/picture/v1.png"
                alt="Image Not Found"
                style="height: 300px"
              />
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
// import "../assets/css/style.css";
import dayjs from 'dayjs';
const getMockData = (date) => {
  const data = [{ id: 1, name: 'income', createAt: formatDate(date) }];
  return data;
  function formatDate(date) {
    return dayjs(date).format('YYYY-MM-DD HH:mm:ss');
  }
}
export default {
  name: "Home",
  components: {},
  data() {
    return {
      list1: [],
    };
  },
};
</script>
<style scoped src='../assets/css/style.css'></style>
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
  position: relative;

  z-index: 1;
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
    url("../img/homeback2.png");
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
  /* position: relative; */
  display: flex;
  flex-direction: column;
  width: 100%;
  /* min-width: 960px;
  min-height: calc(100vh - 60px); */
  background: -webkit-linear-gradient(rgba(250, 250, 250, 0.8), #fafafa 50%);
  padding-left: 0;
  padding-top: 193px !important;
  margin-top: -300px;
  padding-bottom: 110px;
  z-index: -1;
}

.bottom-card {
  text-align: center;
  /* background: linear-gradient(220.55deg, #0C3A2D 0%, #6D9773 100%);             */
  /* background: -webkit-linear-gradient(transparent, rgb(250, 250, 250) 0%); */

  color: #050505;
  border-radius: 30px;
  background: linear-gradient(120deg, #eaeaea 0%, #c0c0c0 100%);

  position: relative;

  z-index: 1;
}

.section-header:after {
    display: block;
    width: 100%;
    position: absolute;
    top: 100%;
    left: 0;
    content: ' ';
    height: 3px;
    background: #28a745;
}
/* .container>span { width: 100px; height: 100px; text-align: center; } */
</style>
