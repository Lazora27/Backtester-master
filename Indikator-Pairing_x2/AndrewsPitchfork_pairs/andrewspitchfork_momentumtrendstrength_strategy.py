import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
