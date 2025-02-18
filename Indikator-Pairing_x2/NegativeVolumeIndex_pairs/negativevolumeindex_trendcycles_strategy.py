import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
