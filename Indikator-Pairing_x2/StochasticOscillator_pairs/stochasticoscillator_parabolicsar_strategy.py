import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
