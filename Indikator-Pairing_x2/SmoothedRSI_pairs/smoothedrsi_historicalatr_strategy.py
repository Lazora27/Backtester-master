import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
