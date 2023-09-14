<template>
  <div id="app">
    <div style="">
      <div id="nav" :style="opacityStyle">
        <div id="title" @click="$router.push('/')">
          <!-- <span>DeepCBA</span> -->
          <img src="./img/logo/logo2.png" style="height: 55px" />
        </div>

        <div class="link-wrapper" style="display: flex">
          <router-link to="/">Home</router-link>
          <!-- <a-dropdown placement="bottomCenter">
            <a class="ant-dropdown-link">
              Tools<i class="el-icon-arrow-down el-icon--right"></i>
            </a>
            <a-menu slot="overlay" id="tool">
              <a-menu-item
                ><router-link to="/Expression/index"
                  >Corn</router-link
                ></a-menu-item
              >
              <a-menu-item
                ><router-link to="/Expression/indexShui"
                  >Rice</router-link
                ></a-menu-item
              >
            </a-menu>
          </a-dropdown> -->
          <router-link to="/Expression/index">Tools</router-link>
          <router-link to="/search">Search</router-link>
          <router-link to="/result">Result</router-link>
          <router-link to="/tutorial">Tutorial</router-link>
          <router-link to="/about">Contact</router-link>
        </div>
      </div>
      <section class="featured1"></section>
      <div style="">
        <router-view />
      </div>
      <div class="foot">
        <!-- <h1
          style="
            color: white;
            font-weight: bold;
            font-size: 30px;
            text-align: center;
          "
        >
          Contact
        </h1> -->
        <div style="display: flex;width: 80%;margin: 0 auto;">
          <div style="flex: 1;">
            <h3 style="color: #fff;font-size: 1rem;font-weight: 500;">POWERED BY</h3>
            <el-row >
              <el-col :span="24">
                <a href="http://www.hzau.edu.cn/" target="_blank">
                  <img src="./img/footImg/hzau_logo_h100.png" alt="" class="img-fluid">
                </a>
              </el-col>
            </el-row >
          </div>

          <div style="flex: 7;text-align: center;">
            <h3 style="color: #fff;font-size: 1rem;font-weight: bolder;">LINKS</h3>
            <el-row :gutter="40"  type="flex" justify="center">
              <el-col :span="3">
                <a href="https://figshare.com/articles/dataset/Gossypium_anomalum_B1_genome/17280074" target="_blank">
                  <img src="./img/footImg/Cotton-1-logo.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="3">
                <a href="https://maizegdb.org/" target="_blank">
                  <img src="./img/footImg/maizeGDB.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="3">
                <a href="http://maizego.org/index.html" target="_blank">
                  <img src="./img/footImg/maizego_h100.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="3">
                <a href="https://meme-suite.org/meme/index.html" target="_blank">
                  <img src="./img/footImg/MEME.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="2">
                <a href="http://plantdeepsea.ncpgr.cn/" target="_blank">
                  <img src="./img/footImg/PlantDeepSEA.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="3">
                <a href="http://planttfdb.gao-lab.org/index.php" target="_blank">
                  <img src="./img/footImg/PlantTFDB.png" alt="" class="img-fluid">
                </a>
              </el-col>
              <el-col :span="3">
                <a href="http://rice.hzau.edu.cn/rice_rs2/" target="_blank">
                  <img src="./img/footImg/Rice-data-logo.png" alt="" class="img-fluid">
                </a>
              </el-col>
            </el-row >
          </div>
        </div>
        <p
          style="
            width: 80%;
            text-align: center;
            margin: 0 auto;
            padding: 10px 0;
          "
        >
          Address: Room B320, Research Office of Artificial Intelligence
          Research Group, Huazhong Agricultural university, Wuhan, 430070, China
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backShow: false,
      opacityStyle: {
        opacity: 1, //渐变色从0开始
      },
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      //逐渐填充start
      var scrollTop = document.documentElement.scrollTop;
      // console.log(scrollTop);
      if (scrollTop > 0) {
        let opacity = 0.3 + scrollTop / 210;
        let height = 100 - 40 * (scrollTop / 300);
        height = height < 60 ? 60 : height;
        // console.log("height", height);
        opacity = opacity > 1 ? 1 : opacity; //渐变色从0到1
        this.opacityStyle = {
          // opacity: opacity,
          height: height + "px",
          "line-height": height + "px",
        };
        this.backShow = true;
      } else {
        this.backShow = false;
      }
      //逐渐填充end
    },
    onClick({ key }) {
      this.$router.push(`/tools/${key}`);
      console.log(this.$router);
      console.log(`Click on item ${key}`);
    },
    visibleChange(visible) {
      console.log(visible);
    },
  },
};
</script>

<style>
body {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 1000px;
  margin: 0 auto;
  min-width: 1500px;
}
#title {
  font-size: 30px;
  color: #fff;
  margin-left: 30px;
  /* text-shadow: 0 2px 4px rgba(255, 255, 255, 0.5); */
  text-shadow: 3px 3px 8px rgba(255, 255, 255, 0.5);
  cursor: pointer;
}
/* #welcome{
  width: 100%;
  background-image:url('../dist/img/welcome.jpg');
} */
#nav {
  line-height: 100px;
  background-color: #004b5f;
  /* background-image: url("./img/back.png"); */

  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
  height: 100px;
  display: block;
  margin-bottom: 0;
  padding-bottom: 0;
  display: flex;
}

#nav a {
  font-weight: bold;
  font-size: 25px;
  color: #fff;

  /* text-decoration: none; */
}

#nav .link-wrapper {
  flex: 1;
}

.link-wrapper {
  display: flex;
  justify-content: center;
}

.link-wrapper a {
  max-width: 250px;
  flex: 1;
  text-align: center;
}

#tool a {
  /* Margin  : 10px; */
  height: 50px;
  font-weight: bold;
  font-size: 20px;
  color: #42b983;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
.foot {
  /* position: fixed; */
  bottom: 0px;
  background-color: #2a2730;
  color: white;
  height: 210px;
  /* text-align: center; */
  /* margin: 0 auto; */
  padding-top: 2em;
}
section.featured1 {
  padding: 40px 0 60px;
  /* background-image: url("./img/back.png"); */
  background-color: #004b5f;

  color: #fdfdfd;
}

.img-fluid {
    max-width: 100%;
    height: auto;
}
</style>
