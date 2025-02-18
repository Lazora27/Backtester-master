import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'StochasticOscillator': 1.0
        })
    )
