import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'HilbertTrendline': 1.0
        })
    )
