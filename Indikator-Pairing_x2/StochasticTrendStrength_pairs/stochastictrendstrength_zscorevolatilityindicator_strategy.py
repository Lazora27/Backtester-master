import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
