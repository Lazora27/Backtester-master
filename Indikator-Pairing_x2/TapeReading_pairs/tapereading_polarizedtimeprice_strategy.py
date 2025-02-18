import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
