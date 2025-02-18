import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'CyberCycle': 1.0
        })
    )
