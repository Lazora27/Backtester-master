import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
