import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TapeReading
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TapeReading': 1.0
        })
    )
