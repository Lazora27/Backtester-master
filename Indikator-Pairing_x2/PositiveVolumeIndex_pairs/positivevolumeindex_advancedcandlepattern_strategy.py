import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
