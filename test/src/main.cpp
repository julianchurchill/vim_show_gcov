#include <stdio.h>

int main( int argc, char** argv )
{
    bool run = false;
    if( run )
        printf( "0th path" );
    else {
        if( run )
            run = true;
        else
            run = false;
        printf( "1st path" );
    }
    return 0;
}
