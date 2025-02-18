import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SmoothedCycle': 1.0
        })
    )
