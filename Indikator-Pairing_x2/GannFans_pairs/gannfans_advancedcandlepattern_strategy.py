import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
