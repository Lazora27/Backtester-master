import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
