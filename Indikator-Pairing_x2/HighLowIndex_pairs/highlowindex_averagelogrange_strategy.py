import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
