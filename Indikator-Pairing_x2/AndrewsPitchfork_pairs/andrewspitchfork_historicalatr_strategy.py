import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HistoricalATR': 1.0
        })
    )
