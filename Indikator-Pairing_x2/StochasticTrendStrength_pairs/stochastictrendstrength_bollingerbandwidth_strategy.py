import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
