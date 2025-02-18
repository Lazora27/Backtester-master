import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
