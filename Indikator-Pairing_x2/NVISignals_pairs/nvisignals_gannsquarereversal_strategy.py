import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'GannSquareReversal': 1.0
        })
    )
