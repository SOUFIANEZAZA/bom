#Impoting Modules
from instabot import Bot
import time
import sys
import random
from tqdm import tqdm
import os
from FunctionData.USER_DATABase import *

#Importing Mi Functions
from FunctionData.somefun import *
from MokupData.mokupfun import *
from BotData.ConfiG import *
#Men@c
bot = Bot(
    max_likes_per_day=400,
    max_follows_per_day=240,
    max_unfollows_per_day=240,
    max_messages_per_day=100,
    max_comments_per_day=100,
    min_likes_to_like=10,
    max_likes_to_like=10000000,
    like_delay=30,
    follow_delay=25,
    unfollow_delay=25,
    message_delay=2
    )
#hashtag list to tag in a media
hashtagList = [
            '#casablanca'
]

#Program For Unfollow Everyone
def ig_teamhunter():
    KMFHEADER()
    TEAMHUNTER()
    userdata = input("\u001b[32m[+]\u001b[0m Enter Target Team username:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            bot.follow(userdata)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(240)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            bot.unfollow(userdata)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(30)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

    
    <?php
require('lib/config.php');
$cookieData		= explode('|', file_get_contents('./data/'.$cookieFile));
$cookie 		= $cookieData[0]; // Cookie Instagram
$useragent 		= $cookieData[1]; // Useragent Instagram
$loop			= true;
//feed/user/{$userId}/story/
echo "
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        🅼🅰🆂🆂 🅻🅾🅾🅺🅴🆁 
	$---------$--------$
	1.Mass story views without Action block
	2.Reacts to stories
	3.Auto Poll reactions
	4.Auto Question Ansewring
	$---------$--------$
	
	\n";
echo "[o] $$$$$$$$$$ Auto  Story Viewer by @SOUFSAN $$$$$$$$$$$$$$$$$$ [o]\n";
echo "  $----$----$ Author nthanfp Modified by 🤑 @mohsanjid SOUFAN 🤑 $----$---$   \n\n";
echo " Subscribe my Youtube channel $ PhotoLooz $ for more videos --😍
 \n\n";

if($cookie){
	$getakun	= proccess(1, $useragent, 'accounts/current_user/', $cookie);
	$getakun	= json_decode($getakun[1], true);
	if($getakun['status'] == 'ok'){
		//LOSS
		$getakunV2	= proccess(1, $useragent, 'users/'.$getakun['user']['pk'].'/info', $cookie);
		$getakunV2	= json_decode($getakunV2[1], true);
		echo "[~] Login as @".$getakun['user']['username']." \n";
		echo "[~] [Media : ".$getakunV2['user']['media_count']."] [Follower : ".$getakunV2['user']['follower_count']."] [Following : ".$getakunV2['user']['following_count']."]\n";
		echo "[~] Please wait 5 second for loading script\n";
		echo "[~] "; for($x = 0; $x <= 4; $x++){ echo "========"; sleep(1); } echo "\n\n";
		do {
			$targets	= file_get_contents('./data/'.$targetFile);
			$targets 	= explode("\n", str_replace("\r", "", $targets));
			$targets 	= array($targets)[0];
			foreach($targets as $target){
				$komens		= file_get_contents('./data/'.$answerFile);
				$komen		= explode("\n", str_replace("\r", "", $komens));
				$komen		= array($komen)[0];
				//
				$todays		= file_get_contents('./data/daily/'.date('d-m-Y').'.txt');
				$today		= explode("\n", str_replace("\r", "", $todays));
				$today		= array($today)[0];
				//
				//$proxy		= file_get_contents('https://veonpanel.com/api/panel/proxy?key=MEMEF');
				//$proxy		= json_decode($proxy, true);
				//$prox['ip']			= $proxy['data']['proxy'];
				$prox['ip']			= 0;
				$prox['user']		= 0;
				$prox['is_socks5']	= 0;
				//
				echo "[~] Get followers of ".$target."\n";
				//echo "[~] Proxy ".$prox['ip']."\n";
				$targetid	= json_decode(request(1, $useragent, 'users/'.$target.'/usernameinfo/', $cookie, 0, array(), $prox['ip'], $prox['user'], $prox['is_socks5'])[1], 1)['user']['pk'];
				$gettarget	= proccess(1, $useragent, 'users/'.$targetid.'/info', $cookie, 0, array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
				$gettarget	= json_decode($gettarget[1], true);
				echo "[~] [Media : ".$gettarget['user']['media_count']."] [Follower : ".$gettarget['user']['follower_count']."] [Following : ".$gettarget['user']['following_count']."]\n";
				$jumlah		= $countTarget;
				if(!is_numeric($jumlah)){
					$limit = 1;
				} elseif ($jumlah > ($gettarget['user']['follower_count'] - 1)){
					$limit = $gettarget['user']['follower_count'] - 1;
				} else {
					$limit = $jumlah - 1;
				}
				$next      	= false;
				$next_id    = 0;
				$listids	= array();
				do {
					if($next == true){ $parameters = '?max_id='.$next_id.''; } else { $parameters = ''; }
					$req        = proccess(1, $useragent, 'friendships/'.$targetid.'/followers/'.$parameters, $cookie, 0, array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
					$req        = json_decode($req[1], true);
					if($req['status'] !== 'ok'){
						var_dump($req);
						exit();
					}
					for($i = 0; $i < count($req['users']); $i++):
						if($req['users'][$i]['is_private'] == false):
							if($req['users'][$i]['latest_reel_media']):
								if(count($listids) <= $limit):
									$listids[count($listids)] = $req['users'][$i]['pk'];
								endif;
							endif;
						endif;
					endfor;
					if($req['next_max_id']){ $next = true; $next_id	= $req['next_max_id']; } else { $next = false; $next_id = '0'; }
				} while(count($listids) <= $limit);
				echo "[~] ".count($listids)." followers of ".$target." collected\n";
				$reels		= array();
				$reels_suc	= array();
				for($i = 0; $i < count($listids); $i++):
					$getstory   = proccess(1, $useragent, 'feed/user/'.$listids[$i].'/story/', $cookie, 0, array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
					$getstory   = json_decode($getstory[1], true);
					foreach($getstory['reel']['items'] as $storyitem):
						$reels[count($reels)]	= $storyitem['id']."_".$getstory['reel']['user']['pk'];
						$stories['id']			= $storyitem['id'];
						$stories['reels']		= $storyitem['id']."_".$getstory['reel']['user']['pk'];
						$stories['reel']		= $storyitem['taken_at'].'_'.time();
						if(strpos(file_get_contents('./data/storyData.txt'), $stories['reels']) == false){
							$hook       = '{"live_vods_skipped": {}, "nuxes_skipped": {}, "nuxes": {}, "reels": {"'.$stories['reels'].'": ["'.$stories['reel'].'"]}, "live_vods": {}, "reel_media_skipped": {}}';
							$viewstory  = proccess_v2(1, $useragent, 'media/seen/?reel=1&live_vod=0', $cookie, hook(''.$hook.''), array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
							$viewstory  = json_decode($viewstory[1], true);
							if($storyitem['story_polls']){
								$stories['pool_id']	= $storyitem['story_polls'][0]['poll_sticker']['poll_id'];
								$react_1	  		= proccess(1, $useragent, 'media/'.$stories['id'].'/'.$stories['pool_id'].'/story_poll_vote/', $cookie, hook('{"radio_type": "none", "vote": "'.rand(0,1).'"}'), array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
								$react_1			= json_decode($react_1[1], true);
								if($react_1['status'] == 'ok'){
									echo "[~] ".date('d-m-Y H:i:s')." - Success polling for ".$stories['id']."\n";
								}
								//echo "[Stories Polls True : ".$stories['pool_id']." : ".$react_1[1]."] ";
							}
							if($storyitem['story_questions']){
								$stories['question_id']	= $storyitem['story_questions'][0]['question_sticker']['question_id'];
								$rand					= rand(0, count($komen)-1);
						        $textAnswer 			= $komen[$rand];
								$react_2	  			= proccess(1, $useragent, 'media/'.$stories['id'].'/'.$stories['question_id'].'/story_question_response/', $cookie, hook('{"response": "'.$textAnswer.'", "type": "text"}'), array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
								$react_2				= json_decode($react_2[1], true);
								if($react_2['status'] == 'ok'){
									echo "[~] ".date('d-m-Y H:i:s')." - Question answer for ".$stories['id']." : ".$textAnswer." \n";
								}
								//echo "[Stories Question True : ".$stories['question_id']." : ".$react_2[1]."] ";
							}
							if($storyitem['story_countdowns']){
								$stories['countdown_id']	= $storyitem['story_countdowns'][0]['countdown_sticker']['countdown_id'];
								$react_3	  				= proccess(1, $useragent, 'media/'.$stories['countdown_id'].'/follow_story_countdown/', $cookie, 0, array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
								$react_3					= json_decode($react_3[1], true);
								//echo "[Stories Countdown True : ".$stories['countdown_id']." : ".$react_3[1]."] ";
							}
							if($storyitem['story_sliders']){
								$stories['slider_id']	= $storyitem['story_sliders'][0]['slider_sticker']['slider_id'];
								$react_4	  			= proccess(1, $useragent, 'media/'.$stories['id'].'/'.$stories['slider_id'].'/story_slider_vote/', $cookie, hook('{"radio_type": "wifi-none", "vote": "1"}'), array(), $prox['ip'], $prox['user'], $prox['is_socks5']);
								$react_4				= json_decode($react_4[1], true);
								if($react_2['status'] == 'ok'){
									echo "[~] ".date('d-m-Y H:i:s')." - Success sent slider for ".$stories['id']."\n";
								}
								//echo "[Stories Slider True : ".$stories['slider_id']." : ".$react_4[1]."] ";
							}
							if($storyitem['story_quizs']){
								$stories['quiz_id']	= $storyitem['story_quizs'][0]['quiz_sticker']['quiz_id'];
								//$react_5	  		= proccess(1, $useragent, 'media/'.$stories['id'].'/'.$stories['quiz_id'].'/story_poll_vote/', $cookie, hook('{"radio_type": "none", "vote": "'.rand(0,3).'"}'));
								//echo "[Stories Quiz True : ".$stories['quiz_id']." : ".$react_5[1]."] ";
							}
							if($viewstory['status'] == 'ok'){
								$reels_suc[count($reels_suc)] = $storyitem['id']."_".$getstory['reel']['user']['pk'];
								echo "[~] ".date('d-m-Y H:i:s')." - Seen stories ".$stories['id']." \n";
								saveData('./data/storyData.txt', $stories['reels']);
								saveData('./data/daily/'.date('d-m-Y').'.txt', $stories['reels']);
							}
							sleep($sleep_1);
						}
					endforeach;
					echo "[~] ".date('d-m-Y H:i:s')." - Sleep for ".$sleep_2." second to bypass instagram limit\n"; sleep($sleep_2);
				endfor;
				echo "[~] ".count($reels)." story from ".$target." collected\n";
				echo "[~] ".count($reels_suc)." story from ".$target." marked as seen\n";
				echo "[~] ".count($today)." story reacted today\n";
				echo "[~] ".date('d-m-Y H:i:s')." - Sleep for 30 second to bypass instagram limit\n";
				echo "[~] "; for($x = 0; $x <= 4; $x++){ echo "========"; sleep(6); } echo "\n\n";
			}
			if(count($today) > '1900'){
				echo "[~] ".count($today)." story reacted today\n";
				echo "[~] Limit instagram api 2000 seen/day\n";
				echo "[~] Sleep for 20 hours to bypass instagram limit\n";
				sleep(72000);
				echo "[~] End sleep...\n\n";
			}
		} while($loop == true);
	} else {
		echo "[!] Error : ".json_encode($getakun)."\n";
	}
} else {
	echo "[!] Please login\n";
}
?>
    
#Program For Unfollow Everyone
def ig_masslooker():
    KMFHEADER()
    MASSLOOKER()
    while True:
        try:
            bot.reset_cache()
            user_to_get_likers_of = bot.get_user_id_from_username(username=random.choice(USERID_FOR_MASSLOOKER))
            current_user_id = user_to_get_likers_of
            try:
                bot.reset_cache()
                # GET USER FEED
                if not bot.api.get_user_feed(current_user_id):
                    print("Can't get feed of user_id=%s" % current_user_id)

                # GET MEDIA LIKERS
                user_media = random.choice(bot.api.last_json["items"])
                if not bot.api.get_media_likers(media_id=user_media["pk"]):
                    bot.logger.info(
                        "Can't get media likers of media_id='%s' by user_id='%s'"
                        % (user_media["id"], current_user_id)
                    )

                likers = bot.api.last_json["users"]
                liker_ids = [
                                str(u["pk"])
                                for u in likers
                                if not u["is_private"] and "latest_reel_media" in u
                            ][:30]

                # WATCH USERS STORIES
                if bot.watch_users_reels(liker_ids):
                    bot.logger.info("Total stories viewed: %d" % bot.total["stories_viewed"])

                # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
                countdown(5)
            except Exception as e:
                # If something went wrong - sleep long and start again
                bot.logger.info(e)
                current_user_id = user_to_get_likers_of
                time.sleep(5 * random.random() + 5)

        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Program For ReHashtag
def ig_rehashtag():
    KMFHEADER()
    REHASHTAG()
    postlink = input("\u001b[32m[+]\u001b[0m Enter Media link:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            media_link = postlink
            media_id = bot.get_media_id_from_link(media_link)
            comments = bot.get_media_comments(media_id)
            commented_users = []
            bot.logger.info("Commenting Hashtags to Your Photo")
            bot.comment(media_id, comment_text=random.choice(hashtagList))
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(600)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            for comment in tqdm(comments):
                replied = False
                parent_comment_id = comment["pk"]
                user_id = comment["user"]["pk"]
                comment_type = comment["type"]
                commenter = comment["user"]["username"]
                text = comment["text"]
                #process
                bot.logger.info("Deleting Hashtags From Your Photo")
                bot.delete_comment(media_id,parent_comment_id)
                #commented_users.append(user_id)
                print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
                countdown(60)
                print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Infinity Feed Like
def ig_feedliker():
    KMFHEADER()
    FEEDLIKER()
    while True:
        try:
            bot.like_timeline(amount=10)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(300) #waiting for 3min
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#Inshackle Followers
def ig_inshackle():
    KMFHEADER()
    INSHACKLE()
    while True:
        try:
            bot.follow_users(user_ids=USERID_FOR_INSHACKLE)
            countdown(counter_time=1800)
            bot.unfollow_users(user_ids=USERID_FOR_INSHACKLE)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(120)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Program For Unfollow Non-Followers
def ig_nonfollowers():
    KMFHEADER()
    NONFOLLOWERS()
    while True:
        try:
            bot.unfollow_non_followers(n_to_unfollows=10)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(240)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Direct Message
def ig_directmessage():
    KMFHEADER()
    DIRECTMESSAGE()
    INUsrp_TEXT = input("\u001b[32m[+]\u001b[0m Enter Message want to Sent:-")
    print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            USER = bot.get_hashtag_users(hashtag="CASABLANCA")
            USER_IDD = random.choice(USER)
            NAME = bot.get_username_from_user_id(USER_IDD)
            FULL_TEXT = ("Hi "+NAME+", "+INUsrp_TEXT)
            
            bot.logger.info("Message Sented to "+ NAME)
            countdown(1500)
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#Profile-Scraper
def ig_ProfileScraper():
    KMFHEADER()
    PROFILE_SCRAPER()
    while True:
        try:
            userID = input("\u001b[32m[+]\u001b[0m Enter Username:-")
            user_id = bot.get_user_id_from_username(userID)
            user_info = bot.get_user_info(user_id)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            FULLNAME = print("\u001b[32m[+]\u001b[0m Name:-",user_info['full_name'])
            MEDIA_COUNT = print("\u001b[32m[+]\u001b[0m Media Count:-",user_info['media_count'])
            FOLLOWERS = print("\u001b[32m[+]\u001b[0m Followers:-",user_info['follower_count'])
            FOLLOWING = print("\u001b[32m[+]\u001b[0m Following:-",user_info['following_count'])
            BIO = print("\u001b[32m[+]\u001b[0m Bio:-",user_info['biography'])
            WEBSITE = print("\u001b[32m[+]\u001b[0m Website:-",user_info['external_url'])
            PHONENUMBER = print("\u001b[32m[+]\u001b[0m Phone:-","+",user_info['public_phone_country_code'],user_info['public_phone_number'])
            EMAIL =  print("\u001b[32m[+]\u001b[0m Email:-",user_info['public_email'])
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            print('\u001b[32m[1]\u001b[0m Main-Menu')
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            SCRA_Inpur = input("\u001b[32m[+]\u001b[0m Enter Input:-")
            if SCRA_Inpur == "1":
                Option()
            else:
                clear()
                Option()

        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#---------------------------------------------------------------------------------------------------------------

#Login Process
def Login():
    time.sleep(1)
    KMFHEADER()
    BOTLOGIN()
    USERNAME = input("\u001b[32m[+]\u001b[0m Enter username:-")
    PASSWORD = input("\u001b[32m[+]\u001b[0m Enter password:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    bot.login(username=USERNAME,password=PASSWORD)
    clear()


def MainBot():
    clear()
    Login()
    Option()

def ELSE_BOT():
    Option()

def LogOut():
    exit()
