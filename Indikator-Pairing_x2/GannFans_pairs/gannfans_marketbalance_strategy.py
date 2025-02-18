import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MarketBalance
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MarketBalance': 1.0
        })
    )
