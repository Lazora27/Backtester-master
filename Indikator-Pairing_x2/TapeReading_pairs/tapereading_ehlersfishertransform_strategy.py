import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
