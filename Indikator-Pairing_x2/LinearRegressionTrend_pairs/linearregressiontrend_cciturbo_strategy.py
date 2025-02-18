import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und CCITurbo
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'CCITurbo': 1.0
        })
    )
