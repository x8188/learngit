<template>
  <div>
    <a-affix :offset-top="150" id="steps">
      <el-tooltip
        effect="dark"
        content="Hide/Switch the step prompt"
        placement="right"
      >
        <el-button type="info" circle class="buttonClass" @click="flag = !flag">
          <i v-show="flag" class="el-icon-view"></i>
          <i v-show="!flag" class="el-icon-tickets"></i>
        </el-button>
      </el-tooltip>

      <div v-show="flag">
        <div style="height: 300px">
          <el-steps
            :active="steps1"
            finish-status="success"
            direction="vertical"
          >
            <el-step
              title="steps 1"
              icon="el-icon-thumb"
              description="Select Model"
            ></el-step>
            <el-step
              title="steps 2"
              icon="el-icon-edit"
              description="Manually input or upload files"
            ></el-step>
            <el-step
              title="steps 3"
              icon="el-icon-upload"
              description="Submit to Job Queue"
            ></el-step>
          </el-steps>
          <!-- <el-button style="margin-top: 12px" @click="next">下一步</el-button> -->
        </div>
        <el-button
          plain
          style="margin: 20px 0px 20px 0px"
          @click="$router.push('/search')"
        >
          Go to job queue</el-button
        >
        <div style="height: 200px">
          <el-steps
            :active="steps2"
            finish-status="success"
            direction="vertical"
          >
            <el-step
              title="steps 4"
              icon="el-icon-view"
              description="View Task Queue"
            ></el-step>
            <el-step
              title="steps 5"
              icon="el-icon-circle-check"
              description="Download result file"
            ></el-step>
          </el-steps>
          <!-- <el-button style="margin-top: 12px" @click="next">下一步</el-button> -->
        </div>
      </div>
    </a-affix>
  </div>
</template>

<script>
export default {
  name: "Steps",
  props: ["steps1", "steps2"],
  data() {
    return {
      flag: true,
    };
  },
  methods: {},
};
</script>

<style>
#steps {
  position: absolute;
  z-index: 999;
  left: 30px;
}

.buttonClass {
  width: 50px;
  height: 50px;

  margin-bottom: 10px;
}
.buttonClass i {
  font-size: 20px;
}
</style>
