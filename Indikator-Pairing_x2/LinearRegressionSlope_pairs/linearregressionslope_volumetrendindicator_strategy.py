import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
