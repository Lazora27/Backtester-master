import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
