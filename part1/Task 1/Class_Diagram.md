# Diagramme de classes

```mermaid
classDiagram
    class User {
        UUID id
        String name
        String email
        String password
        Date created_at
        Date updated_at
        +createPlace(Place place)
        +createReview(Review review)
    }

    class Place {
        UUID id
        String name
        String location
        Double price
        User owner
        Date created_at
        Date updated_at
        +addAmenity(Amenity amenity)
        +updateDetails(String name, Double price)
    }

    class Amenity {
        UUID id
        String name
        Date created_at
        Date updated_at
        +updateName(String name)
    }

    class Review {
        UUID id
        String comment
        int rating
        User reviewer
        Place place
        Date created_at
        Date updated_at
        +editReview(String comment, int rating)
    }

    class Amenity_Place {
        UUID place_id
        UUID amenity_id
    }

    User "1" --o "0..*" Place : Owns
    User "1" --o "0..*" Review : Creates
    Place "1" --o "0..*" Review : Refers
    Review "1" --o "1" User : Made by
    Place "1" --o "0..*" Amenity_Place : "Associates"
    Amenity "1" --o "0..*" Amenity_Place : "Associates"
```

Cliquez sur ce lien pour consulter le diagramme: [Mermaid Live Editor](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=banner_ad&utm_campaign=visual_editor#pako:eNqtVE1vwjAM_StWpUndRtG49obGYTvsQ0zcKiHTBpSpTVCaghDiv89N2ioR5UOMHupiPzv2ew77IJUZC-IgzbEsJxxXCotEJQLoMT6YlUzBvvXVz2z2PgGeua4frbhYgcCC9bhZgTzv8a-p_lYqr9IENYNUMTLZHPVRqFpnPaFnm_GdY8pC84Z1_X7sAU3ZhrNtaA0oYzrcof7wCbDl_sdALlPUXApvHFktcupT8dRLMYTLrWDqDrxglo0LJrjehY0FtNanxqZPmCalytAZZuD1eY6ntv6NTN04oHV_UjG363N9NsJf2WYqC5rLO5MLDYrkFKsj2ew2-co563iHeVnGdbPBfocDp68rZJqfWmvT6NznwgSavXFCXnUzfxKMkgCiSNLXy3D4RD_sOTF8bUV5CdtIE8Or4aXD2xodrD_nDY_wpw-YsiVTHb5xuwkjp_WrwGamGD4wY7DYucw8PMD4V1YaKJIj7Uhu_gugQLGLtIxqCxuOQLdMI901rICUkikn3PLiTL6gMQXGTTIRGLTp7e28qUBw-ANs2eHu).
