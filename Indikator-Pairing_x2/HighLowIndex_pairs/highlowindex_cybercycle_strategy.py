import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
