<!-- 
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="tool">
    <h1 id="modelSelect">Please Select PPI/PDI Model</h1>
    <el-row type="flex" style="margin-bottom:30px">
      <el-col :span="12" class="cardFa">
        <el-card class="card">
          <div slot="header">
            <span class="cardTitle">Corn</span>
          </div>
          <div style="text-align: center">
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
            <el-button
              class="rouButton"
              @click="$router.push('/Expression/zs97')"
              >Go Rice</el-button
            >
          </div>
        </el-card>
      </el-col>
    </el-row>
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
.cardFa{
  display:flex;
justify-content:center;
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
