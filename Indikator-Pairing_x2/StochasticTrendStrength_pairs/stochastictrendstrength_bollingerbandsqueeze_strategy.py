import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
