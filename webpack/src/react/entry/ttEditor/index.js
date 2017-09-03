/* eslint-env browser */
import { Provider } from 'react-redux'
import configureStore from './configureStore'
import Editor from 'containers/Editor'
import Preview from 'components/Preview'
import 'styles/editorapp.scss'

const App = () => (
  <section className="EditApp">
    <Editor />
    <Preview />
  </section>
)
const rootStore = configureStore()

export default () => (
  <Provider store={rootStore}>
    <App />
  </Provider>
)
