import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
