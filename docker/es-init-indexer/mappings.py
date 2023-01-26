# create news mapping
news_mapping = {
    "properties": {
        "slug_name": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "section": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "subsection": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "title": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "abstract": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "byline": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "source": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "updated_date": {
            "type":   "date"
        },
        "created_date": {
            "type":   "date"
        },
        "published_date": {
            "type":   "date"
        },
        "first_published_date": {
            "type":   "date"
        },
        "material_type_facet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "des_facet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "org_facet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "per_facet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "geo_facet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        }
    }
}


# create articles mapping
articles_mapping = {
    "properties": {
        "article_id": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "web_url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "abstract": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "snippet": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "lead_paragraph": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "source": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "headline": { # headline.main from response
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "keywords": {
            "type": "nested",
            "properties": {
                "name": { "type": "keyword" },
                "value": { "type": "keyword" },
                "rank": { "type": "integer" },
                "major": { "type": "keyword" }
            }
        },
        "pub_date": {
            "type":   "date"
        },
        "document_type": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "news_desk": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "section_name": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "subsection_name": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "byline": {
            "properties": {
                "original": { "type": "keyword" },
                "organization": { "type": "keyword" },
                "person": {
                    "type": "nested",
                    "properties": {
                        "firstname": { "type": "keyword" },
                        "middlename": { "type": "keyword" },
                        "lastname": { "type": "keyword" },
                        "qualifier": { "type": "keyword" },
                        "title": { "type": "keyword" },
                        "role": { "type": "keyword" },
                        "organization": { "type": "keyword" },
                        "rank": { "type": "integer" }
                    }
                }
            }
        },
        "word_count": {
            "type": "integer"
        }
    }
}


# create popular mapping
popular_mapping = {
    "properties": {
        "popular_type": {
            "type": "text"
        },
        "days": {
            "type": "integer"
        },
        "article_uri": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "id": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "source": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "pub_date": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_section": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_subsection": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_nytdsection": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_adx_keywords": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "byline": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_type": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_title": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "article_abstract": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        }
    }
}
