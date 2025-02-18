import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
