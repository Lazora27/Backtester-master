import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TrendCycles': 1.0
        })
    )
