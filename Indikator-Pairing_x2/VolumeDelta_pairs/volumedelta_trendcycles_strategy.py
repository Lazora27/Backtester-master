import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TrendCycles': 1.0
        })
    )
