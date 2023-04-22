<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="about">
    <div style="margin: 15px">
      <h1 style="font-size: 40px; font-weight: bold">TOUR TEAM</h1>
    </div>
    <!-- <div class="member">
      <a-card
        hoverable
        :bordered="false"
        v-for="item in list1"
        :key="item"
        class="item-card"
      >
        <img class="img" slot="cover" :src="item" />

        <a-card-meta
          title="Description"
          description="This is the description.This is the descriptionThis is the description"
        >
        </a-card-meta>
        <a-card-meta title="Contact" description="lsj<at>google.con" />
      </a-card>
    </div> -->
    <div class="row">
      <div class="services-style-two col-xl-3 col-md-3">
        <div class="services-style-two-item">
          <div class="info">
            <div class="thumb">
              <img src="../assets/picture/34.jpg" alt="Image Not Found" />
            </div>
            <p>
              Continue indulged speaking technical maximum horrible domestic
              position seeing.
            </p>
          </div>
          <h5 class="title">
            <a href=""
              ><i class="flaticon-vegetable"></i> Fresh Vegetables</a
            >
          </h5>
        </div>
      </div>
      <div class="services-style-two col-xl-3 col-md-3">
        <div class="services-style-two-item">
          <div class="info">
            <div class="thumb">
              <img src="../assets/picture/34.jpg" alt="Image Not Found" />
            </div>
            <p>
              Recenting indulged speaking technical maximum horrible domestic
              position seeing.
            </p>
          </div>
          <h5 class="title">
            <a href=""
              ><i class="flaticon-corn"></i> Agricultural</a
            >
          </h5>
        </div>
      </div>
      <div class="services-style-two col-xl-3 col-md-3">
        <div class="services-style-two-item">
          <div class="info">
            <div class="thumb">
              <img src="../assets/picture/34.jpg" alt="Image Not Found" />
            </div>
            <p>
              Continue indulged speaking technical maximum horrible domestic
              position seeing.
            </p>
          </div>
          <h5 class="title">
            <a href=""
              ><i class="flaticon-bees"></i> Organic Products</a
            >
          </h5>
        </div>
      </div>
      <div class="services-style-two col-xl-3 col-md-3">
        <div class="services-style-two-item">
          <div class="info">
            <div class="thumb">
              <img src="../assets/picture/34.jpg" alt="Image Not Found" />
            </div>
            <p>
              Maximum indulged speaking technical maximum horrible domestic
              position seeing.
            </p>
          </div>
          <h5 class="title">
            <a href=""
              ><i class="flaticon-cow-3"></i> Dairy Production</a
            >
          </h5>
        </div>
      </div>
      <!-- End Single Item -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'



export default {
  name: "About",
  components: {},
  data() {
    return {
      list1: [
        "https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png",
        "https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png",
        "https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png",
        "https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png",
      ],
    };
  },
  methods: {},
  created() {},
};
</script>

<style scoped src='../assets/css/bootstrap.css'></style>
<style scoped src='../assets/css/style.css'></style>
<style scoped src='../assets/css/flaticon-set.css'></style>

<style scoped>

.about {
  height: 1000px;
  text-align: center;
  width: 70%;
  margin: 0 auto;
}
.img {
  height: 230px;
  border-radius: 50%;
}
.member {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.item-card {
  width: 230px;
  margin: 15px;
  height: 385px;
}
</style>
<style lang="less" scoped>
/deep/.ant-card-meta-detail > div:not(:last-child) {
  margin-bottom: 0px;
}
</style>
