<template>
  <div class="table">
    <el-table
      :data="tdata"
      style="width: 100%"
      height="400"
      class="customer-table"
    >
      <el-table-column
        v-for="(item, index) in Object.keys(tdata[0] ?? {})"
        :key="index"
        :label="item"
        align="center"
        :width="bigwidth ? '150px' : undefined"
      >
        <template slot-scope="scope">
          <span>{{ scope.row[item] }}</span>
        </template>
      </el-table-column>
    </el-table>
    <!-- <el-table v-show="tableId != 0" :data="tdata" stripe style="width: 100%">
      <el-table-column
        v-for="(item, index) in Object.keys(tdata[0] ?? {})"
        :key="index"
        :label="item"
        align="center"
        width="110"
      >
        <template slot-scope="scope">
          <span>{{ scope.row[item] }}</span>
        </template>
      </el-table-column>
    </el-table> -->
  </div>
</template>

<script>
export default {
  name: "Table",
  props: ["tableId", "tdata"],
  data() {
    return {};
  },
  computed: {
    // header(){
    //   if(this.tableId==1){
    //     return Object.keys(this.tdata[0]);
    //   }
    // }
    bigwidth(){
      if(this.tdata[0].hasOwnProperty('Gene_1')){
        return true
      }else{
        return false
      }
    }
  },
  methods: {},
};
</script>

<style scoped>
/* 去掉表格单元格边框 */
::v-deep.customer-table th {
  border: none;
}
::v-deep.customer-table td,
.customer-table th.is-leaf {
  border: none;
}
/* 表格最外边框 */
::v-deep.el-table--border,
.el-table--group {
  border: none;
}
/* 头部边框 */
/* ::v-deep.customer-table thead tr th.is-leaf{
  border: 1px solid #EBEEF5;
  border-right: none;
} */
::v-deep.customer-table thead tr th:nth-last-of-type(2) {
  border-right: 1px solid #ebeef5;
}
/* 表格最外层边框-底部边框 */
::v-deep.el-table--border::after,
.el-table--group::after {
  width: 0;
}
::v-deep.customer-table::before {
  width: 0;
}
::v-deep.customer-table .el-table__fixed-right::before,
.el-table__fixed::before {
  width: 0;
}
/* 表格有滚动时表格头边框 */
::v-deep.el-table--border th.gutter:last-of-type {
  border: 1px solid #ebeef5;
  border-left: none;
}

/* .table {

width: 100%;

display: flex;

flex-direction: column;
}
.table .el-table__body-wrapper {

flex: 1;

} */
</style>
