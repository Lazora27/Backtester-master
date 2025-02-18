import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
