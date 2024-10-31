EXAMPLE_REPORT = {
    "osn_sved_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Основные сведения"
            ]
        },
        "options": [
            {
                "osn_sved_oo": False,
                "re": r"(ОГРН)"
            },
            {
                "nazv_oo": False,
                "re": "(образовательное)"
            },
            {
                "inf_uchred_oo": False,
                "re": "(учредит)|(Учредительный)"
            },
            {
                "geo_oo": False,
                "re": r"(19\d{4})|(Санкт)"
            },
            {
                "grafik_oo": False,
                "re": "(режим)|(Режим работы)|(График работы)"
            },
            {
                "phones_oo": False,
                "re": r"((\+7|7|8)+([0-9]){10})"
            },
            {
                "mail_oo": False,
                "re": r"[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}"
            },
            {
                "license_oo": False,
                "re": "(лицензия)|(Лицензия)"
            },
            {
                "accredit_oo": False,
                "re": "(аккредитация)|(Аккредитация)"
            }
        ]
    },
    "struct_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Структура и органы управления образовательной организацией"
            ]
        },
        "options": [
            {
                "nazv_podr": False,
                "re": "(сведения о структурных)|(Сведения о структурных)|(подразделения)"
            },
            {
                "geo_podr": False,
                "re": r"(19\d{3})|(Санкт)"
            },
            {
                "mail_podr": False,
                "re": r"[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}"
            },
            {
                "fio_podr": False,
                "re": r"[а-яА-ЯёЁa-zA-Z]+ [а-яА-ЯёЁa-zA-Z]+ ?[а-яА-ЯёЁa-zA-Z]+"
            }
        ]
    },
    "doc_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Документы"
            ]
        },
        "options": [
            {
                "ustav_doc": False,
                "re": "(устав)|(Устав)"
            },
            {
                "raspor_doc": False,
                "re": "(внутреннего распорядка обучающихся)|(Правила внутреннего распорядка обучающихся)"
            },
            {
                "trudo_doc": False,
                "re": "(внутреннего трудового)|(Правила внутреннего трудового распорядка)"
            },
            {
                "pravila_priema_doc": False,
                "re": "(правила приема)|(Правила приема)"
            },
            {
                "rasp_doc": False,
                "re": "(режим)|(Режим занятий)"
            }
        ]
    },
    "obraz_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Образование"
            ]
        },
        "options": [
            {
            }]
    },
    "rukovod_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Руководство"
            ]
        },
        "options": [
            {
            }]
    },
    "pedagog_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Педагогический состав"
            ]
        },
        "options": [
            {
            }]
    },
    "mat_teh_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Материально-техническое обеспечение и оснащенность образовательного процесса",
                "Доступная среда"
            ]
        },
        "options": [
            {
            }]
    },
    "platn_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Платные образовательные услуги",
                "Платные услуги"
            ]
        },
        "options": [
            {
            }]
    },
    "fin_hoz_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Финансово-хозяйственная деятельность"
            ]
        },
        "options": [
            {
            }]
    },
    "vakantn_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Вакантные места",
                "Вакантные места для приема (перевода) обучающихся"
            ]
        },
        "options": [
            {
            }
        ]
    },
    "stipednd_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Стипенд",
                "Стипендии и меры поддержки обучающихся"
            ]
        },
        "options": [
            {
            }
        ]
    },
    "mezhdunarod_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Международн",
                "Международное сотрудничество"
            ]
        },
        "options": [
            {
            }
        ]
    },
    "org_pitan_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Организация питания в образовательной организации"
            ]
        },
        "options": [
            {
            }
        ]
    },
    "standart_razd": {
        "status": False,
        "link": "",
        "pattern": {
            "re": r"",
            "text": [
                "Образовательные стандарты и требования"
            ]
        },
        "options": [
            {
            }
        ]
    }
}
