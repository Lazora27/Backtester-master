import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'UlcerIndex': 1.0
        })
    )
