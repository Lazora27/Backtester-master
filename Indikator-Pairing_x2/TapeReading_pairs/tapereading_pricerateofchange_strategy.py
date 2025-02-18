import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
