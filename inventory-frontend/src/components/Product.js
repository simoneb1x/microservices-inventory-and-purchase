import React, { Component, useEffect, useState } from "react";
import { Wrapper } from "./Wrapper";
import { Link } from "react-router-dom";

export const Products = () => {
  const [products, setProducts] = useState([]);

  // Getting the products
  useEffect(() => {
    (async () => {
      const response = await fetch("http://localhost:8000/products");
      const content = await response.json();
      setProducts(content);
    })();
  }, []);

  return (
    <Wrapper>
      <div className="pt-3 pb-2 mb-3 border-bottom">
        <Link to={"create"} className="btn btn-sm btn-outline-secondary">
          Add
        </Link>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Price</th>
              <th scope="col">Quantity</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => {
              return (
                <tr key={product.id}>
                  <td>{product.id}</td>
                  <td>{product.name}</td>
                  <td>{product.price}</td>
                  <td>{product.quantity}</td>
                  <td>
                    <a href="#" className="btn btn-sm btn-outline-secondary">
                      Delete
                    </a>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </Wrapper>
  );
};
