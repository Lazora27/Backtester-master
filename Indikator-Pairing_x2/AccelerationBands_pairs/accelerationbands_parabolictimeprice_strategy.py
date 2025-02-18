import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
