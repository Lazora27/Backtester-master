import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
