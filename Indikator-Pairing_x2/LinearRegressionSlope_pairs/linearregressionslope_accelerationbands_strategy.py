import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'AccelerationBands': 1.0
        })
    )
