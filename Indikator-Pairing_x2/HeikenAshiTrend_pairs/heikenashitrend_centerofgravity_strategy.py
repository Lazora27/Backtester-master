import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'CenterOfGravity': 1.0
        })
    )
