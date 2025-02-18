import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'CCITurbo': 1.0
        })
    )
