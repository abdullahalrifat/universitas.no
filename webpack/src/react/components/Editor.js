import { connect } from 'react-redux'

import { textChanged, moveCaret } from 'ducks/editor'
import { cleanup } from 'utils/text'
import Preview from 'components/Preview'
import EditorToolBar from 'components/EditorToolBar'
import * as Icon from 'components/Icons'

class Editor extends React.Component {
  onChange = e => {
    let newContent = e.target.value
    const { content, moveCaret, textChanged } = this.props
    if (content.length < newContent.length) newContent = cleanup(newContent)
    textChanged(newContent)
  }
  setCaretPosition = position => {
    this.textArea.selectionEnd = position
    this.textArea.selectionStart = position
    this.props.moveCaret(position)
  }
  componentDidUpdate(prevProps) {
    const { content, caret } = this.props
    const change = content.length - prevProps.content.length
    if (change !== 0) this.setCaretPosition(caret + change)
  }
  render() {
    const moveCaret = e => this.props.moveCaret(e.target.selectionStart)
    return (
      <section className="Editor">
        <EditorToolBar />
        <textArea
          className="TextArea"
          autoCapitalize="sentences"
          lang="no-nn"
          onChange={this.onChange}
          onKeyUp={moveCaret}
          onMouseUp={moveCaret}
          value={this.props.content}
          ref={el => (this.textArea = el)}
        />
      </section>
    )
  }
}

const mapStateToProps = ({ editor: { caret, content } }) => ({
  caret,
  content,
})

const mapDispatchToProps = { textChanged, moveCaret }

Editor = connect(mapStateToProps, mapDispatchToProps)(Editor)

export default Editor