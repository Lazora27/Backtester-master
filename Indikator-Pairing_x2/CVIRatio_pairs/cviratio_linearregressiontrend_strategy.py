import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
