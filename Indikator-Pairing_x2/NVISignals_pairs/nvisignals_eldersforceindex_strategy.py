import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'EldersForceIndex': 1.0
        })
    )
