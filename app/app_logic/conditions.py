def get_conditions_for_table(table_name):
    conditions = []
    if table_name in ['gold_av_total', 'gold_av_centr', 'gold_av_mobila', 'gold_av_depo3', 'gold_av_depo5',
                      'gold_av_depo7', 'gold_av_depo11', 'gold_av_depo34', 'gold_av_depo35', 'gold_av_depo38',
                      'gold_av_depo60', 'api_avto_inkosaciya_av', 'db_1c_av', 'bitrix_portal_av', 'itilium_av',
                      'devops_av', 'tessa_av']:
        conditions = [
            {
                "MEASUREMENT": "gold_av_total",
                "IT_SERVICE": "gold_total",
                "TESTS": {"total_percent": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_centr",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_mobila",
                "IT_SERVICE": "gold_mobile",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo3",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo5",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo7",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo11",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo34",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo35",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo38",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "gold_av_depo60",
                "IT_SERVICE": "gold",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "api_avto_inkosaciya_av",
                "IT_SERVICE": "api_avto_inkosaciya",
                "TESTS": {"percent_value": 100.0}
            },
            {
                "MEASUREMENT": "db_1c_av",
                "IT_SERVICE": "db_1c",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "bitrix_portal_av",
                "IT_SERVICE": "bitrix_portal",
                "TESTS": {"average_percent": 100.0, "download_page_av": 100.0, "login_av": 100.0}
            },
            {
                "MEASUREMENT": "itilium_av",
                "IT_SERVICE": "itilium",
                "TESTS": {"login_portal": 100.0, "average_percent": 100.0}
            },
            {
                "MEASUREMENT": "devops_av",
                "IT_SERVICE": "monitoring",
                "TESTS": {"status_av": 100.0}
            },
            {
                "MEASUREMENT": "tessa_av",
                "IT_SERVICE": "tessa",
                "TESTS": {"average_percent": 100.0, "download_page_av": 100.0, "login_av": 100.0}
            }
        ]
    elif table_name in ['api_tech_av', 'shina_av', 'IBP_public_av_total', 'dostavka_av', 'dixy_av', 'itilium_db_av',
                        'dostavka_bd_av',
                        'mopod_db_1c_av', 'syn_av', 'dixy_group_av', "mobile_dixy_av"]:

        conditions = [
            {
                "MEASUREMENT": "api_tech_av",
                "IT_SERVICE": "api_tech",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0,
                          "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "shina_av",
                "IT_SERVICE": "shina",
                "TESTS": {"shina_total_av": 100.0, "Gold_av_one": 100.0, "DBGateProd_av_one": 100.0,
                          "ubi_av_one": 100.0, "api_av_one": 100.0, "average_percent": 100.0}
            },
            {
                "MEASUREMENT": "IBP_public_av_total",
                "IT_SERVICE": "ibp_total",
                "TESTS": {"total_percent": 100.0}
            },
            {
                "MEASUREMENT": "dostavka_av",
                "IT_SERVICE": "dostavka",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0,
                          "percent_value_catalog": 100.0,
                          "percent_value_select_product": 100.0, "percent_value_ordering": 100.0}
            },
            {
                "MEASUREMENT": "dixy_av",
                "IT_SERVICE": "dixy",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0, "percent_value_one": 100.0}
            },
            {
                "MEASUREMENT": "itilium_db_av",
                "IT_SERVICE": "itilium_db",
                "TESTS": {"percent_value": 100.0}
            },
            {
                "MEASUREMENT": "dostavka_bd_av",
                "IT_SERVICE": "dostavka_bd",
                "TESTS": {"percent_value": 100.0}
            },
            {
                "MEASUREMENT": "mopod_db_1c_av",
                "IT_SERVICE": "mopod_db_1c",
                "TESTS": {"percent_value": 100.0}
            },
            {
                "MEASUREMENT": "syn_av",
                "IT_SERVICE": "syn",
                "TESTS": {"percent_value": 100.0}
            },
            {
                "MEASUREMENT": "dixy_group_av",
                "IT_SERVICE": "dixy",
                "TESTS": {"average_percent": 100.0, "percent_value": 100.0,
                          "percent_value_one": 100.0, "percent_value_two": 100.0}
            },
            {
                "MEASUREMENT": "mobile_dixy_av",
                "IT_SERVICE": "android_dixy",
                "TESTS": {"average_percent": 100.0, "percent_value_basket": 100.0,
                          "percent_value_catalog": 100.0, "percent_value_registration": 100.0,
                          "percent_value_select_product": 100.0}
            }
        ]

    elif table_name in ['axapta_av']:

        conditions = [
            {
                "MEASUREMENT": "axapta_av",
                "IT_SERVICE": "axapta",
                "TESTS": {"percent_value": 100.0}
            }
        ]

    return conditions
