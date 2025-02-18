import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
