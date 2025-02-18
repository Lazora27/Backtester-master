import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MassIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MassIndex': 1.0
        })
    )
