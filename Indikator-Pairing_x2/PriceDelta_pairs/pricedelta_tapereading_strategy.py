import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TapeReading
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TapeReading': 1.0
        })
    )
