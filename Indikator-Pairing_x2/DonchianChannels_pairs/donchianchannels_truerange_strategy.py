import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TrueRange
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TrueRange': 1.0
        })
    )
