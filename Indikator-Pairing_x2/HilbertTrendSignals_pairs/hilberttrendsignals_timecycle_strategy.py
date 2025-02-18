import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'TimeCycle': 1.0
        })
    )
