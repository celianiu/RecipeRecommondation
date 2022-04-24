
import './App.css';
import {Col, Input, Row, Space} from 'antd';
import { Layout, Menu, Breadcrumb } from 'antd';
import { useNavigate } from "react-router-dom";
const { Header, Content, Footer } = Layout;

const { Search } = Input;

function App() {
    let navigate = useNavigate();
  return (
      <Layout>
          <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
              <div className="logo" />
              <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                  <Menu.Item key="1">nav 1</Menu.Item>
                  <Menu.Item key="2">nav 2</Menu.Item>
                  <Menu.Item key="3">nav 3</Menu.Item>
              </Menu>
          </Header>
          <Content className="site-layout" style={{ padding: '0 50px', marginTop: 64 }}>
              <Breadcrumb style={{ margin: '16px 0' }}>
                  <Breadcrumb.Item>Home</Breadcrumb.Item>
              </Breadcrumb>

              <div className="site-layout-background" style={{ padding: 24, minHeight: 380 }}>
                  <Row>
                      <Col span={24}>
                          <center><img
                              width={800}
                              src="https://d18mqtxkrsjgmh.cloudfront.net/public/2021-03/Eating%20More%20Ultraprocessed%20‘Junk’%20Food%20Linked%20to%20Higher%20CVD%20Risk.jpeg"
                          /></center>
                      </Col>
                  </Row>
              </div>
              <div className="site-layout-background" style={{ padding: 24, minHeight: 380 }}>
                  <Row>
                      <Col span={24}>
                          <Search placeholder="input search text" onSearch={(value)=>{
                              if(value!=="") {
                                  navigate('/search/' + value)
                              }
                          }} enterButton />
                      </Col>
                  </Row>
              </div>
          </Content>
          <Footer style={{ textAlign: 'center' }}></Footer>
      </Layout>
  );
}

export default App;
