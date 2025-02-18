import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CoppockCurve': 1.0
        })
    )
