import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
