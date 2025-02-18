import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
