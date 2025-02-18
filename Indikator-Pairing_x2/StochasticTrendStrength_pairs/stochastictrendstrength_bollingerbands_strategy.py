import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BollingerBands': 1.0
        })
    )
