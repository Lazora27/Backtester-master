import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
