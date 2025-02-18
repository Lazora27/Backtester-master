import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
