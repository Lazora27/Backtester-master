import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TickIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TickIndex': 1.0
        })
    )
