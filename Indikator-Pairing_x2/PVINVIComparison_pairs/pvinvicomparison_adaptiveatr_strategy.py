import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AdaptiveATR': 1.0
        })
    )
