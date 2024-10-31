import React from "react";
import ReactDOM from "react-dom";

export default function Abc() {
    const [u, x, w] = ["p", "v", "j"];
    return (
        <div>
            u = {u}<br />
            w = {x}<br />
            j = {w}
        </div>
    );
}

// 如果你想在页面中直接显示组件渲染结果，可以使用如下代码：
ReactDOM.render(<Abc />, document.getElementById("root"));
