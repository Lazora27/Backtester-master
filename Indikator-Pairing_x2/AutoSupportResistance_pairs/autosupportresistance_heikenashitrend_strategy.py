import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
