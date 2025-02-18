import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
