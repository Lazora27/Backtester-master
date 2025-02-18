import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
