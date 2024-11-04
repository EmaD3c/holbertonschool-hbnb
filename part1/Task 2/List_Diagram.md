# Diagramme De Sequence List

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: Get /List of Places (Criteria: Location, Price, )
    API->>BusinessLogic: validateListOfPlaces(Criteria)
    BusinessLogic->>Database: fetchPlaces(criteria)
    Database-->>BusinessLogic: Places found? (List of places/empty)
    alt No places found
        BusinessLogic-->>API: NoPlacesFound()
        API-->>User: 200 (No places matching criteria)
    else Places found
        BusinessLogic->>Database: Get list of place (Criteria: Location, Price, )
        Database-->>BusinessLogic: Return list of place (Criteria: Location, Price, )
        BusinessLogic-->>API: Return list of place (Criteria: Location, Price, )
        API-->>User: 200 Return list (Criteria: Location, Price, ) <br />400 (Data Error)
    end
```

Cliquez sur ce lien pour consulter le diagramme: [Mermaid Live Editor](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=banner_ad&utm_campaign=visual_editor#pako:eNqlkU9LAzEQxb_KsKcttGwRT0EqalWEUovgrZdpdrYGtsmazAoifncTu2m33fUPmmNm3m_evHlLpMkpEYmj55q0pKnCtcXN0i41-FehZSVVhZrh0ZHt-79Y3PV9X9ZOaXJuZtZK9jVMkXGFjkIt1sOM0WTikQJuiSGbKcdgCliUKMlBemUVk1UoYGYksjJ6CAurJA1hECFe7RkH8wW8YKlyZArA-2KL29F20gORh0SPAgpi-dTI5LEsto26cxvjhal1fg5p3Kf6_M5oU_HrDoMlw9w0ta0klrrmYkxzsx1xE9rTQVsQgvBtIVQBJ-MxpHv6Bv0-Sq-hswyVjg5sf-2hHVA4V9ne7nfH-iG-B-La6r-C-xP7H7MTahv3LQXOVhayyWk4RFgZrq01dp-7zpP3D8MJLJQ)   
