import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'TimeCycle': 1.0
        })
    )
