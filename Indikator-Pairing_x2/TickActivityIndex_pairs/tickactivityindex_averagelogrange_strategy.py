import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
