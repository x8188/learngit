<!-- 
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
  <div class="tool">
    <!-- <router-link to="/tools/Methylation"></router-link> -->
    <!-- <router-link to="/Expression"></router-link> -->
    <!-- <router-view /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "index",
  components: {},
  data() {
    return {
      list1: [],
      typelist: ["CHH", "CHG", "CG"],
      InputSeqs: "",
      loading: true,
      methltype: "CHG",
      isShowImg: false,
    };
  },
  methods: {
    handleChange(value) {
      console.log(value);
    },
    confirmtype() {
      this.loading = !this.loading;
      console.log(this.methltype);
    },
    submitseqs() { },
    openimg() {
      this.isShowImg = !this.isShowImg;
      if (this.isShowImg) {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "160%";
        temp.childNodes[0].style.height = "340px";
        temp.childNodes[1].style.width = "160%";
        temp.childNodes[1].style.height = "160px";
        temp.setAttribute("class", "isopenimg");
      } else {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "100%";
        temp.childNodes[0].style.height = "280px";
        temp.childNodes[1].style.width = "100%";
        temp.childNodes[1].style.height = "110px";
        temp.setAttribute("class", "showimg");
      }
    },
  },
  created() { },
};
</script>
<style scoped>
.tool {
  height: 1500px;
}

.tool-up {
  width: 80%;
  margin: 0 auto;
}

.top-text {
  text-align: center;
}

.showimg {
  cursor: zoom-in;
  /* width: 80%; */
}

.isopenimg {
  width: 90%;
  margin: 0 auto;
  overflow-x: scroll;
  cursor: zoom-out;
}
</style>