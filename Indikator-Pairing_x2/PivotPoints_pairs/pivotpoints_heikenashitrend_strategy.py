import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
