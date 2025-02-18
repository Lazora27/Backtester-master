import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SmoothedCycle': 1.0
        })
    )
