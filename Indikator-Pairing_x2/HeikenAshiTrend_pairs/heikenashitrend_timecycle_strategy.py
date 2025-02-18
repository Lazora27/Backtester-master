import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'TimeCycle': 1.0
        })
    )
