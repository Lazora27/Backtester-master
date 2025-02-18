import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AccelerationBands': 1.0
        })
    )
