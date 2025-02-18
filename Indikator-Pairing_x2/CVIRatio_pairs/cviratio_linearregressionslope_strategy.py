import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
