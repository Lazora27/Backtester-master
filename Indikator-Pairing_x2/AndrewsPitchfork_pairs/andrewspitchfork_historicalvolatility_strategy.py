import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
