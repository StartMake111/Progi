#include <iostream>
#include <map>
#include <vector>
#include <http.h>
#include <mutex>

using json = nlohmann::json;
using namespace std;

struct Vec3
{
    double pos[3];

    double &operator[](int i) { return pos[i]; }
    double operator[](int i) const { return pos[i]; }
};

struct Entity
{
    string name;
    unsigned int health;
    Vec3 pos;
    Vec3 rot;
};

struct Game
{
    vector<Entity> players;
    vector<Entity> enimies;
    vector<Vec3> rooms;
};

void to_json(json &j, const Vec3 &v)
{
    j = json{v[0], v[1], v[2]};
}
void from_json(const json &j, Vec3 &v)
{
    for (int i = 0; i < 3; ++i)
        v[i] = j.at(i).get<double>();
}

void to_json(json &j, const Entity &e)
{
    j["pos"] = e.pos;
    j["rot"] = e.rot;
    j["name"] = e.name;
    j["health"] = e.health;
}
void from_json(const json &j, Entity &e)
{
    e.pos = j.at("pos").get<Vec3>();
    e.rot = j.at("rot").get<Vec3>();
    e.name = j.at("name").get<string>();
    e.health = j.at("health").get<double>();
}

void to_json(json &j, const Game &g)
{
    j["players"] = g.players;
    j["enimies"] = g.enimies;
    j["rooms"] = g.rooms;
}
void from_json(const json &j, Game &g)
{
    for (auto &e : j.at("players"))
        g.players.push_back(e);
    for (auto &e : j.at("enimies"))
        g.enimies.push_back(e);
    for (auto &r : j.at("rooms"))
        g.rooms.push_back(r);
}

Game game;
mutex m;

struct Request;
struct Response;

void set_data(const Request &req, Response &res)
{
    json data = json::parse(req->body());

    m.lock();
    game = data;
    m.unlock();

    res.set_content("", "application/json; charset=utf-8");
}

void get_data(const Request &req, Response &res)
{
    m.lock();
    auto str = json(game).dump();
    m.unlock();

    res.set_content(, "application/json; charset=utf-8");
}

int main()
{
    Server srv;

    srv.Get("/", get_data);
    srv.Post("/", set_data);

    srv.run();
}