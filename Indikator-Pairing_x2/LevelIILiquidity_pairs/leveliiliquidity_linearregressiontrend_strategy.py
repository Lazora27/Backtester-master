import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
