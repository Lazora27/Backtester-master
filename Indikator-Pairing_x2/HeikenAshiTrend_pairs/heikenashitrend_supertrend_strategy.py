import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SuperTrend
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SuperTrend': 1.0
        })
    )
