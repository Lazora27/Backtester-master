import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WeightedCycle': 1.0
        })
    )
