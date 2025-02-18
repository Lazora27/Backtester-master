import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'StochasticOscillator': 1.0
        })
    )
