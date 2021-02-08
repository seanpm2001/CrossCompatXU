#import "Forwarder.h"
#import "Recipient.h"

int main(void) {
  Forwarder *forwarder = [Forwarder new];
  Recipient *recipient = [Recipient new];

  [forwarder setRecipient:recipient]; // Set the recipient.
  /*
  * Observe forwarder does not respond to a hello message! It will
  * be forwarded. All unrecognized methods will be forwarded to
  * the recipient
  * (if the recipient responds to them, as written in the Forwarder)
  */
  [forwarder hello];

  [recipient release];
  [forwarder release];

  return 0;
}
