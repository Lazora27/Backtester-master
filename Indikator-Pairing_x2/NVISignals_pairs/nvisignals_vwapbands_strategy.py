import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VWAPBands
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VWAPBands': 1.0
        })
    )
