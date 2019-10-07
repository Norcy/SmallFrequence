<?php
header('Content-Type:text/json;charset=utf-8');
// $isFM = $_GET['isFM'];
// $isFM = False;
// $qingting_fm_prefix="lhttp";
// $qingting_fm_postfix=".mp3";
$qingting_fm_prefix="ls";
$qingting_fm_postfix=".m3u8";
$isFM = True;
$str;
if ($isFM) 
{
    $str = array(
        array(
            'title'=>'澄海人民广播',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/5022439/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 100.5',
            'protocol'=>'hls'
        ),
        // array(
        //     'title'=>'汕头电台新闻资讯之声',
        //     'src'=>'https://sttv-hls.cutv.com/L3y6rt8/64/d6wLpy0.m3u8?sign=2417743d656035126e4b8d6ce1ec57bc&t=5d06067b',
        //     'subtitle'=>'FM 102.0',
        //     'protocol'=>'hls'
        // ),
        // array(
        //     'title'=>'汕头电台音乐广播',
        //     'src'=>'https://sttv-hls.cutv.com/s7k681h/64/y7bxpk0.m3u8?sign=ce4f829e349b538a2d6a834258fd516b&t=5d0608e5',
        //     'subtitle'=>'FM 102.5',
        //     'protocol'=>'hls'
        // ),
        // array(
        //     'title'=>'汕头电台交通之声',
        //     'src'=>'https://sttv-hls.cutv.com/Li7mg21/64/b7yLp70.m3u8?sign=bfe953d10971acf2cbdd5056abf11499&t=5d0608de',
        //     'subtitle'=>'FM 107.2',
        //     'protocol'=>'hls'
        // ),
        array(
            'title'=>'潮州交通音乐广播',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/4594/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 91.4',
            'protocol'=>'hls'
        ),
        array(
            'title'=>'潮州戏曲广播',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/4595/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 103.1',
            'protocol'=>'hls'
        ),
        array(
            'title'=>'潮州综合频率',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/4596/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 94.0',
            'protocol'=>'hls'
        ),
        array(
            'title'=>'普宁人民广播电台',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/5022527/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 102.8',
            'protocol'=>'hls'
        ),
        // array(
        //     'title'=>'茶香',
        //     'src'=>'https://music.163.com/song/media/outer/url?id=411347644',
        //     'subtitle'=>'郑志立/郑湫泓',
        //     'protocol'=>'http'
        // ),
        // array(
        //     'title'=>'灯笼谣',
        //     'src'=>'https://music.163.com/song/media/outer/url?id=33875641',
        //     'subtitle'=>'袁东方',
        //     'protocol'=>'http'
        // ),
        // array(
        //     'title'=>'手牵手行',
        //     'src'=>'https://music.163.com/song/media/outer/url?id=27552373',
        //     'subtitle'=>'张梦弘',
        //     'protocol'=>'http'
        // ),
        array(
            'title'=>'羊城交通台',
            'src'=>'http://rscdn.ajmide.com/r_1758/1758.m3u8',
            'subtitle'=>'FM 105.2',
            'protocol'=>'hls'
        ),
        array(
            'title'=>'深圳生活广播',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/1273/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 94.2',
            'protocol'=>'hls'
        ),
        array(
            'title'=>'深圳交通频率',
            'src'=>'http://'.$qingting_fm_prefix.'.qingting.fm/live/1272/64k'.$qingting_fm_postfix,
            'subtitle'=>'FM 106.2',
            'protocol'=>'hls'
        )
    );
}
else
{
    $str = array(
        array(
            'title'=>'雨落屋檐',
            'src'=>'https://private.psy-1.com/music/bgm038-TIMkgKMzLIF3xN2Mjsgk.mp3?e=1560502360&token=Wxe4Fvn8XfvDpkeUO0RVUj2Sz1E1KVi05wwZAr6x:t2bPVsl5brQLn87qB-l6hIpmh3g=',
            'subtitle'=>'自然旋律',
            'protocol'=>'http'
        ),
        array(
            'title'=>'春雨无声',
            'src'=>'https://private.psy-1.com/music/bgm036-jWcqCHXaslrKc3zAQPJ1.mp3?e=1560502360&token=Wxe4Fvn8XfvDpkeUO0RVUj2Sz1E1KVi05wwZAr6x:FtC8mjitOQY6GnvsN_kic_3abMI=',
            'subtitle'=>'自然旋律',
            'protocol'=>'http'
        ),
        array(
            'title'=>'夏雨倾盆',
            'src'=>'https://private.psy-1.com/music/bgm037-vTWzSK1dDGB6Tynrj4Am.mp3?e=1560502360&token=Wxe4Fvn8XfvDpkeUO0RVUj2Sz1E1KVi05wwZAr6x:XsShtaoq9vgWUCvgEO8nU4LrMBg=',
            'subtitle'=>'自然旋律',
            'protocol'=>'http'
        ),
        array(
            'title'=>'秋雨凄凄',
            'src'=>'https://private.psy-1.com/music/bgm308-VQqUbTzd8R7gKovMFjdE.mp3?e=1560502360&token=Wxe4Fvn8XfvDpkeUO0RVUj2Sz1E1KVi05wwZAr6x:hQcULbAkzkIWBGAgXCYD9NU-zdk=',
            'subtitle'=>'自然旋律',
            'protocol'=>'http'
        ),
        array(
            'title'=>'窗外松声',
            'src'=>'https://music.163.com/song/media/outer/url?id=473627122',
            'subtitle'=>'潮汕弦乐',
            'protocol'=>'http'
        ),
        array(
            'title'=>'雨落落',
            'src'=>'https://fdfs.xmcdn.com/group59/M09/DE/E4/wKgLelzeyqDiTd4zAASusm6_Rew750.m4a',
            'subtitle'=>'潮汕童谣',
            'protocol'=>'http'
        ),
        array(
            'title'=>'拥啊拥',
            'src'=>'https://fdfs.xmcdn.com/group58/M05/DD/54/wKgLc1zey1nQ18N2AAdjVVWXkUU317.m4a',
            'subtitle'=>'潮汕童谣',
            'protocol'=>'http'
        )
    );
}


$jsonencode = json_encode($str);
echo $jsonencode;
?>
