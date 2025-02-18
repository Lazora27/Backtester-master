import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TickActivityIndex': 1.0
        })
    )
