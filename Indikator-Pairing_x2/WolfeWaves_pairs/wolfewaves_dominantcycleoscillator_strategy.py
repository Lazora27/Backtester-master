import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
