import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TickVolume
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TickVolume': 1.0
        })
    )
