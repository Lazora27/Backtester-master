import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'VolumeDelta': 1.0
        })
    )
