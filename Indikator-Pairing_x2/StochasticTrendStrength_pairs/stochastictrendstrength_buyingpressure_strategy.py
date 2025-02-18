import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BuyingPressure': 1.0
        })
    )
