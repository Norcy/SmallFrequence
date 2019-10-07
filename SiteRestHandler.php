<?php 
header('Content-Type:text/json;charset=utf-8');
require_once("SimpleRest.php");
 
class SiteRestHandler extends SimpleRest {
 
    function getAllSites() {    
        $json_string = file_get_contents('FM_List/regions.json');
    	echo $json_string;	
    }
    
    public function getSite($id) {
    }
}
?>
