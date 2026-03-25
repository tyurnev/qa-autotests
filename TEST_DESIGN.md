# April — Test design (data-driven) for GET /posts?userId=

Цель: спроектировать набор кейсов с эквивалентными классами и граничными значениями для фильтрации постов по userId,
а затем реализовать автотесты, напрямую соответствующие этой таблице.

## Предпосылки
- Base URL: https://jsonplaceholder.typicode.com
- Эндпоинт: GET /posts?userId={value}
- Наблюдаемое поведение JSONPlaceholder: при "невалидных" значениях возвращает 200 и пустой список.

## Таблица кейсов

| Case ID | Endpoint               | Input (userId) | Класс/граница             | Ожидаемый статус | Ожидаемое тело               |
| ------- | ---------------------- | -------------: | ------------------------- | ---------------: | ---------------------------- |
| APR-01  | GET /posts?userId={id} |              1 | валидный, нижняя граница  |              200 | список > 0, все `userId==1`  |
| APR-02  | GET /posts?userId={id} |             10 | валидный, верхняя граница |              200 | список > 0, все `userId==10` |
| APR-03  | GET /posts?userId={id} |              0 | ниже границы              |             200* | список пустой*               |
| APR-04  | GET /posts?userId={id} |             11 | выше границы              |             200* | список пустой*               |
| APR-05  | GET /posts?userId={id} |             -1 | отрицательный             |             200* | список пустой*               |
| APR-06  | GET /posts?userId={id} |          "abc" | неверный тип              |             200* | список пустой*               |
| APR-07  | GET /posts             |   (без userId) | параметр отсутствует      |              200 | список > 0                   |
| APR-08  | GET /posts?userId=     |             "" | пустое значение           |             200* | список пустой*               |

## Трассировка (test design → automated tests)

- APR-01..APR-08 → tests/api/test_posts_filter_by_userid_design.py::test_posts_filter_by_userid_matches_test_design
  - параметризация с ids=[APR-01..APR-08] обеспечивает связь “case id → запуск в pytest”
