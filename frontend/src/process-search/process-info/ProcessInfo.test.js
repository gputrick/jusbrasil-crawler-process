import React from 'react';
import ProcessInfo from './ProcessInfo';
import MovesInfo from '../moves-info/MovesInfo'
import RelatedPartsInfo from '../related-parts-info/RelatedPartsInfo'
import { mount } from 'enzyme';
import { Skeleton } from 'antd';
import { processMock } from './process.mock';

test('renders process loading', () => {
    const wrapper = mount(<ProcessInfo loading={true} process={{}} />);
    expect(wrapper.find(Skeleton).exists()).toBeTruthy();
    expect(wrapper.find(MovesInfo).exists()).toBe(false);
});


test('renders process layout', () => {
    const wrapper = mount(<ProcessInfo loading={false} process={processMock} />);
    expect(wrapper.find(Skeleton).exists()).toBe(false);
    expect(wrapper.find('h1').text()).toMatch(new RegExp(processMock.process_number));
    expect(wrapper.find(MovesInfo).exists()).toBe(true);
    expect(wrapper.find(RelatedPartsInfo).exists()).toBe(true);
});