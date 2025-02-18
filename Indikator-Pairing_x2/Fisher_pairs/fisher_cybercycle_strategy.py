import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CyberCycle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CyberCycle': 1.0
        })
    )
