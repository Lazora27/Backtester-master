import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'VWAPBands': 1.0
        })
    )
