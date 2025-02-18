import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
