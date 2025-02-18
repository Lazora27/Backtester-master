import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolatilityIndex': 1.0
        })
    )
