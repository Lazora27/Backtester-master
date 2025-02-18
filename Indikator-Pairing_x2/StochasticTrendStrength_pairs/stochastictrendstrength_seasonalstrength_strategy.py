import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SeasonalStrength': 1.0
        })
    )
