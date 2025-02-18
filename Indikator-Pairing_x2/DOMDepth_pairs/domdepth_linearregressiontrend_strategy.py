import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
