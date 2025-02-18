import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
