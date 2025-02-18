import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
