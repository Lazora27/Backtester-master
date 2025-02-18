import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
