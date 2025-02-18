import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TapeReading
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TapeReading': 1.0
        })
    )
