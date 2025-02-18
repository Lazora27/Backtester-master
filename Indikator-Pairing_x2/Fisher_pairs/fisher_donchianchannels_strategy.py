import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DonchianChannels': 1.0
        })
    )
