import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
