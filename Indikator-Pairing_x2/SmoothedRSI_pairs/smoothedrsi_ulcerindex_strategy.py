import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'UlcerIndex': 1.0
        })
    )
