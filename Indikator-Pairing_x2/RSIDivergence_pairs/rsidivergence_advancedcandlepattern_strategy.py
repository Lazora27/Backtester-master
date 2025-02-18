import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
