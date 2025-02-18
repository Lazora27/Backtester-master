import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'TimeCycle': 1.0
        })
    )
