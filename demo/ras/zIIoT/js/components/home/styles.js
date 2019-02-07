
const React = require('react-native');

const { StyleSheet } = React;
export default {
  container: {
    backgroundColor: '#FBFAFA',
  },
  row: {
  marginTop:10,
  padding:5,
    alignItems: 'center',
  },
  backgroundImage: {
    flex: 1,
    resizeMode: 'cover', // or 'stretch'
    width:100
  },
  accept: {
    fontSize: 20,
    
    alignItems: 'center',
    // borderColor: 'green',
    // borderWidth: 2,
    
    backgroundColor:'rgba(0, 153, 51,0.5)',
    padding:10,
    margin:10
  },
  button: {
    
    backgroundColor: 'green',
    
  },
  reject: {
    fontSize: 20,
    marginBottom: 15,
    alignItems: 'center',
    backgroundColor: 'rgba(255, 0, 0, 0.2)',
    // borderWidth: 2,
    padding:10,
    margin:10
  },
  delete: {
    fontSize: 20,
    marginBottom: 15,
    alignItems: 'center',
    backgroundColor: 'rgba(255, 51, 0,0.2)',
    // borderWidth: 2,
    padding:10,
    margin:10
  },
  mt: {
    marginTop: 18,
  },
};
