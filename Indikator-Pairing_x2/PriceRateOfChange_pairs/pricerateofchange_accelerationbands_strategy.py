import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'AccelerationBands': 1.0
        })
    )
