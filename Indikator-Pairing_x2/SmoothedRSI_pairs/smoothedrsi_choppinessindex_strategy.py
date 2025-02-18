import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
