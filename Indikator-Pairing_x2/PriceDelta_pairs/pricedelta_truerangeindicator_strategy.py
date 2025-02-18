import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
