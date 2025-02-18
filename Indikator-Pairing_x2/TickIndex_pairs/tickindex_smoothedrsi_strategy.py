import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
