import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
