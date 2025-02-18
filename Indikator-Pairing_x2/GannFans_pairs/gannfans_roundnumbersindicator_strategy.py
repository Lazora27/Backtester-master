import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
