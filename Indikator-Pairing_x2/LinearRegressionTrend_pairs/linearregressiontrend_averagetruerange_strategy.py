import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'AverageTrueRange': 1.0
        })
    )
