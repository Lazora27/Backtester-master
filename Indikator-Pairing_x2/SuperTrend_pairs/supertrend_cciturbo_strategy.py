import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'CCITurbo': 1.0
        })
    )
