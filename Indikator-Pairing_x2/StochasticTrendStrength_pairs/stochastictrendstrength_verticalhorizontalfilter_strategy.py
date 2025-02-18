import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_VerticalHorizontalFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und VerticalHorizontalFilter
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'VerticalHorizontalFilter': 1.0
        })
    )
