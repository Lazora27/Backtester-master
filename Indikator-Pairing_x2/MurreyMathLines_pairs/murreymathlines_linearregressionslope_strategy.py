import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
