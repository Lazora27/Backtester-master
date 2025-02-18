import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TapeReading
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TapeReading': 1.0
        })
    )
