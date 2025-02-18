import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VWAPBands
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VWAPBands': 1.0
        })
    )
