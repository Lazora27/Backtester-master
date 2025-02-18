import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
