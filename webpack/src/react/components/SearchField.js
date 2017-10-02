import { connect } from 'react-redux'
import { modelSelectors, modelActions } from 'ducks/basemodel'
import { Clear } from 'components/Icons'

const SearchField = ({
  value = '',
  label = 'search',
  searchChanged,
  clearSearch,
}) => (
  <div className="SearchField">
    <input
      type="text"
      onChange={searchChanged}
      placeholder={label}
      value={value}
    />
    <button disabled={!value} onClick={clearSearch} className="clear">
      <Clear />
    </button>
  </div>
)

const mapStateToProps = (state, { model, attr = 'search' }) => ({
  value: R.prop(attr, modelSelectors(model).getQuery(state)),
})

const mapDispatchToProps = (dispatch, { model, attr = 'search' }) => ({
  searchChanged: e =>
    dispatch(modelActions(model).filterSet(attr, e.target.value)),
  clearSearch: e => dispatch(modelActions(model).filterSet(attr, '')),
})

export default connect(mapStateToProps, mapDispatchToProps)(SearchField)