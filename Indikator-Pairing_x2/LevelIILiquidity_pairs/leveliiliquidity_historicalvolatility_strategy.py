import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
