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
    <!-- <img src="liuLab.jpg" alt="" style="width: 100%;margin: 20px 0px;"> -->
    <div class="container-block">
        <img src="liuLab.jpg">
        <div class="inner-block">
          <div class="slider-top-right"></div>
        </div>
        <div class="block-content">
          <h1>Contact us</h1>
        </div>
      </div>

    <div class="row">
      <div class="services-style-two col-xl-3 col-md-3">
        <div class="services-style-two-item">
          <div class="info">
            <div class="thumb">
              <img src="../assets/picture/34.jpg" alt="Image Not Found" />
            </div>
            <p style="font-size: 25px;font-weight: bolder;">
              xxxxxx
            </p>
            <p>
              email:xxxxxxxxxxxx@xxx.xxx
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
            <p style="font-size: 25px;font-weight: bolder;">
              xxxxxx
            </p>
            <p>
              email:xxxxxxxxxxxx@xxx.xxx
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
            <p style="font-size: 25px;font-weight: bolder;">
              xxxxxx
            </p>
            <p>
              email:xxxxxxxxxxxx@xxx.xxx
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
            <p style="font-size: 25px;font-weight: bolder;">
              xxxxxx
            </p>
            <p>
              email:xxxxxxxxxxxx@xxx.xxx
            </p>
          </div>
          <h5 class="title">
            <a href=""
              ><i class="flaticon-cow-3"></i> Dairy Production</a
            >
          </h5>
        </div>
      </div>
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
  height: 1200px;
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

.container-block {
	color: #fff;
	display: inline-block;
	margin: 2rem;
	// max-width: 500px;
	position: relative;	
	&::before {
		background-color: rgba(0, 0, 0, .1);
		bottom: 0;
		content: '';
		display: block;
		position: absolute;
		top: 0;
		width: 100%;
	}
	&:hover {
		.inner-block:before,
		.slider-top-right:after {
			height: 100%;
		}
		.inner-block:after,
		.slider-top-right:before {
			width: 100%;
		}
	}
	img {
		display: block;
		max-width: 100%;
	}
}

.block-content {
	position: absolute;
	bottom: 10%;
	left: 10%;
	padding: 0 1rem;
}

.slider-top-right:before,
.inner-block:after {
	height: 4px;
	transition: width .75s ease;
	width: 0%;
}

.slider-top-right:after,
.inner-block:before {
	height: 0%;
	transition: height .75s ease;
	width: 4px;
}

.inner-block:before,
.inner-block:after,
.slider-top-right:before,
.slider-top-right:after {
	background-color: #fff;
	content: '';
	display: block;
	position: absolute;
}

.inner-block {
	font-size: 2em;
	width: 90%;
	height: 90%;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	margin: auto;
	&:before {
		bottom: 0;
		left: 0;
	}
	&:after {
		bottom: 0;
		right: 0;
	}
}

.slider-top-right {
	position: relative;
	width: 100%;
	height: 100%;
	&:before {
		top: 0;
		left: 0;
	}
	&:after {
		top: 0;
		right: 0;
	}
}
</style>
