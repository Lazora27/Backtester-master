import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
