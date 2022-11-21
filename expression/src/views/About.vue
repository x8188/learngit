<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="about">
    <div style="margin: 15px">
      <h1 style="font-size: 40px; font-weight: bold">TOUR TEAM</h1>
    </div>
    <div class="member">
      <a-card
        hoverable
        :bordered="false"
        v-for="item in list1"
        :key="item"
        class="item-card"
      >
        <img class="img" slot="cover" :src="item" />
        <!-- <template slot="actions" class="ant-card-actions"> -->
        <!-- <a-icon key="setting" type="setting" /> -->
        <!-- <a-icon key="edit" type="edit" /> -->
        <!-- <a-icon key="ellipsis" type="ellipsis" /> -->
        <!-- </template> -->
        <a-card-meta
          title="Description"
          description="This is the description.This is the descriptionThis is the description"
        >
          <!-- <a-avatar
            slot="avatar"
            src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
          /> -->
        </a-card-meta>
        <a-card-meta title="Contact" description="lsj<at>google.con" />
      </a-card>
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
<style scoped>
.about {
  height: 1000px;
  text-align: center;
  width: 80%;
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