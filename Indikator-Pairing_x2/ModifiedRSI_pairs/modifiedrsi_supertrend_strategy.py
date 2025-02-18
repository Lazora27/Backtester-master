import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
