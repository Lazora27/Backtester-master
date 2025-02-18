import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
