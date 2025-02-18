import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
