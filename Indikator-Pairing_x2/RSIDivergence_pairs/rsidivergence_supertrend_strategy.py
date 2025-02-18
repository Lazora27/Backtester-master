import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SuperTrend
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SuperTrend': 1.0
        })
    )
