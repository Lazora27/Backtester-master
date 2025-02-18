import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SmoothedCycle': 1.0
        })
    )
