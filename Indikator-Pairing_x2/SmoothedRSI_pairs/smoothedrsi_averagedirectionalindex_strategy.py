import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
