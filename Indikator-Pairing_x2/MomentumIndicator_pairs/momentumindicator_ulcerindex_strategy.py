import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
