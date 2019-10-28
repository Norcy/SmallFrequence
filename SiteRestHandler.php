<?php 
header('Content-Type:text/json;charset=utf-8');
require_once("SimpleRest.php");
 
class SiteRestHandler extends SimpleRest {
 
 	function getAllRegions() {    
        $json_string = file_get_contents('FM_List/regions.json');
        $json_string = "{\"version\":111, \"data\":".$json_string."}";
    	echo $json_string;	
    }

    function getAllSites() {    
        $json_string = file_get_contents('FM_List/all.json');
    	echo $json_string;	
    }
    
    function getSite($id) {
        $json_string = file_get_contents('FM_List/'.$id.'.json');
        echo $json_string;  
    }
}
?>
