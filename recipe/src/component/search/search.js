import { Layout, Menu, Breadcrumb } from 'antd';
import axios from 'axios'
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';
import {useLocation,useNavigate} from "react-router-dom";
import React,{useEffect,useState} from "react";
import { Card } from 'antd';
import Recipe from './recipe'
const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;
const url = 'http://127.0.0.1:8080/'


function Search(){
    let location = useLocation()
    let navigate = useNavigate();
    let keyWord = location.pathname.split('/')[2]

    const [result,setResult] = useState([])
    let config = {
        url:url+"search/"+keyWord,
        method:"post",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': 'true'
        }
    }

    useEffect(()=>{
        const fetchRecipe = async ()=>{
            const {data:response} = await axios.request(config);
            let all = []
            for(let i = 0;i<response.length;i++){
                all.push(
                    <Menu.Item key={response[i]} onClick={()=>{

                        navigate('/search/'+keyWord+'/'+response[i])
                    }}>{response[i]}</Menu.Item>
                )
            }
            setResult(all)
        }

            fetchRecipe();






    },[])



  return (
      <Layout>
          <Header className="header">
              <div className="logo" />
              <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                  <Menu.Item key="1">nav 1</Menu.Item>
                  <Menu.Item key="2">nav 2</Menu.Item>
                  <Menu.Item key="3">nav 3</Menu.Item>
              </Menu>
          </Header>
          <Layout>
              <Sider width={200} className="site-layout-background">
                  <Menu
                      mode="inline"
                      defaultSelectedKeys={['1']}
                      defaultOpenKeys={['sub1']}
                      style={{ height: '100%', borderRight: 0 }}
                  >{
                      result

                  }


                  </Menu>
              </Sider>
              <Layout style={{ padding: '0 24px 24px' }}>
                  <Breadcrumb style={{ margin: '16px 0' }}>
                      <Breadcrumb.Item>Home</Breadcrumb.Item>
                      <Breadcrumb.Item>Search</Breadcrumb.Item>
                  </Breadcrumb>
                  <Content
                      className="site-layout-background"
                      style={{
                          padding: 24,
                          margin: 0,
                          minHeight: 280,
                      }}
                  >
                      <Recipe/>

                  </Content>
              </Layout>
          </Layout>
      </Layout>
  );

}
export default Search;