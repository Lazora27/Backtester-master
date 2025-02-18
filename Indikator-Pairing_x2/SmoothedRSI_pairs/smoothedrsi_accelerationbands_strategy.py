import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
