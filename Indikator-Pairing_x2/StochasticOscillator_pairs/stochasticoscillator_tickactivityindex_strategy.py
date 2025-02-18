import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
