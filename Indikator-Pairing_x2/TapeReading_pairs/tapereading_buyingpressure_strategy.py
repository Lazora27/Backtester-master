import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BuyingPressure': 1.0
        })
    )
