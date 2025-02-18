import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
