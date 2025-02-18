import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
