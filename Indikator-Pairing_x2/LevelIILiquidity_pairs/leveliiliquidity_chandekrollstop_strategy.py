import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
