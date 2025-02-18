import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AAIISentiment': 1.0
        })
    )
