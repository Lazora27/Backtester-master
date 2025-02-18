import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HistoricalATR': 1.0
        })
    )
