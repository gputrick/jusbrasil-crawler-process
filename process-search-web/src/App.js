import 'antd/dist/antd.css';
import React, { Component } from 'react';
import './App.scss';
import { Layout } from 'antd';
const { Header, Content, Footer } = Layout;

class App extends Component {
    render() {
        return (
            <div className="App" style={{ height: '100%' }}>
                <Layout className="layout">
                    <Header>
                        <h3>Crawler Jusbrasil</h3>
                    </Header>
                    <Content>
                        {this.props.children}
                    </Content>
                    <Footer style={{ textAlign: 'end' }}>Teste para jusbrasil</Footer>
                </Layout>
            </div>
        )
    }
}

export default App;
