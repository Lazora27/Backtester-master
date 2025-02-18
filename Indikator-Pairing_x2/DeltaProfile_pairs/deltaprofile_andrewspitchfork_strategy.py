import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
