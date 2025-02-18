import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'DonchianVolatility': 1.0
        })
    )
