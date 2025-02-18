import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
