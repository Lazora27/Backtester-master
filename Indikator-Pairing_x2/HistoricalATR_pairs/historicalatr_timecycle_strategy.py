import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TimeCycle': 1.0
        })
    )
