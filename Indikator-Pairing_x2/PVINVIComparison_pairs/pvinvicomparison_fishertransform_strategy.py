import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FisherTransform
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FisherTransform': 1.0
        })
    )
