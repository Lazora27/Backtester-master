import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'EhlersDecycler': 1.0
        })
    )
