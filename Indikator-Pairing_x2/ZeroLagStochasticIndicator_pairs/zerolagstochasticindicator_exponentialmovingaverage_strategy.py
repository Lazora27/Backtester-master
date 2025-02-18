import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagStochasticIndicator_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagStochasticIndicator und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'ZeroLagStochasticIndicator': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
