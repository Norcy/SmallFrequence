<?php 
require_once("SimpleRest.php");
require_once("Site.php");
 
class SiteRestHandler extends SimpleRest {
 
    function getAllSites() {    
 
        $site = new Site();
        $rawData = $site->getAllSite();
 
        if(empty($rawData)) {
            $statusCode = 404;
            $rawData = array('error' => 'No sites found!');        
        } else {
            $statusCode = 200;
        }
 
        $requestContentType = $_SERVER['HTTP_ACCEPT'];
               
        if(strpos($requestContentType,'text/html') !== false){
            $this ->setHttpHeaders('text/html', $statusCode);
            $response = $this->encodeHtml($rawData);
            echo $response;
        } else if(strpos($requestContentType,'application/xml') !== false){
            $this ->setHttpHeaders('application/xml', $statusCode);
            $response = $this->encodeXml($rawData);
            echo $response;
        } else {
            // 默认输出 JSON
            $this ->setHttpHeaders('application/json', $statusCode);
            $response = $this->encodeJson($rawData);
            echo $response;
        }
    }
    
    public function encodeHtml($responseData) {
    
        $htmlResponse = "<table border='1'>";
        foreach($responseData as $key=>$value) {
                $htmlResponse .= "<tr><td>". $key. "</td><td>". $value. "</td></tr>";
        }
        $htmlResponse .= "</table>";
        return $htmlResponse;        
    }
    
    public function encodeJson($responseData) {
        $jsonResponse = json_encode($responseData);
        return $jsonResponse;        
    }
    
    public function encodeXml($responseData) {
        // 创建 SimpleXMLElement 对象
         $xml = new SimpleXMLElement('<?xml version="1.0"?><site></site>');
        foreach($responseData as $key=>$value) {
            $xml->addChild($key, $value);
        }
        return $xml->asXML();
    }
    
    public function getSite($id) {
 
        $site = new Site();
        $rawData = $site->getSite($id);
 
        if(empty($rawData)) {
            $statusCode = 404;
            $rawData = array('error' => 'No sites found!');        
        } else {
            $statusCode = 200;
        }
 
        $requestContentType = $_SERVER['HTTP_ACCEPT'];
                
        if(strpos($requestContentType,'text/html') !== false){
            $this ->setHttpHeaders('text/html', $statusCode);
            $response = $this->encodeHtml($rawData);
            echo $response;
        } else if(strpos($requestContentType,'application/xml') !== false){
            $this ->setHttpHeaders('application/html', $statusCode);
            $response = $this->encodeXml($rawData);
            echo $response;
        } else {
            $this ->setHttpHeaders('application/json', $statusCode);
            $response = $this->encodeJson($rawData);
            echo $response;
        }
    }
}
?>
