ThisBuild / scalaVersion := "2.13.14"
ThisBuild / organization := "com.example.playground"
ThisBuild / version := "0.1.0-SNAPSHOT"

lazy val root = (project in file("."))
  .settings(
    name := "example_project",
    scalacOptions ++= Seq("-deprecation", "-feature", "-unchecked"),
    Compile / run / mainClass := Some("com.example.playground.Main"),
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.19" % Test
  )
