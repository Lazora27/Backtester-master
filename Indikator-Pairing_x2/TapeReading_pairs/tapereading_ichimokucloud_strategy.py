import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'IchimokuCloud': 1.0
        })
    )
