import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'BradleySiderograph': 1.0
        })
    )
