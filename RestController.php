<?php
require_once("SiteRestHandler.php");
        
$fm = "";
$region = "";
if(isset($_GET["fm"]))
    $fm = $_GET["fm"];
elseif (isset($_GET["region"])) {
    $region = $_GET["region"];
}

/*
 * RESTful service 控制器
 * URL 映射
*/
switch($fm){
 
    case "all":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getAllSites();
        break;
        
    case "single":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getSite($_GET["id"]);
        break;
 
    case "" :
        //404 - not found;
        break;
}

switch($region){
 
    case "all":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getAllRegions();
        break;
        
    case "" :
        //404 - not found;
        break;
}
?>
