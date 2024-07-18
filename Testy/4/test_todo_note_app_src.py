# uses pytest-mock
import pytest
from src import check_pos, add_todo, remove_todo, edit_todo, remove_all


class TestTodoNoteApp:
    @staticmethod
    @pytest.fixture
    def mocked_todos_list(mocker):
        return mocker.patch("src.todos", [])

    @staticmethod
    @pytest.fixture
    def mocked_check_pos_function(mocker):
        return mocker.patch("src.check_pos", return_value=None)


class TestCheckPosFunc(TestTodoNoteApp):
    @staticmethod
    @pytest.mark.parametrize(
        "todos, pos, expected", [
            (["hello", "world"], 1, None),
            (["1", "2", "3", "4", "5"], 4, None)
        ]
    )
    def test_should_pass_and_return_none_value(mocked_todos_list, todos, pos, expected):
        mocked_todos_list[:] = todos

        result = check_pos(1)

        assert result == expected

    @staticmethod
    @pytest.mark.parametrize(
        "todos, pos", [
            ([], 1),
            ([], 5)
        ])
    def test_should_raise_no_more_todos_exception(mocked_todos_list, todos, pos):
        mocked_todos_list[:] = todos

        with pytest.raises(Exception, match=r"No more todos!"):
            check_pos(pos)

    @staticmethod
    @pytest.mark.parametrize("todos, pos", [
        (["item1", "item2", "item3"], 3),
        (["1", "2", "3"], -1),
    ])
    def test_should_raise_no_such_item_exception(mocked_todos_list, todos, pos):
        mocked_todos_list[:] = todos

        with pytest.raises(Exception, match=r"No such item number!"):
            check_pos(pos)


class TestAddTodoFunc(TestTodoNoteApp):
    @staticmethod
    @pytest.mark.parametrize(
        "todos_before, content, todos_after", [
            (["hello", "world"], "trolled", ["hello", "world", "trolled"]),
            (["1", "2", "3"], "4", ["1", "2", "3", "4"])
        ])
    def test_should_add_value_to_the_todos_list(mocked_todos_list, todos_before, content, todos_after):
        mocked_todos_list[:] = todos_before

        add_todo(content)

        assert mocked_todos_list[:] == todos_after


class TestRemoveTodoFunc(TestTodoNoteApp):
    @staticmethod
    @pytest.mark.parametrize(
        "todos_before, pos, todos_after", [
            (["hello", "world"], 1, ["hello"]),
            (["hello", "world", "123", "321"], 2, ["hello", "world", "321"])
        ])
    def test_should_remove_value_from_the_todos_list(
            mocked_check_pos_function, mocked_todos_list, todos_before, pos, todos_after
    ):
        mocked_todos_list[:] = todos_before

        remove_todo(pos)

        assert mocked_todos_list[:] == todos_after


class TestEditTodoFunc(TestTodoNoteApp):
    @staticmethod
    @pytest.mark.parametrize(
        "todos_before, pos, content, todos_after", [
            (["hello", "world"], 1, "lord", ["hello", "lord"]),
            (["hello", "world", "123"], 2, "321", ["hello", "world", "321"])
        ])
    def test_should_change_note_position_content(
            mocked_check_pos_function, mocked_todos_list, todos_before, pos, content, todos_after
    ):
        mocked_todos_list[:] = todos_before

        edit_todo(pos, content)

        assert mocked_todos_list[pos] == content


class TestRemoveAllTodosFunc(TestTodoNoteApp):
    @staticmethod
    @pytest.mark.parametrize(
        "todos_before, todos_after", [
            (["hello", "world"], []),
            (["hello", "world", "123"], [])
        ])
    def test_should_remove_everything_from_todos_list(mocked_todos_list, todos_before, todos_after):
        mocked_todos_list[:] = todos_before

        remove_all()

        assert mocked_todos_list[:] == todos_after
