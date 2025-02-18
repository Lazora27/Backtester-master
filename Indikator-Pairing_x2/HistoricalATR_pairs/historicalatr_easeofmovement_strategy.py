import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'EaseOfMovement': 1.0
        })
    )
