<template>
  <div>
    <!-- slider范围 -->
    <!-- <div
        class="block"
        style="margin-left: 50px; margin-right: 50px; margin-top: 50px"
      >
        <el-slider :min="0" :max="6000" v-model="value" range> </el-slider>
      </div> -->
    <!-- 折线图 -->
    <div class="echart" :id="chartName" :style="myChartStyle"></div>
    <!-- 热图 -->
    <div
      class="echart"
      :id="chartHotname"
      style="margin-top: 50px; width: 100%; height: 400px; float: left"
    ></div>
    <!-- <div
      class="echart"
      :id="chartName + 'xx'"
      style="margin-top: 50px; width: 100%; height: 300px; float: left"
    ></div> -->
  </div>
</template>
  
  <script>
import * as echarts from "echarts";

export default {
  name: "Chart",
  props: ["chartName", "chartHotname", "visData", "chartHotData"],
  watch: {
    visData: {
      handler(newVal, oldVal) {
        this.initEcharts();
      },
    },
    chartHotData: {
      handler(newVal, oldVal) {
        this.initEchartsHot();
      },
    },
  },
  computed: {
    data2() {
      return this.chartHotData.map(function (item) {
        return [item[1], item[0], item[2] || "-"];
      });
    },
  },
  data() {
    return {
      value: [1000, 2000], //范围检索
      // xData: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], //横坐标
      xData: Array.from(
        { length: this.visData.length },
        (_, index) => index + 1
      ), //折线图横坐标
      // yData: [23, 24, 18, 25, 27, 28, 25], //折线图纵坐标
      //下面的data由后台传过来，一维数组

      //以下是热图的数据--------------------------------------------------------------------------------------------------------
      hours: [], //横坐标不显示字符
      // hours : Array.from({length: 7}, (_, index) => index + 1),//有参
      // days : [],//纵坐标不显示字符
      days: ["T", "G", "C", "A"], //纵坐标
      //下面的dataHot是二维数组，是值，后台直接传过来
      dataHot: [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 2],
        [0, 3, 3],
        [0, 4, 1],
        [0, 5, 2],
        [0, 6, 3],
        [1, 0, 7],
        [1, 1, 5],
        [1, 2, 7],
        [1, 3, 9],
        [1, 4, 7],
        [1, 5, 5],
        [1, 6, 7],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 3],
        [2, 4, 1],
        [2, 5, 0],
        [2, 6, 3],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 6],
        [3, 3, 8],
        [3, 4, 7],
        [3, 5, 3],
        [3, 6, 6],
      ].map(function (item) {
        return [item[1], item[0], item[2] || "-"];
      }),

      myChartStyle: { float: "left", width: "100%", height: "400px" }, //图表样式
    };
  },
  mounted() {
    //折线图初始化
    this.initEcharts();

    //热图初始化
    this.initEchartsHot();
    // this.initTem();
  },
  methods: {
    //折线图初始化
    initEcharts() {
      // 基本柱状图
      const option = {
        title: {
          text: this.chartName,
        },
        tooltip: {
          trigger: "axis",
        },
        grid: {
          left: "5%",
          right: "15%",
          bottom: "10%",
        },
        xAxis: {
          data: this.xData,
        },
        yAxis: {
          type: "value",
        },
        toolbox: {
          right: 50,
          feature: {
            dataZoom: {
              yAxisIndex: "none",
            },
            restore: {},
            saveAsImage: {},
          },
        },
        dataZoom: [
          {
            startValue: "0",
          },
          {
            type: "inside",
          },
        ],
        visualMap: {
          top: 50,
          right: 50,
          pieces: [
            {
              gt: 0,
              lte: 0.2,
              color: "#93CE07",
            },
            {
              gt: 0.2,
              lte: 0.4,
              color: "#FBDB0F",
            },
            {
              gt: 0.4,
              lte: 0.6,
              color: "#FC7D02",
            },
            {
              gt: 0.6,
              lte: 0.8,
              color: "#FD0100",
            },
            {
              gt: 0.8,
              lte: 1,
              color: "#AA069F",
            },
          ],
          precision: 2, //显示小数点后两位
          outOfRange: {
            color: "#999",
          },
        },
        series: [
          {
            // type: "bar", //形状为柱状图
            type: "line", //形状为折线图
            data: this.visData,
            smooth: true,
            color: ["#91cc75"],
          },
        ],
      };
      const myChart = echarts.init(document.getElementById(this.chartName));
      myChart.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        myChart.resize();
      });
    },
    //热图初始化
    initEchartsHot() {
      // this.chartHotData=await this.chartHotData.map(function (item) {
      //   return [item[1], item[0], item[2] || "-"];
      // })
      // 基本柱状图
      let data = this.chartHotData;
      const option = {
        title: {
          text: this.chartHotname,
        },
        xAxis: {
          type: "category",
          data: this.xData,
        },
        yAxis: {
          type: "category",
          data: this.days,
        },
        tooltip: {},
        visualMap: {
          type: "piecewise",
          min: 0,
          max: 0.5,
          left: "right",
          top: "center",
          calculable: true,
          realtime: false,
          splitNumber: 10,
          minOpen: true,
          maxOpen: true,
          inRange: {
            color: [
              "#313695",
              "#4575b4",
              "#74add1",
              "#abd9e9",
              "#e0f3f8",
              "#ffffbf",
              "#fee090",
              "#fdae61",
              "#f46d43",
              "#d73027",
              "#a50026",
            ],
          },
        },
        // visualMap: {
        //   min: 0,
        //   max: 0.5,
        //   calculable: true,
        //   realtime: false,
        //   inRange: {
        //     color: [
        //       "#313695",
        //       "#4575b4",
        //       "#74add1",
        //       "#abd9e9",
        //       "#e0f3f8",
        //       "#ffffbf",
        //       "#fee090",
        //       "#fdae61",
        //       "#f46d43",
        //       "#d73027",
        //       "#a50026",
        //     ],
        //   },
        // },
        series: [
          {
            name: "Gaussian",
            type: "heatmap",
            // data: this.chartHotData,
            data: data,
            emphasis: {
              itemStyle: {
                borderColor: "#333",
                borderWidth: 1,
              },
            },
            progressive: 1000,
            animation: false,
          },
        ],
        dataZoom: [
          {
            startValue: "0",
          },
          {
            type: "inside",
          },
        ],
        toolbox: {
          right: 50,
          feature: {
            saveAsImage: {},
          },
        },
      };
      const myChartHot = echarts.init(
        document.getElementById(this.chartHotname)
      );
      myChartHot.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        myChartHot.resize();
      });
    },
    // initTem() {
    //   // 模拟数据。改成自己数据时可以不管
    //   console.log(this.chartHotData)
    //   let data1 = this.chartHotData.map(function (item) {
    //     return [item[0], item[1]+4, item[2]];
    //   });
    //   let data2 = this.chartHotData.slice(0,12000).map(function (item) {
    //     return [item[0], item[1]+8, item[2]];
    //   });
    //   let data = this.chartHotData.concat(data1).concat(data2);

    //   const option = {
    //     title: {
    //       text: this.chartHotname,
    //     },
    //     xAxis: {
    //       type: "category",
    //       nameLocation: "middle",
    //       nameGap: 30,
    //       data: this.xData,
    //       splitArea: {
    //         show: false,
    //       },
    //       axisTick: {
    //         show: true,
    //       },
    //       axisLine: {
    //         show: true,
    //       },
    //     },
    //     yAxis: {
    //       type: "category",
    //       data: [
    //         "chr1",
    //         "chr2",
    //         "chr3",
    //         "chr4",
    //         "chr5",
    //         "chr6",
    //         "chr7",
    //         "chr8",
    //         "chr9",
    //         "chr10",
    //       ],
    //       axisLine: {
    //         show: true,
    //       },
    //       axisTick: {
    //         show: false,
    //       },
    //       splitArea: {
    //         show: false,
    //       },
    //       splitLine: {
    //         show: true,
    //         lineStyle: {
    //           color: "#ffff",
    //           width: 5,
    //         },
    //       },
    //     },
    //     tooltip: {
    //       trigger: "item",
    //       formatter: function (params) {
    //         let res =
    //           "Variation Density<br>" +
    //           params.data[0] +
    //           "Mb: " +
    //           params.data[2];
    //         return res;
    //       },
    //       // position: 'top'
    //     },
    //     visualMap: {
    //       min: 0, //1,//365,
    //       max: 0.5, //13313,//78178,
    //       calculable: true,
    //       // orient: 'horizontal',
    //       left: "right",
    //       text: ["High", "Low"],
    //       // bottom: '5%',
    //       inRange: {
    //         color: ["#0d6e11", "#feff08", "#d01c10"],
    //       },
    //     },
    //     series: [
    //       {
    //         type: "heatmap",
    //         // data: this.chartHotData,
    //         data: data,
    //         label: {
    //           normal: {
    //             show: false,
    //           },
    //         },
    //         emphasis: {
    //           shadowBlur: 10,
    //           shadowColor: "rgba(0, 0, 0, 0.5)",
    //         },
    //         zlevel: -1,
    //       },
    //     ],
    //     dataZoom: [
    //       {
    //         startValue: "0",
    //       },
    //       {
    //         type: "inside",
    //       },
    //     ],
    //     toolbox: {
    //       right: 50,
    //       feature: {
    //         saveAsImage: {},
    //       },
    //     },
    //   };
    //   const myChartHot = echarts.init(
    //     document.getElementById(this.chartName + "xx")
    //   );
    //   myChartHot.setOption(option);
    //   //随着屏幕大小调节图表
    //   window.addEventListener("resize", () => {
    //     myChartHot.resize();
    //   });
    // },
    // initTem() {
    //   let data = this.chartHotData.slice(0, 6000);
    //   console.log(data);
    //   const option = {
    //     title: {
    //       text: "Rainfall vs Evaporation",
    //       left: "center",
    //     },
    //     tooltip: {
    //       trigger: "item",
    //       axisPointer: {
    //         animation: false,
    //       },
    //     },
    //     axisPointer: {
    //       link: [
    //         {
    //           xAxisIndex: "all",
    //         },
    //       ],
    //     },
    //     dataZoom: [
    //       {
    //         show: true,
    //         realtime: true,
    //         start: 30,
    //         end: 70,
    //         xAxisIndex: [0, 1, 2],
    //       },
    //       {
    //         type: "inside",
    //         realtime: true,
    //         start: 30,
    //         end: 70,
    //         xAxisIndex: [0, 1, 2],
    //       },
    //       {
    //         type: "inside",
    //         realtime: true,
    //         start: 30,
    //         end: 70,
    //         xAxisIndex: [0, 1, 2],
    //       },
    //     ],
    //     grid: [
    //       {
    //         left: 60,
    //         right: 50,
    //         height: "5%",
    //       },
    //       {
    //         left: 60,
    //         right: 50,
    //         top: "45%",
    //         height: "5%",
    //       },
    //       {
    //         left: 60,
    //         right: 50,
    //         top: "75%",
    //         height: "5%",
    //       },
    //     ],
    //     xAxis: [
    //       {
    //         type: "category",
    //       },
    //       {
    //         gridIndex: 1,
    //         type: "category",
    //       },
    //       {
    //         gridIndex: 2,
    //         type: "category",
    //         data: this.xData,
    //       },
    //     ],
    //     yAxis: [
    //       {
    //         type: "category",
    //         data: ["T"],
    //       },
    //       {
    //         gridIndex: 1,
    //         type: "category",
    //         data: ["T"],
    //       },
    //       {
    //         gridIndex: 2,
    //         type: "category",
    //         data: ["T"],
    //       },
    //     ],
    //     series: [
    //       {
    //         type: "heatmap",
    //         name: "snp density",
    //         symbolSize: 8,
    //         data: data,
    //         emphasis: {
    //           itemStyle: {
    //             borderColor: "#333",
    //             borderWidth: 1,
    //           },
    //         },
    //         progressive: 1000,
    //         animation: false,
    //       },
    //       {
    //         type: "heatmap",
    //         name: "snp density",
    //         symbolSize: 8,
    //         data: data,
    //         emphasis: {
    //           itemStyle: {
    //             borderColor: "#333",
    //             borderWidth: 1,
    //           },
    //         },
    //         progressive: 1000,
    //         animation: false,
    //         xAxisIndex: 1,
    //         yAxisIndex: 1,
    //       },
    //       {
    //         type: "heatmap",
    //         name: "snp density",
    //         symbolSize: 8,
    //         data: data,
    //         emphasis: {
    //           itemStyle: {
    //             borderColor: "#333",
    //             borderWidth: 1,
    //           },
    //         },
    //         progressive: 1000,
    //         animation: false,
    //         xAxisIndex: 2,
    //         yAxisIndex: 2,
    //       },
    //     ],
    //     visualMap: {
    //       min: 0,
    //       max: 0.5,
    //       calculable: true,
    //       realtime: false,
    //       inRange: {
    //         color: [
    //           "#313695",
    //           "#4575b4",
    //           "#74add1",
    //           "#abd9e9",
    //           "#e0f3f8",
    //           "#ffffbf",
    //           "#fee090",
    //           "#fdae61",
    //           "#f46d43",
    //           "#d73027",
    //           "#a50026",
    //         ],
    //       },
    //     },
    //   };
    //   const myChartHot = echarts.init(
    //     document.getElementById(this.chartName + "xx")
    //   );
    //   myChartHot.setOption(option);
    //   //随着屏幕大小调节图表
    //   window.addEventListener("resize", () => {
    //     myChartHot.resize();
    //   });
    // },
  },
};
</script>
  