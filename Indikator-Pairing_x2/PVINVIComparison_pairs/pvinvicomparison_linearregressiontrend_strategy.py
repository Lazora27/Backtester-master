import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
