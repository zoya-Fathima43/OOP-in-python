class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0 
        self.comments = [] 

    # --- Original Methods ---
    def display_title(self):
        print(f"The title of the reel is {self.title}")
    def display_description(self):
        print(f"The description of the reel is {self.description}")
    def display_likes(self):
        print(f"The likes of the reel is {self.likes}")
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1 

    # --- New Methods ---
    def display_creator(self):
        print(f"Creator: {self.creator_name}")
    def display_location(self):
        print(f"Location: {self.location}")
    def add_comment(self, comment_text):
        """Adds a new string comment to the list using append()."""
        self.comments.append(comment_text)
    def display_comments(self):
        print("Comments:")
        if not self.comments:
            print("- No comments yet.")
        for comment in self.comments:
            print(f"- {comment}")
    def remove_last_comment(self):
        """Removes the last comment using pop()."""
        if self.comments:
            self.comments.pop()
            print("Last comment removed.")
        else:
            print("No comments to remove.")

# --- Example Usage ---
reel1 = Instagram("dancing", "dancing with friends", "Alex", "New York")
reel1.add_comment("Great moves!")
reel1.add_comment("Love the song choice.")
reel1.display_creator()
reel1.display_location()
reel1.display_comments()
reel1.remove_last_comment()
reel1.display_comments()
