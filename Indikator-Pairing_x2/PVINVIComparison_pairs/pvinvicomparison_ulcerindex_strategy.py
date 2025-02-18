import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'UlcerIndex': 1.0
        })
    )
