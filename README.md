# Streamlit Double Input Error Demo

Some issues arise in streamlit when we want to hide a widget or set of widgets.
The SessionState hack mostly gets around this, but brings up another problem
where a user has to make a change twice for it to "stick". The files in this
repo demo these issues.

## Instructions

First run `streamlit run 0_hideable_column_selection_no_sessionstate.py`. This
shows why storing the output of the hideable widget with SessionState looks
necessary to me.

Next, run `streamlit run 1_hideable_column_selection_with_sessionstate.py`.
This shows the problem that I run into when actually using SessionState

Finally, run `streamlit run 2_sessionstate_default_value_error_mvp.py`. This
is an MVP showing the problem I'm facing.
