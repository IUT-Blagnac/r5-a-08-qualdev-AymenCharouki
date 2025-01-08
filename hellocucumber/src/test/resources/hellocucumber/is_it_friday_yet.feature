Feature: Est-ce déjà vendredi ?
    Scenario Outline: Vérifier si c'est vendredi
        Given aujourd'hui c'est "<day>"
        When je demande si c'est déjà vendredi
        Then on devrait me dire "<answer>"

    Examples:
        | day            | answer |
        | vendredi       | Oui    |
        | dimanche       | Non    |
        | lundi          | Non    |
        | anything else! | Non    |