import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StochasticOscillator': 1.0
        })
    )
