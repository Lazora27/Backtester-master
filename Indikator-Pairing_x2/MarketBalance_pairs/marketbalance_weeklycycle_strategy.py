import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'WeeklyCycle': 1.0
        })
    )
