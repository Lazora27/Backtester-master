import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
