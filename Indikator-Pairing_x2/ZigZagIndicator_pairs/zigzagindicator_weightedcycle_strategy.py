import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
