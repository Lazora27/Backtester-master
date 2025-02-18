import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'CycleFinder': 1.0
        })
    )
