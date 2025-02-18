import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'LiquidityIndex': 1.0
        })
    )
