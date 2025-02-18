import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
