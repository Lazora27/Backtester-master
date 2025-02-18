import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MarketBalance': 1.0
        })
    )
