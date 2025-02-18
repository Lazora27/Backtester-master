import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SuperTrend
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SuperTrend': 1.0
        })
    )
