<?php
require_once("SiteRestHandler.php");
        
$fm = "";
$region = "";
if (isset($_GET["fm"])) {
    $fm = $_GET["fm"];
}
elseif (isset($_GET["region"])) {
    $region = $_GET["region"];
}

$version = $_GET["version"];

$postData = json_decode(file_get_contents('php://input'), true);

//var_dump($postData);

$userData = $postData["userData"];

if ($userData['openId'] == "oKa7r4rL4mIpYja76NSt71rjPCTw") {
    echo "Hit!!!!";
    return;
}

/*
 * RESTful service 控制器
 * URL 映射
*/
switch($fm){
 
    case "all":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getAllSites($version);
        break;
        
    case "single":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getSite($_GET["id"], $version);
        break;
 
    case "" :
        //404 - not found;
        break;
}

switch($region){
 
    case "all":
        $siteRestHandler = new SiteRestHandler();
        $siteRestHandler->getAllRegions($version);
        break;
        
    case "" :
        //404 - not found;
        break;
}
?>
