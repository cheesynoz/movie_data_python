USE [testforproject]
GO

/****** Object:  Table [dbo].[Movie Data]    Script Date: 12/23/2022 3:49:01 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Movie Data](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Title] [varchar](max) NOT NULL,
	[Genre] [varchar](max) NULL,
	[Director] [varchar](max) NULL,
	[Release Year] [varchar](50) NOT NULL,
	[Country] [varchar](max) NULL,
	[Rating] [int] NULL,
	[Date Watched] [varchar](50) NULL,
	[TMDB_id] [int] NOT NULL,
 CONSTRAINT [PK_Movie Data] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


