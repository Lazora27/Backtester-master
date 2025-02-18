import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AccelerationBands': 1.0
        })
    )
