import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
