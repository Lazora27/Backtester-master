import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WilliamsR
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WilliamsR': 1.0
        })
    )
