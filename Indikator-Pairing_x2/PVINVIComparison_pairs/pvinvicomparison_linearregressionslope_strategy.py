import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
