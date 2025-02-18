import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SuperTrend': 1.0
        })
    )
