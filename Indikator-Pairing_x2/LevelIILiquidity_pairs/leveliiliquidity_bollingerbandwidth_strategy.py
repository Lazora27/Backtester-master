import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
