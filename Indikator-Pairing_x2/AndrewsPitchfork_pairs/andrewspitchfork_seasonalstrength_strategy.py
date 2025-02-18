import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'SeasonalStrength': 1.0
        })
    )
