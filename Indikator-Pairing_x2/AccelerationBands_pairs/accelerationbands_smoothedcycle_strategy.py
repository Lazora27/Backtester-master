import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'SmoothedCycle': 1.0
        })
    )
