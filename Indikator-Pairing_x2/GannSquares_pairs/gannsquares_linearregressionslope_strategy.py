import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
