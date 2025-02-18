import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
