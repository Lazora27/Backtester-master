import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PriceDelta
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PriceDelta': 1.0
        })
    )
