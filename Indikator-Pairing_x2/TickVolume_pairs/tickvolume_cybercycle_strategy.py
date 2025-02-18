import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CyberCycle': 1.0
        })
    )
