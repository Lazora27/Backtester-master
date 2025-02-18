import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
