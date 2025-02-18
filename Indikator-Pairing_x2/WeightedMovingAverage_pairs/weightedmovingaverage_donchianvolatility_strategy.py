import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'DonchianVolatility': 1.0
        })
    )
