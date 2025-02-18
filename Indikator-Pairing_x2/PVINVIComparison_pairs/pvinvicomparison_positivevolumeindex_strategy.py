import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
