import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HistoricalATR': 1.0
        })
    )
