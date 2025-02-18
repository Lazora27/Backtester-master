import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
