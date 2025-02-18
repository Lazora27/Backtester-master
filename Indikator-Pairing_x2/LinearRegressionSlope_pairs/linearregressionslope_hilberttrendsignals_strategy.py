import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
