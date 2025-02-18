import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
