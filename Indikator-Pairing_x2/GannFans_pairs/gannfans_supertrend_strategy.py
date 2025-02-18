import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SuperTrend
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SuperTrend': 1.0
        })
    )
