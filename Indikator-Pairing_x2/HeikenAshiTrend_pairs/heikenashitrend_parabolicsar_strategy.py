import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ParabolicSAR': 1.0
        })
    )
