<template>
  <div>
    <el-table v-if="tableId==0" :data="tdata" stripe style="width: 100%" height="400">
      <el-table-column prop="Annotation1" label="Annotation1">
      </el-table-column>
      <el-table-column prop="Annotation2" label="Annotation2">
      </el-table-column>
      <el-table-column prop="exp" label="exp"> </el-table-column>
      <el-table-column prop="pre" label="pre"> </el-table-column>
    </el-table>
    <el-table v-else :data="tdata" stripe style="width: 100%">
            <el-table-column
              v-for="(item, index) in Object.keys(tdata[0]??{})"
              :key="index"
              :label="item"
              align="center"
              width="110"
            >
              <template slot-scope="scope">
                <span>{{ scope.row[item] }}</span>
              </template>
            </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {

  name: "Table",
  props: ["tableId","tdata"],
  data(){
    return{
    }
  },
  computed:{
    // header(){
    //   if(this.tableId==1){
    //     return Object.keys(this.tdata[0]);
    //   }
    // }
  },
  methods:{
  }
};
</script>

<style></style>
