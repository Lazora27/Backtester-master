import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und GannFans
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'GannFans': 1.0
        })
    )
