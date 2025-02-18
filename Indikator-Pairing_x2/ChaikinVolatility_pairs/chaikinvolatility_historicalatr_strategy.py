import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HistoricalATR': 1.0
        })
    )
