### 1. REST API Design

#### **Subreddit Timeline**
- **GET /subreddits/{subredditId}/posts**
  - Fetches a list of posts in a subreddit, ordered by recency.
  - Parameters: `subredditId` (path), optional `limit` and `offset` for pagination.
  - Response: List of posts with metadata (title, content, upvotes, creation time).

#### **User Subscription**
- **POST /users/{userId}/subscriptions**
  - Allows a user to subscribe to a subreddit.
  - Parameters: `userId` (path), `subredditId` (body).
  - Response: Success or failure message.
- **DELETE /users/{userId}/subscriptions/{subredditId}**
  - Allows a user to unsubscribe from a subreddit.
  - Response: Success or failure message.

#### **Post Submission**
- **POST /subreddits/{subredditId}/posts**
  - Submits a new post to a subreddit.
  - Parameters: `subredditId` (path), `userId`, `title`, and `content` (body).
  - Response: Created post ID or error message.

#### **Upvotes**
- **POST /posts/{postId}/upvotes**
  - Adds an upvote to a post (one per user).
  - Parameters: `postId` (path), `userId` (body).
  - Response: Updated vote count or error message.

#### **Comments**
- **POST /posts/{postId}/comments**
  - Adds a comment to a post.
  - Parameters: `postId` (path), `userId`, and `content` (body).
  - Response: Comment ID or error message.

#### **User Profile**
- **GET /users/{userId}/profile**
  - Fetches a user's profile, including subscribed subreddits and upvote count.
  - Parameters: `userId` (path).
  - Response: List of subscribed subreddits and total upvotes.

---

### 2. Conceptual Database Model

#### **Entities and Relationships**
1. **User**
   - Attributes: `userId`, `username`, `email`, `passwordHash`, `profileInfo`.
   - Relationships: Subscribes to Subreddits, Creates Posts, Upvotes Posts, Comments on Posts.

2. **Subreddit**
   - Attributes: `subredditId`, `name`, `description`, `createdAt`.
   - Relationships: Contains Posts.

3. **Post**
   - Attributes: `postId`, `title`, `content`, `createdAt`, `subredditId`, `userId`.
   - Relationships: Receives Upvotes, Contains Comments.

4. **Comment**
   - Attributes: `commentId`, `content`, `createdAt`, `postId`, `userId`.
   - Relationships: Belongs to a Post.

5. **Upvote**
   - Attributes: `upvoteId`, `userId`, `postId`.
   - Relationships: Belongs to a Post and a User.

6. **Subscription**
   - Attributes: `subscriptionId`, `userId`, `subredditId`.
   - Relationships: Links Users and Subreddits.

---

### 3. Potential Performance Problem and Solution
- **Problem:** High traffic on the subreddit timeline API (`GET /subreddits/{subredditId}/posts`) may result in slow response times due to repeated database queries.
- **Solution:** Implement database indexing on the `createdAt` field and caching for frequently accessed subreddit timelines.

---

### 4. Potential Security Problem and Solution
- **Problem:** API endpoints (e.g., for voting or posting) can be abused by unauthorized or malicious users.
- **Solution:** Enforce authentication using OAuth 2.0 or JWT and validate user actions through role-based access control (RBAC) to ensure authorized usage.