Feature: Testing camp set
    Scenario: test setting camp set with answers 2 0 1
        Given answers for states 1, 2, 3 : 2, 0, 1
        When setting camp
        Then we should see В итоге: Локация: Пустыня. В рюкзаке: Палатка. Способ передвижения: Вертолет. /setstate, чтобы очистить и собрать заново.

    Scenario: test setting camp set with answers 1 2 2
        Given answers for states 1, 2, 3 : 1, 2, 2
        When setting camp
        Then we should see В итоге: Локация: Горы. В рюкзаке: Фен. Способ передвижения: Караван верблюдов. /setstate, чтобы очистить и собрать заново.