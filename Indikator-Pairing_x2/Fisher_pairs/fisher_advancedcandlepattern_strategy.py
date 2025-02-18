import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
