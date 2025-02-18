import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
