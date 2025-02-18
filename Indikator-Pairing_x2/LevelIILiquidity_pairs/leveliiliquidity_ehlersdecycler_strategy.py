import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'EhlersDecycler': 1.0
        })
    )
