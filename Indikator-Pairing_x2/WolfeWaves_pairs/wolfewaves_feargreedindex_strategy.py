import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'FearGreedIndex': 1.0
        })
    )
