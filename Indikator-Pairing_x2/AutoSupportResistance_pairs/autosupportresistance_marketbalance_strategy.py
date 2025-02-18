import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MarketBalance': 1.0
        })
    )
