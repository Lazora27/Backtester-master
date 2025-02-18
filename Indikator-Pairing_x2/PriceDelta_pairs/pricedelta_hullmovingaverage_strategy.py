import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HullMovingAverage': 1.0
        })
    )
