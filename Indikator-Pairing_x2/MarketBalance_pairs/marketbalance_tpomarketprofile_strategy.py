import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
