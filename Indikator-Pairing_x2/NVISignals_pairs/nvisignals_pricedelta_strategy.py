import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PriceDelta
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PriceDelta': 1.0
        })
    )
