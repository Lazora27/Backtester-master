import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
