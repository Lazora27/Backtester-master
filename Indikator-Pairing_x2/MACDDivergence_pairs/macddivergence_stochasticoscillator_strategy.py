import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'StochasticOscillator': 1.0
        })
    )
