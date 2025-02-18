import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'StochasticOscillator': 1.0
        })
    )
