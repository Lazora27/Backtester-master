import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MassIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MassIndex': 1.0
        })
    )
