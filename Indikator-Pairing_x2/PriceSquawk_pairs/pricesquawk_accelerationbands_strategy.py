import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AccelerationBands': 1.0
        })
    )
