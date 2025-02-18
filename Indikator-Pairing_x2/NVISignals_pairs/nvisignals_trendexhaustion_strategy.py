import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TrendExhaustion': 1.0
        })
    )
