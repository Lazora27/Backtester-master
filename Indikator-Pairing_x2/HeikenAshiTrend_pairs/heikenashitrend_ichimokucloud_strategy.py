import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'IchimokuCloud': 1.0
        })
    )
