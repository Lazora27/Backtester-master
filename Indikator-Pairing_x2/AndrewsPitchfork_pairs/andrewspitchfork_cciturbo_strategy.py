import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CCITurbo': 1.0
        })
    )
