import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
