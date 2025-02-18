import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
