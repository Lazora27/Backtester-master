import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
