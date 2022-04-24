import axios from 'axios'
import {useLocation} from "react-router-dom";
import React, {useEffect, useState} from "react";
import {Card} from "antd";
const url = 'http://127.0.0.1:8080/'
function Recipe(){
    let location = useLocation()
    let keyWord = location.pathname.split('/')[2]
    const [oneResult,setOne] = useState([])
    let recipe = location.pathname.split('/').length===3?"":location.pathname.split('/')[3]


    let configForOne = {
        url:recipe===""?url+"search/"+keyWord:url+"recom/"+decodeURIComponent(recipe),
        method:"post",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': 'true'
        }
    }
    useEffect(()=>{
        const fetchOneRecipe = async ()=>{
            const {data:response} = await axios.request(configForOne);
            setOne(
                response
            )
        }

        fetchOneRecipe()
    },)
    console.log(oneResult)
    return(
        oneResult!==[] && <Card title={decodeURIComponent(recipe)}>
            <Card type="inner" title="Link" extra={<a href="#">More</a>}>
                {oneResult["link"]}
            </Card>
            <Card type="inner" title="Ingredient" extra={<a href="#">More</a>}>
                {oneResult["ingredient"]}
            </Card>
            <Card type="inner" title="Instruction" extra={<a href="#">More</a>}>
                {oneResult["instruction"]}
            </Card>
            <Card type="inner" title="Nutrients" extra={<a href="#">More</a>}>
                {oneResult["nutrients"]}
            </Card>
        </Card>
    )

}
export default Recipe