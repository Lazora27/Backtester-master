import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
