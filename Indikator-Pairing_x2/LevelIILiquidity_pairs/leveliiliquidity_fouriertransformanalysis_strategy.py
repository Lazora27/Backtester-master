import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
