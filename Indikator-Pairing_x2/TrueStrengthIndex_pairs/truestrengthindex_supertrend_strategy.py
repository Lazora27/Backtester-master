import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
