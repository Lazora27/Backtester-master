import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und TrendCycles
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'TrendCycles': 1.0
        })
    )
