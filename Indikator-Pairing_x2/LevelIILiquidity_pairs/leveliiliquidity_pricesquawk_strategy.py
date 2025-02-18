import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PriceSquawk': 1.0
        })
    )
