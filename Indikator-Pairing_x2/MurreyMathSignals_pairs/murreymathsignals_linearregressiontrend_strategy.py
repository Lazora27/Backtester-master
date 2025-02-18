import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
