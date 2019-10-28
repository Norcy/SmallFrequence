<?php 
header('Content-Type:text/json;charset=utf-8');
require_once("SimpleRest.php");
 
class SiteRestHandler extends SimpleRest {
 
 	function getAllRegions($version) {    
        $json_string = file_get_contents('FM_List/regions.json');
    	echo $json_string;	
    }

    function getAllSites($version) {    
        $json_string = file_get_contents('FM_List/all.json');
    	echo $json_string;	
    }
    
    function getSite($id, $version) {
        $json_string = file_get_contents('FM_List/'.$id.'.json');
        echo $json_string;  
    }
}
?>
