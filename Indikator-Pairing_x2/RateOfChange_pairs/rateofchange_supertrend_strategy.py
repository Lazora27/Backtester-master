import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SuperTrend
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SuperTrend': 1.0
        })
    )
