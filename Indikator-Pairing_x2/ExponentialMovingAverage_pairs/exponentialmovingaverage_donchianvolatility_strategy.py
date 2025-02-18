import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'DonchianVolatility': 1.0
        })
    )
