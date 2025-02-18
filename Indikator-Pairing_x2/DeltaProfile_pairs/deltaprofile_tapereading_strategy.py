import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TapeReading
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TapeReading': 1.0
        })
    )
