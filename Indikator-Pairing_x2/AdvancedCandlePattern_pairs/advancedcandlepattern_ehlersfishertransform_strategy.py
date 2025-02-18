import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
