import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'DonchianVolatility': 1.0
        })
    )
