import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
