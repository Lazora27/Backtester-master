import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AverageLogRange': 1.0
        })
    )
