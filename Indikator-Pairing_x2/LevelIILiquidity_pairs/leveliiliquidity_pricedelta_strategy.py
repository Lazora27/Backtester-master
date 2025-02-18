import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PriceDelta
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PriceDelta': 1.0
        })
    )
