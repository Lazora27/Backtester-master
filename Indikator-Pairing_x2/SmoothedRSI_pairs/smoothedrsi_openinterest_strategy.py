import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'OpenInterest': 1.0
        })
    )
