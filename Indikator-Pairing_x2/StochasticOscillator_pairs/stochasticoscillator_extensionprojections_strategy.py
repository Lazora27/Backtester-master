import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
