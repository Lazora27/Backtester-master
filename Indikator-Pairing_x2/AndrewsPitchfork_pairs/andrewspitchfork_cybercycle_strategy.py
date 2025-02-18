import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CyberCycle': 1.0
        })
    )
