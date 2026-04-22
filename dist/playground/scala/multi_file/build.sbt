ThisBuild / scalaVersion := "2.13.14"
ThisBuild / organization := "com.kegyi.playground"
ThisBuild / version := "0.1.0-SNAPSHOT"

lazy val root = (project in file("."))
  .settings(
    name := "scala-multi-file-playground",
    scalacOptions ++= Seq("-deprecation", "-feature", "-unchecked"),
    Compile / run / mainClass := Some("com.kegyi.playground.multifile.Main"),
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.19" % Test
  )
