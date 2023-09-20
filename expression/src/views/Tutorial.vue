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
        <!-- <i class="el-icon-s-management" ref="top1">导航1</i>
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
        </p> -->

        <div class="Section0" style="layout-grid: 15.6pt">
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                >DeepCBA Documentation</span
              ></b
            ><b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                ><o:p></o:p></span
            ></b>
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Welcome! This is the documentation for DeepCBA, a deep learning web
              service based on </span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
                background: rgb(255, 255, 0);
                mso-highlight: rgb(255, 255, 0);
              "
              >Selene Python SDK and Django</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >. DeepCBA is freely accessible for all users. This website provides
              the function of high-precision prediction of gene expression based on
              chromatin interactions in four species: Maize, rice, cotton and
              wheat.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                ><o:p>&nbsp;</o:p></span
              ></b
            >
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 14pt;
                  mso-font-kerning: 1pt;
                "
                >Citation</span
              ></b
            ><b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                >&nbsp;:
              </span></b
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Wang ZY#, Peng Y#, Li J#, Xie A, Zhang JL, Li KQ, Shi JQ, Xing GJ,
              Shi WH, Liu JX* and Yan JB*(2023). Precise prediction of maize gene
              expression from chromatin interactions with DeepCBA.</span
            ><b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: ����;
                  mso-ascii-font-family: 'Times New Roman';
                  mso-hansi-font-family: 'Times New Roman';
                  mso-bidi-font-family: 'Times New Roman';
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                ><o:p></o:p></span
            ></b>
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 11pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: 'Times New Roman';
                  mso-fareast-font-family: ����;
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                >Overview</span
              ></b
            ><b
              ><span
                style="
                  mso-spacerun: 'yes';
                  font-family: ����;
                  mso-ascii-font-family: 'Times New Roman';
                  mso-hansi-font-family: 'Times New Roman';
                  mso-bidi-font-family: 'Times New Roman';
                  font-weight: bold;
                  font-size: 16pt;
                  mso-font-kerning: 1pt;
                "
                ><o:p></o:p></span
            ></b>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l5 level1 lfo1;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Home Page</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l2 level1 lfo2;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">Tools</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">S</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >pecies Select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">M</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >odel Select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Target Interaction Pair Sequence Input(online or upload from
              disk)</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Submit Task</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l0 level1 lfo4;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">S</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >earch</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">Q</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >uery Your Job</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Job Queue</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Detailed Results Display of Your Job</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l4 level1 lfo5;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">R</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >esults</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Species Select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Statistics</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l4 level1 lfo5;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">T</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >utorial</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 64pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l1 level1 lfo3;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#108;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Service Guide</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="20"
            style="
              margin-left: 22pt;
              text-indent: -22pt;
              mso-char-indent-count: 0;
              line-height: 21pt;
              mso-line-height-rule: exactly;
              mso-list: l3 level1 lfo6;
            "
          >
            <![if !supportLists]><span
              style="
                font-family: Wingdings;
                mso-fareast-font-family: ����;
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><span style="mso-list: Ignore">&#216;<span>&nbsp;</span></span></span
            ><![endif]><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">R</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >esources</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >1</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="����">��</font
              ><font face="Times New Roman">H</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >ome P</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">age</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              >The appearance of the home page is shown in the figure below.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" align="center" style="text-align: center">
            <img
              width="416"
              height="774"
              src="tutorial.files/tutorial889.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p
            class="MsoNormal"
            style="
              text-align: left;
              line-height: 21pt;
              mso-line-height-rule: exactly;
            "
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              >Here, you can select the species, go to Toos, result, statistics,
              tutorial.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p
            class="MsoNormal"
            style="
              text-align: left;
              line-height: 21pt;
              mso-line-height-rule: exactly;
            "
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              >You can click the home button to return to the home page.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">2</font><font face="����">��</font
              ><font face="Times New Roman">Tools</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >1)Species Select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In this interface, you can choose any of the four species of maize,
              rice, cotton, and wheat to predict the target task.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" align="center" style="text-align: center">
            <img
              width="554"
              height="210"
              src="tutorial.files/tutorial1172.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Then jump to the model select interface, where you will see the model
              name you need to chose(as shown in the follwing figure).</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >2)Model select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" align="center" style="text-align: center">
            <img
              width="554"
              height="262"
              src="tutorial.files/tutorial1317.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal" style="text-align: left">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >3) Target Interaction Pair Sequence Input(online or upload from
              disk)</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="145"
              src="tutorial.files/tutorial1393.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Here, you can use two modes: online upload and local upload to
              determine the sequence damage of the target task. We provide an
              example format and precautions for official data. You can obtain
              relevant information through [Note].</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >4)Submit Task</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="230"
              src="tutorial.files/tutorial1639.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >When submitting a task, you must provide a reliable email address to
              receive reminders of the running status of the job in the future. At
              the same time, to prevent robot operations, you need to input dynamic
              information.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >3</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="����">��</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Search </span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >1)Query Your Job</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="172"
              src="tutorial.files/tutorial1890.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >After submitting your task, you will receive a unique job ID. After
              receiving an email notifying you that the submitted task has completed
              running, you can query your task through the job ID in the Search
              interface and collect the results.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >2)Job Queue</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="236"
              src="tutorial.files/tutorial2145.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In this interface, you can view the running status of your task (with
              a check indicating successful operation and a cross indicating failed
              operation). Clicking on the View results button will display the
              predicted results and statistical information of DeepCBA in detail (as
              shown in the follwing figure).</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p
            class="MsoNormal"
            style="line-height: 21pt; mso-line-height-rule: exactly"
          >
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >3)</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              >&nbsp;Detailed Results Display of Your Job</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="701"
              src="tutorial.files/tutorial2497.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 12pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In this interface, you can check the results of the submitted tasks
              in detail, including prediction of expression levels, acquisition of
              model gradients, and capture of important sections(as shown in the
              follwing figure).</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="181"
              src="tutorial.files/tutorial2721.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In the prediction task of maize species, we have provided the true
              expression levels of genes under the V4 version in three tissues and
              five sets of published data for your convenience.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="224"
              src="tutorial.files/tutorial2909.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In this interface, you can visually observe important positions in
              the input sequence through gradient values. You can select the target
              range for gradient observation by sliding the button at the
              bottom.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="200"
              src="tutorial.files/tutorial3116.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >In this interface, you can visually observe which segments in the
              input sequence are more prominent through gradient values. You can
              select the target range by sliding the button at the bottom to observe
              the importance of the base, and also download and save the current
              results.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">4</font
              ><font face="����">��</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Result</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >1)Species Select</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="127"
              src="tutorial.files/tutorial3425.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >We have provided the predicted gene expression levels of DeepCBA in
              four species: corn, rice, cotton, and wheat. You can select and view
              them through species selection.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">(</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >2)Statistics</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >The gene expression levels predicted by DeepCBA were calculated for
              different species.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal" align="center" style="text-align: center">
            <img
              width="554"
              height="239"
              src="tutorial.files/tutorial3697.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">5</font
              ><font face="����">��</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >T</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="Times New Roman">u</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >torial</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >Here is an online guide for users to use DeepCBA.</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >6</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><font face="����">��</font
              ><font face="Times New Roman">Re</font></span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >sources</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              >At the bottom of each interface, we provide link addresses for
              commonly used resources, which you can access and download according
              to your actual needs(as shown in the follwing figure).</span
            ><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p></o:p
            ></span>
          </p>
          <p class="MsoNormal">
            <img
              width="554"
              height="481"
              src="tutorial.files/tutorial3961.png"
            /><span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: 'Times New Roman';
                mso-fareast-font-family: ����;
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
          <p class="MsoNormal">
            <span
              style="
                mso-spacerun: 'yes';
                font-family: ����;
                mso-ascii-font-family: 'Times New Roman';
                mso-hansi-font-family: 'Times New Roman';
                mso-bidi-font-family: 'Times New Roman';
                font-size: 14pt;
                mso-font-kerning: 1pt;
              "
              ><o:p>&nbsp;</o:p></span
            >
          </p>
        </div>
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

