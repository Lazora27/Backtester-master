import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
