import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
