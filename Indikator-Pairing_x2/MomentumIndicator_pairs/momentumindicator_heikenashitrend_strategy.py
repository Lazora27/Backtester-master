import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
