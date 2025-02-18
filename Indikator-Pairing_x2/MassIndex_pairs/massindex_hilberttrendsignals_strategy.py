import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
