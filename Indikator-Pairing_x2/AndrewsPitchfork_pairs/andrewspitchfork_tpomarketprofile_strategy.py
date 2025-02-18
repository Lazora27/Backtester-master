import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
