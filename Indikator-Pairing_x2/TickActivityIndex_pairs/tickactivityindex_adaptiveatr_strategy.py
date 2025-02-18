import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
