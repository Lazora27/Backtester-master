import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'CycleFinder': 1.0
        })
    )
