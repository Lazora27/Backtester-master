import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
