import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AdaptiveATR': 1.0
        })
    )
