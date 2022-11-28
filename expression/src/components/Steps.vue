<template>
  <div>
    <a-affix :offset-top="150" id="steps">
      <div style="height: 300px">
        <el-steps :active="steps1" finish-status="success" direction="vertical" >
          <el-step
            title="步骤 1"
            icon="el-icon-thumb"
            description="选择模型"
          ></el-step>
          <el-step
            title="步骤 2"
            icon="el-icon-edit"
            description="手动输入或者上传文件"
          ></el-step>
          <el-step
            title="步骤 3"
            icon="el-icon-upload"
            description="提交到作业序列"
          ></el-step>
        </el-steps>
        <!-- <el-button style="margin-top: 12px" @click="next">下一步</el-button> -->
      </div>
      <el-button plain style="margin:20px 0px 20px 0px;">查看作业队列</el-button>
      <div style="height: 200px">
        <el-steps :active="steps2" finish-status="success" direction="vertical" >
          <el-step
            title="步骤 4"
            icon="el-icon-view"
            description="查看可视化结果"
          ></el-step>
          <el-step
            title="步骤 5"
            icon="el-icon-edit"
            description="手动输入序列或者上传序列文件"
          ></el-step>
        </el-steps>
        <!-- <el-button style="margin-top: 12px" @click="next">下一步</el-button> -->
      </div>
    </a-affix>
  </div>
</template>

<script>
export default {
  name: "Steps",
  props: ['steps1',"steps2"],
  data() {
    return {
    };
  },
  methods: {

  },
};
</script>

<style>
#steps {
  position: absolute;
  z-index: 999;
  left: 30px;
}
</style>
