import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
