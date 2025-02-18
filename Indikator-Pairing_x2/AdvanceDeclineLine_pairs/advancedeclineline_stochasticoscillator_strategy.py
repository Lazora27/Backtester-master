import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'StochasticOscillator': 1.0
        })
    )
