import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TapeReading
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TapeReading': 1.0
        })
    )
