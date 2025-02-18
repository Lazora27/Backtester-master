import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'SmoothedCycle': 1.0
        })
    )
