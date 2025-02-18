import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'PhaseDivergence': 1.0
        })
    )
