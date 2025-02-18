import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TimeCycle
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TimeCycle': 1.0
        })
    )
