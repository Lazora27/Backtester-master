import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
