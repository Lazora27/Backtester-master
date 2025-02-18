import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
