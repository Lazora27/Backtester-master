import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HistoricalATR': 1.0
        })
    )
