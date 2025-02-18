import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HistoricalATR': 1.0
        })
    )
