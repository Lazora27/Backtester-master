import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
