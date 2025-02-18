import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TapeReading': 1.0
        })
    )
