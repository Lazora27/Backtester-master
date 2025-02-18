import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und GannAngles
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'GannAngles': 1.0
        })
    )
