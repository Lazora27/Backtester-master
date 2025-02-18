import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'EhlersDecycler': 1.0
        })
    )
