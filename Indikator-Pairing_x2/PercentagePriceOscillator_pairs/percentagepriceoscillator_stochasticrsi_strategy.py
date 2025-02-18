import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
