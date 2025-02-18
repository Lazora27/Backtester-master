import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'StochasticOscillator': 1.0
        })
    )
