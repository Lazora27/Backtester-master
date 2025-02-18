import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
