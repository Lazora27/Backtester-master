import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
