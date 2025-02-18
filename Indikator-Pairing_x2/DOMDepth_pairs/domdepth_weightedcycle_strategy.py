import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'WeightedCycle': 1.0
        })
    )
