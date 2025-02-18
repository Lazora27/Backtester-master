import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
