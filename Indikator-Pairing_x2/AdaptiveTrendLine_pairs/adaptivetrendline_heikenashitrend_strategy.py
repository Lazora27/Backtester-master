import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
