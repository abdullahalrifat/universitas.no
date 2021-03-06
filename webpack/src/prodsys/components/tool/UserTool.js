import { connect } from 'react-redux'
import { logOut, logIn, getUser } from 'ducks/auth'

const Avatar = ({ src, title }) => (
  <img className="Avatar" alt="avatar" src={src} title={title} />
)

const UserTool = ({ first_name, last_name, username, logOut, avatar }) => {
  const name = first_name ? `${first_name} ${last_name}` : username
  return (
    <div className="UserTool">
      {avatar ? (
        <Avatar src={avatar} title={name} />
      ) : (
        <span className="username">{name}</span>
      )}
      <button className="button" onClick={logOut}>
        Logg ut
      </button>
    </div>
  )
}

export default connect(
  getUser,
  { logOut },
)(UserTool)
