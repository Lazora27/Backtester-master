import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'CenterOfGravity': 1.0
        })
    )
