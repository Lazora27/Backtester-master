import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
