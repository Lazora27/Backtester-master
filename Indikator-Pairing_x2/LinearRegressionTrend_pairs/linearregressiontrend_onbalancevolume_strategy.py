import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
