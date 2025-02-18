import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SmoothedRSI': 1.0
        })
    )
