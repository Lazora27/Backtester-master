import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'CyberCycle': 1.0
        })
    )
