import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PriceDelta
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PriceDelta': 1.0
        })
    )
