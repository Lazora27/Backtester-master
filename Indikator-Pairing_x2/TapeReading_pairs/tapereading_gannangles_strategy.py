import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und GannAngles
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'GannAngles': 1.0
        })
    )
