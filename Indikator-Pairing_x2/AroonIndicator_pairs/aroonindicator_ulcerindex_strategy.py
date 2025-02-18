import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
