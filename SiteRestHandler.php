<?php 
require_once("SimpleRest.php");
 
class SiteRestHandler extends SimpleRest {
 
    function getAllSites() {    
        $json_string = file_get_contents('FM_List/regions.json');
        $data = json_decode($json_string, true);
        var_dump($data);
    }
    
    public function encodeJson($responseData) {
        $jsonResponse = json_encode($responseData);
        return $jsonResponse;        
    }
    
    public function getSite($id) {
    }
}
?>
