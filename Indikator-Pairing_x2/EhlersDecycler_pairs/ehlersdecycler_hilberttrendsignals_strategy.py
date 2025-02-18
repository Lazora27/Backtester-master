import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
