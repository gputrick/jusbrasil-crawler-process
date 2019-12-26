import React from 'react';
import App from './App'
import { mount } from 'enzyme';
import { Layout } from 'antd';
const { Header, Content, Footer } = Layout;

test('reders toolbar content and footer', () => {

    const wrapper = mount(<App />);

    expect(wrapper.find(Header).exists()).toBeTruthy();

    expect(wrapper.find(Content).exists()).toBeTruthy();

    expect(wrapper.find(Footer).exists()).toBeTruthy();
});
