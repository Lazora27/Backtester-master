import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und CyberCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'CyberCycle': 1.0
        })
    )
