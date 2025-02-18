import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BollingerBands
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BollingerBands': 1.0
        })
    )
