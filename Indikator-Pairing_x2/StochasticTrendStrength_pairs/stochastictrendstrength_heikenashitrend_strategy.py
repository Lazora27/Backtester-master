import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
