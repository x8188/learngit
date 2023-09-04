<!-- 
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="tool">
    <h1 id="modelSelect">Please Select species</h1>            
    
    <!-- <p class="modelP">
              In this study, the definition of the proximal region of the
              promoter based on prior research is as follows: the proximal
              region of the gene promoter is defined as 1Kb upstream and 0.5Kb
              downstream of the transcription start site (TSS), and the
              transcription stop site (TTS ) consists of upstream 0.5Kb and
              downstream 1Kb.
            </p>
            <p class="modelP">
              At the same time, the following definition is
              given for the identification of PPI: both ends of the interaction
              fragment have an intersection with the gene promoter (the segment
              from 2Kb upstream to 1.5Kb downstream of the gene transcription
              start site), which is defined as the region adjacent to the
              promoter Interaction (Promoter proximal region interaction, PPI).
            </p> -->
                        <!-- <p class="modelP">
              Compared with the definition of the proximal region of the gene
              promoter defined in this study, any region that does not conform
              to the proximal region is defined as the distal region of the gene
              promoter, that is, one end of the interaction fragment intersects
              with the gene promoter and the other end Intersection with distal
              elements is defined as Promoter-distal element interactions (PDI).
            </p>
            <p class="modelP">
              In this study, when predicting gene expression based on chromatin
              distal interaction, we selected a sequence of 1500 bp upstream 1k
              and 0.5k downstream of the gene promoter as the chromatin sequence
              corresponding to the gene.
            </p> -->
    <!-- <el-row type="flex" style="margin-bottom: 30px">
      <el-col :span="12" class="cardFa">
        <el-card class="card">
          <div slot="header">
            <span class="cardTitle">Corn</span>
          </div>
          <div style="text-align: center">

            <el-button
              class="rouButton"
              @click="$router.push('/Expression/PPI')"
              >Go Corn</el-button
            >
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="cardFa">
        <el-card class="card">
          <div slot="header">
            <span class="cardTitle">Rice</span>
          </div>
          <div style="text-align: center">
            <el-button
              class="rouButton"
              @click="$router.push('/Expression/zs97')"
              >Go Rice</el-button
            >
          </div>
        </el-card>
      </el-col>
    </el-row> -->
    <div class="gallery-style-one-area default-padding-top">
      <div class="">
        <div class="row justify-content-md-center">
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                @click=" $router.push('/Expression/maize') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/8.jpg"
                  alt="Thumb"
                />
                <div class="overlay">
                  <span>PPI/PDI</span>
                  <h4><a style="pointer-events: none">Maize</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  Provide online and real-time services for high-precision prediction of gene expression levels based on near- and far-end interactions of chromatin in maize.
                <br>(1) Prediction of gene expression based on chromatin interaction (training data and three tissues in the source B73 material)
                <br>(2) Mining important segments in chromatin interaction sequences that affect gene expression
                </p>
              </div>
            </div>
          </div>
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                @click=" $router.push('/Expression/rice') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/shuidao.jpg"
                  alt="Thumb"
                />
                <div class="overlay">
                  <span>zs97/mh63</span>
                  <h4><a style="pointer-events: none">Rice</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  Provide online real-time services for high-precision prediction of gene expression based on gene-gene interaction in rice species.
                  <br>(1) Model construction based on different data sets under the two materials of rice MH63 and ZS97 to achieve high-precision prediction of rice gene expression
                </p>
              </div>
            </div>
          </div>
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                @click=" $router.push('/Expression/cotton') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/mianhua.jpg"
                  alt="Thumb"
                />
                <div class="overlay" style="">
                  <span>A2/B1/C1/D5...</span>
                  <h4><a style="pointer-events: none">Cotton</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  Provide online real-time service of high-precision prediction of gene expression based on gene-gene interaction for eight materials of cotton species.
                  <br>(1) The cotton materials involved are: A2, B1, C1, D5, E1, F1, G1, K2
                </p>
              </div>
            </div>
          </div>
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                id="ex2"
                @click=" $router.push('/Expression/wheat') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/xiaomai.jpg"
                  alt="Thumb"
                />
                <div class="overlay">
                  <span>TPM</span>
                  <h4><a style="pointer-events: none">Wheat</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  Provide online real-time service for high-precision prediction of gene expression based on gene-gene interaction in wheat species.
                </p>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="row justify-content-md-center">
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                @click=" $router.push('/Expression/cotton') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/mianhua.jpg"
                  alt="Thumb"
                />
                <div class="overlay" style="">
                  <span>Cotton</span>
                  <h4><a style="pointer-events: none">Cotton</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  BnIRis a a multi-omics collaborative resource and tool
                  platform for Brassica napus. It integrates and analyzes
                  datasets from genomics, epigenomics, transcriptomics,
                  metabolomics and phenomics, and offers multiple tools.
                </p>
              </div>
            </div>
          </div>
          <div class="col-xl-3 Colcenter">
            <div>
              <div
                class="gallery-style-one cursor"
                id="ex2"
                @click=" $router.push('/Expression/zs97') "
              >
                <img
                  class="hvr-grow-shadow"
                  src="../../assets/picture/7.jpg"
                  alt="Thumb"
                />
                <div class="overlay">
                  <span>Crop Phenotype <br />Management Platform</span>
                  <h4><a style="pointer-events: none">表型</a></h4>
                </div>
              </div>
              <div>
                <p class="detailP">
                  The crop phenotype data management platform offers the search
                  and analysis of massive experimental data such as water
                  saving, drought resistance, tillering, genome-wide association
                  study (GWAS), recombinant inbred lines (RIL), quantitative
                  trait locus (QTL).
                </p>
              </div>
            </div>
          </div>
        </div> -->
      </div>
    </div>
    <Back></Back>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "index",
  components: {},
  data() {
    return {};
  },
  methods: {},
  created() {},
};
</script>

<style scoped src='../../assets/css/bootstrap.min.css'></style>
<style scoped src='../../assets/css/style.css'></style>

<style scoped>
.tool {
  width: 80%;
  margin: 0 auto;
  height: 800px;
}

.cardTitle {
  margin-left: 20px;
  /* margin: auto; */
  font-size: 30px;
  font-weight: bold;
  color: #22cab3;
}
.card {
  width: 80%;
  height: 100%;
}
.cardFa {
  display: flex;
  justify-content: center;
}
.modelP {
  text-align: justify;
  font-size: 18px;
}

#modelSelect {
  text-align: center;
  font-weight: bold;
  color: #003164;
  margin: 50px;
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
</style>
