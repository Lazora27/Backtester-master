import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
