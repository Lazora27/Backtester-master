import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
