import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BuyingPressure': 1.0
        })
    )
