import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WolfeWaves': 1.0
        })
    )
