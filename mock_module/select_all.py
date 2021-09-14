from flask import Flask
from flask import request
from flask import jsonify



app = Flask(__name__)

@app.route('/select_all', methods=['POST'])
def select_all():
    mediaCode = request.json.get("mediaCode")
    mediaAccountIdList = request.json.get("mediaAcoountIdList")
    adPlatform = request.json.get('adPlatform')
    camLandingType = request.json.get('camLandingType')
    adDownloadType = request.json.get('adDownloadType')
    autoBidType = request.json.get('utoBidType')
    adDeliveryRange = request.json.get('adDeliveryRange')
    convertSourceType = request.json.get('convertSourceType')




"""
{"mediaCode":"toutiao","mediaAccountIdList":["2100130"],"adPlatform":"ANDROID",
"camLandingType":"APP","adDownloadType":"DOWNLOAD_URL","autoBidType":"SMART_BID_CUSTOM",
"adDeliveryRange":"UNION","convertSourceType":"AD_CONVERT_SOURCE_TYPE_APP_DOWNLOAD"}

{
	"code":200,
	"data":{
		"2100130":{
			"DEEP_BID_DEFAULT":[
				{
					"action_track_url":"https://uri6.com/tkio/YNzYZra?imei=__IMEI__&mac=__MAC1__&androidid=__ANDROIDID__&oaid=__OAID__&ip=__IP__&ts=__TS__&os=__OS__&callback_param=__CALLBACK_PARAM__&callback=__CALLBACK_URL__&ry_adgroup_id=__CAMPAIGN_ID__&ry_adplan_id=__AID__&ry_adplan_name=__AID_NAME__&ry_adcreative_id=__CID__&ctype=__CTYPE__&csite=__CSITE__&siteid=__UNION_SITE__&vid=__VID__&ry_adcreative_name=__CID_NAME__&aid=__AID__&ry_adgroup_name=__CAMPAIGN_NAME__&accountid=__ADVERTISER_ID__&noredirect=true",
					"convert_app_id":"1700881655283726",
					"convert_id":"1710392768455688",
					"convert_name":"激活-0909-1",
					"convert_source_type":{
						"code":"AD_CONVERT_SOURCE_TYPE_APP_DOWNLOAD",
						"value":"应用下载API"
					},
					"convert_type":{
						"code":"AD_CONVERT_TYPE_ACTIVE",
						"value":"激活"
					},
					"deep_external_action":{
						"code":"XXX",
						"value":"无"
					},
					"display_track_url":"",
					"down_url":"https://apps.bytesfield.com/download/basic/cur/72fd2d101fd89ee81801d7aea5f0b564c3f3551b",
					"form_id":"",
					"form_index":"",
					"package_name":"com.quliang.wifijsb"
				}
			],
			"ROI_COEFFICIENT":[],
			"ROI_PACING":[],
			"DEEP_BID_MIN":[],
			"DEEP_BID_PACING":[],
			"BID_PER_ACTION":[]
		}
	},
	"message":"转化跟踪查询成功",
	"success":true
}
"""



@app.route('/select', methods = ['POST'])
def select():
    type = request.json.get('type')
    current = request.json.get('current')
    size = request.json.get('size')
    media_code = request.json.get('media_code')
    media_account_id = request.json.get('media_account_id')


    # {"type": "SITE", "current": 1, "size": 1, "media_code": "toutiao", "media_account_id": "2100130"}
    # {type: "THIRD_SITE", current: 1, size: 14, media_code: "toutiao", media_account_id: "2100130"}
    """{
	"code":200,
	"data":{
		"current":1,
		"hitCount":false,
		"optimizeCountSql":true,
		"orders":[],
		"pages":1,
		"records":[
			{
				"thumbnail":"https://p1-ad.byteimg.com/img/ad-tetris-site/screenshot/95b8d449bdf9b6568bd0ab1985dde07c~noop.jpeg",
				"type":"SITE",
				"website_id":"6979154707403702308",
				"website_name":"新建站点_好看一点的",
				"website_url":"https://www.chengzijianzhan.com/tetris/page/6979154707403702308"
			},
			{
				"thumbnail":"https://p6-ad.byteimg.com/img/ad-tetris-site/screenshot/a81b86c8b177c9a1252598c98e1ae1a7~noop.jpeg",
				"type":"SITE",
				"website_id":"6979023376015900679",
				"website_name":"wifi闪电宝1",
				"website_url":"https://www.chengzijianzhan.com/tetris/page/6979023376015900679"
			}
		],
		"searchCount":true,
		"size":14,
		"total":2
	},
	"message":"Success",
	"success":true
}"""
    if type == "SITE":
        sql  = "select * from ads_site where media_code = %s and media_account_id = %s order by create_time limit %s" %( media_code, media_account_id, size)
    elif type == "THIRD_SITE":
        sql = "select * from ads_third_site where media_code = %s and media_account_id = %s order by create_time limit %s" %( media_code, media_account_id, size)

    else:
        return "site type error"



@app.route('own_site/search', methods = ["POST"])
def search():       #  Request URL: http://pre-api.adsdesk.cn/adsdesk/api/tools/own_site/search
    # {"current": 1, "size": 14, "media_code": "toutiao", "advertiserId": "1702893990353933"}
    current = request.json.get('current')
    size = request.json.get('size')
    media_code = request.json.get('media_code')
    adversiserId = request.json.get('advertiserId')
    #  {
    # 	"code":200,
    # 	"data":{
    # 		"current":1,
    # 		"hitCount":false,
    # 		"optimizeCountSql":true,
    # 		"orders":[],
    # 		"pages":0,
    # 		"records":[],
    # 		"searchCount":true,
    # 		"size":14,
    # 		"total":0
    # 	},
    # 	"message":"Success",
    # 	"success":true
    # }
    sql = " select * from"