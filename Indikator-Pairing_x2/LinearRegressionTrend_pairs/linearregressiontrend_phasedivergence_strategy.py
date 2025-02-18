import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'PhaseDivergence': 1.0
        })
    )
