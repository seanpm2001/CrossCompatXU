#import <objc/Object.h>
@interface Forwarder : Object {
id recipient; // The object we want to forward the message to.
}
// Accessor methods.
- (id)recipient;
- (id)setRecipient:(id)_recipient;
@end
