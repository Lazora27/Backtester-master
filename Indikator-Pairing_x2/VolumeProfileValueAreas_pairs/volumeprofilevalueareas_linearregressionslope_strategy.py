import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfileValueAreas_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfileValueAreas und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'VolumeProfileValueAreas': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
