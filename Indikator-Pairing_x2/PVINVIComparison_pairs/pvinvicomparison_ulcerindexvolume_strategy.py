import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
