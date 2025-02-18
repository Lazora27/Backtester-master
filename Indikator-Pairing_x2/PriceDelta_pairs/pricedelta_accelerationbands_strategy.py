import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AccelerationBands': 1.0
        })
    )
