import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SmoothedCycle': 1.0
        })
    )
