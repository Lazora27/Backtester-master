import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
