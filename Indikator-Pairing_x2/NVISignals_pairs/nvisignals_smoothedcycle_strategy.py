import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SmoothedCycle': 1.0
        })
    )
