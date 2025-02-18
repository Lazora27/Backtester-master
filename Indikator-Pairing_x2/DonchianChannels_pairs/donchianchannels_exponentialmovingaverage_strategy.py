import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
