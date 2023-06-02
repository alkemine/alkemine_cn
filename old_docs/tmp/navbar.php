<?php
function navbar(){
    echo "
        <header class=\"navbar navbar-inverse navbar-fixed-top \" role=\"banner\">
        <div class=\"container\">
            <div class=\"navbar-header\">
                <button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\".navbar-collapse\">
                    <span class=\"sr-only\">Toggle navigation</span>
                    <i class=\"fa fa-bars\"></i>
                </button>
<!--                 <a class=\"navbar-brand\" href=\"index.html\"><h1><span class=\"pe-7s-science bounce-in\"></span>ALKEMIE</h1></a>-->
<!--                <a class=\"navbar-brand\" href=\"index.html\"><h1><object data=\"images/logo.svg\" type=\"image/svg+xml\"></object>ALKEMIE</h1></a>-->
                <a class=\"navbar-brand\" href=\"index.html\"> <h1> <img width=\"35px\" src=\"images/logo.svg\" style=\"margin-bottom: 5px\"></img>ALKEMIE </h1></a>

            </div>
            <div class=\"collapse navbar-collapse\">
                <ul class=\"nav navbar-nav navbar-right\">
                    <li><a href=\"index.html\">Home</a></li>
                    <li><a href=\"https://alkemine.cn\" target=\"_blank\">About Us</a></li>
<!--                    <li><a href=\"services.html\">Services</a></li>-->
<!--                    <li><a href=\"portfolio.html\">Portfolio</a></li>-->
<!--                    <li><a href=\"blog.html\">Blog</a></li>-->
<!--                    <li><a href=\"contact-us.html\">Contact</a></li>-->
                    <li class=\"dropdown active\">
                        <a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\">目录 <i class=\"icon-angle-down\"></i></a>
                        <ul class=\"dropdown-menu\">
                            <li><a href=\"#alkemie-workflow-preview\">平台概览</a></li>
                            <li><a href=\"#AMDIV\">设计理念</a></li>
                            <li><a href=\"#IntergratedSoftwares\">Skills</a></li>
                            <li><a href=\"#PlatformInfo\">基本信息</a></li>
                            <li><a href=\"#Functions\">功能特色</a></li>
                            <li><a href=\"#DBInfo\">数据库</a></li>
                            <li><a href=\"#Papers\">发表论文</a></li>
                            <li><a href=\"#TeamMembers\">团队成员</a></li>
                            <li><a href=\"#WorkFlowList\">工作流算例</a></li>
                            <li class=\"active\"><a href=\"https://alkemine.org\" target=\"_blank\">ALKEMIE使用手册</a></li>
                            <li><a href=\"https://alkemine.cn\" target=\"_blank\">课题组官网</a></li>
                        </ul>
                    </li>
<!--                    <li><span class=\"search-trigger\"><i class=\"fa fa-search\"></i></span></li>-->
                </ul>
            </div>
        </div>
    </header><!--/header-->



    ";
}