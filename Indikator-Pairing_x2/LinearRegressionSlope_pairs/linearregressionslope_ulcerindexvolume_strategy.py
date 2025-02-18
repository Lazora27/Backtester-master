import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
