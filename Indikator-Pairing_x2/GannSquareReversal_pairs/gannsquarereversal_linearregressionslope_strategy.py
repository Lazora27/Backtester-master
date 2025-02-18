import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
