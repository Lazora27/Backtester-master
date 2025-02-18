import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
