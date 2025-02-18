import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
