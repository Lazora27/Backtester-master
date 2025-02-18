import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
