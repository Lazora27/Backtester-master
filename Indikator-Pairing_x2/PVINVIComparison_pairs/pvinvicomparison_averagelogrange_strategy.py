import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AverageLogRange': 1.0
        })
    )
