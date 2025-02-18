import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
