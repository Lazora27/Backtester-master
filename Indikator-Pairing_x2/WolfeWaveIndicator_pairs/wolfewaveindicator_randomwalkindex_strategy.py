import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
