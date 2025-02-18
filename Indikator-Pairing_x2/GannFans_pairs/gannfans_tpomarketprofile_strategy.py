import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
