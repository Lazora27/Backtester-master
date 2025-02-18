import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DonchianChannels': 1.0
        })
    )
