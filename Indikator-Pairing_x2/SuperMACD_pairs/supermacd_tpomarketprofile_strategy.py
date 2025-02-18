import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
