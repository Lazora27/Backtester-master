import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'StochasticOscillator': 1.0
        })
    )
