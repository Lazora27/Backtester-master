import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BollingerPercentB': 1.0
        })
    )
