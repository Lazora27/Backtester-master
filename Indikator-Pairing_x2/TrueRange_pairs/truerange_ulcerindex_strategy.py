import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'UlcerIndex': 1.0
        })
    )
