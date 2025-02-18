import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
