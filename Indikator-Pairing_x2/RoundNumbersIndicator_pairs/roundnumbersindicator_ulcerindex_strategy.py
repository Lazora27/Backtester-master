import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
