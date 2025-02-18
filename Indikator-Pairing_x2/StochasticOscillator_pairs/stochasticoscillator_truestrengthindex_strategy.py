import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
