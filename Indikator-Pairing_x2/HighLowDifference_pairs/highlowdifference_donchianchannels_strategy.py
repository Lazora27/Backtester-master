import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DonchianChannels': 1.0
        })
    )
