import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
