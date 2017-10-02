import { connect } from 'react-redux'
import { Magic, Add, Delete, Laptop, Tune, Close } from 'components/Icons'
import { push } from 'redux-little-router'
import { modelSelectors, modelActions } from 'ducks/basemodel'

const model = 'images'
const { fieldChanged } = modelActions(model)
const { getItem } = modelSelectors(model)

const openUrl = url => () => window.open(url)

const Tool = ({ Icon, ...props }) => (
  <div className="Tool" {...props}>
    <Icon />
  </div>
)

const ToolBar = props => <div {...props} />

const PhotoTools = ({ autocrop, close, openAdmin }) => (
  <ToolBar className="DetailToolBar">
    <Tool Icon={Close} title="lukk saken" onClick={close} />
    <Tool Icon={Magic} title="autocrop" onClick={autocrop} />
    <Tool Icon={Tune} title="rediger i django-admin" onClick={openAdmin} />
  </ToolBar>
)

const mapStateToProps = (state, { pk }) => getItem(pk)

const mapDispatchToProps = (dispatch, { pk }) => ({
  autocrop: () => dispatch(fieldChanged(pk, 'cropping_method', 1)),
  close: () => dispatch(push(`/${model}`)),
  openAdmin: openUrl(`/admin/photo/imagefile/${pk}/change/`),
})

export default connect(mapStateToProps, mapDispatchToProps)(PhotoTools)