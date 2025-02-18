import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
