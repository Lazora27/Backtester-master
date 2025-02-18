import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
