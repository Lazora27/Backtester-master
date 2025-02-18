import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SuperTrend
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SuperTrend': 1.0
        })
    )
