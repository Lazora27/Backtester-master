import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
