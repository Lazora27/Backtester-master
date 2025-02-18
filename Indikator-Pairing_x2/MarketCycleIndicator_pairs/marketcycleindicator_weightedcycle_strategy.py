import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
