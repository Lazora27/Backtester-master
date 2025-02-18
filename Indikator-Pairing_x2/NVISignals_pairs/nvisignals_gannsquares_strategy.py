import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und GannSquares
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'GannSquares': 1.0
        })
    )
