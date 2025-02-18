import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ParabolicSAR': 1.0
        })
    )
