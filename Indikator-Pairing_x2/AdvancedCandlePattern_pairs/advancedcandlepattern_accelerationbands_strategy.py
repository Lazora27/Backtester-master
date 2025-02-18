import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'AccelerationBands': 1.0
        })
    )
