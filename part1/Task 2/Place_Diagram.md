# Diagramme De Sequence Place

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: POST /place (Place data)
    API->>BusinessLogic: validatePlaceData
    BusinessLogic->>Database: checkPlaceData
    Database-->>BusinessLogic: Data Place Exist ? (true/false)
    alt Place Data
        BusinessLogic-->>API: PlaceDataExistsError()
        API-->>User: 409 Conflict (Place exist)
    else Place does not exist
        BusinessLogic->>Database: insertPlace(Name, Price, Location, Amenity, Owner)
        Database-->>BusinessLogic: Place created
        BusinessLogic-->>API: placeCreated/Error (Data Place)
        API-->>User: 201 Created (Place) <br />400 (Data Error)
    end
```

Cliquez sur ce lien pour consulter le diagramme: [Mermaid Live Editor](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=banner_ad&utm_campaign=visual_editor#pako:eNqFks1uwjAQhF9llVMigZJWXBpVIAocKqESqe2Ny-Is1GqwqW36o6rvXtuJIRHQ-mLJ-83ueOzviMmSojzS9LYnwWjKcaNwu1RLAXbtUBnO-A6FgWdN6tz5uLg_d3y311yQ1nO54ewcMEWDK9TkaqHuZvSHQ9syh2Lx-ATprkJGEBd-K60kCayFLNoZk8M7VtxS5Hk3IdAdzurC9BzYC7HXEz7U-6czXAlqQ7NPrg2MIDZqT-kaK00Hf1iZhmr3PfVyuG-w4JvqmVJSxUlb525saRdSDoPsBiZSrCvOTMiHnPIgIeumcVBK0iCkqYnLXtq5cGHnGK-PH3BLPSgUZ3abS4aGS9GD8ZYEN189WHwIUh2vf-RXW2KK7DuV_-fif8CkplOfCsTHJ7gc0HV2BY2sySeB25WCdDjIsqaFb3cMTJTRzy-hQQEq)
