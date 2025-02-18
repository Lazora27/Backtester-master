import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
