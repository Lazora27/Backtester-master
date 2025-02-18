import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
