import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AroonIndicator': 1.0
        })
    )
