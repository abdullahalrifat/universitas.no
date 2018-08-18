import cx from 'classnames'
import { connect } from 'react-redux'
import Thumb from 'components/Thumb'
import { PhotoStats } from '.'
import { MODEL as model, actions, selectors } from './model.js'
import './PhotoGrid.scss'

const Frame = () => <rect className="Frame" width="100%" height="100%" />

const FullThumbWithCropBox = ({ src, title, width, height, crop_box }) => {
  const { left, x, right, top, y, bottom } = crop_box
  const boxPath = `M0, 0H1V1H0Z M${left}, ${top}V${bottom}H${right}V${top}Z`
  return (
    <svg className="Thumb" viewBox={`0 0 ${width} ${height}`}>
      <image xlinkHref={src} width="100%" height="100%" />
      <svg
        viewBox="0 0 1 1"
        preserveAspectRatio="none"
        height="100%"
        width="100%"
      >
        <path className="cropOverlay" fillRule="evenodd" d={boxPath} />
      </svg>
      <Frame />
    </svg>
  )
}

const FullThumb = ({ src, title, width, height }) => (
  <svg className="Thumb" viewBox={`0 0 ${width} ${height}`}>
    <image xlinkHref={src} width="100%" height="100%" />
    <Frame />
  </svg>
)

const GridItem = ({ pk, detail, onClick, small, className, ...data }) => (
  <div key={pk} onClick={onClick} className={className}>
    {detail == 'crop' ? (
      <FullThumbWithCropBox src={small} title={data.filename} {...data} />
    ) : (
      <FullThumb src={small} title={data.filename} {...data} />
    )}
    <PhotoStats pk={pk} {...data} />
  </div>
)

const ConnectedGridItem = connect(
  (state, { pk }) => {
    const data = selectors.getItem(pk)(state) || {}
    const selected = selectors.getCurrentItemId(state) === pk
    const { dirty } = data
    const className = cx('GridItem', { dirty, selected })
    const detail = R.pathOr(null, ['router', 'params', 'detail'], state)
    return { ...data, className, model, detail }
  },
  (dispatch, { clickAction }) => ({ onClick: e => dispatch(clickAction) }),
)(GridItem)

const PhotoGrid = ({
  items = [],
  clickHandler = id => actions.reverseUrl({ id }),
}) => (
  <div className="ItemGrid">
    {items.map(pk => (
      <ConnectedGridItem clickAction={clickHandler(pk)} key={pk} pk={pk} />
    ))}
  </div>
)
export default connect(state => ({ items: selectors.getItemList(state) }))(
  PhotoGrid,
)
