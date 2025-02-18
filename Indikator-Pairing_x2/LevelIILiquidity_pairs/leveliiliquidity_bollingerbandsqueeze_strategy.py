import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
