import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
