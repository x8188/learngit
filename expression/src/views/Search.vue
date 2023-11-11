<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="result">
    <!-- <div class="top wrap1">
      <div class="box box1">
        <h1 style="font-size: 30px">Statistics of Data Used in PlantDeepSEA</h1>
      </div>
    </div>
    <div class="contain" style="text-align: center">
      <a-row :gutter="24" style="font-size: 20px; font-weight: bold">
        <a-col :span="5">ID</a-col>
        <a-col :span="4">Methyl_Type</a-col>
        <a-col :span="4">Methyl_Level</a-col>
        <a-col :span="4">SuppReads_Methyl</a-col>
        <a-col :span="6">SuppReads_ALL</a-col>
      </a-row>
      <a-row
        :gutter="24"
        style="font-size: 15px"
        v-for="item in DataList"
        :key="item.id"
      >
        <a-col :span="5">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="4">{{ item.name }}</a-col>
        <a-col :span="6">{{ item.description }}</a-col>
      </a-row>
    </div>
    <div class="top">
      <h1 style="font-size: 30px">Statistics of Result</h1>
    </div>
    <div class="contain">
      <h3 style="margin-top: 20px; margin-left: 10px">
        We counted the experimental data
      </h3>
      <div style="text-align: center">
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
        <img src="../img/statistic.png" style="width: 40%" />
      </div>
    </div>
    <div class="top">
      <h1 style="font-size: 30px">Evaluations of Models</h1>
    </div>
    <div class="contain">
      <h3 style="margin-top: 20px; margin-left: 10px">We get ROC curve</h3>
      <div style="text-align: center">
        <img src="../img/roc.png" style="width: 65%" />
      </div>
    </div> -->
    <!-- <Steps :steps1="3" :steps2="steps2"></Steps> -->
    <div class="top-text">
      <h1 style="font-size: 40px; font-weight: bolder; color: #22cac4">
        Task Queue
      </h1>
    </div>

    <!-- <h1 style="color: #0dbc79; font-size: 30px">Result retrieval</h1> -->
    <el-divider></el-divider>
    <!-- <p style="font-size: 20px">
      NOTE: The result files will be kept for 10 days on our server. Please
      download and save your files on time.
    </p> -->
    <div style="text-align: center">
      <el-input
        v-model="searchValue"
        placeholder="Input job identifier here"
        style="width: 50%; margin: 20px 0px"
        @keyup.enter.native="searchJob"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="searchJob"
        ></el-button>
      </el-input>
      <p style="color: #0dbc79; font-size: 20px; text-align: left">
        Job queue monitor(update every 10 seconds):
      </p>
      <div style="text-align: right; margin-top: -50px">
        <!-- <el-button @click="clearFilter" type="warning" plain class="reFilter"
          >Reset all Filters</el-button
        > -->
        <el-tooltip effect="dark" content="Refresh task list" placement="top">
          <el-button
            icon="el-icon-refresh-right"
            circle
            class="reBtn"
            @click="refresh"
          ></el-button>
        </el-tooltip>
      </div>

      <el-card class="box-card">
        <el-table :data="taskTable" ref="filterTable" style="font-size: 15px;"  max-height="500">
          <el-table-column prop="taskID" label="Task ID"> </el-table-column>
          <el-table-column
            prop="modelName"
            label="Model Name"
            :filters="filters"
            :filter-method="filterHandler"
            
          >
          </el-table-column>
          <el-table-column
            label="Task Status"
            :filters="filter_statu"
            :filter-method="filterStatu"
            width="150"
          >
            <template slot-scope="{ row }">
              <div id="status">
                <i
                  class="el-icon-success"
                  style="color: #0dbc79"
                  v-show="row.status == 2"
                ></i>
                <i
                  class="el-icon-error"
                  style="color: #d32f2f"
                  v-show="row.status == 3"
                ></i>
                <i class="el-icon-loading" v-show="row.status == 1"></i>
                <span class="iconfont icon-paidui" v-show="row.status == 0" style="font-size:20px"></span>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="submitTime" label="Submit Time">
          </el-table-column>
          <!-- <el-table-column prop="ttl1" label="Time Remaining" width="210">
          </el-table-column> -->
          <el-table-column label="Details Result(Click)">
            <template slot-scope="{ row }">
              <el-button
                type="primary"
                icon="el-icon-download"
                size="mini"
                @click="visTask(row)"
                class="viewBtn"
                >View results</el-button
              >
              <!-- <el-popconfirm title="确定删除吗？" @onConfirm="deleteTask(row)">
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                slot="reference"
              ></el-button>
            </el-popconfirm> -->
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <!-- <span class="iconfont icon-shaixuan"></span> -->
      <!-- <el-pagination
        @size-change="handleSizeChange"
        @current-change="getPageList"
        :current-page="page"
        :page-sizes="[5, 10, 50, 100]"
        :page-size="limit"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

// require这个函数是为了正确显示本地图片，将来换成网络地址不加

