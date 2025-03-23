# Blog Post Management Functionality

This module provides a set of functions to manage blog posts, including creating, reading, updating, and deleting (CRUD) operations.

## Functions

1. **`createPost(title, content, author)`**: Creates a new blog post with the given title, content, and author.
    - **Parameters**:
      - `title` (string): The title of the blog post.
      - `content` (string): The content of the blog post.
      - `author` (string): The author of the blog post.
    - **Returns**: An object representing the newly created blog post.

2. **`getPostById(postId)`**: Retrieves a blog post by its unique identifier.
    - **Parameters**:
      - `postId` (string): The unique identifier of the blog post.
    - **Returns**: An object representing the blog post, or `null` if no post is found.

3. **`updatePost(postId, updatedData)`**: Updates an existing blog post with new data.
    - **Parameters**:
      - `postId` (string): The unique identifier of the blog post to be updated.
      - `updatedData` (object): An object containing the updated data for the blog post.
    - **Returns**: An object representing the updated blog post, or `null` if no post is found.

4. **`deletePost(postId)`**: Deletes a blog post by its unique identifier.
    - **Parameters**:
      - `postId` (string): The unique identifier of the blog post to be deleted.
    - **Returns**: A boolean indicating whether the deletion was successful.

5. **`getAllPosts()`**: Retrieves all blog posts.
    - **Returns**: An array of objects, each representing a blog post.

6. **`searchPosts(query)`**: Searches for blog posts that match the given query.
    - **Parameters**:
      - `query` (string): The search query to filter blog posts.
    - **Returns**: An array of objects representing the blog posts that match the query.

## Usage Example

```javascript
const newPost = createPost('My First Post', 'This is the content of my first post.', 'Author Name');
const post = getPostById(newPost.id);
const updatedPost = updatePost(newPost.id, { title: 'Updated Title' });
const allPosts = getAllPosts();
const searchResults = searchPosts('First');
const isDeleted = deletePost(newPost.id);
```
