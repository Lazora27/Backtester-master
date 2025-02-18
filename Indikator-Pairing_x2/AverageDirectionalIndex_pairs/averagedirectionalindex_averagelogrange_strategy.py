import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
