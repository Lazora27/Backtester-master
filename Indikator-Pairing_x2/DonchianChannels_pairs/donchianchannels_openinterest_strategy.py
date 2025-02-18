import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'OpenInterest': 1.0
        })
    )
