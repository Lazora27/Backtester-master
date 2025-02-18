import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
