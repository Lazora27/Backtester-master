import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MovingAverage
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MovingAverage': 1.0
        })
    )
