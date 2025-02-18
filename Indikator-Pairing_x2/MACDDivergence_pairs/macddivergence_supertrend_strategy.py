import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SuperTrend': 1.0
        })
    )
