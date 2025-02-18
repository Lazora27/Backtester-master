import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
