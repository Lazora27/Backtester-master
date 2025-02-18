import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BarStrength
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BarStrength': 1.0
        })
    )
