/**
 * IoT SDK Device & Client REST API
 * REST API definition for End-to-end testing of the Azure IoT SDKs.  All SDK APIs that are tested by our E2E tests need to be defined in this file.  This file takes some liberties with the API definitions.  In particular, response schemas are undefined, and error responses are also undefined.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator 2.3.1.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/*
 * EventhubApi.h
 *
 * 
 */

#ifndef EventhubApi_H_
#define EventhubApi_H_


#include <memory>
#include <corvusoft/restbed/session.hpp>
#include <corvusoft/restbed/resource.hpp>
#include <corvusoft/restbed/service.hpp>

#include "ConnectResponse.h"
#include <string>

namespace io {
namespace swagger {
namespace server {
namespace api {

using namespace io::swagger::server::model;

class  EventhubApi: public restbed::Service
{
public:
	EventhubApi();
	~EventhubApi();
	void startService(int const& port);
	void stopService();
};


/// <summary>
/// Connect to eventhub
/// </summary>
/// <remarks>
/// Connect to the Azure eventhub service.
/// </remarks>
class  EventhubApiEventhubConnectResource: public restbed::Resource
{
public:
	EventhubApiEventhubConnectResource();
    virtual ~EventhubApiEventhubConnectResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// wait for telemetry sent from a specific device
/// </summary>
/// <remarks>
/// 
/// </remarks>
class  EventhubApiEventhubConnectionIdDeviceTelemetryDeviceIdResource: public restbed::Resource
{
public:
	EventhubApiEventhubConnectionIdDeviceTelemetryDeviceIdResource();
    virtual ~EventhubApiEventhubConnectionIdDeviceTelemetryDeviceIdResource();
    void GET_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// Disconnect from the eventhub
/// </summary>
/// <remarks>
/// Disconnects from the Azure eventhub service
/// </remarks>
class  EventhubApiEventhubConnectionIdDisconnectResource: public restbed::Resource
{
public:
	EventhubApiEventhubConnectionIdDisconnectResource();
    virtual ~EventhubApiEventhubConnectionIdDisconnectResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};

/// <summary>
/// Enable telemetry
/// </summary>
/// <remarks>
/// 
/// </remarks>
class  EventhubApiEventhubConnectionIdEnableTelemetryResource: public restbed::Resource
{
public:
	EventhubApiEventhubConnectionIdEnableTelemetryResource();
    virtual ~EventhubApiEventhubConnectionIdEnableTelemetryResource();
    void PUT_method_handler(const std::shared_ptr<restbed::Session> session);
};


}
}
}
}

#endif /* EventhubApi_H_ */

