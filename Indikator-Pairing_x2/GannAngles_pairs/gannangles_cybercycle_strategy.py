import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CyberCycle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CyberCycle': 1.0
        })
    )
