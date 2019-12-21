<?php
header('Content-Type:text/json;charset=utf-8');
require_once ("SimpleRest.php");

class MusicRestHandler extends SimpleRest {
    private $dic = "Music_List";
    function getAllRegions($version) {
        $json_string = file_get_contents($this->dic . "/regions.json");
        // 用参数true把JSON字符串强制转成PHP数组
        $data = json_decode($json_string, true);
        #echo $version;
        #echo $data["version"];
        if ($version == null || $version >= $data["version"]) {
            return;
        }
        echo $json_string;
    }
    function getAllSites($version) {
        $json_string = file_get_contents($this->dic . "/all.json");
        $data = json_decode($json_string, true);
        if ($version == null || $version >= $data["version"]) {
            return;
        }
        echo $json_string;
    }
    function getSite($id, $version) {
        $json_string = file_get_contents($this->dic . $id . '.json');
        $data = json_decode($json_string, true);
        if ($version == null || $version >= $data["version"]) {
            return;
        }
        echo $json_string;
    }
}
?>
