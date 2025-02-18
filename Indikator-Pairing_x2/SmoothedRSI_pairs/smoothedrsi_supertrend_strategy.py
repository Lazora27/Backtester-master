import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
