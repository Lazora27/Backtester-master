import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
