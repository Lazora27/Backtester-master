import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
