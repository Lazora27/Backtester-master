import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
