import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
