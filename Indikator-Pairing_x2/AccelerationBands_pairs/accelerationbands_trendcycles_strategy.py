import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'TrendCycles': 1.0
        })
    )
