import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'WeeklyCycle': 1.0
        })
    )
