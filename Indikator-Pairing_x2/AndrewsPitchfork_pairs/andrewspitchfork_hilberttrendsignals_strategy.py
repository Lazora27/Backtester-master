import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
