USE [testforproject]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Movie Data](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Title] [varchar](max) NOT NULL,
	[Genre] [text] NOT NULL,
	[Director] [text] NULL,
	[Release Year] [int] NOT NULL,
	[Country] [text] NULL,
	[Rating] [int] NULL,
	[Favorite?] [bit] NOT NULL,
	[Date Watched] [date] NULL,
 CONSTRAINT [PK_Movie Data] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[Movie Data] ADD  CONSTRAINT [DF__Movie Dat__Favor__35BCFE0A]  DEFAULT ((0)) FOR [Favorite?]
GO


