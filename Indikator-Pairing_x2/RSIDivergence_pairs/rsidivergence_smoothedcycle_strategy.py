import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SmoothedCycle': 1.0
        })
    )
