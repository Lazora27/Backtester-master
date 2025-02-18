import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