<style scoped>
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

<!-- <style scoped>
@font-face {
  font-family: "Times New Roman";
}

@font-face {
  font-family: "����";
}

@font-face {
  font-family: "����";
}

@font-face {
  font-family: "Wingdings";
}

@list l0:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F0D8;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 22pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 44pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 66pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 88pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 110pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 132pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 154pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 176pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l0:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 198pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 64pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 86pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 108pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 130pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 152pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 174pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 196pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 218pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l1:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 240pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F0D8;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 22pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 44pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 66pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 88pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 110pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 132pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 154pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 176pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l2:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 198pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F0D8;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 22pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 44pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 66pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 88pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 110pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 132pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 154pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 176pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l3:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 198pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F0D8;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 22pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 64pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 66pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 88pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 110pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 132pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 154pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 176pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l4:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 198pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level1 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F0D8;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 22pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level2 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 44pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level3 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 66pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level4 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 88pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level5 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 110pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level6 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 132pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level7 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06C;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 154pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level8 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F06E;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 176pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

@list l5:level9 {
  mso-level-number-format: bullet;
  mso-level-suffix: tab;
  mso-level-text: \F075;
  mso-level-tab-stop: none;
  mso-level-number-position: left;
  margin-left: 198pt;
  text-indent: -22pt;
  font-family: Wingdings;
}

