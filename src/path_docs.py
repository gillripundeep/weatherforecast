"""Open Docs API"""


open_api_docs = {
    "openapi":"3.1.0",
    "info":{
        "title":"Weather Forecast API",
        "version":"0.1.0"
    },
    "paths":{
        "/":{
            "get":{
                "summary":"Weather Forecast API Metadata",
                "description":"Weather Forecast API Metadata",
                "operationId":"read_root__get",
                "responses":{
                    "200":{
                        "description":"Successful Response",
                        "content":{
                            "application/json":{
                                "schema":{}
                            }
                        }
                    }
                }
            }
        },
        "/weatherforecast":{
            "post":{
                "summary":"Weatherforecast",
                "description":"Weather Forecast POST API",
                "operationId":"weatherforecast_weatherforecast_post",
                "requestBody":{
                    "content":{
                        "application/json":{
                            "schema":{
                                "$ref":"#/components/schemas/CityData"
                            }
                        }
                    },
                    "required":True
                },
                "responses":{
                    "200":{
                        "description":"Successful Response",
                        "content":{
                            "application/json":{
                                "schema":{}
                            }
                        }
                    },
                    "422":{
                        "description":"Validation Error",
                        "content":{
                            "application/json":{
                                "schema":{
                                    "$ref":"#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components":{
        "schemas":{
            "CityData":{
                "properties":{
                    "city":{
                        "type":"string",
                        "title":"City"
                    }
                },
                "type":"object",
                "required":["city"],
                "title":"CityData"
            },
            "HTTPValidationError":{
                "properties":{
                    "detail":{
                        "items":{
                            "$ref":"#/components/schemas/ValidationError"
                        },
                        "type":"array",
                        "title":"Detail"
                    }
                },
                "type":"object",
                "title":"HTTPValidationError"
            },
            "ValidationError":{
                "properties":{
                    "loc":{
                        "items":{
                            "anyOf":[
                                {"type":"string"},
                                {"type":"integer"}
                            ]
                        },
                        "type":"array",
                        "title":"Location"
                    },
                    "msg":{
                        "type":"string",
                        "title":"Message"
                    },
                    "type":{
                        "type":"string",
                        "title":"Error Type"
                    }
                },
                "type":"object",
                "required":["loc","msg","type"],
                "title":"ValidationError"
            }
        }
    }
}
