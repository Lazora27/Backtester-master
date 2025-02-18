import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
