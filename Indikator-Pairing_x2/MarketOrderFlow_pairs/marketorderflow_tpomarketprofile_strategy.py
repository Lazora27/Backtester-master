import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
