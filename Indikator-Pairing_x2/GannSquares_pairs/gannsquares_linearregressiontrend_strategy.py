import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
