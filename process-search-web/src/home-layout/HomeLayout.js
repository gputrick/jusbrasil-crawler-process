import { Layout } from 'antd';
import React, { Component } from 'react';
import ProcessSearch from '../process-search/ProcessSearch';
import './HomeLayout.scss';

const { Header, Content, Footer } = Layout;

class HomeLayout extends Component {
    render() {
        return (
            <div className="HomeLayout" style={{ height: '100%' }}>
                <Layout className="layout">
                    <Header>
                        <h3>Crawler Jusbrasil</h3>
                    </Header>
                    <Content>
                        {/* Colocar rotas */}
                        <ProcessSearch />
                    </Content>
                    <Footer style={{ textAlign: 'end' }}>Teste para jusbrasil</Footer>
                </Layout>,
            </div>
        )
    }
}

export default HomeLayout