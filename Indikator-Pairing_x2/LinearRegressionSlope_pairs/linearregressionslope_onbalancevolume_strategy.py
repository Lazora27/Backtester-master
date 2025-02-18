import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
