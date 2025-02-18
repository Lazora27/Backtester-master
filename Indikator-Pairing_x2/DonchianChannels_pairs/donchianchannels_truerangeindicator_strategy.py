import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
