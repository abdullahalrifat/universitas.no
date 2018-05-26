// Lenses
const sliceLens = R.lensProp('site')

// Selectors
export const getSite = R.view(sliceLens)

// Actions
export const SITE_REQUESTED = 'site/SITE_REQUESTED'
export const siteRequested = () => ({ type: SITE_REQUESTED, payload: {} })

export const SITE_FETCHED = 'site/SITE_FETCHED'
export const siteFetched = data => ({ type: SITE_FETCHED, payload: { data } })

// reducers
const initialState = { fetching: false }

const getReducer = ({ type, payload, error }) => {
  switch (type) {
    case SITE_REQUESTED:
      return R.over(sliceLens, R.assoc('fetching', true))
    case SITE_FETCHED:
      return R.compose(
        R.over(sliceLens, R.assoc('fetching', false)),
        R.over(sliceLens, R.merge)
      )
    default:
      return R.identity
  }
}

export default (state = initialState, action) => getReducer(action)(state)
