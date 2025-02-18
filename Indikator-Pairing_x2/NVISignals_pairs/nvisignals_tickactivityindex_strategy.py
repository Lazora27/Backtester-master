import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TickActivityIndex': 1.0
        })
    )
