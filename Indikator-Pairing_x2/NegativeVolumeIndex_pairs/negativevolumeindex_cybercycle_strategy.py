import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
