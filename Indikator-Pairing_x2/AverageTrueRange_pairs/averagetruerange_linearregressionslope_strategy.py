import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
