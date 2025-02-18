import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und MassIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'MassIndex': 1.0
        })
    )
