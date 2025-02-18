import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'PhaseDivergence': 1.0
        })
    )
