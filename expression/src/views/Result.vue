<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="result">
    <!-- <div style="margin: 15px; margin: 0 auto; width: 80%; text-align: center">
      <h1>This is an result page</h1>
    </div> -->
    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 30px">Promoter proximal region interaction</h1>
      <!-- </div> -->
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 40px">
      <a-row>
        <a-col :span="12">
          <div>
            <p style="margin-top: 35px; font-size: 25px">
              &nbsp; &nbsp;&nbsp;&nbsp;这对目标 数据集(五套 PPI
              数据)分别以回归分析中的皮尔逊相关系数 Pearson 和决定系数 R-Square
              来衡量模型的 优异，结果显示五套数据中 Pearson 最高为 0.94[Shoot
              (Li et al. 2019)]，最低为 0.85[Tassel (Sun et al. 2020)],
              五套数据中 R2 最大为 0.88，最小为 0.73;
            </p>
          </div>
        </a-col>
        <a-col :span="12">
          <div style="width: 80%; height: 80%; margin: 0 auto">
            <img
              style="width: 100%; height: 100%"
              src="../img/results/PPI/PPI_Saliency.jpg"
            />
          </div>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="6">
          <img style="width: 100%" src="../img/results/PPI/PPI_Ear_li.jpg" />
        </a-col>
        <a-col :span="6">
          <img style="width: 100%" src="../img/results/PPI/PPI_Ear_sun.jpg" />
        </a-col>
        <a-col :span="6">
          <img style="width: 100%" src="../img/results/PPI/PPI_Shoot_li.jpg" />
        </a-col>
        <a-col :span="6">
          <img
            style="width: 100%"
            src="../img/results/PPI/PPI_Shoot_peng.jpg"
          />
        </a-col>
      </a-row>
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 35px">
      <p style="font-size: 25px">
        &nbsp; &nbsp;&nbsp;&nbsp;展示的为 DeepCBA 模型所预测的基于 PPI 的 Gene
        表达量真实 值和预测值间的拟合分布，从拟合分布图可以看出在玉米 B73 材料中
        DeepCBA 模型针对不同组织下的表 达量预测十分精准。
      </p>
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 10px">
      <a-row>
        <a-col :span="12">
          <img style="width: 100%" src="../img/results/PPI/Ear_sun.jpg" />
        </a-col>
        <a-col :span="12">
          <img style="width: 100%" src="../img/results/PPI/Shoot_Li.jpg" />
        </a-col>
      </a-row>
      <!-- <img style="width: 100%; height: 280px" src="../img/CHG_TN.png" />
      <img style="width: 100%; height: 150px" src="../img/seqs.png" /> -->
    </div>
    <div class="top wrap1">
      <!-- <div class="box box1"> -->
      <h1 style="font-size: 30px">Promoter-distal element interaction</h1>
      <!-- </div> -->
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 35px">
      <p style="font-size: 25px">
        &nbsp; &nbsp;&nbsp;&nbsp;展示的为 DeepCBA 模型所预测的基于 PDI 的 Gene
        表达量的真实值和预测值之间的拟合分布，从实验 结果可知基于 PDI 的 Gene
        表达量预测中，最终的结果很大程度会受到原始数据中远端元件的分布、数量
        等因素的影响。
      </p>
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 40px">
      <a-row>
        <a-col :span="8">
          <img style="width: 100%" src="../img/results/PDI/Ear_Li.jpg" />
        </a-col>
        <a-col :span="8">
          <img style="width: 100%" src="../img/results/PDI/Shoot_Li.jpg" />
        </a-col>
        <a-col :span="8">
          <img style="width: 100%" src="../img/results/PDI/Shoot_Peng.jpg" />
        </a-col>
      </a-row>
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 35px">
      <p style="font-size: 25px">
        &nbsp; &nbsp;&nbsp;&nbsp;展示的为 DeepCBA 模型所预测的基于 PDI 的 Gene
        表达量的真实值和预测值之间的拟合分布，从实验 结果可知基于 PDI 的 Gene
        表达量预测中，最终的结果很大程度会受到原始数据中远端元件的分布、数量
        等因素的影响。
      </p>
    </div>
    <div
      style="width: 80%; margin: 0 auto; margin-top: 10px; margin-bottom: 30px"
    >
      <a-row>
        <a-col :span="8">
          <img style="width: 100%" src="../img/results/PDI/PDI_Ear_li.jpg" />
        </a-col>
        <a-col :span="8">
          <img style="width: 100%" src="../img/results/PDI/PDI_Shoot_li.jpg" />
        </a-col>
        <a-col :span="8">
          <img
            style="width: 100%"
            src="../img/results/PDI/PDI_Shoot_peng.jpg"
          />
        </a-col>
      </a-row>
      <!-- <img style="width: 100%; height: 280px" src="../img/CHG_TN.png" />
      <img style="width: 100%; height: 150px" src="../img/seqs.png" /> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Result",
  components: {},
  data() {
    return {};
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
.result {
  /* height: 80%; */
  /* text-align: center; */
  /* width: 80%; */
  margin: 0 auto;
}
.top {
  width: 90%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  margin: 15px;
  margin: 0 auto;
  height: 50px;
  margin-top: 50px;
  background-color: #f0f8ff;
}
</style>