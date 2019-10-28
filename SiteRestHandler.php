<?php 
header('Content-Type:text/json;charset=utf-8');
require_once("SimpleRest.php");
 
class SiteRestHandler extends SimpleRest {
 
 	function getAllRegions($version) {    
        $json_string = file_get_contents('FM_List/regions.json');
        // 用参数true把JSON字符串强制转成PHP数组  
        $data = json_decode($json_string, true);
        #echo $version;
        #echo $data["version"];
        if ($version < $data["version"]) {
            return;
        }
    	echo $json_string;	
    }

    function getAllSites($version) {    
        $json_string = file_get_contents('FM_List/all.json');
    	$data = json_decode($json_string, true);
	if ($version < $data["version"]) {
            return;
        }
	echo $json_string;	
    }
    
    function getSite($id, $version) {
        $json_string = file_get_contents('FM_List/'.$id.'.json');
        $data = json_decode($json_string, true);
        if ($version < $data["version"]) {
            return;
        }
	echo $json_string;  
    }
}
?>
