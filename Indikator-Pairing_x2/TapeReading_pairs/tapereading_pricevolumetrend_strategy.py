import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
