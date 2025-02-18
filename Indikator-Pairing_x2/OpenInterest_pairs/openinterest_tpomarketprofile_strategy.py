import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
