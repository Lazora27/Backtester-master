import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
