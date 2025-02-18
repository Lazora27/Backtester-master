import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
