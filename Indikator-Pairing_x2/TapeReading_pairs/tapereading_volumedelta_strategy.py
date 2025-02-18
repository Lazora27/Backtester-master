import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolumeDelta': 1.0
        })
    )
