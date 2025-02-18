import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
