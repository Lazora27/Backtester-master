import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HullMovingAverage': 1.0
        })
    )
