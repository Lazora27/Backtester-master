import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
