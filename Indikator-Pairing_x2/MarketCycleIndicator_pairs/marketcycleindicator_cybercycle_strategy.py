import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
