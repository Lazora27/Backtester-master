import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MassIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MassIndex': 1.0
        })
    )
