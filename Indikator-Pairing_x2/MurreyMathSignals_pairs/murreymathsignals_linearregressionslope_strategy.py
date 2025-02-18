import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