export default {
  name: "Result",
  components: {},
  data() {
    return {
      page: 1,
      limit: 5,
      // total: data.length,

      isShowImg: false,

      visid: undefined,
      img_chg: "",
      img_seq: "",
      steps2: 0,

      taskTable: [
        {
          email: "",
          modelName: "",
          status: "",
          submitTime: "",
          taskID: "",
          ttl: 0,
        },
      ],

      searchValue: "",

      filters: [],
      filter_statu: [
        { text: "wait", value: 0 },
        { text: "run", value: 1 },
        { text: "success", value: 2 },
        { text: "fail", value: 3 },
      ],

      statu: ["wait", ""],
      timer:null,
    };
  },
  methods: {
    deleteTask(row) {
      // 在此向服务器发请求，成功后删除
    },
    visTask(row) {
      if (row.status == 0) {
        this.$alert("This task is queuing", "Please wait patiently", {
          confirmButtonText: "confrim",
          type: "warning",
        });
        return;
      }
      else if(row.status == 1){
        this.$alert("This task is running", "Please wait patiently", {
          confirmButtonText: "confrim",
          type: "info",
        });
        return;
      }
      else if(row.status == 3){
        this.$alert("This task failed to run", "Error", {
          confirmButtonText: "confrim",
          type: "error",
        });
        return;
      }
      else {
        this.$router.push({
          path: `/show/${row.taskID}`,
        });
        return;
      }
    },
    getPageList(pager = 1) {
      this.page = pager;
      // 这里应该向后端发个请求，page limit
      // 参数包括当前页数以及每页所展示的数据个数
    },
    handleSizeChange(limit) {
      this.limit = limit;
      this.getPageList();
    },
    formatSeconds(value) {
      var secondTime = parseInt(value); // 秒
      var minuteTime = 0; // 分
      var hourTime = 0; // 小时
      var dayTime = 0; // 天
      var result = "";
      if (value < 60) {
        result = secondTime + " sec ";
      } else {
        if (secondTime >= 60) {
          // 如果秒数大于60，将秒数转换成整数
          // 获取分钟，除以60取整数，得到整数分钟
          minuteTime = parseInt(secondTime / 60);
          // 获取秒数，秒数取佘，得到整数秒数
          secondTime = parseInt(secondTime % 60);
          // 如果分钟大于60，将分钟转换成小时
          if (minuteTime >= 60) {
            // 获取小时，获取分钟除以60，得到整数小时
            hourTime = parseInt(minuteTime / 60);
            // 获取小时后取佘的分，获取分钟除以60取佘的分
            minuteTime = parseInt(minuteTime % 60);
            if (hourTime >= 24) {
              // 获取天数， 获取小时除以24，得到整数天
              dayTime = parseInt(hourTime / 24);
              // 获取小时后取余小时，获取分钟除以24取余的分；
              hourTime = parseInt(hourTime % 24);
            }
          }
        }
        if (secondTime > 0) {
          secondTime =
            parseInt(secondTime) >= 10 ? secondTime : "0" + secondTime;
          result = "" + secondTime + " sec ";
        }
        if (minuteTime > 0) {
          minuteTime =
            parseInt(minuteTime) >= 10 ? minuteTime : "0" + minuteTime;
          result = "" + minuteTime + " min " + result;
        }
        if (hourTime > 0) {
          result = "" + parseInt(hourTime) + " hour " + result;
        }
        if (dayTime > 0) {
          result = "" + parseInt(dayTime) + " day " + result;
        }
      }
      return result;
    },

    isEqual(object1, object2) {
      return object1.text === object2.text;
    },
    async getTasks() {
      let result = await this.$API.reqTasksInfo();
      if (result.code == 200) {
        this.taskTable = result.tasks;
        // this.taskTable.ttl=this.formatSeconds(this.taskTable.ttl)
        this.filters = [];
        this.taskTable.forEach((el) => {
          el["ttl1"] = this.formatSeconds(el.ttl);

          this.filters.push({ text: el.modelName, value: el.modelName });

        });
        const res = new Map();
        this.filters = this.filters.filter(
          (a) => !res.has(a.text) && res.set(a.text, 1)
        )
      }
      // console.log(this.filters[0]);
    },
    async searchJob() {
      await this.getTasks()
      this.taskTable = this.taskTable.filter((el) => {
        // console.log(el.taskID.search(this.searchValue))
        if(el.taskID.search(this.searchValue)!=-1) return true
        else return false
        // return el.taskID === this.searchValue;
      });
    },
    filterHandler(value, row, column) {
      // const property = column['property'];
      // return row[property] === value;
      return row.modelName === value;
    },
    filterStatu(value, row, column) {
      // const property = column['property'];
      // return row[property] === value;
      // console.log(row.status,value)
      return row.status == value;
    },
    refresh(){
      this.$refs.filterTable.clearFilter();
      this.getTasks()
      this.searchValue=""
    }
  },
  created() {
    this.getTasks();
  },
  mounted(){
    this.timer =setInterval(() => {
        this.getTasks()
      }, 10000);
  },
  beforeDestroy(){
    clearInterval(this.timer);
  },
};
</script>
<style scoped>
/* .result {
  height: 2000px;
  width: 80%;
  margin: 0 auto;
}
.top {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 15px;
  margin: 0 auto;
  height: 75px;
  margin-top: 50px;
  background-color: #f0f8ff;
}
.contain {
  border-style: solid;
  border-color: #f5f5f5;
} */
.result {
  width: 80%;
  margin: 0 auto;

  min-height: 1000px;
}

#status i {
  font-size: 25px;
}

.top-text {
  text-align: center;
  margin: 0 auto;
  height: 70px;
  margin-top: 30px;
  width: 800px;
  /* background:-webkit-linear-gradient(left,#93a5cf,#e4efe9) ; */
  /* background:-webkit-linear-gradient(top,#accbee,#e7f0fd) ; */
  border-radius: 8px;

  text-shadow: 0 2px 4px rgb(11 90 88 / 50%);
}

.viewBtn {
  margin: 0px 10px;
  font-size: 15px;
}

.reBtn {
  height: 55px;
  width: 55px;
  font-size: 25px;
  margin: 20px;
}
.reFilter {
  height: 50px;
  font-size: 15px;
}

::v-deep .el-table__column-filter-trigger .el-icon-arrow-down {
  font-family: "iconfont" !important;
  font-size: 15px;
  font-weight: bold;

  transform: unset
}
::v-deep .el-table__column-filter-trigger .el-icon-arrow-down:before {
  content: "\e74a";
}

</style>
