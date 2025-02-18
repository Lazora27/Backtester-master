import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'DonchianVolatility': 1.0
        })
    )
