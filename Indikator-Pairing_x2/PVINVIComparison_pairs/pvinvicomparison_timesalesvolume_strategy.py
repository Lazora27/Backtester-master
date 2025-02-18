import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