p.MsoNormal {
  mso-style-name: ����;
  mso-style-parent: "";
  margin: 0pt;
  margin-bottom: 0.0001pt;
  mso-pagination: none;
  text-align: justify;
  text-justify: inter-ideograph;
  font-family: ����;
  mso-bidi-font-family: "Times New Roman";
  font-size: 10.5pt;
  mso-font-kerning: 1pt;
}

span.10 {
  font-family: ����;
}

span.15 {
  font-family: ����;
  color: rgb(96, 94, 92);
  background: rgb(225, 223, 221);
  mso-shading: rgb(225, 223, 221);
}

span.16 {
  font-family: ����;
  color: rgb(5, 99, 193);
  text-decoration: underline;
  text-underline: single;
}

span.17 {
  font-family: ����;
  font-size: 9pt;
}

span.18 {
  font-family: ����;
  font-size: 9pt;
}

p.MsoFooter {
  mso-style-name: ҳ��;
  mso-style-noshow: yes;
  margin: 0pt;
  margin-bottom: 0.0001pt;
  layout-grid-mode: char;
  mso-pagination: none;
  text-align: left;
  font-family: ����;
  mso-bidi-font-family: "Times New Roman";
  font-size: 9pt;
  mso-font-kerning: 1pt;
}

p.20 {
  mso-style-name: "List Paragraph";
  margin: 0pt;
  margin-bottom: 0.0001pt;
  text-indent: 21pt;
  mso-char-indent-count: 2;
  mso-pagination: none;
  text-align: justify;
  text-justify: inter-ideograph;
  font-family: ����;
  mso-bidi-font-family: "Times New Roman";
  font-size: 10.5pt;
  mso-font-kerning: 1pt;
}

p.MsoHeader {
  mso-style-name: ҳü;
  mso-style-noshow: yes;
  margin: 0pt;
  margin-bottom: 0.0001pt;
  layout-grid-mode: char;
  mso-pagination: none;
  text-align: center;
  font-family: ����;
  mso-bidi-font-family: "Times New Roman";
  font-size: 9pt;
  mso-font-kerning: 1pt;
}

span.msoIns {
  mso-style-type: export-only;
  mso-style-name: "";
  text-decoration: underline;
  text-underline: single;
  color: blue;
}

span.msoDel {
  mso-style-type: export-only;
  mso-style-name: "";
  text-decoration: line-through;
  color: red;
}

table.MsoNormalTable {
  mso-style-name: ��ͨ����;
  mso-style-parent: "";
  mso-style-noshow: yes;
  mso-tstyle-rowband-size: 0;
  mso-tstyle-colband-size: 0;
  mso-padding-alt: 0pt 5.4pt 0pt 5.4pt;
  mso-para-margin: 0pt;
  mso-para-margin-bottom: 0.0001pt;
  mso-pagination: widow-orphan;
  font-family: "Times New Roman";
  font-size: 10pt;
  mso-ansi-language: #0400;
  mso-fareast-language: #0400;
  mso-bidi-language: #0400;
}
@page {
  mso-page-border-surround-header: no;
  mso-page-border-surround-footer: no;
}
@page Section0 {
  margin-top: 72pt;
  margin-bottom: 72pt;
  margin-left: 90pt;
  margin-right: 90pt;
  size: 595.3pt 841.9pt;
  layout-grid: 15.6pt;
  mso-header-margin: 42.55pt;
  mso-footer-margin: 49.6pt;
}
div.Section0 {
  page: Section0;
}
</style>
 -->

