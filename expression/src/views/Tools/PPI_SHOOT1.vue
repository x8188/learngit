<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
-->
<template>
    <div class="tool">
        <div class="tool-up">
            <div class="top-text">
                <h1 style="font-size: 35px">Maize Expression prediction base on DNA</h1>
                <h3>Introductions how to use?</h3>
            </div>
            <div style="margin-top: 50px">
                <h3>
                    The family assignment rules (see details) and thresholds determined by
                    established methods (see details) are used to identify transcrption
                    factors from the input sequences. When you input nucleic acid
                    sequences, ESTScan 3.0 is employed to identify CDS regions of input
                    nucleic acid sequences and translate them to protein sequences. By
                    checking "Best hit in Arabidopsis thaliana", you will get the links
                    for predicted transcription factors to the best hits in Arabidopsis
                    thaliana in the result.
                </h3>
                <div style="width: 100%">
                    <h2>Paste one sequence(3001bp) here 👇</h2>
                    <a-input-group compact>
                        <a-input prefix=">" style="width: 50%" v-model="Seq1" />
                        <a-input prefix=">" style="width: 50%" v-model="Seq2" />
                    </a-input-group>

                    <a-row style="text-align: center">
                        <a-col :span="6">
                            <h2 style="margin-top: 6px; font-weight: bold">
                                Or load it from disk:
                            </h2>
                        </a-col>
                        <a-col :span="2" style="margin-top: 10px">
                            <a-upload :file-list="fileList" :before-upload="handleChange" @change="changestatue">
                                <a-button>
                                    <a-icon type="upload" />Click to Upload
                                </a-button>
                            </a-upload>
                        </a-col>
                        <a-col :span="5" style="margin-top: 5px">
                            <h1 style="float: left; margin-left: 40%">E-mail:</h1>
                        </a-col>
                        <a-col :span="6" style="margin-top: 10px">
                            <a-input style="margin-left: -50px" v-model="email" />
                        </a-col>
                        <a-col :span="4" style="margin-top: 5px">
                            <a-button style="margin-top: 6px" type="primary" block @click="submitseqs">
                                {{ uploading ? "Uploading" : "Start Upload" }}
                            </a-button>
                        </a-col>
                    </a-row>
                </div>
            </div>
        </div>
        <div style="width: 80%; margin-left: 10%">
            <h1 style="font-weight: bold">Output:</h1>

            <div class="contain" style="text-align: center; font-size: 30px">
                <a-table :columns="columns" :data-source="data" bordered>
                    <template slot="name" slot-scope="text">
                        <a>{{ text }}</a>
                    </template>
                </a-table>
            </div>
            <a-button style="margin-top: 6px; width: 20%" type="primary" @click="submitseqs">
                Dowload Results
            </a-button>
            <hr />
        </div>
        <!-- <div style="width: 80%; margin-left: 10%">
            <h3>
                We use Saliency to show contribution scores. The family assignment rules
                (see details) and thresholds determined by established methods (see
                details) are used to identify transcrption factors from the input
                sequences. When you input nucleic acid sequences
            </h3>
        </div>
        <div id="imgId" @click="openimg" class="showimg">
            <img style="width: 100%; height: 280px" src="../../img/CHG_TN.png" />
            <img style="width: 100%; height: 110px" src="../../img/seqs.png" />
        </div> -->
    </div>
</template>
  
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: "Expression",
    components: {},
    data() {
        return {
            list1: [],
            InputSeqs: "",
            loading: true,
            isShowImg: false,
            fileList: [],
            email: "",
            Seq1: "",
            Seq2: "",
            uploading: false,
            PPImodellist: [
                "SHOOT1",
                "EAR1",
                "SHOOT2",
                "EAR2",
                "TASSEL",
            ],
            PDImodellist: [
                "SHOOT1",
                "EAR",
                "SHOOT2",

            ],
            options: [{ value: "1" }, { value: "2" }],
            columns: [
                {
                    title: "Chromosome",
                    dataIndex: "chromosome",
                },
                {
                    title: "Expression",
                    dataIndex: "expression",
                },
            ],
            data: [
                {
                    key: "1",
                    chromosome: "John Brown",
                    expression: "300,000.00",
                },
                {
                    key: "2",
                    chromosome: "John Brown",
                    expression: "￥00,000.00",
                },
            ],
        };
    },
    methods: {
        handleChange(file) {
            return false;
        },
        confirmtype() {
            this.loading = !this.loading;
            console.log(this.methltype);
        },
        submitseqs() {
            let dataForm = new FormData();
            dataForm.append("file", this.fileList[0]);
            dataForm.append("seq", strArr);
            dataForm.append("email", this.email);
            dataForm.append("modelName", "NCNR_CG_DP");

            let seqdata = {
                email: "344501734@qq.com",
                modelName: "NCNR_CG",
                seq: strArr,
            };

            console.log(seqdata);
            uploadseq(seqdata).then((res) => {
                console.log(res);
            });
        },

        changestatue(info) {
            let fileList = [...info.fileList];

            // 1. Limit the number of uploaded files
            //    Only to show two recent uploaded files, and old ones will be replaced by the new
            fileList = fileList.slice(-1);
            this.fileList = fileList;
            console.log(this.fileList);
        },
        handleChange(value) {
            console.log(`selected ${value}`);
        },
        PPIchangeTools(value) {
            this.$router.push(`/Tools/PPI_${value}`);
            console.log(value);
        },
        PDIchangeTools(value) {
            this.$router.push(`/Tools/PDI_${value}`);
            console.log(value);
        },
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
    /* height: 1500px; */
    margin-bottom: 250px;
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

th.column-money,
td.column-money {
    text-align: right !important;
}
</style>