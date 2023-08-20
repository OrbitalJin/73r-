style: str = """

/*------------- Terminal ---------------*/ 

#Terminal #TermOut {
    background-color: black;
    color: white;
    border: 1px solid green;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}

#Terminal #TermIn {
    background-color: black;
    color: white;
    border: 1px solid green;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

/*------------- Scroll Bar | Vertical---------------*/ 
QScrollBar:vertical  {
	border: none;
	background: transparent;
	width: 4px;
	margin: 21px 0 21px 0;
	border-radius: 3px;
}
QScrollBar::handle:vertical  {
	background: green;
	min-height: 25px;
	border-radius: 4px
}
QScrollBar::add-line:vertical  {
	border: none;
	background: transparent;
}
QScrollBar::sub-line:vertical  {
	border: none;
	background: transparent;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical  {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical  {
	background: none;
}
"""