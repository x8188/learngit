<template>
  <div>
    <a-affix :offset-top="100" id="content">
      <!-- <i class="el-icon-notebook-2" style="font-weight: bold; font-size: 40px"
        >CONTENT</i
      > -->
      <!-- <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
      >
        <el-submenu index="1" @click="goTop(1)">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>导航一</span>
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="2" @click="goTop(2)">
          <i class="el-icon-menu"></i>
          <span slot="title">导航二</span>
        </el-menu-item>
        <el-menu-item index="3" @click="goTop(3)">
          <i class="el-icon-document"></i>
          <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4" @click="goTop(4)">
          <i class="el-icon-setting"></i>
          <span slot="title">导航四</span>
        </el-menu-item>
      </el-menu> -->

      <el-tree
        :data="data"
        :props="defaultProps"
        @node-click="handleNodeClick"

        :default-expand-all="true"
      ></el-tree>
    </a-affix>

    <el-row class="tac" type="flex" justify="center">
      <el-col :span="12" id="doc">
        <i class="el-icon-s-management" ref="top1">导航1</i>
        <h2>选项1</h2>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <h2>选项2</h2>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <h2>选项3</h2>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <h2>选项4</h2>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>

        <i class="el-icon-s-management" ref="top2">导航2</i>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <i class="el-icon-s-management" ref="top3">导航3</i>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <i class="el-icon-s-management" ref="top4">导航4</i>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
        <i class="el-icon-s-management" ref="top5">导航5</i>
        <p>
          xxx xxxxxx xxxxxxx xxxxxxx xxxx xxxx xxxx xx xxx xxxx xxxxx xxx xx
          xxxxx xxx xxx xxxx xxx xxxx xxx xxxx xxxxx xxx xxx xxxxx xx xxx xxx
          xxxx xxx xx xx xxx xx xx x xxx xx xxx xxx xxx xx xxx xxx xxx xxxx xxx
          xxx xxx xx xx xxx xxx xx xxx xxxx xx xxx xxx xx xxx xxx x xxxx x xx
          xxx xx xx xxxx xxxx xxxx xxxxx xxxxxx xxxxx xxxxxx xxxx xxx xxx xx xxx
          xx xxx xxx xxx xxx xxx xxx xxx xxxx xxx xx xxxx xxxx
        </p>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          label: "导航1",
          ref:"top1",
          children: [
            {
              label: "选项1",
            },
            {
              label: "选项2",
            },
            {
              label: "选项3",
            },
            {
              label: "选项4",
            },
          ],
        },
        {
          label: "导航2",
          ref:"top2",
        },
        {
          label: "导航3",
          ref:"top3",
        },
        {
          label: "导航4",
          ref:"top4",
        },
      ],
      defaultProps: {
        children: "children",
        label: "label",
      },
    };
  },
  methods: {
    handleNodeClick(data) {
      // console.log(data);
      // console.log(data.label);

      this.$refs[data.ref].scrollIntoView({
        behavior: "smooth", // 平滑过渡
        block: "center", // start 上边框  center 中间  end 底部边框 与视窗顶部平齐
      });
    },
  },
};
</script>

<style>
#content {
  position: absolute;
  /* height: 600px; */
  width: 300px;
  z-index: 999;
}
#doc i {
  font-weight: bold;
  font-size: 30px;
}

#doc p{
  font-size: 20px;
  font-family: "Roboto",sans-serif;
  font-weight: 300;
}

.el-tree-node__label {
width: auto;
margin-top: 12px;
margin-left: 50px;
/* float: right; */
font-family: “Trebuchet MS”, Arial, Helvetica, sans-serif;
font-size: 18px;
/* color: #999999; */
line-height: 50px;
letter-spacing: 1px;
}

.el-tree-node__content {
  height: 35px;
}

.el-tree-node__expand-icon {
    color: #22CAB3;
    font-size: 20px;
}

.el-tree-node:focus > .el-tree-node__content {
    /* background-color: #66b1ff87 !important; */
    color: #22CAB3;
}
</style>
