import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
