import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
