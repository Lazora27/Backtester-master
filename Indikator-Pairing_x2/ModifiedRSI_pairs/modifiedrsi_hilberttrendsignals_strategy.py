import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
